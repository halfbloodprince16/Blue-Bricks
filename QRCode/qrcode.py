from PIL import Image
import zbarlight
import sys
 
if len(sys.argv) < 2:
    exit
file_path = sys.argv[1]
with open(file_path, 'rb') as image_file:
    image = Image.open(image_file)
    image.load()
 
codes = zbarlight.scan_codes('qrcode', image)
print('QR codes: %s' % codes)