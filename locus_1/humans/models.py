from django.db import models
from django.urls import reverse

from core.constants import LOCUSES


class Human(models.Model):

    # human_id = models.CharField(max_length=10, unique=True)

    def get_absolute_url(self):
        return reverse('humans:list_human')

    def __eq__(self, other):
        self_dict = self.__dict__.copy()
        other_dict = other.__dict__.copy()
        # self_dict.pop('human_id')
        self_dict.pop('id')
        self_dict.pop('_state')
        # other_dict.pop('human_id')
        other_dict.pop('id')
        other_dict.pop('_state')
        return self_dict == other_dict

    def eq_task_2(self, other):
        self_dict = self.__dict__.copy()
        other_dict = other.__dict__.copy()

        self_dict.pop('id')
        self_dict.pop('_state')
        other_dict.pop('id')
        other_dict.pop('_state')

        for locus in LOCUSES:
            locus_1 = locus + '_1'
            locus_2 = locus + '_2'
            self_list = [self_dict[locus_1], self_dict[locus_2]]
            other_list = [other_dict[locus_1], other_dict[locus_2]]
            self_set = set(self_list)
            other_set = set(other_list)
            if self_set == {None} or other_set == {None}:
                continue
            if None in self_set:
                self_set.remove(None)
            if None in other_set:
                other_set.remove(None)
            if self_set & other_set:
                return False

        return True


for locus in LOCUSES:
    Human.add_to_class(locus + '_1', models.FloatField(blank=True, null=True))
    Human.add_to_class(locus + '_2', models.FloatField(blank=True, null=True))
