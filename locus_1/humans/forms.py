from django import forms
from django.core.exceptions import ObjectDoesNotExist

from core.constants import LOCUSES
from humans.models import Human


class HumanPrepareForm(forms.Form):
    human_id = forms.IntegerField(label='ID записи')

    def clean_human_id(self):
        id = self.cleaned_data.get('human_id')
        try:
            Human.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise forms.ValidationError(
                f'Записи с ID: {id} нет в базе!'
            )
        return self.cleaned_data


class HumanForm(forms.ModelForm):

    class Meta:
        model = Human
        exclude = ('added_by',)

    def clean(self):
        for locus in LOCUSES:
            locus_1 = locus + '_1'
            locus_2 = locus + '_2'
            locus_1_value = self.cleaned_data.get(locus_1)
            locus_2_value = self.cleaned_data.get(locus_2)
            if locus_1_value and locus_2_value:
                if locus_1_value > locus_2_value:
                    raise forms.ValidationError(
                        f'ОШИБКА: {locus_1} [{locus_1_value}] >'
                        f'{locus_2} [{locus_2_value}]!')
        return self.cleaned_data
