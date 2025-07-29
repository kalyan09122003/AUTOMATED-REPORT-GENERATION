
## AUTOMATED REPORT GENERATION

COMPANY: CODTECH IT SOLUTIONS

NAME: Guraka kalyan

INTERN ID : CT06DZ415

DOMAIN: PYTHON

DURATION: 6 WEEKS

MENTOR: NEELA SANTHOSH

Here’s a polished and professional **`README.md`** tailored for your **Cricket Centurions Analysis** project, inspired by GitHub standards and best practices:

---


## Cricket Centurions Analysis – Automated Report Generation

**Internship Project – CodTech IT Solutions**

**Intern:** Guraka Kalyan (Intern ID: CT06DZ415)  
**Domain:** Python Development | **Mentor:** Neela Santhosh | **Duration:** 6 Weeks

---

## 📌 Project Overview

This Python-based project automates the generation of a PDF report that analyzes the top international cricket players with the most career centuries (100s) across Test, ODI, and T20I formats.  
It demonstrates how to process structured data (CSV), calculate statistics, and produce professional reports using the **FPDF** library — with optional visualization.

---

## 🎯 Features

- ✅ Reads player data from a CSV (`centuries_split.csv`)  
- ✅ Calculates total centuries across formats  
- ✅ Filters and sorts players based on highest century count  
- ✅ Generates a formatted PDF report (`centuries_report.pdf`) using **FPDF**  
- 📊 *(Optional)* Generates bar charts for top performers using **matplotlib**

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
├── centuries\_split.csv         # Input data file (Player vs format-wise 100s)
├── report\_generator.py         # Script to analyze data and create PDF
├── centuries\_report.pdf        # Output PDF report (sample)
└── README.md                   # Project documentation

````

---

## 🚀 Setup & Run

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

---

## Output
<img width="960" height="540" alt="2025-07-29 (1)" src="https://github.com/user-attachments/assets/19571a27-7385-4efa-9557-adc7148587f8" />


[centurion_report.pdf](https://github.com/user-attachments/files/21490518/centurion_report.pdf)
