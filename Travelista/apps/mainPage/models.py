from django.core.validators import MaxLengthValidator, EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    name = models.CharField(_('Full Name'), max_length=100, null=False, blank=True,
                            validators=[MaxLengthValidator])
    email = models.EmailField(_('Email Address'), max_length=255, null=False, blank=False,
                              validators=[EmailValidator])
    subject = models.CharField(_('Subject'), max_length=255, blank=True,
                               validators=[MaxLengthValidator])
    message = models.TextField(_('Message Text'), null=False, blank=False)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date'), auto_now=True)

    class Meta:
        verbose_name = _('Contact',)
        verbose_name_plural = _('Contacts',)
        ordering = ('-created_date',)

    def __str__(self) -> str:
        return f"{self.name} - {self.subject}"
