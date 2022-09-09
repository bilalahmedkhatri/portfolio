from django.forms import ModelForm
from .models import ConvertFile


class CreateForm(ModelForm):
    class Meta:
        model = ConvertFile
        fields = ['id', 'file_upload', 'paid_status', 'conversion_limit']