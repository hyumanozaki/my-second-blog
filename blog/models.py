from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# ユーザーアカウントのモデルクラス
class MBO22(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    MBO22A1 = models.TextField(blank=True)
    MBO22B1 = models.TextField(blank=True)
    MBO22C1 = models.TextField(blank=True)
    MBO22D1 = models.TextField(blank=True)
    MBO22E1 = models.TextField(blank=True)
    MBO22F1 = models.TextField(blank=True)
    MBO22G1 = models.TextField(blank=True)

    MBO22AP = models.IntegerField(default=0)
    MBO22BP = models.IntegerField(default=0)
    MBO22CP = models.IntegerField(default=0)
    MBO22DP = models.IntegerField(default=0)
    MBO22EP = models.IntegerField(default=0)
    MBO22FP = models.IntegerField(default=0)
    MBO22GP = models.IntegerField(default=0)

    MBO22A2 = models.TextField(blank=True)
    MBO22B2 = models.TextField(blank=True)
    MBO22C2 = models.TextField(blank=True)
    MBO22D2 = models.TextField(blank=True)
    MBO22E2 = models.TextField(blank=True)
    MBO22F2 = models.TextField(blank=True)
    MBO22G2 = models.TextField(blank=True)

    MBO22A3 = models.TextField(blank=True)
    MBO22B3 = models.TextField(blank=True)
    MBO22C3 = models.TextField(blank=True)
    MBO22D3 = models.TextField(blank=True)
    MBO22E3 = models.TextField(blank=True)
    MBO22F3 = models.TextField(blank=True)
    MBO22G3 = models.TextField(blank=True)

    MBO22A4 = models.TextField(blank=True)
    MBO22B4 = models.TextField(blank=True)
    MBO22C4 = models.TextField(blank=True)
    MBO22D4 = models.TextField(blank=True)
    MBO22E4 = models.TextField(blank=True)
    MBO22F4 = models.TextField(blank=True)
    MBO22G4 = models.TextField(blank=True)

    MBO22AR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    MBO22BR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    MBO22CR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    MBO22DR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    MBO22ER = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    MBO22FR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    MBO22GR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

#    MBO22Q1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
#    MBO22Q2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
#    MBO22Q3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
#    MBO22Q4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)

    MBO22Q1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    MBO22Q2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    MBO22Q3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    MBO22Q4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)

    MBO22Q1A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    MBO22Q2A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    MBO22Q3A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    MBO22Q4A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)

    MBO22Q1Y = models.IntegerField(default=0)
    MBO22Q2Y = models.IntegerField(default=0)
    MBO22Q3Y = models.IntegerField(default=0)
    MBO22Q4Y = models.IntegerField(default=0)

    MBO22Q1M = models.IntegerField(default=0)
    MBO22Q2M = models.IntegerField(default=0)
    MBO22Q3M = models.IntegerField(default=0)
    MBO22Q4M = models.IntegerField(default=0)

    MBO22Q1D = models.IntegerField(default=0)
    MBO22Q2D = models.IntegerField(default=0)
    MBO22Q3D = models.IntegerField(default=0)
    MBO22Q4D = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

point_choices = (
    (1,'1'),(1.5,'1.5'),(2,'2'),(2.5,'2.5'),(3,'3'),(3.5,'3.5'),(4,'4'),(4.5,'4.5'),(5,'5')
)


