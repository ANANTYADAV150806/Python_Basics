import qrcode
a=input("enter the text or url you want to convert into QR code:")
b=input("enter the name of the file to save the QR code (without extension):")
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(a)
image = qr.make_image(fill_color="black", back_color="white")
image.save(f"{b}.png")
print(f"QR code generated and saved as {b}.png")


