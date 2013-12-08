from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^admin/$', 'meditate.views.admin.dashboard' ),
    (r'^admin/classes/$', 'meditate.views.admin.entities_classes'),
    (r'^admin/classes/add$', 'meditate.views.admin.entities_classes_edit'),
    (r'^admin/classes/(?P<class_pk>\d+)/edit$', 'meditate.views.admin.entities_classes_edit'),
    (r'^admin/classes/(?P<class_pk>\d+)/types$', 'meditate.views.admin.entities_classes_types'),
    (r'^admin/classes/(?P<class_pk>\d+)/types/add$', 'meditate.views.admin.entities_classes_types_edit'),
    (r'^admin/classes/(?P<class_pk>\d+)/types/(?P<type_pk>\d+)/$', 'meditate.views.admin.entities_classes_types_edit'),
    (r'^admin/classes/(?P<class_pk>\d+)/fieldgroups$', 'meditate.views.admin.entities_classes_field_groups'),
    (r'^admin/classes/(?P<class_pk>\d+)/fieldgroups/add$', 'meditate.views.admin.entities_classes_field_group_edit'),
    (r'^admin/classes/(?P<class_pk>\d+)/fieldgroups/(?P<field_group_pk>\d+)/edit$', 'meditate.views.admin.entities_classes_field_group_edit'),
    (r'^admin/classes/(?P<class_pk>\d+)/fieldgroups/(?P<field_group_pk>\d+)/field/add$', 'meditate.views.admin.entities_classes_field_edit'),
    (r'^admin/classes/(?P<class_pk>\d+)/fieldgroups/(?P<field_group_pk>\d+)/field/(?P<field_pk>\d+)/edit$', 'meditate.views.admin.entities_classes_field_edit'),

    (r'^edition/$', 'meditate.views.edition.dashboard'),
    (r'^edition/entity/((?P<parent_pk>\d+)/)?add/(?P<class_type_name>[\ \w\d]+)/$', 'meditate.views.edition.entity_edit'),
    (r'^edition/entity/(?P<entity_pk>\d+)/edit$', 'meditate.views.edition.entity_edit'),
)
