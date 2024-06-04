import fitz
from pathlib import Path
from utils.constants import PDF_DIR_PATH, TEMP_QR_PATH


def extract_qr_from_pdf(pdf_file: str) -> None:
    """
    Extract the QR code from the first page of a PDF file and save it to a temporary file.

    :param pdf_file: The name of the PDF file to extract the QR code from.
    """
    pdf_path = Path(PDF_DIR_PATH) / pdf_file
    temp_qr_path = Path(TEMP_QR_PATH)

    with fitz.open(str(pdf_path)) as pdf_document:
        page = pdf_document.load_page(0)
        xref = page.get_images()[-2][0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        image_format = base_image["ext"]

        image_filename = temp_qr_path / f"qr_{pdf_file}.{image_format}"
        with open(image_filename, "wb") as image_file:
            image_file.write(image_bytes)