# -*- encoding: utf-8 -*-
# Third party
from pytesseract import pytesseract
import os

# import django modules
from django.conf import settings

# local import
from file_convert.models import ConvertFile


class GetText:
    
    def __init__(self, image_file, file_name, id):
        self.id = id
        self.image_file = image_file
        self.file_name = file_name
        self.MEDIA_ROOT = settings.MEDIA_ROOT
    
    def get_extension(self):
        return os.path.splitext(self.image_file)[1].replace('.', "")
    
    def get_text(self):
        PATH_TESSERACT = os.getenv("PATH_TESSERACT")
        pytesseract.tesseract_cmd = PATH_TESSERACT
        custom_configr = "preserve_inerword_spaces=1 --psm 6"
        conv_img_text = pytesseract.image_to_string(self.image_file, config=custom_configr)
        return conv_img_text
    
    def remove_new_line(self):
        rem_new_line = self.get_text()
        return "".join(rem_new_line.splitlines())
    
    # for GPT3
    # def text_correction(self):
    #     pass
    
    def save_text(self):
        save_text = ConvertFile.objects.filter(id=self.id)
        save_text.update(
            get_text=self.remove_new_line(),
            text_status = True,
            file_extension =self.get_extension()
        )