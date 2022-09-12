from django.forms import ModelForm
from .models import ConvertFile


class CreateForm(ModelForm):
    class Meta:
        model = ConvertFile
        fields = ['id', 'file_upload']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['file_upload'].widget.attrs.update({"class": 'form-control'})
