# Install all the libraries needed
# Create a function that collects a text and converts it to a QR Code
# Save the QR Code as an image
# Run the function

import qrcode


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")


generate_qrcode("https://brunolpsousa.duckdns.org")
