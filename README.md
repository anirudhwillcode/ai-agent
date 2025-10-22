# AI Code Agent — toy agentic code editor (README)

> A small, educational Python project that demonstrates how to build an LLM-powered code agent (think: lightweight Claude Code / Cursor agent).
> The agent uses the Google Gemini API for reasoning + function-calling, runs iterative feedback loops, inspects a codebase, proposes edits, and applies fixes — useful for learning about agent design, safety checks, and developer tooling.

---

## 🔦 What this is

This repo contains a **toy agentic code editor** implemented in Python.
It’s designed as a learning project that demonstrates:

* How to structure a code-fixing agent (observe → propose → execute → verify → iterate).
* Integrating a language model (Gemini) via function-calling to produce structured actions.
* Safe/limited execution of proposed code changes.
* A simple feedback loop for validating fixes (unit tests / lint run / run script).
* Minimal, clear architecture so you can extend it.

This is **not** production-level tooling — it’s an educational reference and prototype.

---

## ✅ Key features

* Agent loop: **Plan → Act → Observe → Reflect → Repeat**.
* Function-calling interface: LLM returns structured actions (e.g., `read_file`, `write_file`, `run_tests`, `run_command`).
* Sandbox execution of changes (configurable).
* Test-driven verification: run project's tests or a custom validation command after edits.
* Configurable max iterations & safety constraints (to avoid runaway edits).
* Logging and change summarization for each iteration.

---

## 📦 Repo layout (example)

```
.
├── agent/                  # core agent code
│   ├── agent.py            # main agent loop
│   ├── llm_client.py       # Gemini wrapper & function-call helpers
│   ├── executor.py         # sandboxed execution, run commands, run tests
│   └── fs_utils.py         # safe file read/write helpers
├── examples/               # demo projects the agent can operate on
├── tests/                  # unit/integration checks for the agent itself
├── README.md
├── requirements.txt
└── .env.example            # environment variables example
```

---

## 🔧 Requirements

* Python 3.10+
* `pip` to install dependencies (see `requirements.txt`)
* A Google Gemini API key (set as `GEMINI_API_KEY` in env or `.env`)
* Optional: `git` if you want agent to commit / branch edits

---

## ⚙️ Installation

```bash
git clone <your-repo-url>
cd ai-code-agent
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows PowerShell
pip install -r requirements.txt

# copy and update .env.example to .env
cp .env.example .env
# put your GEMINI_API_KEY in .env or export to environment:
# export GEMINI_API_KEY="sk-..."
```

`requirements.txt` should include things like:

```
requests
python-dotenv
pytest     # optional, for running tests
# plus any wrapper lib for Gemini if you are using one
```

---

## 🧭 How to use (example)
<img width="1529" height="961" alt="image" src="https://github.com/user-attachments/assets/322c0fa0-6b2c-4c10-b4b5-e25564b502b6" />


```bash
python agent/agent.py \
  --target-dir examples/simple-buggy-app \
  --validate-cmd "pytest -q" \
  --max-iterations 5 \
  --dry-run
```

Flags:
-- verbose - just try and check for yourselves
---


## 🔒 Safety & constraints

* **Max iterations** prevents runaway loops.
* **Dry-run mode** to preview changes.
* **Sandbox/Escrow**: run commands inside a disposable environment or container if you integrate that.
* **Restricted function set**: only allow explicit functions (`read_file`, `write_file`, `run_tests`, `run_command`) — no arbitrary shell execution unless explicitly enabled.
* **Manual review** recommended before merging edits into main branches.

---

## 📝 Example usage snippet (Python)

```python
from agent.agent import CodeAgent

agent = CodeAgent(
    llm_api_key=os.getenv("GEMINI_API_KEY"),
    target_dir="examples/simple-buggy-app",
    validate_cmd="pytest -q",
    max_iterations=5,
    dry_run=True
)

result = agent.run()
print(result.summary())
```

---


## ♻️ Extending the agent

Ideas to add:

* Git integration: create branch, commit, push changes and create a PR.
* CI integration: automatically run full CI pipeline for verification.
* Multi-file patch support with unified diffs.
* Better static analysis: integrate `mypy`, `ruff`, `pylint`.
* Safety policies: restrict edits by path, filename pattern, or file size.
* Interactive mode: human-in-the-loop approval per change.

---
