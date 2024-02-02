from django import forms
from .models import Contact

class ContactModelForm(forms.ModelForm):
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
