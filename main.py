from convert import *

# Kí tự
chars = "@%#=-:. "

# Mã ANSI (0 để lấy mặc định)
ansi = 1
color = f"\033[0;{ansi}m"

# Đường dẫn GIF
gif_path = "gif/4.gif"

if __name__ == '__main__':
    while True:
        convert_gif(gif_path)