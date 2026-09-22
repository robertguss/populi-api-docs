---
name: populi-api
description:
  Populi API2 reference, kept fresh. Use whenever work touches the Populi API -
  writing or debugging code that calls it, finding an endpoint, object fields,
  filter conditions, expands, or permissions, handling Populi webhooks, or
  asking what changed in Populi's API.
---

# populi-api: Populi's API2 reference, freshened

The reference is a local copy of <https://populi.co/api/> at
`~/Projects/wts-dops/populi-api-docs` (or `$POPULI_DOCS_ROOT`), rebuilt for
agents and kept current by a weekly GitHub Action in
`robertguss/populi-api-docs`. Populi changes its API without announcing it, so
answer from the reference, freshened, rather than from recall.

## 1. Freshen, once per session

Run `scripts/freshen.sh` from this skill's directory, with a Bash timeout of
five minutes (a sync, when one is needed, takes two or three). It prints one
`populi-docs:` status line:

- `current`: read on.
- `updated`: Populi published a new version and it is now pulled. Read the top
  entry of `CHANGES.md`, and tell the user what changed if it bears on the task.
- `behind`: the copy is older than the live docs and could not be brought level.
  Read on, and tell the user which docs version you read.

Pass any `warning:` line on to the user. Done when the status line is printed.
Later lookups in the same session skip this step; `--force` re-checks.

## 2. Look up

Search the reference in this order, stopping when you have the answer:

1. `reference/endpoints.md`: grep a path fragment or keyword. One line per
   endpoint, linked to its model page.
2. `reference/models/<model>.md`: the object's fields, then every endpoint with
   its parameters, filter conditions, expands, permissions, a curl example, and
   an example response.
3. `reference/overview.md`: what every request shares: auth, the JSON body,
   expands, paging, the `filter` syntax, errors, rate limits.
4. `reference/models/webhooks.md`: events and their payloads.
5. `reference/catalog.json`: the whole reference as JSON, for questions that
   span many endpoints (every endpoint with an `updated_at` filter, every
   endpoint a role can call). Query it with python or jq.
6. `CHANGES.md`, or `uv run populi-docs diff --against <git ref>` in the repo:
   what changed and when.

Done when every Populi path, field, filter condition, and expand in your answer
or code has been found in the reference by grep, and you have named the model
page you used and the docs version from step 1.

## Reading the reference

- Paths are relative to `https://<school>.populiweb.com/api2`; `(name)` in a
  path is an id.
- `filter`, `expand`, and `page` travel in the JSON body, GET requests included;
  `overview.md` shows the shapes.
- The reference is Populi's docs, and the docs have errors: when a live response
  disagrees, the live response wins, and the difference is worth telling the
  user. Known: the `term_updated` webhook's example payload is an online
  payment.
- The reference is generated. A rendering problem is fixed in the repo's parser
  (its `CLAUDE.md` says how), then rebuilt.
