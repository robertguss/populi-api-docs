# populi-api-docs

A local, LLM-oriented copy of Populi's API2 reference and the `populi-docs` tool
that refreshes it. Read `README.md` for what it does and how.

## If you are here to look something up

Read `llms.txt`, then `reference/endpoints.md`, then the model page. Do not
change anything.

## If you are here to change the tool

- `reference/`, `llms.txt`, and `raw/` are generated. Never edit them by hand.
  Change the parser or renderer, then `uv run populi-docs build` (offline, from
  `raw/`) and read the diff of `reference/`.
- A parser change that alters `reference/catalog.json` shows up as "changes" in
  `populi-docs build` output. Make sure every one is intended; a parser bug must
  not look like a Populi change.
- Keep `sync` safe: nothing is written until the whole fetch has parsed and
  passed `sanity()`.
- `CHANGES.md` entries are written by `sync`; the section below the entries
  marked as hand-written is the only part edited by hand.
- Tests use `tests/pages.py` and `tests/fixtures/`; no network in tests.
- `just test` and `just lint` green before any commit.
- The live site is fetched only by `populi-docs check` and `populi-docs sync`,
  at a quarter second per page. Do not add parallel fetching.

## Commands

`just setup`, `just test`, `just lint`, `just check`, `just sync`, `just build`,
`just diff`.
