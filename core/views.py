from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Topic

### ----------------------------------###
class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = 'Ola vamos anotar algums topicos importantes para voce'
        return context


### ----------------------------------###
class TopicCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Topic
    fields = ['title','text']
    template_name = 'core/form.html'
    success_url = reverse_lazy('list_topic')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.is_valid()
        form.save()
        return super().form_valid(form)

### ----------------------------------###
class TopicListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Topic
    fields = '__all__'
    context_object_name = 'object'
    paginate_by = 1
    template_name = 'core/topic.html'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

