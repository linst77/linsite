from django import forms
from .models import MoTestModel


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = MoTestModel
        fields = ['father', 'mother', 'baby', 'email', 'phone', 'event_date']

        lables ={
            'father':'',
            'mother': '',
            'baby': '',
            'email': '',
            'phone': '',
            'event_date': '',
        }
        widgets = {
            'father': forms.TextInput( attrs={'class' : 'form-control'}),
            'mother':forms.TextInput( attrs={'class' : 'form-control'}),
            'baby': forms.TextInput( attrs={'class' : 'form-control'}),
            'email': forms.TextInput( attrs={'class' : 'form-control'}),
            'phone': forms.TextInput( attrs={'class' : 'form-control'}),
            'event_date': forms.TextInput( attrs={'class' : 'form-control'}),
        }

class FirstUpload( forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    content_first = forms.CharField(label='First Content', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',}))

    widgets = {
        'content_first': forms.TextInput(attrs={'class': 'form-control'}),
    }

class SecondUpload( forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    content_sec = forms.CharField(label='Second Content', max_length=100)