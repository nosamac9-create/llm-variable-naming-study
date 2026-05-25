# LLM-Generated Variable Names vs. Human-Written Variable Names in Java

Replication package for the CCSW 325 (Software Construction) course project at the University of Jeddah.

**Authors:** Joury Ghorab (2312080), Jana Akkad (2313200), Enas Alqarni (2314104)
**Instructor:** Qamar Naith
**Department:** Software Engineering, College of Computer Science and Engineering, University of Jeddah

## Overview

This study evaluates whether ChatGPT (GPT-4) can generate variable names in Java that match the clarity, readability, and meaningfulness of names written by human developers. We curated 25 Java snippets containing 132 variables, replaced the original identifiers with generic placeholders (`v1`, `v2`, …), asked GPT-4 to suggest new names, and then compared the LLM suggestions to the originals using both automatic metrics and a blinded human survey.

## Repository Structure

```
.
├── README.md                 # This file
├── snippets/
│   ├── original/             # 25 Java snippets with original (human) variable names
│   └── obfuscated/           # Same 25 snippets with names replaced by v1, v2, ...
├── scripts/
│   ├── obfuscate.py          # Script that produces obfuscated/ from original/
│   └── evaluate.py           # Computes exact match and edit-distance metrics
├── llm_outputs/
│   └── gpt4_responses.json   # Raw API responses from GPT-4 (3 runs per snippet)
├── survey/
│   ├── survey_instrument.md  # The blinded survey shown to participants
│   └── responses.csv         # Anonymized responses from 8 participants
├── results/
│   ├── automatic_metrics.csv # Per-variable exact match and NEDS scores
│   ├── survey_summary.csv    # Aggregated Likert and preference data
│   └── prompt.txt            # The final prompt used for the experiment
├── report/
│   └── CCSW325_Final_Report.pdf   # Full course project report

## How to Reproduce

1. **Obfuscate the dataset:**
   ```bash
   python scripts/obfuscate.py snippets/original snippets/obfuscated
   ```

2. **Run GPT-4 on each obfuscated snippet** using the prompt in `results/prompt.txt`. Generation parameters: `model=gpt-4`, `temperature=0.2`, three runs per snippet, take the modal name.

3. **Compute automatic metrics:**
   ```bash
   python scripts/evaluate.py snippets/original llm_outputs/gpt4_responses.json
   ```

4. **Survey results** in `survey/responses.csv` were collected using the instrument in `survey/survey_instrument.md` from 8 Software Engineering students.

## Headline Results

| Metric | Value |
|--------|-------|
| Exact Match Rate | 23.9% (27/113) |
| Semantic Similarity (NEDS ≥ 0.6 or shared head noun) | 70.8% (80/113) |
| Mean NEDS | 0.51 |
| Convention Compliance | 96.2% |
| Survey Preference (LLM vs. Human vs. None) | 47.5% / 38.0% / 14.5% |

See the project report (`CCSW325_Final_Report.pdf`) for the full discussion.

## License

The Java snippets in `snippets/original/` were either drawn from open-source repositories under permissive licenses or written by the authors for this study. All experimental artifacts (scripts, results, survey data) are released for academic, non-commercial use.
