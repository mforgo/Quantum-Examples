# Quantum Examples

![NTC logo](./Media/logo.png)

A collection of educational Jupyter notebooks for learning quantum computing, developed under NTC Západočeská univerzita’s “Kvantová pětka” initiative.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Qiskit](https://img.shields.io/badge/Qiskit-enabled-632CA6.svg)

## Overview

Quantum Examples is a hands-on repository designed to teach and demonstrate core concepts in quantum computing. The interactive notebooks cover topics from basic quantum gates to advanced algorithms.

## Getting Started

### 1) Clone the repository
```bash
git clone https://github.com/your-org/quantum-informatics-notebooks.git
cd quantum-informatics-notebooks
```

### 2) Set up the environment

Choose one of the options below.

- Conda (recommended)
  ```bash
  conda env create -f environment.yml
  conda activate ntc
  ```

- Python venv (Windows)
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  pip install -r requirements.txt
  ```

- Python venv (Linux/macOS)
  ```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

### 3) Launch Jupyter
```bash
jupyter notebook
```

### 4) Open a notebook
Browse the notebooks/ directory and open a topic of interest.

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-topic
   ```
3. Add or improve notebooks, documentation, or helper scripts.
4. Ensure notebooks run top-to-bottom without errors and include clear explanations.
5. Submit a pull request for review.

Guidelines:
- Follow the existing notebook style (headings, explanations, code-cell length).
- Prefer small, focused notebooks over very long ones.
- Include minimal working examples and references when adding new topics.
- If adding dependencies, update environment.yml and requirements.txt consistently.

## Requirements

- Python 3.10+ (recommended)
- Jupyter Notebook or JupyterLab
- Qiskit and scientific Python stack (installed via environment.yml or requirements.txt)

## Support and Contact

For issues, questions, or suggestions, please open an issue in the repository or submit a pull request. If this is part of an internal NTC ZČU initiative, follow the team’s standard contribution workflow.