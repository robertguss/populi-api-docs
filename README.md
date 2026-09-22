# populi-api-docs

A local copy of Populi's API2 reference (<https://populi.co/api/>), rebuilt for
LLMs and agents, and the `populi-docs` tool that keeps it current. One copy for
every WTS project that calls Populi, instead of a stale copy in each.

Populi changes its reference without announcing it. Between the copy synced on
2026-07-31 and the site of 2026-09-21 it added three models, thirteen endpoints,
a `deleted_at` filter on people, organizations, and custom data, and new fields
on five objects. Each sync here records changes like that in
[CHANGES.md](CHANGES.md), and git keeps the history.

## For agents: where to look

Start at [llms.txt](llms.txt). Then:

| file                           | what it holds                                                                                                                                        |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `reference/overview.md`        | Populi's introduction: auth, request format, expands, paging, filter conditions, errors, rate limits                                                 |
| `reference/endpoints.md`       | every endpoint on one line, sorted by path, linked to its model page                                                                                 |
| `reference/models/<model>.md`  | one model: its object's fields, then each endpoint with parameters, filter conditions, expands, permissions, a curl example, and an example response |
| `reference/models/webhooks.md` | webhook setup, the event list, and every event's example payload                                                                                     |
| `reference/catalog.json`       | the same reference as JSON for programs (no examples, no prose)                                                                                      |
| `CHANGES.md`                   | what changed in Populi's reference, per sync, newest first                                                                                           |

Everything under `reference/`, plus `llms.txt`, is generated. Do not edit it by
hand; fix the parser and rebuild.

## Using the tool

```sh
just setup                 # uv sync
uv run populi-docs check   # is the live reference newer? exit 0 no, 1 yes
uv run populi-docs sync    # fetch and rebuild if it changed; --force to refetch
uv run populi-docs build   # rebuild reference/ from raw/, offline (parser work)
uv run populi-docs diff    # changes to the reference since a git ref (default HEAD)
```

`sync --commit` commits the result. To run `populi-docs` from anywhere, install
it once with `uv tool install --editable .` from this directory.

A sync reads one page to compare Populi's "documentation updated on" stamp with
`raw/meta.json`, and stops there if they match. When the stamp has moved, it
fetches all 178 pages (about 50 seconds, a quarter second apart), parses them,
and checks the result before writing anything: at least 100 models and 400
endpoints, no page that parses to nothing, and no drop of more than 5% from the
last copy. A failed check writes nothing and leaves the fetched pages in
`.sync-tmp/raw` for inspection; `--allow-shrink` overrides it when the change is
real.

## Keeping it current

GitHub Actions is the only writer. `.github/workflows/sync.yml` runs every
Monday (and on demand from the Actions tab, with an optional force refetch): it
runs the tests, then `populi-docs sync --commit`, then pushes. An unchanged week
costs one request to Populi and makes no commit. A failed sanity check fails the
run, writes nothing, and keeps the rejected pages as a run artifact for 14 days.

Local checkouts only `git pull`. The `populi-api` Claude Code skill pulls,
compares the live docs stamp with the repo's, and dispatches the workflow when
Populi is ahead, so a change lands between Mondays when someone needs it. A
local `populi-docs sync` works too, but its commit would race the workflow's.

GitHub disables scheduled workflows after 60 days without repository activity,
which can happen here when Populi publishes nothing for two months. The skill
re-enables the workflow before it dispatches it.

## The populi-api skill

`skill/populi-api/` is a Claude Code skill: agents reach for it whenever work
touches the Populi API. It freshens the copy once per session with
`scripts/freshen.sh` (pull; compare stamps; dispatch the workflow and pull again
if Populi is ahead; skip all of it if a check succeeded in the last 12 hours),
then looks things up in the order `endpoints.md`, model page, overview,
webhooks, `catalog.json`. The dispatch path needs `gh`, logged in.

Install it once by linking it into your skills:

```sh
ln -s "$PWD/skill/populi-api" ~/.claude/skills/populi-api
```

The script assumes the checkout is at `~/Projects/wts-dops/populi-api-docs`; set
`POPULI_DOCS_ROOT` if it lives elsewhere (it clones there if missing).

## How it works

The site is a static Slate site with one page per model. Every page has the same
shape, and the parser reads it structurally instead of converting HTML to
Markdown wholesale:

- `h2` "The X object": a JSON example and an Attribute, Required, Data Type
  table.
- `h2` per action (index, show, create, ...): six code tabs, a description, then
  `h3` sections for HTTP Request, Parameters, Filter Condition Parameters,
  Action Parameters, Expandable Properties, and Permissions.
- The Webhooks page: guide prose, an Event/Name table, and one section per event
  with its payload.

Of the six code tabs, the curl and JSON ones are kept; Ruby, Python, C#, and PHP
are dropped. Anything the parser does not recognise is kept as Markdown and
reported as a warning in `catalog.json`, never dropped.

The change report compares catalogs, not text: models, endpoints, fields,
parameters, filters, expands, permissions, and webhook events, plus which
endpoint descriptions were reworded. Examples are not compared, because Populi's
examples carry random ids and timestamps that change on every build of their
site.

`raw/` keeps the pages exactly as fetched, so the reference can be rebuilt when
the parser improves and any line can be checked against its source.

## Layout

```
llms.txt              entry point for agents (generated)
reference/            the generated reference
raw/                  the pages as fetched, with meta.json (stamp, time, hashes)
CHANGES.md            per-sync change log (generated entries)
src/populi_docs/      fetch, parse, html2md, render, diff, sync, cli
tests/                parser, diff, and pipeline tests; no network
```
