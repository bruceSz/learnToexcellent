from django.shortcuts import render
from django.http import HttpResponseRedirect
from books.contact.forms import ContactForm


def contact(request):
    # simple method.
    #
    # errors = []
    # if request.method == 'POST':
    #     if not request.POST.get('subject',''):
    #         errors.append('Enter a subject.')
    #     if not request.POST.get('message',''):
    #         errors.append('Enter a message')
    #     if request.POST.get('email') and '@' not in request.POST['email']:
    #         errors.append('Enter a valid e-mail address.')
    #     if not errors:
    #         send_mail(
    #             request.POST['subject'],
    #             request.POST['message'],
    #             request.POST.get('email','noreplay@example.com'),
    #             ['siteowner@example.com'],
    #         )
    #         return HttpResponseRedirect('/contact/thanks')
    # return render(request,'contact_form.html',{'errors':errors})

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(
            initial={'subject':'I love your site!'}
        )
    return render(request,'contact_form.html',{'form':form})
