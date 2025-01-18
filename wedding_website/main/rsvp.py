from django import forms

class RSVPForm(forms.Form):
    name = forms.CharField(
        label='Your Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    attending = forms.ChoiceField(
        label='Will you attend?',
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=forms.RadioSelect
    )
