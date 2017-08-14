from django import forms
from .models import Partner
from .models import PartnerKnown

class PartnerForm(forms.ModelForm):

    class Meta:
        model = Partner
        fields = ('firstname', 'lastname', 'birthday', 'comment')


class PartnerKnownForm(forms.ModelForm):

    seen = forms.MultipleChoiceField(
        required=False,
        choices = PartnerKnown.SEEN_LIST,
        widget  = forms.CheckboxSelectMultiple
    )

    class Meta:
        model = PartnerKnown
        fields = ('seen',)
