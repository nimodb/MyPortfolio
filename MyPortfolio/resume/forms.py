from django import forms
from resume.models import Contact
from django_recaptcha.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ("full_name", "email", "subject", "message", "captcha")
        widgets = {
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Full Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email Address"}
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Subject"}
            ),
            "message": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Message", "rows": 7}
            ),
        }
