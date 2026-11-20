# Copilot instructions for viikko4/tdd-ostoskori

## Scope

These instructions apply to the `tdd-ostoskori` TDD exercise in `viikko4/tdd-ostoskori/`. Commands below are run from that directory unless stated otherwise.

## Build and test commands

The project uses `uv` and declares pytest 9 in `pyproject.toml`. It requires Python 3.14 or newer.

```bash
cd viikko4/tdd-ostoskori
uv sync
uv run pytest
```

Run one test file:

```bash
uv run pytest -q src/tests/ostoskori_test.py
```

Run one test method:

```bash
uv run pytest -q src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa
```

There is no configured lint or formatting command.

## Architecture

This is a small Python exercise with all implementation modules in `src/`:

- `Tuote` is a product with an immutable name and price exposed by `nimi()` and `hinta()`.
- `Ostos` wraps one `Tuote` and tracks quantity with `lukumaara()`. Quantity changes use `muuta_lukumaaraa(muutos)` and never go below zero; `hinta()` returns quantity multiplied by the product price.
- `Ostoskori` is the main exercise area. It currently has only method signatures and stubs; adding behavior and tests is the intended TDD work.
- `index.py` is a placeholder and contains no runnable exercise logic.

`Ostoskori` is expected to coordinate `Ostos` and `Tuote` objects. Its public methods in `src/ostoskori.py` are:

- `tavaroita_korissa()`
- `hinta()`
- `lisaa_tuote(lisattava)`
- `poista_tuote(poistettava)`
- `tyhjenna()`
- `ostokset()`

## Conventions

- Tests use Python's `unittest` style under `src/tests/` and pytest is the runner.
- Put shared setup for a test class in `setUp()`.
- Import exercise modules directly by name (for example `from ostoskori import Ostoskori`) from the pytest working directory.
- Preserve the existing method and return types while implementing `Ostoskori`; many methods are intentionally left incomplete.
- Do not edit `src/ostos.py` or `src/tuote.py`; treat both as fixed supporting code.
- Do not edit tests unless the user explicitly asks.
- Implement only the minimal code needed to make the current tests pass.
- `Tuote` must be constructed as `Tuote(nimi, hinta)`. `Ostos` must be constructed with a `Tuote`.
- Use Finnish domain and method names consistently with the existing exercise API.
- Work in small TDD steps: add or update a focused test, run it, implement the smallest behavior needed, then rerun the test and the full suite.
