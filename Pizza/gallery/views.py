from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.views.generic.edit import FormMixin

from .forms import ContactForm
from .models import Pizza


class MenuView(FormMixin, ListView):
    template_name = 'index.html'
    model = Pizza
    context_object_name = 'all_pizza'
    paginate_by = 4
    form_class = ContactForm

    def form_valid(self, request, *args, **kwargs):
        form = self.get_form()
        if request.method == 'POST':
            if form.is_valid():
                mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'email от кого отправлять',
                                 ['список email кому отправлять'], fail_silently=True)
                if mail:
                    messages.success(request, 'Письмо отправлено!')
                    return redirect('contact')
                else:
                    messages.error(request, 'Ошибка отправки')
            else:
                messages.error(request, 'Ошибка валидации')
        else:
            form = ContactForm()
        return super().form_valid(form)


class Detail_Pizza(DetailView):
    model = Pizza
    template_name = 'details.html'
    context_object_name = 'pizza'
