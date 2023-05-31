from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ('nom', 'descriptif')
        labels = {
            'nom' : _('Nom'),
            'descriptif' : _('Descriptif')
        }