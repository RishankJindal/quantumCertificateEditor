import fitz

from utils.constants import NEW_NAME, PDF_DIR_PATH, TEMP_PDF_PATH, TEXT_RECT  # PyMuPDF

def change_name_in_pdf(pdf_file):
    # Open the PDF
    pdf_document = fitz.open(f"{PDF_DIR_PATH}/{pdf_file}")

    # Iterate through each page
    # for page_number in range(len(pdf_document)):
    page = pdf_document.load_page(0)

    old_name = page.get_textbox(TEXT_RECT)

    text_instances = page.search_for(old_name)

    # Iterate through all instances of the search_text found
    # for inst in text_instances:
    # Get the font properties
    font_info = page.get_text('dict', clip=text_instances[0])['blocks'][0]['lines'][0]['spans'][0]
    font_size = font_info['size']
    color = font_info['color']

    # Adjust the Y-coordinate slightly for accurate placement
    x, y = text_instances[0][:2]
    y_adjusted = y + (font_size / 1.0)  # Adjust Y-coordinate as needed

    # Erase the found text
    page.add_redact_annot(text_instances[0], fill=(1, 1, 1))
    page.apply_redactions()

    # Insert the replacement text with the same font properties
    try:
        page.insert_text((x, y_adjusted), NEW_NAME, fontname="helvetica-bold", fontsize=font_size, color=color)
    except Exception as e:
        print(f"Could not insert text with 'helvetica-bold' font: {e}. Using fallback font.")
        page.insert_text((x, y_adjusted), NEW_NAME, fontname="helv", fontsize=font_size, color=color)

    # Save the modified PDF to a new file
    new_pdf_file = f"{TEMP_PDF_PATH}/changed_name_{pdf_file}"
    pdf_document.save(new_pdf_file)
    pdf_document.close()
