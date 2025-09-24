import qrcode
import os
import subprocess

website_url = "https://youtu.be/d0w4w9gXcQ?si=gMMWiAg5X9af1vn3"
qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(website_url)
qr.make()

img = qr.make_image(fill='black', back_color='white')

# Direkt masaüstüne kaydet
save_path = "/Users/alkan/Desktop/youtube_qr.png"
img.save(save_path)
print("Kaydedilen dosya:", save_path)

# Varsayılan resim görüntüleyicide aç
img.show()

# Finder'da dosyayı göster
subprocess.run(["open", "-R", save_path])
