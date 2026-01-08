<!-- Auto-generated guidance for AI coding agents; keep concise and actionable -->
# Copilot / AI Agent Instructions — 100 Days of Python

Purpose
- Provide focused, actionable guidance for an AI coding agent working in this repository.

Repository snapshot (discoverable)
- This repo is a small collection of single-file daily exercises; current root contains `Day01.py` (empty).
- No package structure, build system, test suite, or CI config detected in the workspace.

Big picture
- Single-file exercises named with the pattern `DayNN.py` at repository root (e.g. `Day01.py`).
- Each file is expected to run as a standalone script. There are no service boundaries, servers, or external integrations present.

Immediate developer workflows (what works here)
- Run a day script locally with the system Python interpreter. Example (PowerShell):

```powershell
python "Day01.py"
```

- There are no tests/CI files detected; validate changes by running modified or new `DayNN.py` files locally.

Project-specific conventions and patterns to follow
- File naming: follow existing `DayNN.py` pattern when adding new exercises.
- Keep changes minimal and additive: add new `DayNN.py` files rather than reorganizing the repository.
- Use a `if __name__ == "__main__":` guard for runnable behavior so imports remain safe when files are used as modules.

What NOT to assume
- Do not assume presence of a virtual environment, requirements.txt, or any external services.
- Do not create large framework scaffolding (packages, CI) without explicit user approval.

When editing or creating files
- Prefer small, self-contained commits focused on a single day's exercise.
- If adding dependencies, also add a `requirements.txt` and include a one-line run example in the new file's header.

Key files to reference
- Day files in repo root (e.g. `Day01.py`) — entrypoints for exercises and examples.

Merge guidance
- If `.github/copilot-instructions.md` already exists, merge by preserving any author notes in the top sections and append/update the "Repository snapshot" and "Big picture" sections with concrete findings from the workspace.

If you need clarification
- Ask whether the user prefers a single-file exercise layout to be preserved, or if they want consolidation into a package structure.

Next step for humans or agents
- Create new `DayNN.py` files for additional exercises and run them locally for validation; return here and update this file if the repository structure changes.
