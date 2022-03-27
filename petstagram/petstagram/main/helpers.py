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
            if 'class' not in fields.widget.attrs:
                fields.widget.attrs['class'] = ''

            fields.widget.attrs['class'] += ' form-control'
