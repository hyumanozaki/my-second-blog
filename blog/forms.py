from django import forms
from .models import MBO22,ADC22,PDI22#PDI22G
from django.core.exceptions import ValidationError
from .models import Post
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# 例外処理
from django.core.exceptions import ObjectDoesNotExist

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

Achoice=[('0','aprovar'),('1','pede ele/ela para corrigir'),]

class MBO22AForm(forms.Form):
    choices=forms.ChoiceField(label='',choices=Achoice,widget=forms.RadioSelect())
        

class MBO22Q1Form(forms.ModelForm):
    # パスワード入力：非表示対応
    #password = forms.CharField(widget=forms.PasswordInput(),label="senha")

    class Meta():
        # ユーザー認証
        model = MBO22
        # フィールド指定
        fields = ('MBO22A1','MBO22AP','MBO22B1','MBO22BP','MBO22C1','MBO22CP','MBO22D1','MBO22DP','MBO22E1','MBO22EP','MBO22F1','MBO22FP','MBO22G1','MBO22GP')
        #fields = ('MBO22A1','MBO22B1','MBO22C1','MBO22D1','MBO22E1','MBO22F1','MBO22G1','MBO22AP','MBO22BP','MBO22CP','MBO22DP','MBO22EP','MBO22FP','MBO22GP')
        labels = {'MBO22A1':"meta1",'MBO22B1':"meta2",'MBO22C1':"meta3",'MBO22D1':"meta4",'MBO22E1':"meta5",'MBO22F1':"meta6",'MBO22G1':"meta7",'MBO22AP':"peso% de meta1",'MBO22BP':"peso% de meta2",'MBO22CP':"peso% de meta3",'MBO22DP':"peso% de meta4",'MBO22EP':"peso% de meta5",'MBO22FP':"peso de meta6",'MBO22GP':"peso% de meta7"}
         #fields = ('MBO22A1','MBO22B1','MBO22C1','MBO22D1','MBO22E1','MBO22F1','MBO22G1')
        #fields = ('username','email','password')
        # フィールド名指定
        #labels = {'username':"Usuario",'email':"Email"}

class MBO22Q2Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2')
        labels = {'MBO22A2':"meta1",'MBO22B2':"meta2",'MBO22C2':"meta3",'MBO22D2':"meta4",'MBO22E2':"meta5",'MBO22F2':"meta6",'MBO22G2':"meta7"}
        
class MBO22Q3Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3')
        labels = {'MBO22A3':"meta1",'MBO22B3':"meta2",'MBO22C3':"meta3",'MBO22D3':"meta4",'MBO22E3':"meta5",'MBO22F3':"meta6",'MBO22G3':"meta7"}
        
class MBO22Q4Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO22A4','MBO22AR','MBO22B4','MBO22BR','MBO22C4','MBO22CR','MBO22D4','MBO22DR','MBO22E4','MBO22ER','MBO22F4','MBO22FR','MBO22G4','MBO22GR')
        labels = {'MBO22A4':"meta1",'MBO22B4':"meta2",'MBO22C4':"meta3",'MBO22D4':"meta4",'MBO22E4':"meta5",'MBO22F4':"meta6",'MBO22G4':"meta7",'MBO22AR':"pontuação",'MBO22BR':"pontuação",'MBO22CR':"pontuação",'MBO22DR':"pontuação",'MBO22ER':"pontuação",'MBO22FR':"pontuação",'MBO22GR':"pontuação"}

#class AddAccountForm(forms.ModelForm):
#    class Meta():
        # モデルクラスを指定
#        model = Account
#        fields = ('last_name','first_name',)
#        labels = {'last_name':"苗字",'first_name':"名前",}
#        fields = ('last_name','first_name','account_image',)
#        labels = {'last_name':"苗字",'first_name':"名前",'account_image':"写真アップロード",}


class ADC22CForm(forms.ModelForm):

    class Meta ():

        model = ADC22
        fields = ('ADC22G1C','ADC22G2C','ADC22G3C','ADC22G4C','ADC22G5C','ADC22G6C','ADC22G7C','ADC22E1C','ADC22E2C')
        labels = {'ADC22G1C':"auto avaliação",'ADC22G2C':"auto avaliação",'ADC22G3C':"auto avaliação",'ADC22G4C':"auto avaliação",'ADC22G5C':"auto avaliação",'ADC22G6C':"auto avaliação",'ADC22G7C':"auto avaliação",'ADC22E1C':"auto avaliação",'ADC22E2C':"auto avaliação"}


class ADC22AOForm(forms.ModelForm):

    class Meta ():

        model = ADC22
        fields = ('ADC22G1A','ADC22G1O','ADC22G2A','ADC22G2O','ADC22G3A','ADC22G3O','ADC22G4A','ADC22G4O','ADC22G5A','ADC22G5O','ADC22G6A','ADC22G6O','ADC22G7A','ADC22G7O','ADC22E1A','ADC22E1O','ADC22E2A','ADC22E2O')
        labels = {'ADC22G1A':"avaliação por avaliador/a",'ADC22G1O':"observação por avaliador/a",'ADC22G2A':"avaliação por avaliador/a",'ADC22G2O':"observação por avaliador/a",'ADC22G3A':"avaliação por avaliador/a",'ADC22G3O':"observação por avaliador/a",'ADC22G4A':"avaliação por avaliador/a",'ADC22G4O':"observação por avaliador/a",'ADC22G5A':"avaliação por avaliador/a",'ADC22G5O':"observação por avaliador/a",'ADC22G6A':"avaliação por avaliador/a",'ADC22G6O':"observação por avaliador/a",'ADC22G7A':"avaliação por avaliador/a",'ADC22G7O':"observação por avaliador/a",'ADC22E1A':"avaliação por avaliador/a",'ADC22E1O':"observação por avaliador/a",'ADC22E2A':"avaliação por avaliador/a",'ADC22E2O':"observação por avaliador/a"}


class PDI22Form(forms.ModelForm):

    class Meta ():

        model = PDI22
        fields = ('PDI22G1C','PDI22G2C','PDI22G3C','PDI22G1PD','PDI22G2PD','PDI22G3PD','PDI22E1PD','PDI22E2PD','PDI22G1','PDI22G2','PDI22G3','PDI22E1','PDI22E2')
        labels = {'PDI22G1C':"foco1",'PDI22G2C':"foco2",'PDI22G3C':"foco3",'PDI22G1PD':"ponto-a-desenvolver-1",'PDI22G2PD':"ponto-a-desenvolver-2",'PDI22G3PD':"ponto-a-desenvolver-3",'PDI22E1PD':"ponto-a-desenvolver-4",'PDI22E2PD':"ponto-a-desenvolver-5",'PDI22G1':"PDI-1",'PDI22G2':"PDI-2",'PDI22G3':"PDI-3",'PDI22E1':"PDI-4",'PDI22E2':"PDI-5"}


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
        