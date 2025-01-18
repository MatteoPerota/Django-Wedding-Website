from django.shortcuts import render
from .models import RSVP as rsvp
from .forms import RSVPForm

def home(request):
    success_message = None
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            # Save the RSVP to the database
            RSVP.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                attending=form.cleaned_data['attending']
            )
            success_message = f"Thank you for your RSVP, {form.cleaned_data['name']}!"
            form = RSVPForm()  # Reset the form
    else:
        form = RSVPForm()

    return render(request, 'home.html', {'form': form, 'success_message': success_message})
