from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, FormView, ListView,
                                  UpdateView)

from core.constants import LOCUSES
from humans.forms import HumanForm, HumanPrepareForm
from humans.models import Human


class HumanCreateView(LoginRequiredMixin, CreateView):
    form_class = HumanForm
    template_name = 'humans/create_update.html'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('humans:create')


class HumanPrepareUpdateView(LoginRequiredMixin, FormView):
    form_class = HumanPrepareForm
    template_name = 'humans/prepare.html'

    def get_success_url(self):
        return reverse_lazy(
            'humans:update',
            kwargs={'id': int(self.get_form_kwargs().
                              get('data').get('human_id'))}
        )


class HumanUpdateView(LoginRequiredMixin, UpdateView):
    form_class = HumanForm
    template_name = 'humans/create_update.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Human, pk=self.kwargs['id'])

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('humans:update_prepare')


class HumanDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'humans/delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Human, pk=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.kwargs['id']
        return context

    def get_success_url(self):
        return reverse_lazy('humans:index')


class HumanListView(LoginRequiredMixin, ListView):
    model = Human
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        human_list = context.get('human_list')

        data = [[''] * (self.paginate_by * 2 + 1) for _ in range(
            len(LOCUSES) + 2)]
        data[0] = [''] * (self.paginate_by + 1)
        data[0][0] = 'ID'
        data[1] = [''] * (self.paginate_by + 1)
        data[1][0] = 'Добавил(а)'
        row_num = 2
        for locus in LOCUSES:
            data[row_num][0] = locus
            row_num += 1

        col_num = 1
        col_num_id = 1
        for human in human_list:
            human_dict = human.__dict__
            data[0][col_num_id] = human_dict.get('id')
            if human.added_by:
                data[1][col_num_id] = human.added_by.username
            else:
                data[1][col_num_id] = ''
            col_num_id += 1
            row_num = 2
            for locuse in LOCUSES:
                locuse_1 = locuse + '_1'
                locuse_2 = locuse + '_2'
                locuse_1_value = human_dict.get(locuse_1)
                locuse_2_value = human_dict.get(locuse_2)
                data[row_num][col_num] = locuse_1_value or ''
                data[row_num][col_num + 1] = locuse_2_value or ''
                row_num += 1
            col_num += 2

        context['data'] = data
        return context


class HumanTask1PrepareView(LoginRequiredMixin, FormView):
    form_class = HumanPrepareForm
    template_name = 'humans/prepare.html'

    def get_success_url(self):
        return reverse_lazy(
            'humans:task_1',
            kwargs={'id': int(self.get_form_kwargs().
                              get('data').get('human_id'))}
        )


class HumanTask1ListView(HumanListView):
    template_name = 'humans/task.html'
    result = 0
    target_human = None

    def get_queryset(self):
        id = self.kwargs.get('id')
        self.target_human = get_object_or_404(Human, pk=id)
        humans = Human.objects.exclude(pk=id)
        list_of_ids = []
        for human in humans:
            if self.target_human.task_1(human):
                list_of_ids.append(human.id)
                self.result += 1
        return Human.objects.filter(id__in=list_of_ids)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = self.result
        context['target_human'] = self.target_human

        return context


class HumanTask2PrepareView(LoginRequiredMixin, FormView):
    form_class = HumanPrepareForm
    template_name = 'humans/prepare.html'

    def get_success_url(self):
        return reverse_lazy(
            'humans:task_2', kwargs={'id':
                                     int(self.get_form_kwargs().
                                         get('data').get('human_id'))}
        )


class HumanTask2ListView(HumanListView):
    template_name = 'humans/task.html'
    result = 0
    target_human = None

    def get_queryset(self):
        id = self.kwargs.get('id')
        self.target_human = get_object_or_404(Human, pk=id)
        humans = Human.objects.exclude(pk=id)
        list_of_ids = []
        for human in humans:
            if self.target_human.task_2(human):
                list_of_ids.append(human.id)
                self.result += 1
        return Human.objects.filter(id__in=list_of_ids)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = self.result
        context['target_human'] = self.target_human
        return context


class Index(HumanListView):
    template_name = 'humans/index.html'
