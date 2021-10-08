from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView

from mahnaWebsite.views import EmailThread
from .forms import PrfoesssionForm

from documents.models import ProfessionDocument


class AllProfessionDocuments(View):
    def get(self, request):
        data = ProfessionDocument.objects.all()
        return render(request, 'documents/allPrfoession.html', context={"data": data})


class AddProfession(View):
    def get(self, request):
        professionForm = PrfoesssionForm()
        return render(request, 'documents/AddProfession.html',
                      {'proform': professionForm})

    def post(self, request):
        professionForm = PrfoesssionForm(request.POST)
        if professionForm.is_valid():
            profession = professionForm.save()
            profession.save()
            domain = get_current_site(request).domain
            email_subject = 'You have added A Document'
            email_body = "Hi. Please contact the admin team of " + domain + ". If there are any problem." + ".\n\n You are receiving this message because you had added  on " + domain + ". If you didn't notice the document please contact support team on " + domain
            fromEmail = 'noreply@mahna.com'
            email = EmailMessage(
                email_subject,
                email_body,
                fromEmail,
                [request.user.email],
            )
            messages.success(request, "Added Succesfully. Check Email for confirmation")
            EmailThread(email).start()
            return redirect('all-professions')
        else:
            print(professionForm.errors)
            return render(request, 'documents/AddProfession.html',
                          {'proform': professionForm})


class UpdateProfession(UpdateView):
    model = ProfessionDocument
    form_class = PrfoesssionForm
    template_name = 'documents/updateProfession.html'

    def get_success_url(self):
        return reverse('all-professions')
