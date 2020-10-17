from django import forms
from .models import Comment
from .models import Collab


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class NewCollabForm(forms.ModelForm):
    class Meta:
        model = Collab
        fields = ['content']