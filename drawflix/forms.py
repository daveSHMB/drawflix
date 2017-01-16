from django import forms
from drawflix.models import Drawing

class DrawingForm(forms.ModelForm):

    film = forms.CharField(max_length=200)
    image = forms.CharField()
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and Drawing model
        model = Drawing

        fields = ('image', 'film')
        exclude = ('user', 'date')
