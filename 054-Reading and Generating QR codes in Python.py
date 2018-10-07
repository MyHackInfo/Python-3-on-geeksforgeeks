'''
### Reading and Generating QR codes in Python Using QRtools
-QR code, or quick response code, is a trademark for a type of 2 dimensional barcode.
-2 dimensional barcodes are similar to one dimensional barcodes, but can store more information per unit area.

# Generate a QR Code
    -qrtools contains a class QR (can be viewed in the source code),
    -for which we must initially create an object.
    -The object takes the following arguments

        1-> data
        2-> pixel_size
        3-> level
        4-> margin_size
        5-> data_type

'''
from qrtools.qrtools import QR


# Create or object
my_qr = QR(data = u"narsi")

# encodes to a qr code
my_qr.encode()
