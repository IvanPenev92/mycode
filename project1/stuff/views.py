from django.views.generic import ListView, DetailView

from .models import Page


class IndexView(ListView):
    template_name = 'stuff/pages_list.html'
    model = Page
    context_object_name = "objects"


class AnyPageView(DetailView):
    template_name = 'stuff/page.html'
    model = Page

#   Context with ListView
#   def get_context_data(self, *, object_list=None, **kwargs):
    #   context = super().get_context_data(object_list=object_list, **kwargs)
    #   context['title'] = Page.objects.get(pk=self.kwargs['pk']).title
    #   context['text'] = Page.objects.get(pk=self.kwargs['pk']).page_text
    #   context['image'] = Page.objects.get(pk=self.kwargs['pk']).image
    #   return context
