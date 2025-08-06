from django import forms

TIPO_CHOICES = [
    ('apartamento', 'Apartamento'),
    ('casa', 'Casa'),
    # agrega otros tipos si tienes más
]

UPZ_CHOICES = [
    ('Chapinero', 'Chapinero'),
    ('Ciudad Bolivar', 'Ciudad Bolívar'),
    ('Engativá', 'Engativá'),
    ('Fontibón ', 'Fontibón'),
    ('Kennedy', 'Kennedy'),
    ('Puente Aranda', 'Puente Aranda'),
    ('Santa Fe', 'Santa Fe'),
    ('Suba', 'Suba'),
    ('Usaquén', 'Usaquén'),
    # agrega otros tipos si tienes más
]
class PrediccionForm(forms.Form):
    tipo = forms.ChoiceField(choices=TIPO_CHOICES, label="Tipo de inmueble")
    habitaciones = forms.IntegerField(label="Número de habitaciones", min_value=0)
    baños = forms.IntegerField(label="Número de baños", min_value=0)
    area = forms.FloatField(label="Área en m²", min_value=0)
    upz = forms.ChoiceField(choices=UPZ_CHOICES, label="UPZ")
    barrio = forms.CharField(label="Barrio", max_length=100)