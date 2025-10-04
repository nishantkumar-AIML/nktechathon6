# utils/report_generator.py
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_report(df, out_path):
    doc = SimpleDocTemplate(out_path, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []
    elements.append(Paragraph("Provider Directory Validation Report", styles['Title']))
    elements.append(Spacer(1, 12))
    summary = f"Total Providers: {len(df)} | Verified: {len(df[df.status=='VERIFIED'])} | Review: {len(df[df.status=='REVIEW'])} | Manual: {len(df[df.status=='MANUAL_CHECK'])}"
    elements.append(Paragraph(summary, styles['Normal']))
    elements.append(Spacer(1, 12))

    cols = ['id','name','city','phone','validated_phone','address','validated_address','confidence','status']
    table_data = [cols]
    for _, row in df.head(50).iterrows():
        table_data.append([row.get(c) for c in cols])

    t = Table(table_data, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#d3d3d3')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('FONT', (0,0), (-1,0), 'Helvetica-Bold'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    elements.append(t)
    doc.build(elements)
