from django.shortcuts import render
from .models import Contacts


def contact(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        contact = Contacts.objects.create(
            email=email, name=name, phone_number=phone_number, message=message)
        contact.save()
    return render(request, 'contacts/contact.html')
