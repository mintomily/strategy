from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Characters, Bulletin
from .forms import CharacterForm, ContactForm, BulletinForm
from django.contrib import messages
from django.core.mail import EmailMessage

class IndexView(ListView):
    template_name = 'index.html'
    queryset = Characters.objects.order_by('-posted_at')

class BulletinView(ListView):
    template_name = 'bulletin.html'
    queryset = Bulletin.objects.order_by('-posted_at')

class DetailView(DetailView):
    template_name = 'detail.html'
    model = Characters

class CategoryView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = Characters.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories

@method_decorator(login_required, name='dispatch')

class BulletinFormView(CreateView):
    form_class = BulletinForm
    template_name = "bulletin_form.html"
    success_url = reverse_lazy('strapp:bulletin')

    def form_valid(self, form):
        text_data = form.save(commit=False)
        text_data.user = self.request.user
        text_data.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')

class CharacterFormView(CreateView):
    form_class = CharacterForm
    template_name = "character_form.html"
    success_url = reverse_lazy('strapp:character_done')

    def form_valid(self, form):
        character_data = form.save(commit=False)
        character_data.user = self.request.user
        character_data.save()
        return super().form_valid(form)

class CharacterSuccessView(TemplateView):
    template_name = 'character_success.html'

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('strapp:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:{3}'\
            .format(name, email, title, message)
        from_email = 'xxxx@gmail.com'
        to_list = ['guitaizuochuan@gmail.com']
        message = EmailMessage(subject=subject,
                                body=message,
                                from_email=from_email,
                                to=to_list,
                                )
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)

class CharacterDeleteView(DeleteView):
    model = Characters
    template_name = 'character_delete.html'
    success_url = reverse_lazy('strapp:index')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
        