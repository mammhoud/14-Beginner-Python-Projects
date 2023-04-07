import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

data: str = 'Mahmoud Ezzat'
qr = qrcode.QRCode(version=2, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='red', back_color='white')
img.save("/saved-files/im-qr.png")

# img = qrcode.make(data)
# img.save('im-qr.png')
#############################################################

img = Image.open('im-qr.png')
result = decode(img)
print(result)
