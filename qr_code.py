import qrcode
import os
import subprocess

website_url = {input('Lütfen QR koduna dönüştürmek istediğiniz Url'yi girin')}
qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(website_url)
qr.make()

img = qr.make_image(fill='black', back_color='white')
img.show()
subprocess.run(["open", "-R", save_path])
