from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"
        exclude = ['name']  


        widgets={

            'title': forms.TextInput(attrs={'placeholder': 'Post Ttitle'}),
            'blog_content': forms.Textarea(attrs={'placeholder': 'Your Content ..'}),
           
        }



# Overriding  the label
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # self.fields['doc_name'].empty_label = 'Select Doctor'

        # Remove labels for specific fields
        self.fields['title'].label = False
        self.fields['blog_content'].label = False
        self.fields['post_image'].label = False
        self.fields['Category'].label = False
       