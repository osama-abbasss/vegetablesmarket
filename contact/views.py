from django.shortcuts import render
from django.core.mail import send_mail




def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        mail = 'this message from : '+ email + '\n name : ' + name + '\n' + message


        send_mail(subject, mail, 'osama.it.utc@gmail.com', ['eng.oabbass@gmail.com'], fail_silently=False,)

    
    template_name = 'contact/contact.html'
    context = {}

    return render(request, template_name, context)