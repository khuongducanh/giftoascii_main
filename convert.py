# this is convert , no run code
import os, time, shutil
from main import chars, color, gif_path

try:
    from PIL import Image
except ImportError:
    import pip
    pip.main(['install', 'Pillow'])
    from PIL import Image

# Hàm làm sạch Terminal
def clear():
    #os.system('clear||cls')
    print('\033[2J\033[H', end='')

# Hàm resize ảnh
def resize(image):
    width, height = image.size
    ratio = height / width / 1.9
    re_width = min(shutil.get_terminal_size().columns, width)
    re_height = int(re_width * ratio)
    resized_image = image.resize((re_width, re_height))
    return resized_image

# Hàm chuyển pixel thành kí tự phù hợp
def to_ascii(image):
    image = image.convert("L")
    pixels = image.getdata()
    ascii = ''
    for pixel in pixels:
        ascii += chars[pixel // 32]
    return ascii

# Hàm chuyển ảnh thành kí tự
def convert(image):
    image = resize(image)
    ascii = to_ascii(image)
    ascii_img = '\n'.join(ascii[i:(i+image.width)] for i in range(0, len(ascii), image.width))
    return ascii_img

# Hàm chuyển GIF thành ảnh
def convert_gif(gif_path):
    gif = Image.open(gif_path)
    try:
        while True:
            frame = gif.convert("RGBA")
            print_char(frame)
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass
    gif.close()

# Hàm in chuỗi kí tự chuyển đổi
def print_char(image):
    ascii = convert(image)
    if ascii:
        clear()
        print(color + ascii)
        time.sleep(0.1)