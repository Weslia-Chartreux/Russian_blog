from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from testik.models import Post

from testik.models import Community


class NewPostForm(forms.Form):
    name = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    list_group = [(False, 'Без группы')] + list([(i.id, i) for i in Community.objects.all()])
    group = forms.ChoiceField(choices=list_group)

    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data) >= 100:
            raise ValidationError('Слишком длинное название')
        return ' '.join(data.split())
