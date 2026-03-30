from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOADS_DIR = os.path.join(BASE_DIR, 'uploads')
PDF_FONT_NAME = 'GeoUnicode'
LOGO_PATH_CANDIDATES = [
    os.path.join(BASE_DIR, 'Baumer-Logo.png'),
    os.path.join(BASE_DIR, 'baumer-logo.png'),
    os.path.join(BASE_DIR, 'assets', 'Baumer-Logo.png'),
    os.path.join(BASE_DIR, 'assets', 'baumer-logo.png'),
    os.path.join(BASE_DIR, '..', 'Baumer-Logo.png'),
    os.path.join(BASE_DIR, '..', 'baumer-logo.png'),
    os.path.join(BASE_DIR, '..', 'frontend', 'public', 'Baumer-Logo.png'),
    os.path.join(BASE_DIR, '..', 'frontend', 'public', 'baumer-logo.png'),
    os.path.join(BASE_DIR, '..', 'frontend', 'src', 'assets', 'Baumer-Logo.png'),
    os.path.join(BASE_DIR, '..', 'frontend', 'src', 'assets', 'baumer-logo.png'),
]


def _ensure_pdf_font():
    if PDF_FONT_NAME in pdfmetrics.getRegisteredFontNames():
        return PDF_FONT_NAME

    candidate_paths = [
        os.path.join(BASE_DIR, 'fonts', 'NotoSansGeorgian-Regular.ttf'),
        r'C:\Windows\Fonts\Sylfaen.ttf',
        r'C:\Windows\Fonts\arial.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/Library/Fonts/Arial Unicode.ttf',
    ]

    for path in candidate_paths:
        if os.path.exists(path):
            pdfmetrics.registerFont(TTFont(PDF_FONT_NAME, path))
            return PDF_FONT_NAME

    return 'Helvetica'


def _build_output_paths(prefix):
    os.makedirs(UPLOADS_DIR, exist_ok=True)
    filename = f"{prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    absolute_path = os.path.join(UPLOADS_DIR, filename)
    relative_path = os.path.join('uploads', filename)
    return absolute_path, relative_path


def _get_logo_path():
    for path in LOGO_PATH_CANDIDATES:
        normalized = os.path.abspath(path)
        if os.path.exists(normalized):
            try:
                width, height = ImageReader(normalized).getSize()
                if height > 0 and (width / float(height)) >= 2.2:
                    return normalized
            except Exception:
                continue
    return None


def _append_logo(story):
    logo_path = _get_logo_path()
    if not logo_path:
        return

    logo = Image(logo_path, width=2.8 * inch, height=0.85 * inch)
    logo.hAlign = 'LEFT'
    story.append(logo)
    story.append(Spacer(1, 0.15 * inch))


def _append_branding_header(story, styles):
    """Render logo when available; otherwise render visible BAUMER text header."""
    logo_path = _get_logo_path()
    if logo_path:
        _append_logo(story)
    else:
        story.append(Paragraph('BAUMER', styles['Heading2']))
        story.append(Paragraph('Engineering Excellence', styles['Normal']))
        story.append(Spacer(1, 0.12 * inch))

    separator = Table([['']], colWidths=[6.2 * inch], rowHeights=[0.01 * inch])
    separator.setStyle(TableStyle([
        ('LINEABOVE', (0, 0), (-1, -1), 0.8, colors.HexColor('#003154')),
    ]))
    story.append(separator)
    story.append(Spacer(1, 0.15 * inch))

