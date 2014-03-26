from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from meditate.forms.admin import ClassForm, ClassTypeForm, ClassFieldGroupForm, ClassFieldForm
from meditate.models import Class, ClassType, ClassFieldGroup, ClassField


def dashboard(request):
    return render_to_response('meditate/admin/dashboard.html')

def entities_classes(request):
    c = RequestContext(request, {
        'classes': Class.objects.all(),
    })
    return render_to_response('meditate/admin/classes_entities.html', c)


def entities_classes_edit(request, class_pk=None):
    if class_pk:
        class_object = get_object_or_404(Class, pk=class_pk)
    else:
        class_object = Class()

    if request.method == "POST":
        form = ClassForm(request.POST, instance=class_object)
        if form.is_valid():
            form.save()
            return redirect(reverse('meditate.views.admin.entities_classes_types', kwargs={'class_pk': form.instance.pk,}))
    else:
        form = ClassForm(instance=class_object)

    c = RequestContext(request, {
        'class': class_object,
        'form': form,
    })

    return render_to_response('meditate/admin/classes_entities_edit.html', c)


def entities_classes_types(request, class_pk):
    class_object = get_object_or_404(Class, pk=class_pk)

    c = RequestContext(request, {
        'class': class_object,
    })
    return render_to_response('meditate/admin/classes_entities_types.html', c)


def entities_classes_types_edit(request, class_pk, type_pk=None):
    class_object = get_object_or_404(Class, pk=class_pk)

    if type_pk:
        type_object = get_object_or_404(ClassType, genre=class_pk, pk=type_pk)
    else:
        type_object = ClassType(genre=class_object)

    if request.method == "POST":
        form = ClassTypeForm(request.POST, instance=type_object)
        if form.is_valid():
            form.save()
            return redirect(reverse('meditate.views.admin.entities_classes_types', kwargs={'class_pk': class_object.pk}))
    else:
        form = ClassTypeForm(instance=type_object)

    c = RequestContext(request, {
        'form': form,
        'class': class_object,
        'type': type_object,
    })

    return render_to_response('meditate/admin/classes_entities_types_edit.html', c)

def entities_classes_field_groups(request, class_pk):
    class_object = get_object_or_404(Class, pk=class_pk)

    c = RequestContext(request, {
        'class': class_object,
        'field_groups': class_object.field_groups.all().order_by('rank')
    })
    return render_to_response('meditate/admin/classes_entities_field_groups.html', c)


def entities_classes_field_group_edit(request, class_pk, field_group_pk=None):
    class_object = get_object_or_404(Class, pk=class_pk)

    if field_group_pk:
        field_group_object = get_object_or_404(ClassFieldGroup, genre=class_pk, pk=field_group_pk)
    else:
        field_group_object = ClassFieldGroup(genre=class_object)

    if request.method == "POST":
        form = ClassFieldGroupForm(request.POST, instance=field_group_object)
        if form.is_valid():
            form.save()
            return redirect(reverse('meditate.views.admin.entities_classes_field_groups', kwargs={'class_pk': class_object.pk}))
    else:
        form = ClassFieldGroupForm(instance=field_group_object)

    c = RequestContext(request, {
        'form': form,
        'class': class_object,
        'field_group': field_group_object,
    })

    return render_to_response('meditate/admin/classes_entities_field_groups_edit.html', c)

def entities_classes_field_edit(request, class_pk, field_group_pk, field_pk=None):
    class_object = get_object_or_404(Class, pk=class_pk)
    field_group_object = get_object_or_404(ClassFieldGroup, genre=class_pk, pk=field_group_pk)

    if field_pk:
        field_object = get_object_or_404(ClassField, group=field_group_pk, genre=class_object, pk=field_pk)
    else:
        field_object = ClassField(group=field_group_object, genre=class_object)

    if request.method == "POST":
        form = ClassFieldForm(request.POST, instance=field_object)
        if form.is_valid():
            form.save()
            return redirect(reverse('meditate.views.admin.entities_classes_field_groups', kwargs={'class_pk': class_pk}))
    else:
        form = ClassFieldForm(instance=field_object)

    c = RequestContext(request, {
        'form': form,
    })

    return render_to_response('meditate/admin/classes_entities_edit.html', c)
