# Code Agent Test Repository

This repository is designed to **evaluate [potproject/code-agent](https://github.com/potproject/code-agent)**.

## Contents

- **backend/** – Small Flask API with known bugs and TODOs
- **frontend/** – Simple JavaScript app with a logic bug
- **utils/** – Functions with refactoring opportunities
- **tests/** – Unit tests (some failing by design)

## How to Use

1. Fork this repo to your GitHub account.
2. Add the required secrets:
   - `ANTHROPIC_API_KEY`
   - `OPENAI_API_KEY`
3. Create an issue or PR, then comment with:
   - `/claude fix bug in backend/app.py`
   - `/codex refactor utils/math_utils.py`
   - `/claude add tests for frontend/script.js`

The agent should propose commits or PRs automatically.

## Goal

Use this repo to test:

- Bug fixing
- Feature implementation
- Refactoring
- Test generation
- Documentation updates
