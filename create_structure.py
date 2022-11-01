import os
from PIL import Image
from os import path


class CreateStructureFolder:
    def __init__(self, default_location, company):
        self.default_location = default_location
        self.company = company

    def create_structure(self):
        current_working_directory = os.getcwd()
        os.chdir(current_working_directory)

        for folder in ['exported_photos', 'exported_info', 'default_image']:
            if path.exists(folder):
                print(f'The {folder} already exists...')
            else:
                os.mkdir(folder)
    def check_and_create_folder(self, folder_name="exported_photos"):
        folder_location = folder_name + '\\' + self.company
        print(f'Create folder were info will be exported...')
        if os.path.isdir(folder_location):
            print(f'The {folder_name} already exists! Continuing...')
        else:
            os.mkdir(folder_location)
            print(f'{folder_name} created! Location: {folder_location}')
        return folder_location
