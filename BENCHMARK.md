# BENCHMARK — paleo output savings

Empirical measurement of how much `paleo` compresses agent output, by level.

## Method
- **Sample:** one realistic verbose LLM reply (Python venv setup guide) — prose + verbatim code.
- **Code kept byte-exact** across every mode (per skill rule: never compress code/commands).
- **Metrics:** character count + heuristic token count (words + standalone punctuation). Real BPE ≈ ±10%.
- **Baseline:** same reply, uncompressed.

## Results

| Mode | Chars | Char saved | Tokens ~ | Token saved |
|------|------:|-----------:|---------:|------------:|
| baseline | 652 | — | 140 | — |
| `lite` | 311 | 52.3% | 68 | 51.4% |
| `full` (default) | 239 | 63.3% | 61 | 56.4% |
| `ultra` | 181 | 72.2% | 57 | 59.3% |

Skill claim *"cut output tokens ~60–70%"* → **validated** at `full` / `ultra`.

> Savings scale with baseline verbosity. Code-dominated or already-concise replies save less (nothing left to trim). `paleo` is output-only; pair with `paleo-trim-context` + `paleo-skip-preamble` + `paleo-budget` for whole-session reduction.

## Before / After

### Baseline (verbose)
```
Sure! Here is a complete guide to setting up a Python virtual environment for your project.

First, you will want to make sure that you have Python installed on your system. Then, you can create a new virtual environment by running the command `python3 -m venv myenv`. After that, you should activate it so that your packages stay isolated. On Linux, you would run `source myenv/bin/activate`. On Windows, you would run `myenv\Scripts\activate`. Once activated, you can install packages with `pip install requests`. This keeps your dependencies clean and separate from the system Python.

I hope this helps! Let me know if you have any other questions.
```

### `lite` — trim filler, keep sentences
```
Guide to setting up Python virtual environment.
Ensure Python installed on your system. Create env: `python3 -m venv myenv`. Activate to isolate packages. Linux: `source myenv/bin/activate`. Windows: `myenv\Scripts\activate`. Install deps: `pip install requests`. Keeps dependencies separate from system Python.
```

### `full` (default) — drop articles, tight clauses
```
Setup Python venv.
- Python installed first.
- Create: `python3 -m venv myenv`
- Activate (Linux): `source myenv/bin/activate`
- Activate (Win): `myenv\Scripts\activate`
- Install: `pip install requests`
- Isolates deps from system Python.
```

### `ultra` — subject-verb only, symbols
```
Python venv setup:
- Py installed
- mk: `python3 -m venv myenv`
- act(L): `source myenv/bin/activate`
- act(W): `myenv\Scripts\activate`
- inst: `pip install requests`
- deps != sys
```

## Quality note
Compression targets filler, articles, preamble, and redundant clauses. **Code, CLI commands, error strings, file paths, numbers, and API names stay byte-exact.** The answer is preserved — only verbosity is cut. At `ultra`, explanations may be abbreviated; use `full` / `lite` when nuance matters.

---
paleo v2.2.0
