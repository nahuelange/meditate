from django.forms.widgets import Widget, Textarea, TextInput, HiddenInput, EmailInput


class MeditateWidget(Widget):
    @staticmethod
    def factory(widget, default):
        if widget is DefaultWidget:
            return default()
        else:
            return widget()

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

