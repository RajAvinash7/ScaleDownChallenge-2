from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

os.makedirs("data", exist_ok=True)

docs = {
    "admission_policy.pdf": """
Admission Policy 2024

Eligibility:
- Candidates must have passed 12th with minimum 60%.
- Entrance exam score is mandatory.

Important Dates:
- Application opens: 1st June
- Last date: 30th June
""",

    "fee_structure.pdf": """
Fee Structure 2024

B.Tech:
- Tuition Fee: ₹1,20,000 per year
- Hostel Fee: ₹40,000 per year

M.Tech:
- Tuition Fee: ₹1,50,000 per year
""",

    "hostel_rules.pdf": """
Hostel Rules

- Hostel curfew is 10:30 PM.
- Visitors are allowed till 7 PM.
- Ragging is strictly prohibited.
"""
}

for name, content in docs.items():
    c = canvas.Canvas(f"data/{name}", pagesize=A4)
    text = c.beginText(40, 800)
    for line in content.split("\n"):
        text.textLine(line)
    c.drawText(text)
    c.save()

print("PDFs generated successfully!")