def generate_migeba_act(data):
    """Generate Migeba Chabarebis Act (Transfer Act) PDF"""
    font_name = _ensure_pdf_font()

    pdf_abs_path, pdf_rel_path = _build_output_paths('migeba_act')
    doc = SimpleDocTemplate(
        pdf_abs_path,
        pagesize=A4,
        title='მიღება ჩაბარების აქტი / Transfer Act',
        author='Baumer',
        subject='Transfer Act Document'
    )
    story = []
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = font_name
    styles['BodyText'].fontName = font_name
    styles['Heading1'].fontName = font_name
    styles['Heading2'].fontName = font_name

    _append_branding_header(story, styles)
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName=font_name,
        fontSize=18,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=6,
        alignment=1
    )
    
    section_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontName=font_name,
        fontSize=12,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=8,
        spaceBefore=8
    )
    
    # Title
    story.append(Paragraph('მიღება ჩაბარების აქტი / Transfer Act', title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Date
    date_text = f"თარიღი: {datetime.now().strftime('%d.%m.%Y')}"
    story.append(Paragraph(date_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Parties Section
    story.append(Paragraph('I. ინფორმაცია', section_style))
    
    parties_data = [
        ['გამყიდველი / Seller:', data.get('seller_name', '')],
        ['ID ნომერი / ID:', data.get('seller_id', '')],
        ['მყიდველი / Buyer:', data.get('buyer_name', '')],
        ['ID ნომერი / ID:', data.get('buyer_id', '')]
    ]
    
    parties_table = Table(parties_data, colWidths=[2*inch, 4*inch])
    parties_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(parties_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Property Section
    story.append(Paragraph('II. ქონების აღწერა', section_style))
    story.append(Paragraph(data.get('property_description', ''), styles['BodyText']))
    story.append(Spacer(1, 0.2*inch))
    
    # Price Section
    story.append(Paragraph('III. ფასი', section_style))
    price_data = [
        ['თანხა / Amount:', f"{data.get('price', '')} ₾"],
        ['გადახდის მეთოდი / Payment Method:', data.get('receipt_method', 'ნაღდი ფული')]
    ]
    
    price_table = Table(price_data, colWidths=[2*inch, 4*inch])
    price_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(price_table)
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph('გამყიდველის ხელმოწერა ________________________', styles['Normal']))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(data.get('seller_name', ''), styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph('მყიდველის ხელმოწერა ________________________', styles['Normal']))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(data.get('buyer_name', ''), styles['Normal']))
    
    try:
        doc.build(story)
        return pdf_rel_path
    except Exception as e:
        print(f"Error generating PDF: {e}")
        raise


def generate_forma2(data):
    """Generate Forma 2 (Registration Form) PDF"""
    font_name = _ensure_pdf_font()

    pdf_abs_path, pdf_rel_path = _build_output_paths('forma2')
    doc = SimpleDocTemplate(
        pdf_abs_path,
        pagesize=A4,
        title='ფორმა ორი / Form 2',
        author='Baumer',
        subject='Property Registration Form'
    )
    story = []
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = font_name
    styles['BodyText'].fontName = font_name
    styles['Heading1'].fontName = font_name
    styles['Heading2'].fontName = font_name

    _append_branding_header(story, styles)
    
    #  styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName=font_name,
        fontSize=16,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=6,
        alignment=1
    )
    
    section_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontName=font_name,
        fontSize=11,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=8,
        spaceBefore=8
    )
    
    # Title
    story.append(Paragraph('ფორმა ორი', title_style))
    story.append(Paragraph('საკუთრების რეგისტრაციის განცხადება', styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Owner Information 
    story.append(Paragraph('I. ინფორმაცია', section_style))
    
    owner_data = [
        ['სახელი:', data.get('owner_name', '')],
        ['ID ნომერი:', data.get('owner_id', '')],
        ['ტელეფონი:', data.get('phone', '')],
        ['ელ-ფოსტა:', data.get('email', '')],
        ['მისამართი:', data.get('owner_address', '')],
    ]
    
    owner_table = Table(owner_data, colWidths=[2*inch, 4*inch])
    owner_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(owner_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Property 
    story.append(Paragraph('II. ქონების დეტალები', section_style))
    
    property_data = [
        ['ქონების მისამართი:', data.get('property_address', '')],
        ['ქონების ტიპი:', data.get('property_type', '')],
        ['ფართი (m²):', data.get('area', '')],
        ['რეგ. ნომერი:', data.get('registration_number', '')],
        ['სამართლებრივი საფუძველი / Legal Basis:', data.get('legal_basis', 'მიღება ჩაბარების აქტი / Transfer Act')],
        ['თარიღი:', datetime.now().strftime('%d.%m.%Y')],
    ]
    
    property_table = Table(property_data, colWidths=[2*inch, 4*inch])
    property_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(property_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Signature 
    story.append(Paragraph('ხელმოწერა ________________________', styles['Normal']))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(data.get('owner_name', ''), styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph('თარიღი: ' + datetime.now().strftime('%d.%m.%Y'), styles['Normal']))
    
    #  PDF
    try:
        doc.build(story)
        return pdf_rel_path
    except Exception as e:
        print(f"Error generating PDF: {e}")
        raise
