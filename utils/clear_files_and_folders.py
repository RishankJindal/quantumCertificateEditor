import pathlib
import logging

from utils.constants import TEMP_QR_PATH

def clear_files_and_folders(folder_path):
    folder_path = pathlib.Path(folder_path)

    # Check if the folder exists
    if not folder_path.exists():
        raise FileNotFoundError(f"The folder {folder_path} does not exist.")

    # Iterate over all files and subdirectories in the folder
    for file_path in folder_path.glob('*'):
        try:
            if file_path.is_file():
                logging.debug(f"Removing file: {file_path}")
                file_path.unlink()  # Remove the file
            elif file_path.is_dir():
                logging.debug(f"Removing directory: {file_path}")
                with file_path.rmdir() as dir_removed:
                    pass  # Remove the directory and all its contents
        except Exception as e:
            logging.error(f"Failed to delete {file_path}. Reason: {e}")