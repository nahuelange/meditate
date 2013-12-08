from django.forms.widgets import Widget, Textarea, TextInput, HiddenInput, EmailInput


class MeditateWidget(Widget):
    pass

class DefaultWidget(MeditateWidget):
    pass

class HiddenInput(MeditateWidget, HiddenInput):
    pass

class Textarea(MeditateWidget, Textarea):
    pass

class TextInput(MeditateWidget, TextInput):
    pass

class EmailInput(MeditateWidget, EmailInput):
    pass

