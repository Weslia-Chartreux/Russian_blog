from django.shortcuts import render
from django.views.generic.base import TemplateView


# Класс, который отвечает за показ страницы с информацией о авторе 'author/'
class AboutAuthorView(TemplateView):
    template_name = 'author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# Класс, который отвечает за показ страницы с информацией о технологиях 'tech/'
class AboutTechView(TemplateView):
    template_name = 'tech.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

