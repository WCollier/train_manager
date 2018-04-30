from django.forms import ModelForm

from .models import Collection, ModelTrain 

class CollectionForm(ModelForm):
    class Meta:
        model = Collection 

        fields = ['name', 'description', 'trains']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')

        super(CollectionForm, self).__init__(*args, **kwargs)

        self.fields['trains'].queryset = ModelTrain.objects.filter(owner=user)