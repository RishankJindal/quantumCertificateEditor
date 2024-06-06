import os
from PyPDF2 import PdfMerger

def merge_pdfs(folder_path, output_filename):
    merger = PdfMerger()
    
    # Get all PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith('.pdf')]
    pdf_files.sort()  # Sort files alphabetically
    
    for pdf_file in pdf_files:
        file_path = os.path.join(folder_path, pdf_file)
        merger.append(file_path)
    
    # Write merged PDF to output file
    with open(output_filename, 'wb') as merged_file:
        merger.write(merged_file)


