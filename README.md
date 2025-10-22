
# AI AGENT

If you've ever used Cursor or Claude Code as an "agentic" AI editor, you'll understand what is this project.

We're building a toy version of Claude Code using Google's free Gemini API! As long as you have an LLM at your disposal, it's actually surprisingly simple to build a (somewhat) effective custom agent.

---

## What Does the Agent Do?

The program we're building is a CLI tool that:

* Accepts a coding task (e.g., `"strings aren't splitting in my app, pweeze fix 🥺👉🏽👈🏽"`)
* Chooses from a set of predefined functions to work on the task, for example:

  * Scan the files in a directory
  * Read a file's contents
  * Overwrite a file's contents
  * Execute the Python interpreter on a file
* Repeats step 2 until the task is complete (or it fails miserably, which is possible)

---

### Example

For example, I have a buggy calculator app, so I used my agent to fix the code:

```
> uv run main.py "fix my calculator app, its not starting correctly"
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. The output shows the expression and the result in a formatted way.
```

---

## What Does the Agent Do?

The program we're building is a CLI tool that:

* Accepts a coding task (e.g., `"strings aren't splitting in my app, pweeze fix 🥺👉🏽👈🏽"`)
* Chooses from a set of predefined functions to work on the task, for example:

  * Scan the files in a directory
  * Read a file's contents
  * Overwrite a file's contents
  * Execute the Python interpreter on a file
* Repeats step 2 until the task is complete (or it fails miserably, which is possible)

---

### Example

For example, I have a buggy calculator app, so I used my agent to fix the code:

```
> uv run main.py "fix my calculator app, its not starting correctly"
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. The output shows the expression and the result in a formatted way.
```

---

## Prerequisites

* Python 3.10+ installed (see the bookbot project for help if you don't already have it)
* uv project and package manager
* Access to a Unix-like shell (e.g. zsh or bash)

---
## How To Setup 

Here’s your setup guide formatted neatly for a **GitHub README.md** section — ideal for the “Getting Started” or “Setup Instructions” part of your project:

---

## 🧠 Getting Started

Follow these steps to set up and test the project after forking it.

---

### 1. 🚀 Clone and Set Up Environment

```bash
# Clone your forked repository
git clone <your-fork-url>
cd ai-agent

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

---

### 2. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. 🔐 Set Up API Key

```bash
# Create a .env file
touch .env

# Add your Gemini API key to the file
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

> 💡 You can get your Gemini API key from [Google AI Studio](https://aistudio.google.com/).

---

### 4. 🧪 How To check the working of the agent ? 
SCENARIO :- 

Manually update calculator/pkg/calculator.py and change the precedence of the + operator to 3.
Run the calculator app, to make sure it's now producing incorrect results: 
uv run calculator/main.py "3 + 7 * 2" (this should be 17, but because we broke it, it says 20)
Run your agent, and ask it to "fix the bug: 3 + 7 * 2 shouldn't be 20"


### 📁 Project Structure

```
ai-agent/
│
├── calculator/
│   ├── calculator.py        # Calculator logic
│   ├── tests.py             # Unit tests
│
├── functions/               # Utility functions
│
├── main.py                  # Main interface
├── requirements.txt
├── .env                     # Environment variables
└── pyproject.toml
```

---

### 🧩 Troubleshooting

If you encounter issues, check:

* Python version → `python --version`
* Virtual environment activation
* `.env` file setup
* Dependency installation → `pip list`


