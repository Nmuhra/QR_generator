import qrcode

qr = qrcode
data = str(input("link: "))
qr.add_data(data)
qr.make(fit=True)
color_1 = input("color 1: ")
color_2 = input("color 2: ")
img = qr.make_image(fill="color_1", back_color="color_2")
img.save
