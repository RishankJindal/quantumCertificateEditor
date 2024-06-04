import os

def get_pdf_files(directory):
    pdf_files = [file for file in os.listdir(directory) if file.endswith('.pdf')]
    return pdf_files


