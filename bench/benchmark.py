#!/usr/bin/env python3
"""
paleo benchmark harness — reproducible token-savings measurement.

Compares a BASELINE (default verbose assistant) vs PALEO (terse system prompt
derived from skills/paleo + skills/paleo-skip-preamble) on a fixed task corpus.

Metric: delivery tokens = len(assistant_content) / 4  (matches how paleo
compresses what the user actually reads; excludes any reasoning/thinking tokens).

Usage:
  export IDROUTER_API_KEY=...        # or pass --api-key
  python3 bench/benchmark.py --model claude-sonnet-4.5
  python3 bench/benchmark.py --model deepseek-v4-flash --runs 3

Requires only the Python standard library (urllib). OpenAI-compatible endpoint.
"""
import argparse
import json
import os
import statistics
import sys
import urllib.request

PALEO_SYSTEM = (
    "You are a terse technical assistant. Rules:\n"
    "- Drop filler: no 'Sure!', 'Here is', 'Let me', no apologies, no hedging.\n"
    "- Short clauses. One idea per line. Bullets over paragraphs.\n"
    "- Keep verbatim: code, CLI commands, API names, error strings, file paths, numbers.\n"
    "- No greetings, apologies, or meta-commentary. Lead with the answer.\n"
    "- Explain only if explicitly asked.\n"
)

# Fixed corpus: tasks that naturally produce verbose answers.
TASKS = [
    "Explain how OAuth 2.0 authorization code flow works, step by step.",
    "Write a Python function to parse a CSV file into a list of dicts, with a short explanation of each part.",
    "Summarize the trade-offs between REST and GraphQL for a beginner backend engineer.",
    "Walk me through setting up a CI pipeline with GitHub Actions, including a sample workflow.",
    "What are the differences between processes, threads, and coroutines? Give a concrete example of each.",
    "Explain the difference between TCP and UDP, and when you would use each. Keep it practical.",
]


def chat(api_base, api_key, model, system, user, timeout=120):
    url = api_base.rstrip("/") + "/chat/completions"
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": user})
    body = json.dumps({
        "model": model,
        "messages": messages,
        "temperature": 0.2,
        "max_tokens": 1200,
    }).encode()
    req = urllib.request.Request(url, data=body, headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=timeout) as r:
        resp = json.load(r)
    content = resp["choices"][0]["message"]["content"]
    usage = resp.get("usage", {})
    return content, usage


def delivery_tokens(content):
    return max(1, len(content) // 4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--api-base", default="https://id.solution.qzz.io/v1")
    ap.add_argument("--api-key", default=None)
    ap.add_argument("--model", default="claude-sonnet-4.5")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--out", default="bench/results.json")
    args = ap.parse_args()

    api_key = args.api_key or os.environ.get("IDROUTER_API_KEY")
    if not api_key:
        sys.exit("API key required: set IDROUTER_API_KEY or pass --api-key")
    rows = []
    for task in TASKS:
        base_chars = paleo_chars = 0
        base_api = paleo_api = 0
        for _ in range(args.runs):
            b_content, b_usage = chat(args.api_base, api_key, args.model, None, task)
            p_content, p_usage = chat(args.api_base, api_key, args.model, PALEO_SYSTEM, task)
            base_chars += len(b_content)
            paleo_chars += len(p_content)
            base_api += b_usage.get("completion_tokens", delivery_tokens(b_content))
            paleo_api += p_usage.get("completion_tokens", delivery_tokens(p_content))
        base_dt = base_chars // 4
        paleo_dt = paleo_chars // 4
        save = (base_dt - paleo_dt) / base_dt * 100 if base_dt else 0
        rows.append({
            "task": task[:48] + ("…" if len(task) > 48 else ""),
            "baseline_delivery_tokens": base_dt,
            "paleo_delivery_tokens": paleo_dt,
            "savings_pct": round(save, 1),
            "baseline_api_tokens": base_api // args.runs,
            "paleo_api_tokens": paleo_api // args.runs,
        })

    savings = [r["savings_pct"] for r in rows]
    summary = {
        "model": args.model,
        "runs": args.runs,
        "tasks": len(TASKS),
        "median_savings_pct": round(statistics.median(savings), 1),
        "mean_savings_pct": round(statistics.mean(savings), 1),
        "rows": rows,
    }
    with open(args.out, "w") as f:
        json.dump(summary, f, indent=2)

    # Print markdown table
    print(f"\n# paleo benchmark — model `{args.model}`, {args.runs} run(s), {len(TASKS)} tasks\n")
    print("| Task | Baseline tokens | paleo tokens | Savings |")
    print("|---|---|---|---|")
    for r in rows:
        print(f"| {r['task']} | {r['baseline_delivery_tokens']} | {r['paleo_delivery_tokens']} | **{r['savings_pct']}%** |")
    print("| | | **median** | **" + f"{summary['median_savings_pct']}%" + "** |")
    print(f"\nMean savings: {summary['mean_savings_pct']}%  ·  Median: {summary['median_savings_pct']}%")
    print(f"Results written to {args.out}")


if __name__ == "__main__":
    main()
