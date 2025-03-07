from django.shortcuts import render
from .models import RSVP as rsvp
from .forms import RSVPForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages


def home(request):
    success_message = None
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            # Save the RSVP to the database
            rsvp.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                attending=form.cleaned_data['attending']
            )
            success_message = f"Thank you for your RSVP, {form.cleaned_data['name']}!"
            form = RSVPForm()  # Reset the form
    else:
        form = RSVPForm()

    return render(request, 'home.html', {'form': form, 'success_message': success_message})

def rsvp_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        attendance = request.POST.get('attendance')

        subject = f"RSVP from {name} at {email}"
        body = f"Message:\n\n{attendance}\n\n{message}"
        recipient_email = "m38586082@gmail.com"

        # Send email
        send_mail(
            subject,
            body,
            "test@gmail.com",  # Replace with your sender email
            [recipient_email],
            fail_silently=False,
        )

        messages.success(request, "Your RSVP has been submitted successfully!")

        return redirect('rsvp')  # Redirect back to the RSVP page

    return render(request, 'rsvp.html')  # Ensure you have an `rsvp.html` template

