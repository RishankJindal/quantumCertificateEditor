from utils.clear_files_and_folders import clear_files_and_folders
from utils.constants import MODIFIED_PDF_PATH, NEW_NAME, PDF_DIR_PATH, TEMP_PDF_PATH, TEMP_QR_PATH
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
        unedited_pdf_count = 0

        if not pdf_files:
            print("No PDF files found in the directory.")
            return
        
        clear_files_and_folders(MODIFIED_PDF_PATH)

        # Iterate over each pdf file
        for pdf_file in pdf_files:
            try:
                change_name_in_pdf(pdf_file)
                extract_qr_from_pdf(pdf_file)

                image_path = f"{TEMP_QR_PATH}/qr_{pdf_file}.png"
                prev_qr_data = scan_data_from_qr(image_path=image_path)
                modified_qr_data = modify_qr_data(prev_qr_data,pdf_file,unedited_pdf_count)
                if not modified_qr_data['data']:
                    unedited_pdf_count = modified_qr_data['unedited_pdf_count']
                    print(f"Failed to edit pdf -> {modified_qr_data['file_name']}")
                    continue
                new_qr_img_path = generate_new_qr(modified_qr_data, pdf_file)

                pdf_path = f"{TEMP_PDF_PATH}/changed_name_{pdf_file}"
                output_file_path = f"{MODIFIED_PDF_PATH}/{NEW_NAME} 0{pdf_files.index(pdf_file)+1}.pdf"
                replace_qr_in_pdf(pdf_path, new_qr_img_path, output_file_path)

            except Exception as e:
                print(f"Error occurred while processing {pdf_file}: {e}")

        clear_files_and_folders(TEMP_QR_PATH)
        clear_files_and_folders(TEMP_PDF_PATH)

        print(f"\nTotal number of unedited files - {unedited_pdf_count}")

        print('''
Editing completed 😁
              ''')

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()