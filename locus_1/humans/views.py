from django.views.generic import CreateView, ListView

from .models import Human
from .forms import HumanForm


class HumanCreateView(CreateView):
    model = Human
    form_class = HumanForm
    template_name = 'humans/create.html'


class HumanListView(ListView):
    model = Human
    template_name = 'humans/list.html'


class HumanTask1View(ListView):
    template_name = 'humans/task-1.html'
    coincidence = 0

    def get_queryset(self):
        id = self.kwargs.get('id')
        current_human = Human.objects.get(pk=id)
        humans = Human.objects.exclude(pk=id)
        list_of_ids = []
        for human in humans:
            if human == current_human:
                list_of_ids.append(human.id)
                self.coincidence += 1
        return Human.objects.filter(id__in=list_of_ids)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coincidence'] = self.coincidence
        return context


class HumanTask2View(ListView):
    template_name = 'humans/task-1.html'
    coincidence = 0

    def get_queryset(self):
        id = self.kwargs.get('id')
        current_human = Human.objects.get(pk=id)
        humans = Human.objects.exclude(pk=id)
        list_of_ids = []
        for human in humans:
            if current_human.eq_task_2(human):
                list_of_ids.append(human.id)
                self.coincidence += 1
        return Human.objects.filter(id__in=list_of_ids)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coincidence'] = self.coincidence
        return context
