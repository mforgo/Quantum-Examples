![NTC ZCU Kvantová pětka Logo](Media/logo.png)
# Quantum Informatics Notebooks

Collection of educational Jupyter notebooks in quantum computing, developed under NTC Západočeská univerzita’s “Kvantová pětka” initiative.

## Overview

Quantum Informatics Notebooks is a hands-on repository designed to teach and demonstrate core concepts in quantum computing. This living collection of interactive notebooks covers everything from basic quantum gates to advanced algorithms, all built with Qiskit and Python. It is actively developed by the NTC ZCU team as part of the Kvantová pětka program.

## Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-org/quantum-informatics-notebooks.git
   cd quantum-informatics-notebooks
   ```

2. **Create the Conda environment**  
Conda
   ```bash
   conda env create -f environment.yml
   conda activate ntc
   ```
Venv Windows
   ```bash
   python -m venv ./venv/
   .\venv\Scripts\activate.bat
   pip install requirements.txt
   ```
Venv Linux
   ```bash
   python -m venv ./venv/
   python -m venv venv
   pip install requirements.txt
   ```

3. **Launch Jupyter**  
   ```bash
   jupyter notebook
   ```

4. **Open a Notebook**  
   Browse the `notebooks/` directory and select a topic to explore.

## Contributing

This repository is under active development by the NTC ZCU Kvantová pětka team. Contributions are welcome:

1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/your-topic
   ```
3. Add or improve notebooks, documentation, or scripts.  
4. Submit a pull request for review.

Please follow the existing notebook style and include clear explanations for any new material.