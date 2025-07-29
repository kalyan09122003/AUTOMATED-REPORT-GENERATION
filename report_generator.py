import pandas as pd
from fpdf import FPDF

# Read the CSV
df = pd.read_csv("centurions.csv")

# Calculate total 100s
df["Total"] = df["Tests"] + df["ODIs"] + df["T20Is"]
df = df.sort_values(by="Total", ascending=False)

# PDF setup
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, " Cricket Centurions Report", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", "B", 12)
pdf.cell(50, 10, "Player", 1)
pdf.cell(30, 10, "Tests", 1)
pdf.cell(30, 10, "ODIs", 1)
pdf.cell(30, 10, "T20Is", 1)
pdf.cell(30, 10, "Total", 1)
pdf.ln()

pdf.set_font("Arial", "", 12)
for index, row in df.iterrows():
    pdf.cell(50, 10, row["Player"], 1)
    pdf.cell(30, 10, str(row["Tests"]), 1)
    pdf.cell(30, 10, str(row["ODIs"]), 1)
    pdf.cell(30, 10, str(row["T20Is"]), 1)
    pdf.cell(30, 10, str(row["Total"]), 1)
    pdf.ln()

# Save the PDF
pdf.output("centurion_report.pdf")
print("✅ PDF report generated: centurion_report.pdf")
