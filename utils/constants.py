# Import required modules
from pymupdf import Rect

# Define directory paths
PDF_DIR_PATH = 'pdfs'  # Path to the input PDF files
TEMP_PDF_PATH = 'temp/generated_pdfs'  # Path to temporary generated PDF files
TEMP_QR_PATH = 'temp/generated_qrs'  # Path to temporary generated QR code files
MODIFIED_PDF_PATH = 'new_pdfs'  # Path to the output modified PDF files

# Define constants for name insertion
NEW_NAME = "DUMMY NAME"  # Default name to be inserted
NAME_FONT = "helvetica-bold"  # Font to be used for the name
NAME_FONT_SIZE = 11  # Font size to be used for the name

# Define the rectangle coordinates for text insertion
TEXT_RECT = Rect(
    158.8959991455078,  # x1
    161.688037109375,  # y1
    233.89326171875,  # x2
    173.4734313964844  # y2
)  # Rectangle coordinates for text insertion