class ADC22(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ADC22E1 = models.CharField(blank=True, max_length=50)
    ADC22E2 = models.CharField(blank=True, max_length=50)

    ADC22G1C = models.FloatField(choices=point_choices, default=1)
    ADC22G2C = models.FloatField(choices=point_choices, default=1)
    ADC22G3C = models.FloatField(choices=point_choices, default=1)
    ADC22G4C = models.FloatField(choices=point_choices, default=1)
    ADC22G5C = models.FloatField(choices=point_choices, default=1)
    ADC22G6C = models.FloatField(choices=point_choices, default=1)
    ADC22G7C = models.FloatField(choices=point_choices, default=1)

    ADC22G1A = models.FloatField(choices=point_choices, default=1)
    ADC22G2A = models.FloatField(choices=point_choices, default=1)
    ADC22G3A = models.FloatField(choices=point_choices, default=1)
    ADC22G4A = models.FloatField(choices=point_choices, default=1)
    ADC22G5A = models.FloatField(choices=point_choices, default=1)
    ADC22G6A = models.FloatField(choices=point_choices, default=1)
    ADC22G7A = models.FloatField(choices=point_choices, default=1)

    ADC22G1O = models.TextField(blank=True)
    ADC22G2O = models.TextField(blank=True)
    ADC22G3O = models.TextField(blank=True)
    ADC22G4O = models.TextField(blank=True)
    ADC22G5O = models.TextField(blank=True)
    ADC22G6O = models.TextField(blank=True)
    ADC22G7O = models.TextField(blank=True)

    ADC22E1C = models.FloatField(choices=point_choices, default=1)
    ADC22E2C = models.FloatField(choices=point_choices, default=1)
    ADC22E1A = models.FloatField(choices=point_choices, default=1)
    ADC22E2A = models.FloatField(choices=point_choices, default=1)
    ADC22E1O = models.TextField(blank=True)
    ADC22E2O = models.TextField(blank=True)

    ADC22C = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    ADC22A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    ADC22Y = models.IntegerField(default=0)
    ADC22M = models.IntegerField(default=0)
    ADC22D = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

       
CG_choices = (
    ('Foco em Resultados','Foco em Resultados'),('Foco no Cliente','Foco no Cliente'),('Busca por Excelência','Busca por Excelência'),('Liderança','Liderança'),('Senso de Urgência','Senso de Urgência'),('Comunicação','Comunicação'),('Relacionamento','Relacionamento')
    )


class PDI22(models.Model):


    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

#    class textchoise = itemchoice(models.TextChoices):
#        foco em resultados='foco em resultados'
#        foco no cliente='foco no cliente'
#        busca por excelência='busca por excelência'
#        liderança='liderança'
#        senso de urgência='senso de urgência'
#        comunicação='comunicação'
#        relacionamento='relacionamento'

    PDI22G1C = models.CharField(choices=CG_choices, blank=True, max_length=50)
    PDI22G1PD = models.TextField(blank=True) 
    PDI22G1 = models.TextField(blank=True)
    PDI22G2C = models.CharField(choices=CG_choices, blank=True, max_length=50)
    PDI22G2PD = models.TextField(blank=True) 
    PDI22G2 = models.TextField(blank=True)
    PDI22G3C = models.CharField(choices=CG_choices, blank=True, max_length=50)
    PDI22G3PD = models.TextField(blank=True) 
    PDI22G3 = models.TextField(blank=True)
    PDI22E1C = models.CharField(blank=True, max_length=50)
    PDI22E1PD = models.TextField(blank=True) 
    PDI22E1 = models.TextField(blank=True)
    PDI22E2C = models.CharField(blank=True, max_length=50)
    PDI22E2PD = models.TextField(blank=True) 
    PDI22E2 = models.TextField(blank=True)

    PDI22C = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    PDI22A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    PDI22Y = models.IntegerField(default=0)
    PDI22M = models.IntegerField(default=0)
    PDI22D = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class RHDT(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ADC22G1 = models.CharField(blank=True, max_length=50)
    ADC22G1D = models.TextField(blank=True)
    ADC22G2 = models.CharField(blank=True, max_length=50)
    ADC22G2D = models.TextField(blank=True)
    ADC22G3 = models.CharField(blank=True, max_length=50)
    ADC22G3D = models.TextField(blank=True)
    ADC22G4 = models.CharField(blank=True, max_length=50)
    ADC22G4D = models.TextField(blank=True)
    ADC22G5 = models.CharField(blank=True, max_length=50)
    ADC22G5D = models.TextField(blank=True)
    ADC22G6 = models.CharField(blank=True, max_length=50)
    ADC22G6D = models.TextField(blank=True)
    ADC22G7 = models.CharField(blank=True, max_length=50)
    ADC22G7D = models.TextField(blank=True)

    ADC22E1C = models.CharField(blank=True, max_length=50)
    ADC22E1D = models.TextField(blank=True)
    ADC22E2C = models.CharField(blank=True, max_length=50)
    ADC22E2D = models.TextField(blank=True)
    ADC22E3C = models.CharField(blank=True, max_length=50)
    ADC22E3D = models.TextField(blank=True)
    ADC22E4C = models.CharField(blank=True, max_length=50)
    ADC22E4D = models.TextField(blank=True)
    ADC22E5C = models.CharField(blank=True, max_length=50)
    ADC22E5D = models.TextField(blank=True)
    ADC22E6C = models.CharField(blank=True, max_length=50)
    ADC22E6D = models.TextField(blank=True)
    ADC22E7C = models.CharField(blank=True, max_length=50)
    ADC22E7D = models.TextField(blank=True)
    ADC22E8C = models.CharField(blank=True, max_length=50)
    ADC22E8D = models.TextField(blank=True)
    ADC22E9C = models.CharField(blank=True, max_length=50)
    ADC22E9D = models.TextField(blank=True)
    ADC22E10C = models.CharField(blank=True, max_length=50)
    ADC22E10D = models.TextField(blank=True)
    ADC22E11C = models.CharField(blank=True, max_length=50)
    ADC22E11D = models.TextField(blank=True)
    ADC22E12C = models.CharField(blank=True, max_length=50)
    ADC22E12D = models.TextField(blank=True)

    MBOTIME22 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)], default=1)
    MBOTIME23 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], default=0)
    MBOTIME24 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], default=0)

    ADCTIME23 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    ADCTIME24 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)

    def __str__(self):
        return self.user.username



#    PDI22G1C = models.ForeignKey('ADC22GRH', on_delete=models.SET_NULL, blank=True, null=True, related_name='PDI22G1CC', db_column='PDI22G1C')
#    PDI22G2C = models.ForeignKey('ADC22GRH', on_delete=models.SET_NULL, blank=True, null=True, related_name='PDI22G2CC', db_column='PDI22G2C')
#    PDI22G3C = models.ForeignKey('ADC22GRH', on_delete=models.SET_NULL, blank=True, null=True, related_name='PDI22G3CC', db_column='PDI22G3C')

#    def __str__(self):
#        return self.user.username


#    last_name = models.CharField(max_length=100)
#    first_name = models.CharField(max_length=100)
#    account_image = models.ImageField(upload_to="profile_pics",blank=True)

#class MBO(models.Model):
#    username = models.CharField(max_length=200)#models.ForeignKey(Account, on_delete=models.CASCADE)
#    MBO = models.TextField()

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

