# Supermarket Sales Optimizer

An automated Python tool built to analyze supermarket sales data, evaluate inventory risks, and generate actionable restocking and sales optimization plans.

## Project Features
* **Sales Data Analysis:** Processes sales performance metrics, unit turnover, and stock levels.
* **Output Manager (`output_manager.py`):** Formats analysis results for clean terminal viewing and exports timestamped JSON logs to the `outputs/` directory.
* **Automated Testing (`test_optimizer.py`):** Validates input handling, fallbacks for missing data, and file saving functionality using Python's `unittest` library.
* **Secure Environment:** Built-in `.gitignore` rules to keep sensitive API keys (`.env`) and local data logs out of version control.

## Setup & Running

### 1. Requirements
* Python 3.10+
* `python-dotenv` (if using external API integrations)

### 2. Run the Output Manager
Execute the output manager to display sample sales analysis and export JSON records:
```bash
python output_manager.py