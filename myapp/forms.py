from django import forms
from myapp.models import auther

class autherform(forms.ModelForm):
    class Meta:
        model=auther
        fields='__all__'


