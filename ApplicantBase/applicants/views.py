from django.db import IntegrityError
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Applicant


class ApplicantAddView(CreateView):
    model = Applicant

    fields = ['first_name', 'last_name', 'middle_name', 'birth_date',
              'contact_phone', 'contact_email', 'address',]

    template_name = 'applicant_form.html'
    success_url = reverse_lazy('index') #Перенаправление пока на главную, позже понять куда надо


class ApplicantListView(ListView):
    model = Applicant

    template_name = 'applicants_list.html'
    context_object_name = 'applicants'


class ApplicantsDetailView(DetailView):
    model = Applicant

    template_name = 'applicant_detail_view.html'

