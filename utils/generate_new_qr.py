import qrcode
from PIL import Image

from utils.constants import TEMP_QR_PATH

def generate_new_qr(data, pdfFile, output_path=f"{TEMP_QR_PATH}"):
    # Ensure the output directory exists
    import os
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Resize the image to the specified dimensions (1170x1170)
    img = img.resize((1170, 1170), Image.Resampling.LANCZOS)


    # Save the image to the specified path
    image_path = f"{output_path}/new_qr_{pdfFile}.png"  # Use part of the data for the filename
    img.save(image_path)

    return image_path

