from django import forms
from models import UserProfile, ContratoAutoeducacion


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = [ 'fecha_nacimiento', 'sexo','pais'] 

class ContratoAutoeducacionForm(forms.ModelForm):
	class Meta:
		model = ContratoAutoeducacion
		fields = ('afirmar', 'liberar', 'adquirir')
        labels = {
            'afirmar': ('Que quiero afirmar en mi este a  Aspectos positivos valores que tengo'),
            'liberar': ('De que mas me quiero liberar  Comportamientos negativos en mi personalidad que me impiden crecer'),
            'adquirir': ('Que quiero adquirir para mi Actitudes y conductas que quiero conquistar'),
        }
        help_texts = {
            'afirmar': ('Ej Me consideran alegre entonces mi frase Nada me quitara la alegria'),
            'liberar': ('Ej Dejare de compararme con los demas entonces mi frase Soy original y Dios me ama como soy'),
            'adquirir': ('Ej Me gustaria crecer en la oracion entonces mi frase Todos los dias dialogo con Dios'),
            
        }


