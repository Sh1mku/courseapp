from django import forms
from courses.models import Course

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label="kurs basligi", 
#         required=True, 
#         error_messages={
#             "required": "kurs basligi girmelisiniz"}, 
#         widget=forms.TextInput(attrs={"class":"form-control"}))
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))    

class  CourseCreateForm(forms.ModelForm):
    class Meta:
        model=Course
        fields = ('title', 'description', 'imageUrl', 'slug')
        labels ={
            'title' : "kurs basligi",
            'description':'aciklama'
        }
        widgets = {
            'title' : forms.TextInput(attrs={"class":"form-control"}),
            'description' : forms.Textarea(attrs={"class":"form-control"}),
            'imageUrl' : forms.TextInput(attrs={"class":"form-control"}),
            'slug' : forms.TextInput(attrs={"class":"form-control"}),

        }
        error_messages = {
            "title": {
                "required":"kurs basligi girmelisiniz.",
                "max_length": "maksimum 50 karakter girmelisiniz"
            },
            "description":{
                "required":"kurs aciklamasi gereklidir."
            }
        }

class  CourseEditForm(forms.ModelForm):
    class Meta:
        model=Course
        fields = ('title', 'description', 'imageUrl', 'slug','categories','isActive')
        labels ={
            'title' : "kurs basligi",
            'description':'aciklama'
        }
        widgets = {
            'title' : forms.TextInput(attrs={"class":"form-control"}),
            'description' : forms.Textarea(attrs={"class":"form-control"}),
            'imageUrl' : forms.TextInput(attrs={"class":"form-control"}),
            'slug' : forms.TextInput(attrs={"class":"form-control"}),
            "categories":forms.SelectMultiple(attrs={"class":"form-control"})
        }
        error_messages = {
            "title": {
                "required":"kurs basligi girmelisiniz.",
                "max_length": "maksimum 50 karakter girmelisiniz"
            },
            "description":{
                "required":"kurs aciklamasi gereklidir."
            }
        }