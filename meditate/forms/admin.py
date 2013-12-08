from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from meditate.models import Class, ClassType, ClassFieldGroup, ClassField


class ClassForm(forms.ModelForm):

    class Meta:
        model = Class


class ClassTypeForm(forms.ModelForm):

    can_heritate = forms.ModelMultipleChoiceField(widget=CheckboxSelectMultiple, queryset=Class.objects.all())

    class Meta:
        model = ClassType
        exclude = ('genre',)

class ClassFieldGroupForm(forms.ModelForm):

    class Meta:
        model = ClassFieldGroup
        exclude = ('genre',)


class ClassFieldForm(forms.ModelForm):

    class Meta:
        model = ClassField
        exclude = ('genre', 'group')

