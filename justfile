default:
    @just --list

# Install everything, including dev tools.
setup:
    uv sync

test:
    uv run pytest -q

lint:
    uv run ruff check src tests
    uv run ruff format --check src tests

# Is the live reference newer than this copy? One request.
check:
    uv run populi-docs check

# Fetch the live reference and rebuild everything if it changed.
sync *ARGS:
    uv run populi-docs sync {{ARGS}}

# Rebuild reference/ and llms.txt from raw/, offline. For parser work.
build:
    uv run populi-docs build

# What changed in the reference since a git ref (default HEAD).
diff *ARGS:
    uv run populi-docs diff {{ARGS}}
