%pip install qrcode
import qrcode

# take input from user
data = input("ENTER URL OR TEXT: ").strip()   # strip removes white spaces
filename = input("Enter the file name: ").strip() + ".png"

# generate QR code
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# create QR image
img = qr.make_image(fill_color="pink", back_color="white")

# save the QR code
img.save(filename)

print("QR CODE SAVED IN FILE NAME AS", filename)




# the output looks as follows
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: qrcode in c:\users\aishw\appdata\roaming\python\python313\site-packages (8.2)
Requirement already satisfied: colorama in c:\programdata\anaconda3\lib\site-packages (from qrcode) (0.4.6)
Note: you may need to restart the kernel to use updated packages.

ENTER URL OR TEXT:  https://www.youtube.com/watch?v=4qyhKGFS65U
Enter the file name:  link
QR CODE SAVED IN FILE NAME AS link.png
