import qrcode
import qrcode.image.svg as qrcode_svg

# QR code color
QR_COLOR = "BLACK"

# QR code background color
QR_BACKGROUND_COLOR = "WHITE"

# QR code text
QR_TEXT = "Hello World!"

# QR code size
BOX_SIZE = 80

# QR border
BOX_BORDER = 4

# QR code Fragment type
QR_FRAGMENT_TYPE = qrcode_svg.SvgPathImage

# Features of the QR code we want to generate
features = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=BOX_SIZE,
    border=BOX_BORDER,
    image_factory=QR_FRAGMENT_TYPE
)

features.add_data(QR_TEXT)
features.make()

img = features.make_image(fill_color=QR_COLOR, back_color=QR_BACKGROUND_COLOR)
img.save("qr_image.svg")
