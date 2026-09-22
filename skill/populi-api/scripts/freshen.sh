#!/usr/bin/env bash
# Freshen the local Populi API reference before an agent reads it.
#
# Prints one status line, "populi-docs: current|updated|behind ...", plus any
# "populi-docs: warning: ..." lines. Exits 0 unless there is no local copy and
# cloning one fails.
#
#   current  the copy matches the live docs (or was checked recently)
#   updated  the live docs were newer; the sync workflow ran and was pulled
#   behind   the live docs are newer and the copy could not be brought level
#
# GitHub Actions is the only writer: when Populi is ahead, this dispatches the
# repo's sync workflow and pulls its commit, instead of syncing locally.
#
#   --force  check even if a check succeeded in the last 12 hours
#
# POPULI_DOCS_ROOT overrides the checkout; POPULI_DOCS_MAX_AGE_HOURS the 12.

set -uo pipefail

REPO="${POPULI_DOCS_ROOT:-$HOME/Projects/wts-dops/populi-api-docs}"
GH_REPO="robertguss/populi-api-docs"
WORKFLOW="sync.yml"
MAX_AGE_HOURS="${POPULI_DOCS_MAX_AGE_HOURS:-12}"
CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/populi-api-docs"
LAST_CHECK="$CACHE_DIR/last-check"
FORCE=0
[ "${1:-}" = "--force" ] && FORCE=1

say() { echo "populi-docs: $*"; }

local_stamp() {
    python3 -c 'import json, sys; print(json.load(open(sys.argv[1]))["docs_updated_on"])' \
        "$REPO/raw/meta.json" 2>/dev/null || echo "unknown"
}

mark_checked() { mkdir -p "$CACHE_DIR" && touch "$LAST_CHECK"; }

# The live stamp, through the tool's own check: exit 0 current, 1 newer, 2 error.
live_check() {
    uv run --project "$REPO" --quiet populi-docs --root "$REPO" check 2>&1
}

if [ ! -d "$REPO/.git" ]; then
    if ! git clone -q "https://github.com/$GH_REPO.git" "$REPO"; then
        say "no local copy at $REPO, and cloning $GH_REPO failed"
        exit 1
    fi
fi

if [ "$FORCE" = 0 ] && [ -f "$LAST_CHECK" ] &&
    [ -z "$(find "$LAST_CHECK" -mmin +$((MAX_AGE_HOURS * 60)))" ]; then
    say "current (checked in the last ${MAX_AGE_HOURS}h): docs $(local_stamp), at $REPO"
    exit 0
fi

if ! git -C "$REPO" pull -q --ff-only 2>/dev/null; then
    say "warning: git pull failed (offline, or local changes in $REPO); using the copy as it is"
fi

output=$(live_check)
status=$?
if [ "$status" = 0 ]; then
    mark_checked
    say "current: docs $(local_stamp), at $REPO"
    exit 0
fi
if [ "$status" != 1 ]; then
    say "warning: could not read the live docs stamp: $output"
    say "behind (unverified): using docs $(local_stamp), at $REPO"
    exit 0
fi

# Populi is ahead of the repo. Have the workflow sync it, then pull.
say "Populi published newer docs ($output); running the sync workflow"
if ! command -v gh >/dev/null; then
    say "behind: gh is not installed, so the workflow cannot be dispatched; using docs $(local_stamp)"
    exit 0
fi
# GitHub disables a scheduled workflow after 60 days without repo activity.
gh workflow enable "$WORKFLOW" -R "$GH_REPO" >/dev/null 2>&1
before=$(gh run list -R "$GH_REPO" --workflow "$WORKFLOW" --limit 1 \
    --json databaseId --jq '.[0].databaseId // 0' 2>/dev/null || echo 0)
if ! gh workflow run "$WORKFLOW" -R "$GH_REPO" >/dev/null 2>&1; then
    say "behind: could not dispatch $WORKFLOW on $GH_REPO; using docs $(local_stamp)"
    exit 0
fi
run=""
for _ in $(seq 1 20); do
    sleep 3
    latest=$(gh run list -R "$GH_REPO" --workflow "$WORKFLOW" --limit 1 \
        --json databaseId --jq '.[0].databaseId // 0' 2>/dev/null || echo 0)
    if [ "$latest" != "$before" ]; then
        run="$latest"
        break
    fi
done
if [ -z "$run" ]; then
    say "behind: the dispatched run did not appear; using docs $(local_stamp)"
    exit 0
fi
if ! gh run watch "$run" -R "$GH_REPO" --exit-status --interval 10 >/dev/null 2>&1; then
    say "behind: the sync run failed, see https://github.com/$GH_REPO/actions/runs/$run; using docs $(local_stamp)"
    exit 0
fi
git -C "$REPO" pull -q --ff-only 2>/dev/null ||
    say "warning: git pull after the sync failed; the new docs are on GitHub, not here yet"

if live_check >/dev/null; then
    mark_checked
    say "updated: docs $(local_stamp), at $REPO; the top entry of CHANGES.md says what changed"
else
    say "behind: the sync ran but this copy still differs from the live docs; using docs $(local_stamp)"
fi
exit 0
