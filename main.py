from utils.clear_files_and_folders import clear_files_and_folders
from utils.constants import MODIFIED_PDF_PATH, PDF_DIR_PATH, TEMP_PDF_PATH, TEMP_QR_PATH
from utils.change_name_in_pdf import change_name_in_pdf
from utils.extract_qr_from_pdf import extract_qr_from_pdf
from utils.generate_new_qr import generate_new_qr
from utils.get_pdf_files import get_pdf_files
from utils.modify_qr_data import modify_qr_data
from utils.replace_qr_in_pdf import replace_qr_in_pdf
from utils.scan_data_from_qr import scan_data_from_qr


def main():
    try:
        print('''Start editing your pdfs... 🫣
              ''')

        # Getting list of pdf files present
        pdf_files = get_pdf_files(PDF_DIR_PATH)

        if not pdf_files:
            print("No PDF files found in the directory.")
            return

        # Iterate over each pdf file
        for pdf_file in pdf_files:
            try:
                change_name_in_pdf(pdf_file)
                extract_qr_from_pdf(pdf_file)

                image_path = f"{TEMP_QR_PATH}/qr_{pdf_file}.png"
                prev_qr_data = scan_data_from_qr(image_path=image_path)
                modified_qr_data = modify_qr_data(prev_qr_data)
                new_qr_img_path = generate_new_qr(modified_qr_data, pdf_file)

                pdf_path = f"{TEMP_PDF_PATH}/changed_name_{pdf_file}"
                output_path = f"{MODIFIED_PDF_PATH}/{pdf_file}"
                replace_qr_in_pdf(pdf_path, new_qr_img_path, output_path)

            except Exception as e:
                print(f"Error occurred while processing {pdf_file}: {e}")

        clear_files_and_folders(TEMP_QR_PATH)
        clear_files_and_folders(TEMP_PDF_PATH)

        print('''Editing completed 😁
              ''')

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()