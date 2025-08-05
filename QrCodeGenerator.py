import pyqrcode
print("Welcome to our qrcode generator")

msg = input("Type your Secret Message: ")

code = pyqrcode.create(msg)

code.png("QRCODe.png",scale=5)

print("QR Code Generated Successfully!")