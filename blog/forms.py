from django import forms
from .models import MBO22,ADC22,PDI22#PDI22G
from django.core.exceptions import ValidationError
from .models import Post
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class uploadForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password","first_name","last_name"]

class readForm(forms.Form):
    name = forms.CharField(max_length=50)
    boss = forms.CharField(max_length=50)
    FN = forms.CharField(max_length=50)
    LN = forms.CharField(max_length=50)
    PW = forms.CharField(max_length=50)


# 例外処理
from django.core.exceptions import ObjectDoesNotExist

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

Achoice=[('0','aprovar'),('1','pede ele/ela para corrigir'),]


class DeptForm(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('DEPT',)
        lables = {'DEPT':"escolhe seu departamento"}

class MBO22Q1Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO22A1','MBO22AP','MBO22B1','MBO22BP','MBO22C1','MBO22CP','MBO22D1','MBO22DP','MBO22E1','MBO22EP','MBO22F1','MBO22FP','MBO22G1','MBO22GP')
        labels = {'MBO22A1':"meta1",'MBO22B1':"meta2",'MBO22C1':"meta3",'MBO22D1':"meta4",'MBO22E1':"meta5",'MBO22F1':"meta6",'MBO22G1':"meta7",'MBO22AP':"peso% de meta1",'MBO22BP':"peso% de meta2",'MBO22CP':"peso% de meta3",'MBO22DP':"peso% de meta4",'MBO22EP':"peso% de meta5",'MBO22FP':"peso de meta6",'MBO22GP':"peso% de meta7"}
        widgets = {
            'MBO22A1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22B1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22C1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22D1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22E1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22F1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22G1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22AP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22BP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22CP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22DP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22EP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22FP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22GP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            }

class MBO22Q2Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2')
        labels = {'MBO22A2':"meta1",'MBO22B2':"meta2",'MBO22C2':"meta3",'MBO22D2':"meta4",'MBO22E2':"meta5",'MBO22F2':"meta6",'MBO22G2':"meta7"}
        widgets = {
            'MBO22A2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22B2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22C2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22D2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22E2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22F2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22G2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            }
        
class MBO22Q3Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3')
        labels = {'MBO22A3':"meta1",'MBO22B3':"meta2",'MBO22C3':"meta3",'MBO22D3':"meta4",'MBO22E3':"meta5",'MBO22F3':"meta6",'MBO22G3':"meta7"}
        widgets = {
            'MBO22A3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22B3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22C3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22D3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22E3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22F3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22G3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            }
        
class MBO22Q4Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO22A4','MBO22AR','MBO22B4','MBO22BR','MBO22C4','MBO22CR','MBO22D4','MBO22DR','MBO22E4','MBO22ER','MBO22F4','MBO22FR','MBO22G4','MBO22GR')
        labels = {'MBO22A4':"meta1",'MBO22B4':"meta2",'MBO22C4':"meta3",'MBO22D4':"meta4",'MBO22E4':"meta5",'MBO22F4':"meta6",'MBO22G4':"meta7",'MBO22AR':"pontuação",'MBO22BR':"pontuação",'MBO22CR':"pontuação",'MBO22DR':"pontuação",'MBO22ER':"pontuação",'MBO22FR':"pontuação",'MBO22GR':"pontuação"}
        widgets = {
            'MBO22A4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22B4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22C4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22D4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22E4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22F4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22G4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22AR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22BR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22CR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22DR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22ER':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22FR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22GR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            }



class ADC22CForm(forms.ModelForm):

    class Meta ():

        model = ADC22
        fields = ('ADC22G1C','ADC22G1OC','ADC22G2C','ADC22G2OC','ADC22G3C','ADC22G3OC','ADC22G4C','ADC22G4OC','ADC22G5C','ADC22G5OC','ADC22G6C','ADC22G6OC','ADC22G7C','ADC22G7OC','ADC22E1C','ADC22E1OC','ADC22E2C','ADC22E2OC')
        labels = {'ADC22G1C':"auto avaliação",'ADC22G1OC':"observação por colaborador",'ADC22G2C':"auto avaliação",'ADC22G2OC':"observação por colaborador",'ADC22G3C':"auto avaliação",'ADC22G3OC':"observação por colaborador",'ADC22G4C':"auto avaliação",'ADC22G4OC':"observação por colaborador",'ADC22G5C':"auto avaliação",'ADC22G5OC':"observação por colaborador",'ADC22G6C':"auto avaliação",'ADC22G6OC':"observação por colaborador",'ADC22G7C':"auto avaliação",'ADC22G7OC':"observação por colaborador",'ADC22E1C':"auto avaliação",'ADC22E1OC':"observação por colaborador",'ADC22E2C':"auto avaliação",'ADC22E2OC':"observação por colaborador"}
        widgets = {
            'ADC22E1OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22E1C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22E2OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22E2C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G1OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G1C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G2OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G2C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G3OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G3C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G4OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G4C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G5OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G5C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G6OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G6C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G7OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G7C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            }
        

class ADC22AOForm(forms.ModelForm):

    class Meta ():

        model = ADC22
        fields = ('ADC22G1A','ADC22G1O','ADC22G2A','ADC22G2O','ADC22G3A','ADC22G3O','ADC22G4A','ADC22G4O','ADC22G5A','ADC22G5O','ADC22G6A','ADC22G6O','ADC22G7A','ADC22G7O','ADC22E1A','ADC22E1O','ADC22E2A','ADC22E2O')
        labels = {'ADC22G1A':"avaliação por avaliador/a",'ADC22G1O':"observação por avaliador/a",'ADC22G2A':"avaliação por avaliador/a",'ADC22G2O':"observação por avaliador/a",'ADC22G3A':"avaliação por avaliador/a",'ADC22G3O':"observação por avaliador/a",'ADC22G4A':"avaliação por avaliador/a",'ADC22G4O':"observação por avaliador/a",'ADC22G5A':"avaliação por avaliador/a",'ADC22G5O':"observação por avaliador/a",'ADC22G6A':"avaliação por avaliador/a",'ADC22G6O':"observação por avaliador/a",'ADC22G7A':"avaliação por avaliador/a",'ADC22G7O':"observação por avaliador/a",'ADC22E1A':"avaliação por avaliador/a",'ADC22E1O':"observação por avaliador/a",'ADC22E2A':"avaliação por avaliador/a",'ADC22E2O':"observação por avaliador/a"}
        widgets = {
            'ADC22E1O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22E1A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22E2O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22E2A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G1O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G1A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G2O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G2A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G3O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G3A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G4O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G4A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G5O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G5A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G6O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G6A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G7O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G7A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            }


class PDI22Form(forms.ModelForm):

    class Meta ():

        model = PDI22
        fields = ('PDI22G1C','PDI22G2C','PDI22G3C','PDI22G1PD','PDI22G2PD','PDI22G3PD','PDI22E1PD','PDI22E2PD','PDI22G1','PDI22G2','PDI22G3','PDI22E1','PDI22E2')
        labels = {'PDI22G1C':"foco1",'PDI22G2C':"foco2",'PDI22G3C':"foco3",'PDI22G1PD':"ponto-a-desenvolver-1",'PDI22G2PD':"ponto-a-desenvolver-2",'PDI22G3PD':"ponto-a-desenvolver-3",'PDI22E1PD':"ponto-a-desenvolver-4",'PDI22E2PD':"ponto-a-desenvolver-5",'PDI22G1':"PDI-1",'PDI22G2':"PDI-2",'PDI22G3':"PDI-3",'PDI22E1':"PDI-4",'PDI22E2':"PDI-5"}
        widgets = {
            'PDI22G1PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22G2PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22G3PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22E1PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22E2PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22G1':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22G2':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22G3':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22E1':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22E2':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22G1C':forms.Select(attrs={'style': 'width:39ch; height:14ch; border-color:white; background-color:white'}),
            'PDI22G2C':forms.Select(attrs={'style': 'width:39ch; height:14ch; border-color:white; background-color:white'}),
            'PDI22G3C':forms.Select(attrs={'style': 'width:39ch; height:14ch; border-color:white; background-color:white'}),
            }


#class PDI22GForm(forms.ModelForm):

#    class Meta ():

#        model = PDI22
#        fields = ('PDI22G1C','PDI22G1PD','PDI22G1','PDI22G2C','PDI22G2PD','PDI22G2','PDI22G3C','PDI22G3PD','PDI22G3','PDI22E1C','PDI22E1PD','PDI22E1','PDI22E2C','PDI22E2PD','PDI22E2')
#        fields = ('PDI22G1PD','PDI22G1','PDI22G2PD','PDI22G2','PDI22G3PD','PDI22G3')

#class PDI22EForm(forms.ModelForm):

#    class Meta ():

#        model = PDI22
#        fields = ('PDI22G1C','PDI22G1PD','PDI22G1','PDI22G2C','PDI22G2PD','PDI22G2','PDI22G3C','PDI22G3PD','PDI22G3','PDI22E1C','PDI22E1PD','PDI22E1','PDI22E2C','PDI22E2PD','PDI22E2')
#        fields = ('PDI22E1PD','PDI22E1','PDI22E2PD','PDI22E2')


#class PDI22GCForm(forms.ModelForm):
#    PDI22G1C = forms.ModelChoiceField(queryset=ADC22GRH.objects.values('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7'), blank=True)
#    PDI22G2C = forms.ModelChoiceField(queryset=ADC22GRH.objects.values('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7'), blank=True)
#    PDI22G3C = forms.ModelChoiceField(queryset=ADC22GRH.objects.values('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7'), blank=True)
    
#    class Meta ():

#        model = PDI22G
#        fields = ('PDI22G1C','PDI22G2C','PDI22G3C')
        