from django import forms
from .models import upload_file
#DataFlair
class uploadFileForm(forms.ModelForm):
    class Meta:
        model = upload_file
        fields = ('__all__')