from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from meditate.models import Entity, ClassType, Class


def dashboard(request):
    c = RequestContext(request, {
        'classes': Class.objects.all(),
        'entities': Entity.objects.filter(parent__isnull=True),
    })

    return render_to_response('meditate/edition/dashboard.html', c)


def entity_edit(request, parent_pk=None, entity_pk=None, class_type_name=None):
    print(class_type_name)
    if entity_pk:
        entity = get_object_or_404(Entity, pk=entity_pk)
        class_type = entity.class_type
    else:
        class_type = get_object_or_404(ClassType, name=class_type_name)
        entity = Entity(parent=parent_pk, class_type=class_type)

    post_data = request.POST if request.method == "POST" else None

    form = Entity.get_form(entity, class_type, post_data)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse('meditate.views.edition.dashboard'))

    c = RequestContext(request, {
        'form': form,
        'parent': parent_pk,
        'entity': entity,
        'class_type_name': class_type_name,
        })

    return render_to_response('meditate/edition/entity_edit.html', c)