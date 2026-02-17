### 📄 README.md (Professional Technical Version)

```markdown
# 🛡️ Syslog Insight: Enterprise Log Analysis Tool

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-black?style=for-the-badge)
![Security](https://img.shields.io/badge/GPG-Verified%20Commits-brightgreen?style=for-the-badge)

**Syslog Insight** is a high-performance CLI utility designed to parse unstructured system logs, extract critical error metrics, and generate structured reports. It is built for environments requiring reliable data processing and clear observability.

---

## 🏗️ Architecture Overview

This tool follows an **Object-Oriented Design** focused on performance and maintainability:

* **Fast-Path Filtering:** Implements pre-regex string membership checks to minimize CPU cycles when processing large datasets (e.g., 50GB+ log files).
* **Separation of Concerns:** Distinct layers for data ingestion, business logic (parsing), and reporting.
* **Schema Enforcement:** Utilizes Python `dataclasses` for structured internal data representation.
* **Decoupled Configuration:** Logging behavior is managed via an external `logging.yaml` file, supporting both console output and rotating file handlers.

---

## 📂 Project Structure

```bash
log-analyzer/
├── 📂 src/               # Core source code package
│   ├── __init__.py
│   └── analyzer.py       # EnterpriseLogAnalyzer implementation
├── .gitignore            # Git exclusion rules
├── LICENSE               # Apache 2.0 License
├── logging.yaml          # External logging configuration
├── main.py               # CLI entry point and argument parsing
├── README.md             # Technical documentation
└── requirements.txt      # Project dependencies

```

---

## ⚡ Installation

### Prerequisites

* Python 3.10 or higher.
* pip (Python package manager).

### Setup

1. Clone the repository:
```bash
git clone [https://github.com/DenisNaumov7777/log-analyzer.git](https://github.com/DenisNaumov7777/log-analyzer.git)
cd log-analyzer

```


2. Install required dependencies:
```bash
pip install -r requirements.txt

```



---

## 🎮 Usage

The tool is operated via the command line. You must provide an input file and can optionally specify an output destination.

### Run Analysis

```bash
python main.py --input path/to/syslog.log --output report.csv

```

### View CLI Options

```bash
python main.py --help

```

---

## 🔧 Logging & Observability

The application uses a dual-stream logging strategy:

* **Console:** Displays high-level `INFO` status updates during execution.
* **File (`app.log`):** Captures detailed `DEBUG` information and stack traces for technical auditing.

Configuration can be modified in `logging.yaml` without changing the source code.

---

## 📜 License

Distributed under the **Apache License, Version 2.0**. See the [LICENSE]() file for the full legal text.

**Copyright © 2026 Denis Naumov**

