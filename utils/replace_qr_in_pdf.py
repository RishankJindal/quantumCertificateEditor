import fitz  # PyMuPDF
import io
from PIL import Image

def replace_qr_in_pdf(pdf_path, image_path, output_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Load the new QR code image
    new_qr_image = Image.open(image_path)
    new_qr_image_bytes = io.BytesIO()
    new_qr_image.save(new_qr_image_bytes, format='PNG')
    new_qr_image_bytes = new_qr_image_bytes.getvalue()

    # Load the first page
    page = pdf_document.load_page(0)
    # Search for the images on the page
    image_list = page.get_images(full=True)

    # Check if there are images on the page
    if image_list:
        # Use the second last image (as per the original code)
        xref = image_list[-2][0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]

        # Open the image bytes as a PIL image to check if it's a QR code
        image = Image.open(io.BytesIO(image_bytes))
        if image.format == 'PNG':  # Assuming the QR code is in PNG format
            # Get the image rectangle
            image_rects = page.get_image_rects(xref)
            if image_rects:
                image_rect = image_rects[0]
                # Remove the existing image
                page.delete_image(xref)
                # Insert the new image
                page.insert_image(image_rect, stream=new_qr_image_bytes)

    # Save the modified PDF to a new file
    pdf_document.save(output_path)
    pdf_document.close()

