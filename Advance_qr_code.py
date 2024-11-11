import qrcode as qrC
from PIL import Image

qr=qrC.QRCode(version=1,
              error_correction=qrC.ERROR_CORRECT_H,
              box_size=10,border=5,)
qr.add_data("https://github.com/SAMEERSINGHGAUTAM")
qr.make(fit=True)
img=qr.make_image(fill_color="black", back_color="yellow")
img.save("Custom_qr_code.png")