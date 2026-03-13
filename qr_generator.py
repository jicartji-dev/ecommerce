import qrcode

url = "https://cartji.onrender.com"

qr = qrcode.make(url)
qr.save("static/cartji_qr.png")