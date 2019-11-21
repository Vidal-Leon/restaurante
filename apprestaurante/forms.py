from django import forms
from .models import Menu, Plato, Empleado, Venta, Cliente

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('nombre', 'plato')

def __init__ (self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["plato"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["plato"].help_text = "Ingrese los platos del menu"
#En este caso le indicamos que nos muestre todas las tropas, pero aquí podríamos filtrar datos si fuera necesario
        self.fields["plato"].queryset = Plato.objects.all()
