from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from .models import Contact
# import os

class ContactModelForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'light',
        }
    ),
        # public_key=os.environ['RECAPTCHA_PUBLIC_KEY'],
        # private_key=os.environ['RECAPTCHA_PRIVATE_KEY'],
    )
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]

    def save(self, commit=True):
        instance = super(ContactModelForm, self).save(commit=False)
        
        # Modify the 'name' field to 'Anonymous'
        if not instance.name:
            instance.name = 'Anonymous'
        else:
            instance.name = instance.name
        
        if commit:
            instance.save()
        return instance
