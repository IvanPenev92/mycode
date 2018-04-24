from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.views.generic import TemplateView, ListView

from .models import ModelLinks, Page

class IndexView(TemplateView):
    template_name = 'stuff/base.html'
    context_object_name = 'pages_list'


class AnyPageView(ListView):
    template_name = 'stuff/index.html'
    model = Page
    def get_context_data(self):
        context = {
            "title": Page.objects.get(pk=self.kwargs['pk']).title,
            "page": Page.objects.get(pk=self.kwargs['pk']),
            "text": Page.objects.get(pk=self.kwargs['pk']).page_h1_text
        }
        return context


class ListView(ListView):
    template_name = 'stuff/pages.html'
    model = Page
    context = {
        "objects": Page.objects.all(),
        "page": "",
        "title": "Pages",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2iPgwkBmpjZft7" \
                 "lljn7BZ7QfPdkCIxeo6sot0U4Z9nlznI6FV",
        "link_to_1": ModelLinks.link_to_1,
        "text_to_1": ModelLinks.text_to_1,
        "link_to_2": ModelLinks.link_to_2,
        "text_to_2": ModelLinks.text_to_2,
        "link_to_3": ModelLinks.link_to_3,
        "text_to_3": ModelLinks.text_to_3,
        "link_to_4": ModelLinks.link_to_4,
        "text_to_4": ModelLinks.text_to_4,
    }
    def get_context_data(self):
        return self.context


class PageView(ListView):
    model = Page
    template_name = 'stuff/page.html'
    def get_context_data(self):
        context = {
            "text": "This is Page number " + self.kwargs['id'] + ".",
            "title": "Page " + self.kwargs['id'],
            "image": "https://www.sideshowtoy.com/wp-content/uploads/2015/10/star-wars-" \
                     "darth-maul-sixth-scale-feature-100156.jpg",
            "link_to_pages": ModelLinks.link_to_pages,
            "text_to_pages": ModelLinks.text_to_pages
        }
        return context