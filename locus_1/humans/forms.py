from django import forms

from .models import Human
from core.constants import LOCUSES


class HumanForm(forms.ModelForm):

    class Meta:
        model = Human
        fields = '__all__'

    def clean(self):
        for locus in LOCUSES:
            locus_1 = locus + '_1'
            locus_2 = locus + '_2'
            locus_1_value = self.cleaned_data.get(locus_1)
            locus_2_value = self.cleaned_data.get(locus_2)
            if locus_1_value and locus_2_value:
                if locus_1_value > locus_2_value:
                    raise forms.ValidationError(
                        'locus_value_1 > locus_value_2')
        return self.cleaned_data
