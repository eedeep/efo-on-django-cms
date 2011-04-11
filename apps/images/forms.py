
from django import forms


class ImageAdminModelForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        """
        Apply the mceNoEditor class to the caption field.
        Also while we're at it, apply classes for text counter javascript behaviour.
        """
        super(ImageAdminModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            if field == "caption":
                self.fields[field].widget.attrs["class"] = "mceNoEditor text-counter"
                self.fields[field].widget.attrs["maxlength"] = "115"

