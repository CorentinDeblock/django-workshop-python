from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        title = forms.CharField(max_length=100)
        fields = ['cover', 'title']

    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)

        cover = self.fields['cover']
        title = self.fields['title']

        cover.label = "Charger votre fichier"
        title.label = ""
        title.widget.attrs.update({
            'placeholder':'Votre titre'
        })