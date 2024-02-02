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
        instance.name = 'Anonymous'
        
        if commit:
            instance.save()
        return instance
    
    def __init__(self, *args, **kwargs):
        super(ContactModelForm, self).__init__(*args, **kwargs)
        
        # Set a default value for the 'subject' field (in this case blank)
        self.fields['subject'].initial = ''