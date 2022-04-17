from petstagram.main.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]

    return None


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, fields in self.fields.items():
            if not hasattr(fields.widget, 'attrs'):
                setattr(fields.widget, 'attrs', {})

            if 'class' not in fields.widget.attrs:
                fields.widget.attrs['class'] = ''

            fields.widget.attrs['class'] += ' form-control'


class DisableFieldsFormMixin:
    disabled_fields = '__all__'
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            if self.disabled_fields != '__all__' and name not in self.disabled_fields:
                continue

            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['readonly'] = 'readonly'
