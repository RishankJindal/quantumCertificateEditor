import fitz

from utils.constants import NEW_NAME, PDF_DIR_PATH, TEMP_PDF_PATH, TEXT_RECT


def change_name_in_pdf(pdf_file):
    try:
        pdf_document = fitz.open(f"{PDF_DIR_PATH}/{pdf_file}")
        page = pdf_document.load_page(0)

        old_name = page.get_textbox(TEXT_RECT)
        
        if not old_name:
            raise ValueError("Old name not found in the PDF")

        text_instances = page.search_for(old_name)
        if not text_instances:
            raise ValueError("Old name not found in the PDF")

        font_size = abs(text_instances[0][3] - text_instances[0][1])  # Calculate font size

        increase_amount = 1

        x0, y0, x1, y1 = text_instances[0]  # Get coordinates of text instance
        # Increase width and height of the rectangle
        x0 -= increase_amount
        y0 -= increase_amount
        x1 += increase_amount
        y1 += increase_amount
   
        # Add redaction with the same font size
        page.add_redact_annot((x0,y0,x1,y1), text=NEW_NAME, text_color=(0, 0, 0), fontsize=font_size, fontname='helvetica-bold')
        
        
        page.apply_redactions()  # Correct method to apply redactions
        
        # Save the modified PDF to a new file
        new_pdf_file = f"{TEMP_PDF_PATH}/changed_name_{pdf_file}"
        pdf_document.save(new_pdf_file)
        pdf_document.close()
        
    except FileNotFoundError:
        print(f"Error: PDF file {pdf_file} not found in the directory {PDF_DIR_PATH}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")