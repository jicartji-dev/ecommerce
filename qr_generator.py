import qrcode

url = "https://cartji.onrender.com"

qr = qrcode.make(url)
qr.save("cartji_qr.png")

print("QR Code Generated Successfully!")