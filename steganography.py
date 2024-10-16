from PIL import Image


def encode_message(image_path, message):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    encoded_pixels = []
    
     # codam cel mai nesemnificativ bit
    for pixel in pixels:
        r, g, b = pixel
        r = (r & 0xFE) | (message.pop(0) if len(message) > 0 else 0)
        g = (g & 0xFE) | (message.pop(0) if len(message) > 0 else 0)
        b = (b & 0xFE) | (message.pop(0) if len(message) > 0 else 0)
        encoded_pixels.append((r, g, b))
    
    encoded_image = Image.new(image.mode, image.size)
    encoded_image.putdata(encoded_pixels)
    
    encoded_image_path = 'encoded.png'
    encoded_image.save(encoded_image_path)
    
    return encoded_image_path


def decode_message(encoded_image_path):
    encoded_image = Image.open(encoded_image_path)
    encoded_pixels = list(encoded_image.getdata())
    message = []
    
    # decodam cel mai nesemnificativ bit pentru a obtine mesajul
    for pixel in encoded_pixels:
        r, g, b = pixel
        message.append(r & 0x01)
        message.append(g & 0x01)
        message.append(b & 0x01)
    
    return ''.join(str(bit) for bit in message)
