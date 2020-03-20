from django import forms
from .models import Apply

class PostApply(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('name','gender',
        'phone','year','major','url','why','service','memory','coding','files')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['files'].required = False