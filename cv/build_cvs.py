import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, ListFlowable, ListItem

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'cv-data.json').read_text())


def make_pdf(output_path: Path, variant: str):
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=12 * mm,
    )

    styles = getSampleStyleSheet()
    body = ParagraphStyle(
        'Body',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#1A1A1A'),
        wordWrap='CJK',
    )
    heading = ParagraphStyle(
        'Heading',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=24,
        textColor=colors.HexColor('#1A1A1A'),
        spaceAfter=8,
    )
    section = ParagraphStyle(
        'Section',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=13,
        textColor=colors.HexColor('#1A1A1A'),
        borderPadding=2,
        spaceBefore=10,
        spaceAfter=6,
    )
    sub = ParagraphStyle(
        'Sub',
        parent=body,
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#1A1A1A'),
        spaceAfter=3,
    )
    secondary = ParagraphStyle(
        'Secondary',
        parent=body,
        fontName='Helvetica',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#6B6B6B'),
    )

    story = []
    story.append(Paragraph(DATA['name'], heading))
    info_bits = [DATA['email'], DATA['github'], DATA['siteUrl']]
    story.append(Paragraph(' • '.join(info_bits), secondary))
    story.append(Spacer(1, 10))

    story.append(Paragraph('Summary', section))
    story.append(Paragraph(DATA['summary'][variant], body))
    story.append(Spacer(1, 8))

    story.append(Paragraph('Projects', section))
    for project in DATA['projects']:
        story.append(Paragraph(f"{project['name']} — {project['status']}", sub))
        bullets = ListFlowable(
            [ListItem(Paragraph(item, body), leftIndent=16, value='•') for item in project['bullets']],
            bulletType='bullet',
            bulletFontName='Helvetica',
            bulletFontSize=10,
            leftIndent=14,
            spaceAfter=6,
            spacing=6,
        )
        story.append(bullets)

    story.append(Paragraph('Experience', section))
    for item in DATA['experience']:
        story.append(Paragraph(item['role'], sub))
        story.append(Paragraph(item['details'], body))
        story.append(Spacer(1, 4))

    story.append(Paragraph('Education', section))
    for item in DATA['education']:
        story.append(Paragraph(item['title'], sub))
        story.append(Paragraph(item['details'], body))

    story.append(Paragraph('Skills', section))
    for group, values in DATA['skills'].items():
        story.append(Paragraph(f"{group}: {values}", body))

    doc.build(story)


if __name__ == '__main__':
    try:
        import reportlab
    except ImportError as exc:  # pragma: no cover
        raise SystemExit('reportlab is required. Install with: python -m pip install reportlab') from exc

    make_pdf(ROOT / 'Philip-Emoche-Ekele-CV-Developer.pdf', 'developer')
    make_pdf(ROOT / 'Philip-Emoche-Ekele-CV-Ops-Leads.pdf', 'ops')
    print('CVs generated in', ROOT)
