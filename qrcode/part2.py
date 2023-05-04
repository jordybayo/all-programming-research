# ! pip3 install qrcode

import qrcode
from PIL import Image

def create_qr(commercial_id):
    logo = Image.open('logo.png')
    basewidth = 75
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth,hsize), Image.ANTIALIAS)
    qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr_big.add_data('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    qr_big.make(fit=True)
    img_qr_big = qr_big.make_image(fill_color="green", back_color="yellow")
    pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
    img_qr_big.paste(logo, pos)
    img_qr_big.save('qr_big.png')