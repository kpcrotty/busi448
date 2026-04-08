# BUSI 448 — Investments Course

## Overview
University course (BUSI 448) on investments/portfolio management. Repository contains lecture slides, class notebooks (Jupyter/Python), Excel files, and syllabus materials.

## Structure
- `class_notebooks/` — Jupyter notebooks covering topics from Python basics through portfolio theory, factor models, fixed income, performance evaluation, and taxes
- `slides/` — Lecture slides
- `excel/` — Excel-based examples
- `images/` — Supporting images
- `course_notes/` — Synthesized course notes (mini-textbook) in Markdown, organized into 23 chapters across 6 parts

## Tech Stack
- Python with Jupyter notebooks
- Key libraries: `yfinance` (stock data), `pandas` (data manipulation), standard finance/data science stack
- Data typically sourced from Yahoo Finance, resampled to monthly frequency
- Returns indexed by `pandas.Period` (monthly)

## Conventions
- Notebook naming: numbered by topic (e.g., `25b_momentum_etf_perfeval.ipynb`)
- Date ranges commonly start from 2000-01-01
- Monthly returns computed from month-end closing prices via `resample("ME").last().pct_change()`
