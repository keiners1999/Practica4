from django import forms
from apps.equipo.models import Mantenimiento

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model= Mantenimiento
        
        fields = {
            'tipoMantenimiento',
            'EmpleadoId',
            'EquipoId',
            'fecha',
        }
        
        labels = {
            'tipoMantenimiento': 'Ingresar el Tipo de Mantenimiento',
            'EmpleadoId': 'Ingrese el empleado',
            'EquipoId': 'Ingrese el equipo',
            'fecha': 'Ingrese la Fecha',
        }
        
        widgets = {
            'tipoMantenimiento': forms.TextInput(attrs= {'class': 'form-control'}),
            'EmpleadoId': forms.Select(attrs= {'class': 'form-control'}),
            'EquipoId': forms.Select(attrs= {'class': 'form-control'}),
            'fecha': forms.TextInput(attrs= {'class': 'form-control'}),  
        }
        
        
        
    
    
