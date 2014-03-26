import inspect
from inspect import isclass
from meditate import forms
from django.db import models
from django.conf import settings
from meditate.forms.edition import DynamicEntityForm


class Class(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(unique=True, max_length=255)

    def __unicode__(self):
        return self.title


class ClassType(models.Model):
    genre = models.ForeignKey(Class, related_name="class_types")
    title = models.CharField(max_length=255)
    name = models.CharField(unique=True, max_length=255)
    template = models.CharField(max_length=255)
    creation_mode = models.IntegerField(choices=settings.CREATION_MODES)
    default_status = models.IntegerField(choices=settings.ENTITIES_STATUSES)
    can_heritate = models.ManyToManyField(Class)

    def __unicode__(self):
        return self.title
        unique_together = (
            ('genre', 'name',),
            ('genre', 'rank',),
        )

class ClassFieldGroup(models.Model):
    genre = models.ForeignKey(Class, related_name="field_groups")
    title = models.CharField(max_length=255)
    name = models.CharField(unique=True, max_length=255)
    rank = models.IntegerField()

    def __unicode__(self):
        return self.title
        unique_together = (
            ('genre', 'name',),
            ('genre', 'rank',),
        )


class ClassField(models.Model):

    FIELD_TYPES = [(k, v) for k,v in inspect.getmembers(forms) if isclass(v) and issubclass(v, forms.MeditateField)]
    FIELD_WIDGETS = [(k, v) for k,v in inspect.getmembers(forms) if isclass(v) and issubclass(v, forms.MeditateWidget)]

    genre = models.ForeignKey(Class, related_name="fields")
    group = models.ForeignKey(ClassFieldGroup, related_name="fields")

    title = models.CharField(max_length=255)
    name = models.CharField(unique=True, max_length=255)
    field_type = models.CharField(max_length=255, choices=FIELD_TYPES)
    field_widget = models.CharField(max_length=255, choices=FIELD_WIDGETS)
    dc_type = models.CharField(max_length=255)
    default_value = models.CharField(max_length=255, null=True, default=None, blank=True)
    mandatory = models.BooleanField(default=False)
    rank = models.IntegerField()


    def __unicode__(self):
        return self.title


class Entity(models.Model):

    parent = models.ForeignKey('self', related_name="children", null=True)
    class_type = models.ForeignKey(ClassType, related_name="entities")
    status = models.IntegerField(default=0)

    @staticmethod
    def get_form(entity, class_type, post_data):

        form = DynamicEntityForm(entity, class_type, post_data)
        return form

    def __str__(self):
        '''
        La représentation d'une entité est son DC.Title
        '''
        # title_cf = ClassField.objects.get(genre=self.class_type.genre, dc_type="dc.title")
        return self.fields.get(field_type__dc_type="dc.title").field_value

class EntityField(models.Model):
    entity = models.ForeignKey(Entity, related_name="fields")
    field_type = models.ForeignKey(ClassField)
    field_value = models.TextField()

    def __str__(self):
        return self.field_value
