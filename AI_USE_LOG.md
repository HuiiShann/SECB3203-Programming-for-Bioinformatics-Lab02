# AI USE LOG

- Course: SECB3203
- Assessment: Lab2
- Student name: Tan Hui Shan
- Matric no: A24CS0197
- Group ID: n/a
- AI level: 1
- Tools cited: Google. (2026). Gemini. Retrieved 28 October 2026 from https://gemini.google.com, Anthropic (2026). Claude (Claude Sonnet 5.5). Retrieved 28 October 2026 from https://claude.ai

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1
- Date: 28 October 2026, 11:30AM
- Tool: Anthropic (2026). Claude (Claude Sonnet 5.5). Retrieved 28 October 2026 from https://claude.ai
- Purpose: explain, hint
- Prompt: "Guide me from Task 1 to Task 5 step by step. For task 1, what keyword I need to use to keep letters only?"
- Output: Said there is no keyword; use the string method .isalpha() on each character, with .upper() and "".join(). Gave hints for the logic of T1 to T5 and the setup commands, without writing the code.
- Verified by: Tested string methods .isalpha() and .upper() in Python interactive terminal, then ran python -m pytest to confirm clean_sequence passed.
- My change: Wrote clean_sequence and is_valid_dna myself using the hints. No AI code was copied.
- Used in: src/lab02_sequences.py, clean_sequence and is_valid_dna

## Entry 2

- Date: 28 October 2026, 11:40 AM
- Tool: Anthropic (2026). Claude (Claude Sonnet 5.5). Retrieved 28 October 2026 from https://claude.ai
- Purpose: review, debug
- Prompt: "Help me to check for Task 1, any improvement?" + my clean_sequence and is_valid_dna code
- Output: Found a syntax error (the extra "str" in the join expression), suggested consistent spacing, and explained why the empty check must come first and that lower case must be handled in gc_content and transcribe.
- Verified by: Ran python -m pytest and ruff check src in PowerShell to confirm unit tests passed and all syntax errors were resolved.
- My change: Removed the extra "str" and tidied spacing. Kept the rest of my own logic.
- Used in: src/lab02_sequences.py, clean_sequence

## Entry 3

- Date: 28 October 2026, 12:15 PM
- Tool: Anthropic (2026). Claude (Claude Sonnet 5.5). Retrieved 28 October 2026 from https://claude.ai
- Purpose: explain
- Prompt: "is [] means create a new array?"
- Output: Explained that [] creates a list (not an array), and the different meanings of [] (empty list, list with items, indexing, list comprehension).
- Verified by: Ran type([]) in Python interactive terminal to confirm it creates a standard Python list.
- My change: Understanding only. No code was taken.
- Used in: not used directly (helps with find_motif returning a list)

## Entry 4

- Date: 28 October 2026, 12:25 PM
- Tool: Google. (2026). Gemini. Retrieved 28 October 2026 from https://gemini.google.com
- Purpose: review
- Prompt: "Help me to check for the test, and also do you think I should include lower-case for the boundary test? [code snippet of test_lab02_sequences.py provided]"
- Output: Recommended combining lower/mixed-case testing into the boundary test to verify case-insensitivity in find_motif, and corrected indentation/PEP 8 formatting.
- Verified by: Ran python -m pytest to confirm all 8 tests passed and ruff check src returned no errors.
- My change: Updated test_find_motif_boundary_and_case to use mixed-case input "aAaA" and indented all assertion lines.
- Used in: tests/test_lab02_sequences.py
