import cv2

def scan_data_from_qr(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Initialize the QRCode detector
    qr_code_detector = cv2.QRCodeDetector()

    # Detect and decode the QRCode
    data, bbox, _ = qr_code_detector.detectAndDecode(image)

    return data



