from PIL import Image
from draw import WIDTH, ROW
# Open the input GIF
def resize_image():
    gif = ['christmas_images', 'halloween_images']
    for x in gif:
        for i in range(1, 5):
            gif_image = Image.open(f'OG_GIFS/{x}/{i}.gif')
            # Resize the GIF to 50% of its original size
            new_width, new_height = int(WIDTH/ROW), int(WIDTH/ROW)
            gif_image = gif_image.resize((new_width, new_height))

            # Save the resized GIF
            gif_image.save(f'gifs/{x}/{i}.gif', 'GIF')