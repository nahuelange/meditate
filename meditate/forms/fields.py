from django.forms.fields import IntegerField, Field, CharField, EmailField


class MeditateField(Field):
    pass

class CharField(MeditateField, CharField):
    pass

class EmailField(MeditateField, EmailField):
    pass

class IntegerField(MeditateField, IntegerField):
    pass

