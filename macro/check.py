from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def get_data_from_image():
# Open the image
    image = Image.open('screenshot.png').convert('RGB')

    # Create a new image with a white background
    output_image = Image.new('RGB', image.size, (255, 255, 255))

    # Get pixel data
    pixels = image.load()
    output_pixels = output_image.load()

    # Loop through each pixel
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            
            # Define a threshold for black (you may adjust it based on your image)
            if r > 220 and g > 220 and b > 220:
                output_pixels[x, y] = (0, 0, 0)  # Keep black pixels
            else:
                output_pixels[x, y] = (255, 255, 255)  # Set all other pixels to white

    # Save or show the output image
    output_image.save('black_pixels_only.png')
    data = pytesseract.image_to_string(output_image, lang='eng',config='--psm 6')
    # remove space in start and end
    try:
        data = data.strip()
        t_data = data.split('\n')

        if len(t_data) == 3:
            s = f"Gold       : {t_data[0]}💰\nElixir       : {t_data[1]}🔮\nDark Elixir : {t_data[2]}🌑"
        else:
            s = data
        return s
    except Exception as e:
        return "Error"
if __name__ == '__main__':
    s = get_data_from_image()
    print(s)