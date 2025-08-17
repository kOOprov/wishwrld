from.models import Feedback, UploadSongs
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, FileInput, DateInput


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','full_text','date']
        widgets = {
            'name':TextInput(attrs={
                'placeholder': 'imya'
            }),
            'full_text': Textarea(attrs={
                'placeholder': 'add...'
            }),
            'date':DateInput(attrs={
                'placeholder':'date',
                'type': 'date'
            })
        }

class UploadSongsForm(ModelForm):
    class Meta:
        model = UploadSongs
        fields = ['autor','song_name','file']
        widgets = {
            'autor': TextInput(attrs={
                'placeholder': 'autor'
            }),
            'song_name': TextInput(attrs={
                'placeholder': 'song name'
            }),
            'file': FileInput()
        }