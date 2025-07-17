import pandas as pd
from fpdf import FPDF

# Read CSV data
data = pd.read_csv('data.csv')

# Analyze data
average_score = data['Score'].mean()
max_score = data['Score'].max()
min_score = data['Score'].min()
top_scorer = data.loc[data['Score'].idxmax(), 'Name']

# Create PDF Report
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Automated Report', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_summary(self, avg, max_, min_, top):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Average Score: {avg:.2f}', ln=True)
        self.cell(0, 10, f'Highest Score: {max_}', ln=True)
        self.cell(0, 10, f'Lowest Score: {min_}', ln=True)
        self.cell(0, 10, f'Top Scorer: {top}', ln=True)
        self.ln(10)

    def add_table(self, dataframe):
        self.set_font('Arial', 'B', 12)
        self.cell(60, 10, 'Name', 1)
        self.cell(60, 10, 'Score', 1)
        self.ln()
        self.set_font('Arial', '', 12)
        for index, row in dataframe.iterrows():
            self.cell(60, 10, row['Name'], 1)
            self.cell(60, 10, str(row['Score']), 1)
            self.ln()

# Generate and save the PDF
pdf = PDFReport()
pdf.add_page()
pdf.add_summary(average_score, max_score, min_score, top_scorer)
pdf.add_table(data)
pdf.output('report.pdf')

print("Report generated successfully as 'report.pdf'")
