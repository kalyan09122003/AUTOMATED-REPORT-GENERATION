
## AUTOMATED REPORT GENERATION

COMPANY: CODTECH IT SOLUTIONS

NAME: Guraka kalyan

INTERN ID : CT06DZ415

DOMAIN: PYTHON

DURATION: 6 WEEKS

MENTOR: NEELA SANTHOSH

##  Project Overview

This Python-based project automates the generation of a PDF report that analyzes the top international cricket players with the most career centuries (100s) across Test, ODI, and T20I formats.  
It demonstrates how to process structured data (CSV), calculate statistics, and produce professional reports using the **FPDF** library — with optional visualization.

---

##  Features

-  Reads player data from a CSV (`centuries_split.csv`)  
-  Calculates total centuries across formats  
-  Filters and sorts players based on highest century count  
-  Generates a formatted PDF report (`centuries_report.pdf`) using **FPDF**  

---

## 🛠️ Tech Stack

- Python 3.x  
- **pandas** – Data processing  
- **FPDF** – PDF report generation  
- **matplotlib** – Optional chart visualization  
- CSV input file for player data

---

## 📁 Project Structure

```

cricket-centurions-report/
│
├── centuries_split.csv         # Input data file (Player vs format-wise 100s)
├── report_generator.py         # Script to analyze data and create PDF
├── centuries_report.pdf        # Output PDF report (sample)
└── README.md                   # Project documentation

````

---

##  Setup & Run

### Clone the Repo
```bash
git clone https://github.com/kalyan09122003/AUTOMATED-REPORT-GENERATION.git
cd AUTOMATED-REPORT-GENERATION
````

### Install Dependencies

```bash
pip install pandas fpdf matplotlib
```

### Prepare Input File

Ensure `centuries_split.csv` contains:

```csv
Player,Tests,ODIs,T20Is
Sachin Tendulkar,51,49,0
Virat Kohli,29,51,2
...
```

### Run the Script

```bash
python report_generator.py
```

✅ This runs the analysis and creates `centuries_report.pdf` in the same folder.


## Output
<img width="960" height="540" alt="2025-07-29 (1)" src="https://github.com/user-attachments/assets/19571a27-7385-4efa-9557-adc7148587f8" />

<img width="960" height="443" alt="2025-07-29 (2)" src="https://github.com/user-attachments/assets/0fa2205e-4918-44fd-8281-1479ac4a5b8e" />

<img width="960" height="540" alt="2025-07-29 (3)" src="https://github.com/user-attachments/assets/2dcc4dbc-a373-41bd-9650-637827777f1b" />

