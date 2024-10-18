from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

from core.constants import LOCUSES

User = get_user_model()


class Human(models.Model):
    added_by = models.ForeignKey(
        User, verbose_name='Добавил(а)', blank=True,
        null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse_lazy('humans:index')

    def prepare_task(self, other):
        self_dict = self.__dict__.copy()
        other_dict = other.__dict__.copy()
        self_dict.pop('id')
        self_dict.pop('_state')
        other_dict.pop('id')
        other_dict.pop('_state')
        return (self_dict, other_dict)

    def task_1(self, other):
        self_dict, other_dict = self.prepare_task(other)
        return self_dict == other_dict

    def task_2(self, other):
        self_dict, other_dict = self.prepare_task(other)

        for locus in LOCUSES:
            locus_1 = locus + '_1'
            locus_2 = locus + '_2'

            self_set = set([self_dict[locus_1], self_dict[locus_2]])
            other_set = set([other_dict[locus_1], other_dict[locus_2]])

            if self_set == other_set:
                continue
            return False

        return True


for locus in LOCUSES:
    Human.add_to_class(locus + '_1', models.FloatField(blank=True, null=True))
    Human.add_to_class(locus + '_2', models.FloatField(blank=True, null=True))
