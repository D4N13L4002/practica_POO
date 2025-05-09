from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Select
from django import forms
from core.models import Doctor

class DoctorForm(ModelForm):
    # Definir las opciones para el combobox de especialidades
    SPECIALTY_CHOICES = [
        ('', 'Seleccione una especialidad'),
        ('Medicina General', 'Medicina General'),
        ('Cardiología', 'Cardiología'),
        ('Dermatología', 'Dermatología'),
        ('Neurología', 'Neurología'),
        ('Pediatría', 'Pediatría'),
        ('Ginecología', 'Ginecología'),
        ('Oftalmología', 'Oftalmología'),
        ('Traumatología', 'Traumatología'),
        ('Psiquiatría', 'Psiquiatría'),
        ('Odontología', 'Odontología'),
    ]
    
    # Sobreescribir el campo specialty para convertirlo en un select
    # Esto reemplaza el campo CharField del modelo con un campo de selección en el formulario
    specialty = forms.ChoiceField(
        choices=SPECIALTY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Doctor
        # fields = ['name',' email','phone','specialty']
        #cada campo lo convierte a un control html <input type="text" name="name" id="name" class="form-control" placeholder="Nombre del doctor" required>
        fields = '__all__'
        # exclude = ['phone']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'honorarios': NumberInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            # No incluimos specialty aquí porque ya lo definimos arriba
}