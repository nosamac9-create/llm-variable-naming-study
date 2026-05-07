"""
Computes exact match and normalized edit distance similarity (NEDS) between
the original (human) variable names and the LLM-generated names.

Usage:
    python evaluate.py snippets/original llm_outputs/gpt4_responses.json
"""
import json
import os
import sys
import csv


def levenshtein(a, b):
    if len(a) < len(b):
        return levenshtein(b, a)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a):
        curr = [i + 1]
        for j, cb in enumerate(b):
            ins = prev[j + 1] + 1
            dele = curr[j] + 1
            sub = prev[j] + (ca != cb)
            curr.append(min(ins, dele, sub))
        prev = curr
    return prev[-1]


def neds(a, b):
    """Normalized Edit Distance Similarity, between 0 and 1."""
    if not a and not b:
        return 1.0
    return 1.0 - levenshtein(a.lower(), b.lower()) / max(len(a), len(b))


def main(orig_dir, llm_json):
    with open(llm_json) as f:
        llm_data = json.load(f)

    rows = [["snippet", "placeholder", "human_name", "llm_name", "exact_match", "neds"]]
    em_count = 0
    sem_count = 0
    total = 0
    neds_sum = 0.0

    for snippet in sorted(llm_data["snippets"], key=lambda s: s["file"]):
        for var in snippet["variables"]:
            human = var["human_name"]
            llm = var["llm_name"]
            em = int(human.lower() == llm.lower())
            score = neds(human, llm)
            sem = int(score >= 0.6 or var.get("shared_head_noun", False))
            rows.append([snippet["file"], var["placeholder"], human, llm, em, f"{score:.3f}"])
            em_count += em
            sem_count += sem
            neds_sum += score
            total += 1

    out = "results/automatic_metrics.csv"
    with open(out, "w", newline="") as f:
        csv.writer(f).writerows(rows)

    print(f"Total variables       : {total}")
    print(f"Exact match rate      : {em_count}/{total} = {em_count/total*100:.1f}%")
    print(f"Semantic similarity   : {sem_count}/{total} = {sem_count/total*100:.1f}%")
    print(f"Mean NEDS             : {neds_sum/total:.2f}")
    print(f"Wrote per-variable scores to {out}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
