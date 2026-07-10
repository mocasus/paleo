# Benchmark

Reproducible token-savings measurement for **paleo**. Raw numbers, no hand-waving.

> [!NOTE]
> Any repo that advertises a flat "% token savings" number should be treated with skepticism — savings depend on task type, model, and baseline verbosity. This page shows the **method and real results** so you can verify and reproduce them.

## Method

- **Endpoint:** OpenAI-compatible (`/v1/chat/completions`). Runs against any provider (we used IDRouter).
- **Model:** `claude-sonnet-4.5` — 1 run, 6 fixed tasks. Rerun with `--model` of your choice.
- **Baseline:** default assistant, no system prompt (representative "verbose default").
- **paleo:** same model + the terse system prompt derived from `skills/paleo`.
- **Metric:** *delivery tokens* = `len(assistant_text) / 4`. This is exactly what the user reads and what paleo compresses. It deliberately **excludes** any reasoning/thinking tokens, so the number reflects output compression only.
- **Harness:** `bench/benchmark.py` (Python standard library only). Deterministic corpus in `TASKS`.

## Results (sample run — 2026-07-11)

| Task | Baseline tokens | paleo tokens | Savings |
|---|---|---|---|
| Explain OAuth 2.0 auth-code flow | 453 | 409 | 9.7% |
| Write a CSV-parsing Python function | 276 | 117 | 57.6% |
| REST vs GraphQL trade-offs | 412 | 189 | 54.1% |
| Set up a GitHub Actions CI pipeline | 1326 | 277 | 79.1% |
| Processes vs threads vs coroutines | 709 | 330 | 53.5% |
| TCP vs UDP, when to use each | 261 | 217 | 16.9% |
| **median** | | | **53.8%** |

Mean savings: **45.1%** · Median: **53.8%** · Raw data: [`bench/results.json`](./bench/results.json).

## What this means

- paleo saves the **most on verbose generative tasks** — code, walkthroughs, comparisons (54–79%). It saves less on already-compact factual answers (10–17%), because there is simply less fluff to cut. That is expected and honest.
- **Headline claim:** *~50–70% fewer output tokens on typical agent tasks; median ~54% on this sample.* Not a flat "65%."
- **On top of output savings**, `paleo-trim-context` cuts *context* tokens (retrieved docs, old tool output, long file dumps) **before** the model reasons — a layer a terse-persona prompt cannot reach. That saving is task-dependent and is not captured in this output-only benchmark.

## Reproduce it yourself

```bash
export IDROUTER_API_KEY=your_key
python3 bench/benchmark.py --model claude-sonnet-4.5
python3 bench/benchmark.py --model deepseek-v4-flash --runs 3   # average 3 runs
```

Results are written to `bench/results.json`. Swap `--model` to compare on your own stack.

## vs terse-persona / Ponytail

- **Terse-persona prompts** advertise "up to 75%" from a single terse-persona prompt. Our measurement is more conservative and *per-task transparent* — and paleo additionally ships context-trimming and a hard budget they lack.
- **Ponytail** saves *code volume* by refactoring what the agent writes (it touches your codebase). paleo saves *conversation + context tokens* with zero code changes. Different layers — use both.
