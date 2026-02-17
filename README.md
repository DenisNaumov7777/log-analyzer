# 🛡️ Syslog Insight: Enterprise Log Analysis Tool

**Syslog Insight** is a high-performance CLI utility designed to parse unstructured system logs, extract critical error metrics, and generate structured reports. It is built for enterprise environments requiring reliable data processing and clear observability of service health.

---

## 🏗️ Architecture Overview

This tool follows an **Object-Oriented Design (OOD)** focused on performance, scalability, and maintainability.

* **🚀 Fast-Path Filtering:** Implements pre-regex string membership checks to minimize CPU cycles when processing large datasets (e.g., 50GB+ log files).
* **🧩 Separation of Concerns:** Distinct layers for data ingestion, business logic (regex-based parsing), and automated reporting.
* **📊 Schema Enforcement:** Utilizes Python `dataclasses` and `defaultdict` structures for robust internal data representation.
* **⚙️ Decoupled Configuration:** Logging behavior is managed via an external `logging.yaml` file, supporting both console output and rotating file handlers for audit compliance.


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

