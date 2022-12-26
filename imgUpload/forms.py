from django import forms
# from PIL import Image

class ImageUploadForm(forms.Form):
    image = forms.ImageField()