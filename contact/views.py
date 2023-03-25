from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):
    contactForm = ContactForm()
    # instancia del formulario
    #print("Tipo de petición: {}".format(request.method))
    if request.method == "POST":
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            #enviar correo
            email=EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De: {} <{}>\n\nEscribio:\n\n{}".format(name, email, message),
                "correo_prueba@inbox.mailtrap.io",
                ["vflores@itsqmet.edu.ec"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
    return render(request, "contact/contact.html", {'contactForm': contactForm})
