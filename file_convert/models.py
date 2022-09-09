from re import T
from django.db import models
from datetime import datetime


class ConvertFile(models.Model):
    slug = models.SlugField(max_length=256, unique=False, null=True, blank=True)
    ip_address = models.FloatField(null=True, blank=True)
    conversion_limit = models.IntegerField(default=00)
    paid_status = models.BooleanField(default=False)
    
    def file_upload_add(instance, file_upload):
        file_extension = file_upload.split('.')[1]
        current_datetime = datetime.now()
        if file_extension == "pdf":
            return f"convert/pdf/{current_datetime}.{file_extension}"
        elif file_extension == "jpeg" or "jpg" or "tiff":
            return f"convert/image/{current_datetime}.{file_extension}"

    file_upload = models.FileField(upload_to=file_upload_add)
    file_name = models.CharField(max_length=256, default="", null=True, blank=True)
    
    def converted_file(instance, converted_file_dir):
        converted_file_extn = converted_file_dir.split('.')[1]
        if converted_file_extn == "pdf":
            return f"converted/pdf/{converted_file_dir}"
        elif converted_file_extn == "jpeg" or "jpg" or "tiff":
            return f"converted/image/{converted_file_dir}"
    
    converted_file_dir = models.FileField(upload_to=converted_file, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    file_url = models.URLField(null=True, blank=True, editable=False)
    
    get_text = models.TextField(blank=True, null=True)
    text_status = models.BooleanField(default=False, null=True)
    file_extension = models.CharField(null=True, max_length=5)
    
    # def __str__(self) -> str:
    #     return self.file_name
    
    @classmethod
    def get_file_path(self, id):
        file_path = self.objects.get(id=id)
        return file_path.file_upload.path
    
    # Not menually tested
    @classmethod
    def get_file_name(self, id):
        return self.file_upload.tell()
    
    @classmethod
    def get_model(self, id):
        try:
            return self.objects.get(id=id)
        except self.model.DoesNotExist:
            return None
    