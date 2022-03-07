from django import forms
from .models import NewCustomUser
from django.core.validators import EmailValidator

class LoginViewForm(forms.ModelForm):
    class Meta:
        model = NewCustomUser
        fields = ['email', 'phone']

    '''
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = NewCustomUser.objects.get(username=username)
        except user.DoesNotExist:
            return username
        raise forms.ValidationError(u'Username "%s" is already in use.' % username)
    '''