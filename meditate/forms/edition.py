from meditate import forms
from django.forms import Form
import sys

class DynamicEntityForm(Form):

    def __init__(self, entity, class_type, *args, **kwargs):
        self.entity = entity
        self.class_type = class_type
        self.base_fields = {}

        self._init_fields()

        super(DynamicEntityForm, self).__init__(*args, **kwargs)

    def _init_fields(self):
        self.base_fields['entity_pk'] = forms.IntegerField(initial=self.entity.pk, required=False, widget=forms.HiddenInput())

        for field_group in self.class_type.genre.field_groups.all().prefetch_related('fields'):

            for field in field_group.fields.all():
                field_class = getattr(sys.modules['meditate.forms'], field.field_type)
                widget_class = getattr(sys.modules['meditate.forms'], field.field_widget)
                try:
                    self.base_fields[field.name] = field_class(
                        initial=self.entity.fields.get(field_type__name=field.name),
                        required=field.mandatory,
                        widget=widget_class(),
                        label=field.title,
                    )
                except:
                    self.base_fields[field.name] = field_class(
                        required=field.mandatory,
                        widget=widget_class(),
                        label=field.title,
                    )

    def save(self):
        from meditate.models import EntityField, ClassField
        self.entity.save()

        self.cleaned_data.pop('entity_pk')

        for field, value in self.cleaned_data.items():
            class_field = ClassField.objects.get(name=field)
            entity_field = EntityField.objects.get_or_create(entity=self.entity, field_type=class_field)[0]
            entity_field.field_value = value.encode('ascii')
            entity_field.save()

        return self.entity