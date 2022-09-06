import os
from PIL import Image
from os import path


class CreateStructureFolder:
    def __init__(self, default_location):
        self.default_location = default_location

    def create_structure(self):
        current_working_directory = os.getcwd()
        os.chdir(current_working_directory)

        for folder in ['exported_photos', 'exported_info', 'default_image']:
            if path.exists(folder):
                print(f'The {folder} already exists...')
            else:
                os.mkdir(folder)

    def create_default_image(self):
        default_image = self.default_location + '\\default_image'
        logo_path = self.default_location + '\\logo\\logo.jpg'
        os.chdir(default_image)
        default_img = Image.new(mode="RGB", size=(1080, 1080))
        logo_image_open = Image.open(logo_path).convert("RGBA")
        offset = (450, 20)
        default_img.paste(logo_image_open, offset, logo_image_open)
        default_img.save("single_default.png")
        os.chdir(self.default_location)
