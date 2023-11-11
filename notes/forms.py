from django import forms
from django.forms import ModelForm
from .models import Note
from django.core.exceptions import ValidationError
import os


# creating a form for custom validation
class CreateViewForm(forms.ModelForm):

    # Meta class is there for defining and altering various metadata features
    class Meta:
        model = Note
        fields = ['title','content','image','audio']

    def clean(self): # validation function
        cleaned_data = super(CreateViewForm, self).clean()

        input_field_1 = cleaned_data.get('title') # getting input from the title field
        input_field_2 = cleaned_data.get('content') # getting input from the content field

        if input_field_1 is not None and input_field_2 is not None:
            if len(input_field_2)<3:
                # self.add_error(None, ValidationError('The title should be different')) # non-field error
                self.add_error('content', ValidationError('The message is too short')) # title field error

    # #   renaming uploaded images
    # def image_file_name(instance, filename):
    #     ext = filename.split('.')[-1]
    #     filename = "%s_%s.%s" % (instance.date_posted, instance.title, ext) # %s correspond to instances to pass to the new file name
    #     return os.path.join('images', filename)


class UpdateViewForm(forms.ModelForm):

    title = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    image_clear = forms.BooleanField(required=False)
    audio = forms.FileField(required=False)

    class Meta:
        model = Note
        fields = ['title','content','date_posted','image','audio']

    def clean(self):
        cleaned_data = super(UpdateViewForm, self).clean()

        input_field_1 = cleaned_data.get('title')
        input_field_2 = cleaned_data.get('content')

        if input_field_1 is not None and input_field_2 is not None:
            if len(input_field_2)<3:
                self.add_error('content', ValidationError('The message is too short'))