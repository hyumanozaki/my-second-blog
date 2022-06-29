from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import MBO22,ADC22,RHDT,PDI22#, PDI22G
#from .models import MBO
from .forms import PostForm
from .forms import MBO22AForm,MBO22Q1Form,MBO22Q2Form,MBO22Q3Form,MBO22Q4Form,ADC22CForm,ADC22AOForm,PDI22Form#PDI22GForm,PDI22EForm,PDI22GCForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import TemplateView #テンプレートタグ
#from .forms import AccountForm#, AddAccountForm #ユーザーアカウントフォー
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from datetime import datetime
#import numpy as np
#import pandas as pd
#from user.models import User, Order

User = get_user_model()


Y1 = 2022
Q1 = 10
Q2 = 11
Q3 = 12



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
                #return render(request, "blog/home.html",user)
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'blog/login.html')
    
#    numero = Account.objects.all()
#    for item in numero:
#        MBO = AccountForm.objects.userid(item)
#        MBO.save()


def homeA(request):
    result = ''
    result2 = ''
    result3 = ''
    result4 = ''
    result5 = ''
    result6 = ''
    result7 = ''
    result8 = ''
    object_list = User.objects.all()
    for i in object_list:
        result = i.email
        result2 += result
        result2 += ' '
        result3 = i.username
        result4 += result3
        result4 += ' '
        result6 = str(i.id)
        result7 += result6
        result7 += ' '
    result2=result2.split()
    result4=result4.split()
    result7=result7.split()
    k=int(len(result2))
    for j in range(k):
        if (str(result2[j])==str(request.user)):
            result5+=str(result4[j])
            result5+=' '
            result8+=str(result7[j])
            result8+=' '
    result5=result5.split()
    result8=result8.split()
    params = {"C1":result5,"C2":result8,"C3":result4,"UserID":request.user}
#    params = {"C1":object_list}
    return render(request, "blog/homeA.html",params)

def homeB(request):
    result = ''
    result2 = ''
    result3 = ''
    result4 = ''
    result5 = ''
    result6 = ''
    result7 = ''
    result8 = ''
    object_list = User.objects.all()
    for i in object_list:
        result = i.email
        result2 += result
        result2 += ' '
        result3 = i.username
        result4 += result3
        result4 += ' '
        result6 = str(i.id)
        result7 += result6
        result7 += ' '
    result2=result2.split()
    result4=result4.split()
    result7=result7.split()
    k=int(len(result2))
    for j in range(k):
        if (str(result2[j])==str(request.user)):
            result5+=str(result4[j])
            result5+=' '
            result8+=str(result7[j])
            result8+=' '
    result5=result5.split()
    result8=result8.split()
    params = {"C1":result5,"C2":result8,"C3":result4,"UserID":request.user}
#    params = {"C1":object_list}
    return render(request, "blog/homeB.html",params)

def homeC(request):
    result = ''
    result2 = ''
    result3 = ''
    result4 = ''
    result5 = ''
    result6 = ''
    result7 = ''
    result8 = ''
    object_list = User.objects.all()
    for i in object_list:
        result = i.email
        result2 += result
        result2 += ' '
        result3 = i.username
        result4 += result3
        result4 += ' '
        result6 = str(i.id)
        result7 += result6
        result7 += ' '
    result2=result2.split()
    result4=result4.split()
    result7=result7.split()
    k=int(len(result2))
    for j in range(k):
        if (str(result2[j])==str(request.user)):
            result5+=str(result4[j])
            result5+=' '
            result8+=str(result7[j])
            result8+=' '
    result5=result5.split()
    result8=result8.split()
    params = {"C1":result5,"C2":result8,"C3":result4,"UserID":request.user}
#    params = {"C1":object_list}
    return render(request, "blog/homeC.html",params)


@login_required
def PDI2(request, name):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    colaborador = name#request.GET['name']

    result = ''
    result2 = ''
    result3 = ''
    result4 = ''
    result5 = ''
    result6 = 0
    object_list = User.objects.all()
    for i in object_list:
        result = i.username
        result2 += result
        result2 += ' '
        result3 = str(i.id)
        result4 += result3
        result4 += ' '
    result2=result2.split()
    result4=result4.split()
    k=int(len(result2))
    for j in range(k):
        if (str(result2[j])==colaborador):
            result6=int(result4[j])
#    params = {"UserID":request.user,"data1":MBO22.objects.values_list('MBO22A1','MBO22B1','MBO22C1','MBO22D1','MBO22E1','MBO22F1','MBO22G1').get(user=colaborador),"data2":MBO22.objects.values_list('MBO22AP','MBO22BP','MBO22CP','MBO22DP','MBO22EP','MBO22FP','MBO22GP').get(user=colaborador),"data3":MBO22.objects.values_list('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2').get(user=colaborador),"data4":MBO22.objects.values_list('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3').get(user=colaborador),"data5":MBO22.objects.values_list('MBO22A4','MBO22B4','MBO22C4','MBO22D4','MBO22E4','MBO22F4','MBO22G4').get(user=colaborador),"data6":MBO22.objects.values_list('MBO22AR','MBO22BR','MBO22CR','MBO22DR','MBO22ER','MBO22FR','MBO22GR').get(user=colaborador)}

    porta=PDI22.objects.values_list('PDI22C').get(user=result6)
    porta2=PDI22.objects.values_list('PDI22A').get(user=result6) 

    if (int(porta[0])==0):
        time=0
    if (int(porta[0])==1):
        if (int(porta2[0])==0):
            time=1
        else :
            time=2

    today = datetime.now()
    Y = today.year
    M = today.month
    D = today.day

    if (request.method == 'POST'):
        order = request.POST.get('office')
        task = get_object_or_404(PDI22, user=result6)
        if (order == 'aprovar'):
            new_status = 1
            task.PDI22A = new_status
            task.PDI22Y = Y
            task.PDI22M = M
            task.PDI22D = D
            task.save()
            time=2
        if (order == 'pede corrigir'):
            new_status = 0
            task.PDI22C = new_status
            task.save()
            time=0


    Glist=[]
    Glist+=RHDT.objects.values_list('ADC22G1').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G1C').get(user=result6),
    Glist+=ADC22.objects.values_list('ADC22G1A').get(user=result6),
    Glist+=RHDT.objects.values_list('ADC22G2').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G2C').get(user=result6),
    Glist+=ADC22.objects.values_list('ADC22G2A').get(user=result6),
    Glist+=RHDT.objects.values_list('ADC22G3').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G3C').get(user=result6),
    Glist+=ADC22.objects.values_list('ADC22G3A').get(user=result6),
    Glist+=RHDT.objects.values_list('ADC22G4').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G4C').get(user=result6),
    Glist+=ADC22.objects.values_list('ADC22G4A').get(user=result6),
    Glist+=RHDT.objects.values_list('ADC22G5').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G5C').get(user=result6),
    Glist+=ADC22.objects.values_list('ADC22G5A').get(user=result6),
    Glist+=RHDT.objects.values_list('ADC22G6').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G6C').get(user=result6),
    Glist+=ADC22.objects.values_list('ADC22G6A').get(user=result6),
    Glist+=RHDT.objects.values_list('ADC22G7').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G7C').get(user=result6),
    Glist+=ADC22.objects.values_list('ADC22G7A').get(user=result6),

    G1C=[]
    G2C=[]
    G3C=[]
    G1A=[]
    G2A=[]
    G3A=[]

    E1C=[]
    E2C=[]
    E1A=[]
    E2A=[]

    for i in range(7):
        j=i*3
        k=j+1
        l=k+1
        if (PDI22.objects.values_list('PDI22G1C').get(user=request.user)==Glist[j]):
            G1C+=Glist[k]
            G1A+=Glist[l]
        if (PDI22.objects.values_list('PDI22G2C').get(user=request.user)==Glist[j]):
            G2C+=Glist[k]
            G2A+=Glist[l]
        if (PDI22.objects.values_list('PDI22G3C').get(user=request.user)==Glist[j]):
            G3C+=Glist[k]
            G3A+=Glist[l]

    E1C+=ADC22.objects.values_list('ADC22E1C').get(user=request.user)
    E1A+=ADC22.objects.values_list('ADC22E1A').get(user=request.user)
    E2C+=ADC22.objects.values_list('ADC22E2C').get(user=request.user)
    E2A+=ADC22.objects.values_list('ADC22E2A').get(user=request.user)

    if (G1C==[]):
        data11=''
    else :
        data11=G1C[0]
    if (G2C==[]):
        data21=''
    else :
        data21=G2C[0]
    if (G3C==[]):
        data31=''
    else :
        data31=G3C[0]
    if (G1A==[]):
        data12=''
    else :
        data12=G1A[0]
    if (G2A==[]):
        data22=''
    else :
        data22=G2A[0]
    if (G3A==[]):
        data32=''
    else :
        data32=G3A[0]


    params = {"UserID":request.user,
        "avaliado":colaborador,
        "data1":PDI22.objects.values_list('PDI22G1C','PDI22G1PD','PDI22G1').get(user=result6),
        "data11":data11,
        "data12":data12,
        "data2":PDI22.objects.values_list('PDI22G2C','PDI22G2PD','PDI22G2').get(user=result6),
        "data21":data21,
        "data22":data22,
        "data3":PDI22.objects.values_list('PDI22G3C','PDI22G3PD','PDI22G3').get(user=result6),
        "data31":data31,
        "data32":data32,
        "data4":PDI22.objects.values_list('PDI22E1C','PDI22E1PD','PDI22E1').get(user=result6),
        "data41":E1C[0],
        "data42":E1A[0],
        "data5":PDI22.objects.values_list('PDI22E2C','PDI22E2PD','PDI22E2').get(user=result6),
        "data51":E2C[0],
        "data52":E2A[0],
        "time":time,
        }
    return render(request, "blog/PDI2.html", context=params)



@login_required
def Logout2(request, name):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])

    MBO22TIME=[]
    MBO22TIME+=RHDT.objects.values_list('MBOTIME22').get(user=resultb6)
    MBO22TIME=int(MBO22TIME[0])

    colaborador = name#request.GET['name']

    result = ''
    result2 = ''
    result3 = ''
    result4 = ''
    result5 = ''
    result6 = 0
    object_list = User.objects.all()
    for i in object_list:
        result = i.username
        result2 += result
        result2 += ' '
        result3 = str(i.id)
        result4 += result3
        result4 += ' '
    result2=result2.split()
    result4=result4.split()
    k=int(len(result2))
    for j in range(k):
        if (str(result2[j])==colaborador):
            result6=int(result4[j])
#    params = {"UserID":request.user,"data1":MBO22.objects.values_list('MBO22A1','MBO22B1','MBO22C1','MBO22D1','MBO22E1','MBO22F1','MBO22G1').get(user=colaborador),"data2":MBO22.objects.values_list('MBO22AP','MBO22BP','MBO22CP','MBO22DP','MBO22EP','MBO22FP','MBO22GP').get(user=colaborador),"data3":MBO22.objects.values_list('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2').get(user=colaborador),"data4":MBO22.objects.values_list('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3').get(user=colaborador),"data5":MBO22.objects.values_list('MBO22A4','MBO22B4','MBO22C4','MBO22D4','MBO22E4','MBO22F4','MBO22G4').get(user=colaborador),"data6":MBO22.objects.values_list('MBO22AR','MBO22BR','MBO22CR','MBO22DR','MBO22ER','MBO22FR','MBO22GR').get(user=colaborador)}


    today = datetime.now()
    Y = today.year
    M = today.month
    D = today.day

    if (request.method == 'POST'):
        order = request.POST.get('office')
        if (order == 'aprovar'):
            task = get_object_or_404(MBO22, user=result6)
            new_status = 1
            if (Y<=Y1):
                if (M<Q1):
                    task.MBO22Q1A = new_status
                    task.MBO22Q1Y = Y
                    task.MBO22Q1M = M
                    task.MBO22Q1D = D
                    task.save()
                if (Q1<=M<Q2):
                    task.MBO22Q2A = new_status
                    task.MBO22Q2Y = Y
                    task.MBO22Q2M = M
                    task.MBO22Q2D = D
                    task.save()
                if (Q2<=M<Q3):
                    task.MBO22Q3A = new_status
                    task.MBO22Q3Y = Y
                    task.MBO22Q3M = M
                    task.MBO22Q3D = D
                    task.save()
                if (Q3<=M) :
                    task.MBO22Q4A = new_status
                    task.MBO22Q4Y = Y
                    task.MBO22Q4M = M
                    task.MBO22Q4D = D
                    task.save()
        if (order == 'pede corrigir'):
            task = get_object_or_404(MBO22, user=result6)
            new_status = 0
            if (Y<=Y1):
                if (M<Q1):
                    task.MBO22Q1 = new_status
                    task.save()
                if (Q1<=M<Q2):
                    task.MBO22Q2 = new_status
                    task.save()
                if (Q2<=M<Q3):
                    task.MBO22Q3 = new_status
                    task.save()
                if (Q3<=M) :
                    task.MBO22Q4 = new_status
                    task.save()

    
    porta=MBO22.objects.values_list('MBO22Q1').get(user=result6)+MBO22.objects.values_list('MBO22Q2').get(user=result6)+MBO22.objects.values_list('MBO22Q3').get(user=result6)+MBO22.objects.values_list('MBO22Q4').get(user=result6)
    porta2=MBO22.objects.values_list('MBO22Q1A').get(user=result6)+MBO22.objects.values_list('MBO22Q2A').get(user=result6)+MBO22.objects.values_list('MBO22Q3A').get(user=result6)+MBO22.objects.values_list('MBO22Q4A').get(user=result6)
    if (Y<=Y1):
        if (M<Q1):
            if (int(porta[0])==1):
                if (int(porta2[0])==0):
                    time=1
                else:
                    time=10
            else :
                time=0
        if (Q1<=M<Q2):
            if (int(porta[1])==1):
                if (int(porta2[1])==0):
                    time=2
                else:
                    time=10
            else :
                time=0
        if (Q2<=M<Q3):
            if (int(porta[2])==1):
                if (int(porta2[2])==0):
                    time=3
                else:
                    time=10
            else :
                time=0
        if (Q3<=M) :
            if (int(porta[3])==1):
                if (int(porta2[3])==0):
                    time=4
                else:
                    time=10
            else :
                time=0

    obj = MBO22.objects.get(user=result6)
    params = {
        "UserID":request.user,
        "avaliado":colaborador,
        "data1":MBO22.objects.values_list('MBO22A1','MBO22B1','MBO22C1','MBO22D1','MBO22E1','MBO22F1','MBO22G1').get(user=result6),
        "data2":MBO22.objects.values_list('MBO22AP','MBO22BP','MBO22CP','MBO22DP','MBO22EP','MBO22FP','MBO22GP').get(user=result6),
        "data3":MBO22.objects.values_list('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2').get(user=result6),
        "data4":MBO22.objects.values_list('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3').get(user=result6),
        "data5":MBO22.objects.values_list('MBO22A4','MBO22B4','MBO22C4','MBO22D4','MBO22E4','MBO22F4','MBO22G4').get(user=result6),
        "data6":MBO22.objects.values_list('MBO22AR','MBO22BR','MBO22CR','MBO22DR','MBO22ER','MBO22FR','MBO22GR').get(user=result6),
        "form":MBO22AForm,
        "time":time,
        }      
    return render(request, "blog/Logout2.html", context=params)



#ログアウト
@login_required
def Logout(request):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    MBO22TIME=[]
    MBO22TIME+=RHDT.objects.values_list('MBOTIME22').get(user=resultb6)
    MBO22TIME=int(MBO22TIME[0])

    today = datetime.now()
    Y = today.year
    M = today.month
    porta=[]
    porta+=MBO22.objects.values_list('MBO22Q1').get(user=request.user)
    porta+=MBO22.objects.values_list('MBO22Q2').get(user=request.user)
    porta+=MBO22.objects.values_list('MBO22Q3').get(user=request.user)
    porta+=MBO22.objects.values_list('MBO22Q4').get(user=request.user)
#    porta+=int(MBO22.objects.values_list('MBO22Q1').get(user=request.user))
#    porta+=int(MBO22.objects.values_list('MBO22Q2').get(user=request.user))
#    porta+=int(MBO22.objects.values_list('MBO22Q3').get(user=request.user))
#    porta+=int(MBO22.objects.values_list('MBO22Q4').get(user=request.user))
    if (Y<=Y1):
        if (M<Q1):
            if (int(porta[0])==0):
                time=1
            else :
                time=0
        if (Q1<=M<Q2):
            if (int(porta[1])==0):
                time=2
            else :
                time=0
        if (Q2<=M<Q3):
            if (int(porta[2])==0):
                time=3
            else :
                time=0
        if (Q3<=M):
            if (int(porta[3])==0):
                time=4
            else :
                time=0

    if (request.method == 'POST'):
        if (Y<=Y1):
            if (M<Q1):
                ptotal = MBO22.objects.values_list('MBO22AP').get(user=request.user)+MBO22.objects.values_list('MBO22BP').get(user=request.user)+MBO22.objects.values_list('MBO22CP').get(user=request.user)+MBO22.objects.values_list('MBO22DP').get(user=request.user)+MBO22.objects.values_list('MBO22EP').get(user=request.user)+MBO22.objects.values_list('MBO22FP').get(user=request.user)+MBO22.objects.values_list('MBO22GP').get(user=request.user)
                PT = int(ptotal[0])+int(ptotal[1])+int(ptotal[2])+int(ptotal[3])+int(ptotal[4])+int(ptotal[5])+int(ptotal[6])
                if (PT==100):
                    task = get_object_or_404(MBO22, user=request.user)
                    new_status = 1
                    task.MBO22Q1 = new_status
                    task.save()
                else :
                    time = 5
                    params = {"UserID":request.user,"data1":MBO22.objects.values_list('MBO22A1','MBO22B1','MBO22C1','MBO22D1','MBO22E1','MBO22F1','MBO22G1').get(user=request.user),"data2":MBO22.objects.values_list('MBO22AP','MBO22BP','MBO22CP','MBO22DP','MBO22EP','MBO22FP','MBO22GP').get(user=request.user),"data3":MBO22.objects.values_list('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2').get(user=request.user),"data4":MBO22.objects.values_list('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3').get(user=request.user),"data5":MBO22.objects.values_list('MBO22A4','MBO22B4','MBO22C4','MBO22D4','MBO22E4','MBO22F4','MBO22G4').get(user=request.user),"data6":MBO22.objects.values_list('MBO22AR','MBO22BR','MBO22CR','MBO22DR','MBO22ER','MBO22FR','MBO22GR').get(user=request.user),"data7":request.user.email,"time":time,"ptotal":ptotal}
                    return render(request, "blog/Logout.html", context=params)
            if (Q1<=M<Q2):
#                MBO22.objects.values_list('MBO22Q2').get(user=request.user) = 1
#                MBO22.objects.values_list('MBO22Q2').get(user=request.user).save()
                task = get_object_or_404(MBO22, user=request.user)
                new_status = 1
                task.MBO22Q2 = new_status
                task.save()
            if (Q2<=M<Q3):
                task = get_object_or_404(MBO22, user=request.user)
                new_status = 1
                task.MBO22Q3 = new_status
                task.save()
            else:
                task = get_object_or_404(MBO22, user=request.user)
                new_status = 1
                task.MBO22Q4 = new_status
                task.save()
        if (time!=5):
            time=0
            params = {"UserID":request.user,"data1":MBO22.objects.values_list('MBO22A1','MBO22B1','MBO22C1','MBO22D1','MBO22E1','MBO22F1','MBO22G1').get(user=request.user),"data2":MBO22.objects.values_list('MBO22AP','MBO22BP','MBO22CP','MBO22DP','MBO22EP','MBO22FP','MBO22GP').get(user=request.user),"data3":MBO22.objects.values_list('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2').get(user=request.user),"data4":MBO22.objects.values_list('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3').get(user=request.user),"data5":MBO22.objects.values_list('MBO22A4','MBO22B4','MBO22C4','MBO22D4','MBO22E4','MBO22F4','MBO22G4').get(user=request.user),"data6":MBO22.objects.values_list('MBO22AR','MBO22BR','MBO22CR','MBO22DR','MBO22ER','MBO22FR','MBO22GR').get(user=request.user),"data7":request.user.email,"time":time}
            return render(request, "blog/Logout.html", context=params)
    
    params = {"UserID":request.user,"data1":MBO22.objects.values_list('MBO22A1','MBO22B1','MBO22C1','MBO22D1','MBO22E1','MBO22F1','MBO22G1').get(user=request.user),"data2":MBO22.objects.values_list('MBO22AP','MBO22BP','MBO22CP','MBO22DP','MBO22EP','MBO22FP','MBO22GP').get(user=request.user),"data3":MBO22.objects.values_list('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2').get(user=request.user),"data4":MBO22.objects.values_list('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3').get(user=request.user),"data5":MBO22.objects.values_list('MBO22A4','MBO22B4','MBO22C4','MBO22D4','MBO22E4','MBO22F4','MBO22G4').get(user=request.user),"data6":MBO22.objects.values_list('MBO22AR','MBO22BR','MBO22CR','MBO22DR','MBO22ER','MBO22FR','MBO22GR').get(user=request.user),"data7":request.user.email,"time":time,"time2":porta}
    return render(request, "blog/Logout.html",context=params)

def E1D2(request, name):

    colaborador = name
    
    result = ''
    result2 = ''
    result3 = ''
    result4 = ''
    result5 = ''
    result6 = 0
    object_list = User.objects.all()
    for i in object_list:
        result = i.username
        result2 += result
        result2 += ' '
        result3 = str(i.id)
        result4 += result3
        result4 += ' '
    result2=result2.split()
    result4=result4.split()
    k=int(len(result2))
    for j in range(k):
        if (str(result2[j])==colaborador):
            result6=int(result4[j])


    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    Elist=[]  
    Elist+=RHDT.objects.values_list('ADC22E1C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E1D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E2C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E2D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12D').get(user=resultb6)


    CE1=[]
    CE1+=ADC22.objects.values_list('ADC22E1').get(user=result6)
    CE2=''

    for i in range(11):
        j=i*2
        k=j+1
        if Elist[j]==CE1[0]:
            CE2=Elist[k]

    params = {
        'form1': CE2,
        'avaliado':colaborador,
            }
    return render(request, 'blog/E1D2.html', params)

def E2D2(request, name):

    colaborador = name
    
    result = ''
    result2 = ''
    result3 = ''
    result4 = ''
    result5 = ''
    result6 = 0
    object_list = User.objects.all()
    for i in object_list:
        result = i.username
        result2 += result
        result2 += ' '
        result3 = str(i.id)
        result4 += result3
        result4 += ' '
    result2=result2.split()
    result4=result4.split()
    k=int(len(result2))
    for j in range(k):
        if (str(result2[j])==colaborador):
            result6=int(result4[j])

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    CE1=[]
    CE1+=ADC22.objects.values_list('ADC22E2').get(user=result6)
    CE2=''

    Elist=[]  
    Elist+=RHDT.objects.values_list('ADC22E1C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E1D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E2C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E2D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12D').get(user=resultb6)


    for i in range(11):
        j=i*2
        k=j+1
        if Elist[j]==CE1[0]:
            CE2=Elist[k]

    params = {
        'form1': CE2,
        'avaliado':colaborador,
            }
    return render(request, 'blog/E2D2.html', params)


def E1D(request, num):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    Elist=[]  
    Elist+=RHDT.objects.values_list('ADC22E1C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E1D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E2C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E2D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12D').get(user=resultb6)
    
    CE1=request.user.first_name
    CE2=''

    for i in range(11):
        j=i*2
        k=j+1
        if str(Elist[j])==CE1:
            CE2=str(Elist[k])

    params = {
        'form1': CE2
            }
    return render(request, 'blog/E1D.html', params)

def E2D(request, num):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    Elist=[]  
    Elist+=RHDT.objects.values_list('ADC22E1C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E1D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E2C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E2D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12D').get(user=resultb6)

    
    CE1=request.user.last_name
    CE2=''


    for i in range(11):
        j=i*2
        k=j+1
        if str(Elist[j])==CE1:
            CE2=str(Elist[k])

    params = {
        'form1': CE2
            }
    return render(request, 'blog/E2D.html', params)


@login_required
def ADC(request):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    porta=[]
    porta+=ADC22.objects.values_list('ADC22C').get(user=request.user)

    time = int(porta[0])
    if (request.method == 'POST'):
        task = get_object_or_404(ADC22, user=request.user)
        new_status = 1
        task.ADC22C = new_status
        task.save()
        time=1

    CE1=request.user.first_name
    CE2=request.user.last_name

    task2 = get_object_or_404(ADC22, user=request.user)
    task2.ADC22E1 = CE1
    task2.ADC22E2 = CE2
    task2.save()

    Elist=[]  
    Elist+=RHDT.objects.values_list('ADC22E1C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E1D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E2C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E2D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12D').get(user=resultb6)


    CE3=''
    CE4=''

    for i in range(12):
        j=i*2
        k=j+1
        if str(Elist[j])==CE1:
            CE3=str(Elist[k])
        if str(Elist[j])==CE2:
            CE4=str(Elist[k])

    params = {"UserID":request.user,
        "data1":RHDT.objects.values_list('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7').get(user=resultb6),
        "data2":RHDT.objects.values_list('ADC22G1D','ADC22G2D','ADC22G3D','ADC22G4D','ADC22G5D','ADC22G6D','ADC22G7D').get(user=resultb6),
        "data3":ADC22.objects.values_list('ADC22G1C','ADC22G2C','ADC22G3C','ADC22G4C','ADC22G5C','ADC22G6C','ADC22G7C').get(user=request.user),
        "data4":ADC22.objects.values_list('ADC22G1A','ADC22G2A','ADC22G3A','ADC22G4A','ADC22G5A','ADC22G6A','ADC22G7A').get(user=request.user),
        "data5":ADC22.objects.values_list('ADC22G1O','ADC22G2O','ADC22G3O','ADC22G4O','ADC22G5O','ADC22G6O','ADC22G7O').get(user=request.user),
        "data6":request.user.first_name,
        "data7":request.user.last_name,
        "data81":CE3,
        "data82":CE4,
        "data9":ADC22.objects.values_list('ADC22E1C','ADC22E2C').get(user=request.user),
        "data10":ADC22.objects.values_list('ADC22E1A','ADC22E2A').get(user=request.user),
        "data11":ADC22.objects.values_list('ADC22E1O','ADC22E2O').get(user=request.user),
        "time":time
        }
    return render(request, "blog/ADC.html",context=params)

        
def ADC2(request,name):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    colaborador = name#request.GET['name']

    result = ''
    result2 = ''
    result3 = ''
    result4 = ''
    result5 = ''
    result6 = 0
    object_list = User.objects.all()
    for i in object_list:
        result = i.username
        result2 += result
        result2 += ' '
        result3 = str(i.id)
        result4 += result3
        result4 += ' '
    result2=result2.split()
    result4=result4.split()
    k=int(len(result2))
    for j in range(k):
        if (str(result2[j])==colaborador):
            result6=int(result4[j])

    porta=[]
    porta+=ADC22.objects.values_list('ADC22C').get(user=result6)
    porta+=ADC22.objects.values_list('ADC22A').get(user=result6)

    if (int(porta[0])==0):
        time=0
    else :
        if (int(porta[1])==0):
            time=1
        else :
            time=2


    today = datetime.now()
    Y = today.year
    M = today.month
    D = today.day

    if (request.method == 'POST'):
        task = get_object_or_404(ADC22, user=result6)
        new_status = 1
        task.ADC22A = new_status
        task.ADC22Y = Y
        task.ADC22M = M
        task.ADC22D = D
        task.save()
        time=2
            

    params = {"UserID":request.user,
        "data1":RHDT.objects.values_list('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7').get(user=resultb6),
        "data2":ADC22.objects.values_list('ADC22G1C','ADC22G2C','ADC22G3C','ADC22G4C','ADC22G5C','ADC22G6C','ADC22G7C').get(user=result6),
        "data3":ADC22.objects.values_list('ADC22G1A','ADC22G2A','ADC22G3A','ADC22G4A','ADC22G5A','ADC22G6A','ADC22G7A').get(user=result6),
        "data4":ADC22.objects.values_list('ADC22G1O','ADC22G2O','ADC22G3O','ADC22G4O','ADC22G5O','ADC22G6O','ADC22G7O').get(user=result6),
        "data5":ADC22.objects.values_list('ADC22E1','ADC22E2').get(user=result6),
        "data6":ADC22.objects.values_list('ADC22E1C','ADC22E2C').get(user=result6),
        "data7":ADC22.objects.values_list('ADC22E1A','ADC22E2A').get(user=result6),
        "data8":ADC22.objects.values_list('ADC22E1O','ADC22E2O').get(user=result6),
        "time":time,
        "avaliado":colaborador,
        }
    return render(request, "blog/ADC2.html",context=params)


@login_required
def PDI(request):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    porta=[]
    porta+=PDI22.objects.values_list('PDI22C').get(user=request.user)
    time=int(porta[0])

    Glist=[]
    Glist+=RHDT.objects.values_list('ADC22G1').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G1C').get(user=request.user),
    Glist+=ADC22.objects.values_list('ADC22G1A').get(user=request.user),
    Glist+=RHDT.objects.values_list('ADC22G2').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G2C').get(user=request.user),
    Glist+=ADC22.objects.values_list('ADC22G2A').get(user=request.user),
    Glist+=RHDT.objects.values_list('ADC22G3').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G3C').get(user=request.user),
    Glist+=ADC22.objects.values_list('ADC22G3A').get(user=request.user),
    Glist+=RHDT.objects.values_list('ADC22G4').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G4C').get(user=request.user),
    Glist+=ADC22.objects.values_list('ADC22G4A').get(user=request.user),
    Glist+=RHDT.objects.values_list('ADC22G5').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G5C').get(user=request.user),
    Glist+=ADC22.objects.values_list('ADC22G5A').get(user=request.user),
    Glist+=RHDT.objects.values_list('ADC22G6').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G6C').get(user=request.user),
    Glist+=ADC22.objects.values_list('ADC22G6A').get(user=request.user),
    Glist+=RHDT.objects.values_list('ADC22G7').get(user=resultb6),
    Glist+=ADC22.objects.values_list('ADC22G7C').get(user=request.user),
    Glist+=ADC22.objects.values_list('ADC22G7A').get(user=request.user),

    TC=ADC22.objects.values_list('ADC22G2C').get(user=request.user),
    TA=ADC22.objects.values_list('ADC22G2A').get(user=request.user),


    G1C=[]
    G2C=[]
    G3C=[]
    G1A=[]
    G2A=[]
    G3A=[]

    E1C=[]
    E2C=[]
    E1A=[]
    E2A=[]

    for i in range(7):
        j=i*3
        k=j+1
        l=k+1
        if (PDI22.objects.values_list('PDI22G1C').get(user=request.user)==Glist[j]):
            G1C+=Glist[k]
            G1A+=Glist[l]
        if (PDI22.objects.values_list('PDI22G2C').get(user=request.user)==Glist[j]):
            G2C+=Glist[k]
            G2A+=Glist[l]
        if (PDI22.objects.values_list('PDI22G3C').get(user=request.user)==Glist[j]):
            G3C+=Glist[k]
            G3A+=Glist[l]

    E1C+=ADC22.objects.values_list('ADC22E1C').get(user=request.user)
    E1A+=ADC22.objects.values_list('ADC22E1A').get(user=request.user)
    E2C+=ADC22.objects.values_list('ADC22E2C').get(user=request.user)
    E2A+=ADC22.objects.values_list('ADC22E2A').get(user=request.user)

    CE1=request.user.first_name
    CE2=request.user.last_name

    task2 = get_object_or_404(PDI22, user=request.user)
    task2.PDI22E1C = CE1
    task2.PDI22E2C = CE2
    task2.save()

    if (G1C==[]):
        data11=''
    else :
        data11=G1C[0]
    if (G2C==[]):
        data21=''
    else :
        data21=G2C[0]
    if (G3C==[]):
        data31=''
    else :
        data31=G3C[0]
    if (G1A==[]):
        data12=''
    else :
        data12=G1A[0]
    if (G2A==[]):
        data22=''
    else :
        data22=G2A[0]
    if (G3A==[]):
        data32=''
    else :
        data32=G3A[0]

    if (request.method == 'POST'):
        task = get_object_or_404(PDI22, user=request.user)
        new_status = 1
        task.PDI22C = new_status
        task.save()
        time=1

    params = {"UserID":request.user,
        "data1":PDI22.objects.values_list('PDI22G1C','PDI22G1PD','PDI22G1').get(user=request.user),
        "data11":data11,
        "data12":data12,
        "data2":PDI22.objects.values_list('PDI22G2C','PDI22G2PD','PDI22G2').get(user=request.user),
        "data21":data21,
        "data22":data22,
        "data3":PDI22.objects.values_list('PDI22G3C','PDI22G3PD','PDI22G3').get(user=request.user),
        "data31":data31,
        "data32":data32,
        "data4":PDI22.objects.values_list('PDI22E1C','PDI22E1PD','PDI22E1').get(user=request.user),
        "data41":E1C[0],
        "data42":E1A[0],
        "data5":PDI22.objects.values_list('PDI22E2C','PDI22E2PD','PDI22E2').get(user=request.user),
        "data51":E2C[0],
        "data52":E2A[0],
        "time":time,
        "TC":TC,
        "TA":TA,
        }
    return render(request, "blog/PDI.html",context=params)

def edit(request, num):
    obj = MBO22.objects.get(user=request.user)
    if (request.method == 'POST'):
        friend = MBO22Q1Form(request.POST, instance=obj)
        friend.save()
        subject = "você mexeu seu MBO"
        message = "você mexeu seu MBO"
        from_email = 'hyuma2331@gmail.com'  # 送信
        recipient_list = [obj]  # 宛先リスト
        #send_mail(subject, message, from_email, recipient_list)
        return redirect(to='/Logout')

    params = {
            'UserID': request.user,
            'data1': MBO22Q1Form(instance=obj),
            'data2': MBO22.objects.values_list('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2').get(user=request.user),
            'data3': MBO22.objects.values_list('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3').get(user=request.user),
            'data4': MBO22.objects.values_list('MBO22A4','MBO22B4','MBO22C4','MBO22D4','MBO22E4','MBO22F4','MBO22G4','MBO22AR','MBO22BR','MBO22CR','MBO22DR','MBO22ER','MBO22FR','MBO22GR').get(user=request.user),
        }
    return render(request, 'blog/edit.html', params)

def edit2(request, num):
    obj = MBO22.objects.get(user=request.user)
    if (request.method == 'POST'):
        friend = MBO22Q2Form(request.POST, instance=obj)
        friend.save()
        subject = "você mexeu seu MBO"
        message = "você mexeu seu MBO"
        from_email = 'hyuma2331@gmail.com'  # 送信
        recipient_list = [obj]  # 宛先リスト
        #send_mail(subject, message, from_email, recipient_list)
        return redirect(to='/Logout')

    params = {
            'UserID': request.user,
            'title': 'alinha progresso com avaliador. depois de mexer, clique "salvar" em baixo senão vai perder recorde de mexer',
            'data1': MBO22.objects.values_list('MBO22A1','MBO22B1','MBO22C1','MBO22D1','MBO22E1','MBO22F1','MBO22G1').get(user=request.user),
            'data2': MBO22.objects.values_list('MBO22AP','MBO22BP','MBO22CP','MBO22DP','MBO22EP','MBO22FP','MBO22GP').get(user=request.user),
            'data3': MBO22Q2Form(instance=obj),
            'data4': MBO22.objects.values_list('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3').get(user=request.user),
            'data5': MBO22.objects.values_list('MBO22A4','MBO22B4','MBO22C4','MBO22D4','MBO22E4','MBO22F4','MBO22G4','MBO22AR','MBO22BR','MBO22CR','MBO22DR','MBO22ER','MBO22FR','MBO22GR').get(user=request.user),
        }
    return render(request, 'blog/edit2.html', params)

def edit3(request, num):
    obj = MBO22.objects.get(user=request.user)
    if (request.method == 'POST'):
        friend = MBO22Q3Form(request.POST, instance=obj)
        friend.save()
        subject = "você mexeu seu MBO"
        message = "você mexeu seu MBO"
        from_email = 'hyuma2331@gmail.com'  # 送信
        recipient_list = [obj]  # 宛先リスト
        #send_mail(subject, message, from_email, recipient_list)
        return redirect(to='/Logout')

    params = {
            'UserID': request.user,
            'title': 'alinha progresso com avaliador. depois de mexer, clique "salvar" em baixo senão vai perder recorde de mexer',
            'data1': MBO22.objects.values_list('MBO22A1','MBO22B1','MBO22C1','MBO22D1','MBO22E1','MBO22F1','MBO22G1').get(user=request.user),
            'data2': MBO22.objects.values_list('MBO22AP','MBO22BP','MBO22CP','MBO22DP','MBO22EP','MBO22FP','MBO22GP').get(user=request.user),
            'data3': MBO22.objects.values_list('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2').get(user=request.user),
            'data4': MBO22Q3Form(instance=obj),
            'data5': MBO22.objects.values_list('MBO22A4','MBO22B4','MBO22C4','MBO22D4','MBO22E4','MBO22F4','MBO22G4','MBO22AR','MBO22BR','MBO22CR','MBO22DR','MBO22ER','MBO22FR','MBO22GR').get(user=request.user),
        }
    return render(request, 'blog/edit3.html', params)

def edit4(request, num):
    obj = MBO22.objects.get(user=request.user)
    if (request.method == 'POST'):
        friend = MBO22Q4Form(request.POST, instance=obj)
        friend.save()
        subject = "você mexeu seu MBO"
        message = "você mexeu seu MBO"
        from_email = 'hyuma2331@gmail.com'  # 送信
        recipient_list = [obj]  # 宛先リスト
        #send_mail(subject, message, from_email, recipient_list)
        return redirect(to='/Logout')

    params = {
            'UserID': request.user,
            'title': 'alinha progresso com avaliador. depois de mexer, clique "salvar" em baixo senão vai perder recorde de mexer',
            'data1': MBO22.objects.values_list('MBO22A1','MBO22B1','MBO22C1','MBO22D1','MBO22E1','MBO22F1','MBO22G1').get(user=request.user),
            'data2': MBO22.objects.values_list('MBO22AP','MBO22BP','MBO22CP','MBO22DP','MBO22EP','MBO22FP','MBO22GP').get(user=request.user),
            'data3': MBO22.objects.values_list('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2').get(user=request.user),
            'data4': MBO22.objects.values_list('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3').get(user=request.user),
            'data5': MBO22Q4Form(instance=obj),
        }
    return render(request, 'blog/edit4.html', params)

def G1D2(request, name):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])

    colaborador2=name
    params = {
        'form1': RHDT.objects.values_list('ADC22G1D').get(user=resultb6),
        'avaliado' : colaborador2,
            }
    return render(request, 'blog/G1D2.html', params)

def G2D2(request, name):
    colaborador2=name

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G2D').get(user=resultb6),
        'avaliado' : colaborador2,
            }
    return render(request, 'blog/G2D2.html', params)

def G3D2(request, name):
    colaborador2=name

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G3D').get(user=resultb6),
        'avaliado' : colaborador2,
            }
    return render(request, 'blog/G3D2.html', params)

def G4D2(request, name):
    colaborador2=name

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G4D').get(user=resultb6),
        'avaliado' : colaborador2,
            }
    return render(request, 'blog/G4D2.html', params)

def G5D2(request, name):
    colaborador2=name

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G5D').get(user=resultb6),
        'avaliado' : colaborador2,
            }
    return render(request, 'blog/G5D2.html', params)

def G6D2(request, name):
    colaborador2=name

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G6D').get(user=resultb6),
        'avaliado' : colaborador2,
            }
    return render(request, 'blog/G6D2.html', params)

def G7D2(request, name):
    colaborador2=name

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G7D').get(user=resultb6),
        'avaliado' : colaborador2,
            }
    return render(request, 'blog/G7D2.html', params)


def G1D(request, num):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G1D').get(user=resultb6)
            }
    return render(request, 'blog/G1D.html', params)

def G2D(request, num):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G2D').get(user=resultb6)
            }
    return render(request, 'blog/G2D.html', params)

def G3D(request, num):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G3D').get(user=resultb6)
            }
    return render(request, 'blog/G3D.html', params)

def G4D(request, num):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G4D').get(user=resultb6)
            }
    return render(request, 'blog/G4D.html', params)

def G5D(request, num):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G5D').get(user=resultb6)
            }
    return render(request, 'blog/G5D.html', params)

def G6D(request, num):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G6D').get(user=resultb6)
            }
    return render(request, 'blog/G6D.html', params)

def G7D(request, num):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    params = {
        'form1': RHDT.objects.values_list('ADC22G7D').get(user=resultb6)
            }
    return render(request, 'blog/G7D.html', params)

def editADC2(request, name):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    colaborador = name
    
    result = ''
    result2 = ''
    result3 = ''
    result4 = ''
    result5 = ''
    result6 = 0
    object_list = User.objects.all()
    for i in object_list:
        result = i.username
        result2 += result
        result2 += ' '
        result3 = str(i.id)
        result4 += result3
        result4 += ' '
    result2=result2.split()
    result4=result4.split()
    k=int(len(result2))
    for j in range(k):
        if (str(result2[j])==colaborador):
            result6=int(result4[j])

    obj = ADC22.objects.get(user=result6)
    if (request.method == 'POST'):
        friend = ADC22AOForm(request.POST, instance=obj)
        friend.save()
        #return render(request, "blog/home.html")    
        subject = "você mexeu seu MBO"
        message = "você mexeu seu MBO"
#        from_email = 'hyuma17@yahoo.co.jp'  # 送信者
        from_email = 'hyuma2331@gmail.com'  # 送信
        recipient_list = [obj]  # 宛先リスト
        #send_mail(subject, message, from_email, recipient_list)

        #return redirect(to='/ADC2')
        time=1
        params = {"UserID":request.user,
            "data1":RHDT.objects.values_list('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7').get(user=resultb6),
            "data2":ADC22.objects.values_list('ADC22G1C','ADC22G2C','ADC22G3C','ADC22G4C','ADC22G5C','ADC22G6C','ADC22G7C').get(user=result6),
            "data3":ADC22.objects.values_list('ADC22G1A','ADC22G2A','ADC22G3A','ADC22G4A','ADC22G5A','ADC22G6A','ADC22G7A').get(user=result6),
            "data4":ADC22.objects.values_list('ADC22G1O','ADC22G2O','ADC22G3O','ADC22G4O','ADC22G5O','ADC22G6O','ADC22G7O').get(user=result6),
            "data5":ADC22.objects.values_list('ADC22E1','ADC22E2').get(user=result6),
            "data6":ADC22.objects.values_list('ADC22E1C','ADC22E2C').get(user=result6),
            "data7":ADC22.objects.values_list('ADC22E1A','ADC22E2A').get(user=result6),
            "data8":ADC22.objects.values_list('ADC22E1O','ADC22E2O').get(user=result6),
            "time":time,
            "avaliado":colaborador,
            }
        return render(request, 'blog/ADC2.html', params)

    params = {
        'UserID':request.user,
        'form1': RHDT.objects.values_list('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7').get(user=resultb6),
        'form11': ADC22.objects.values_list('ADC22E1','ADC22E2').get(user=result6),
        'form2': ADC22.objects.values_list('ADC22G1C','ADC22G2C','ADC22G3C','ADC22G4C','ADC22G5C','ADC22G6C','ADC22G7C','ADC22E1C','ADC22E2C').get(user=result6),
        'form3': ADC22AOForm(instance=obj),
        'avaliado' : colaborador,
    }
    return render(request, 'blog/editADC2.html', params)


def editADC(request, num):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    obj = ADC22.objects.get(user=request.user)
    if (request.method == 'POST'):
        friend = ADC22CForm(request.POST, instance=obj)
        friend.save()
        #return render(request, "blog/home.html")    
        subject = "você mexeu seu MBO"
        message = "você mexeu seu MBO"
#        from_email = 'hyuma17@yahoo.co.jp'  # 送信者
        from_email = 'hyuma2331@gmail.com'  # 送信
        recipient_list = [obj]  # 宛先リスト
        #send_mail(subject, message, from_email, recipient_list)
        return redirect(to='/ADC')

    params = {
        'UserID':request.user,
        'form1': RHDT.objects.values_list('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7').get(user=resultb6),
        'form51': request.user.first_name,
        'form52': request.user.last_name,
        #,'ADC22G1D','ADC22G2D','ADC22G3D','ADC22G4D','ADC22G5D','ADC22G6D','ADC22G7D'),
        'form2': ADC22CForm(instance=obj),
#        'form3': ADC22.objects.values_list('ADC22G1C','ADC22G2C','ADC22G3C','ADC22G4C','ADC22G5C','ADC22G6C','ADC22G7C','ADC22E1C','ADC22E2C').get(user=request.user),
        'form3': ADC22.objects.values_list('ADC22G1A','ADC22G2A','ADC22G3A','ADC22G4A','ADC22G5A','ADC22G6A','ADC22G7A','ADC22E1A','ADC22E2A').get(user=request.user),
        'form4': ADC22.objects.values_list('ADC22G1O','ADC22G2O','ADC22G3O','ADC22G4O','ADC22G5O','ADC22G6O','ADC22G7O','ADC22E1O','ADC22E2O').get(user=request.user),
    }
    return render(request, 'blog/editADC.html', params)

def editPDI(request, num):



    obj = PDI22.objects.get(user=request.user)
    if (request.method == 'POST'):
        friend = PDI22Form(request.POST, instance=obj)
        friend.save()
        subject = "você mexeu seu MBO"
        message = "você mexeu seu MBO"
        from_email = 'hyuma2331@gmail.com'  # 送信
        recipient_list = [obj]  # 宛先リスト
        #send_mail(subject, message, from_email, recipient_list)
        return redirect(to='/PDI')

    params = {
        'UserID':request.user,
        'form1': PDI22Form(instance=obj),
        'form2': request.user.first_name,
        'form3': request.user.last_name,
    }
    return render(request, 'blog/editPDI.html', params)


#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "blog/home.html",context=params)


@login_required
def RH(request):
    params = {"UserID":request.user,}
    return render(request, "blog/RH.html",context=params)

@login_required
def ES(request):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    Elist=[]  
    Elist+=RHDT.objects.values_list('ADC22E1C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E1D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E2C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E2D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11D').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12D').get(user=resultb6)


    ES='0,'
    AA=[]
    object_list = User.objects.all()
#    for k in range(j):
    for i in object_list:
        ES+=i.username
        ES+=','
        ES+=i.email
        ES+=','
        CE3=0
        for m in object_list:
            if i.email==m.username:
                ES+='OK'
                ES+=','
                CE3=1
        if CE3==0:
            ES+='não'
            ES+=','
        ES+=i.first_name
        ES+=','
        CE1=0
        CE2=0
        for j in range(12):
            k=j*2
            if str(Elist[k])!='':
                if str(Elist[k])==i.first_name:
                    ES+='OK'
                    ES+=','
                    CE1=1
        if CE1==0:
            ES+='não'
            ES+=','
        ES+=i.last_name
        ES+=','
        for j in range(12):
            k=j*2
            if str(Elist[k])!='':
                if str(Elist[k])==i.last_name:
                    ES+='OK'
                    ES+=','
                    CE2=1
        if CE2==0:
            ES+='não'
            ES+=','
        try :
            AA+=MBO22.objects.values_list('MBO22Q1Y').get(user=i.id)
            AA+=MBO22.objects.values_list('MBO22Q1M').get(user=i.id)
            AA+=MBO22.objects.values_list('MBO22Q1D').get(user=i.id)
            if ((int(AA[0])>0)):
                ES+=str(AA[2])+ '-'+str(AA[1])+'-'+str(AA[0])
            else:
                ES+='not yet'
        except:
            ES+='não tem MBO'
        ES+=','
        AA=[]
        try:
            AA+=MBO22.objects.values_list('MBO22Q2Y').get(user=i.id)
            AA+=MBO22.objects.values_list('MBO22Q2M').get(user=i.id)
            AA+=MBO22.objects.values_list('MBO22Q2D').get(user=i.id)
            if ((int(AA[0])>0)):
                ES+=str(AA[2])+ '-'+str(AA[1])+'-'+str(AA[0])
            else:
                ES+='not yet'
        except:
            ES+='não tem MBO'
        ES+=','
        AA=[]
        try :
            AA+=MBO22.objects.values_list('MBO22Q3Y').get(user=i.id)
            AA+=MBO22.objects.values_list('MBO22Q3M').get(user=i.id)
            AA+=MBO22.objects.values_list('MBO22Q3D').get(user=i.id)
            if ((int(AA[0])>0)):
                ES+=str(AA[2])+ '-'+str(AA[1])+'-'+str(AA[0])
            else:
                ES+='not yet'
        except:
            ES+='não tem MBO'
        ES+=','
        AA=[]
        try:
            AA+=MBO22.objects.values_list('MBO22Q4Y').get(user=i.id)
            AA+=MBO22.objects.values_list('MBO22Q4M').get(user=i.id)
            AA+=MBO22.objects.values_list('MBO22Q4D').get(user=i.id)
            if ((int(AA[0])>0)):
                ES+=str(AA[2])+ '-'+str(AA[1])+'-'+str(AA[0])
            else:
                ES+='not yet'
        except:
            ES+='não tem MBO'
        ES+=','
        AA=[]
        try:
            AA+=ADC22.objects.values_list('ADC22Y').get(user=i.id)
            AA+=ADC22.objects.values_list('ADC22M').get(user=i.id)
            AA+=ADC22.objects.values_list('ADC22D').get(user=i.id)
            if ((int(AA[0])>0)):
                ES+=str(AA[2])+ '-'+str(AA[1])+'-'+str(AA[0])
            else:
                ES+='not yet'
        except:
            ES+='não tem ADC'
        ES+=','
        AA=[]
        try:
            AA+=PDI22.objects.values_list('PDI22Y').get(user=i.id)
            AA+=PDI22.objects.values_list('PDI22M').get(user=i.id)
            AA+=PDI22.objects.values_list('PDI22D').get(user=i.id)
            if ((int(AA[0])>0)):
                ES+=str(AA[2])+ '-'+str(AA[1])+'-'+str(AA[0])
            else:
                ES+='not yet'
        except:
            ES+='não tem PDI'
        ES+=','
        AA=[]
        ES+='#'
        ES+=','
    ES=ES.split(',')
    del ES[-1]
    #j=int(int(len(ES))/k)
    #ES=np.reshape(ES,(j,k))
    #ES=pd.DataFrame(ES)
    params = {"UserID":request.user,"time":ES}
    return render(request, "blog/ES.html",context=params)


@login_required
def MBO22RH(request):
    
    object_list = User.objects.all()
    AA=''
    BB=[]
    for i in object_list:
        AA+='#'
        AA+=','
        AA+=i.username
        AA+=','
        AA+='#'
        AA+=','
        try:
            BB=MBO22.objects.values_list('MBO22A1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22AP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22A2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22A3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22A4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22AR').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=MBO22.objects.values_list('MBO22B1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22BP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22B2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22B3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22B4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22BR').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=MBO22.objects.values_list('MBO22C1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22CP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22C2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22C3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22C4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22CR').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=MBO22.objects.values_list('MBO22D1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22DP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22D2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22D3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22D4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22DR').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=MBO22.objects.values_list('MBO22E1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22EP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22E2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22E3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22E4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22ER').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=MBO22.objects.values_list('MBO22F1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22FP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22F2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22F3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22F4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22FR').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=MBO22.objects.values_list('MBO22G1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22GP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22G2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22G3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22G4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=MBO22.objects.values_list('MBO22GR').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
        except:
            AA+='não tem MBO'
            AA+=','
    AA=AA.split(',')
    del AA[-1]
    params = {"UserID":request.user,"time":AA}
    return render(request, "blog/MBO22RH.html",context=params)

@login_required
def ADC22RHA(request):

    colaborador2='hyuma.nozaki@cosmotec.com.br'
    resultb = ''
    resultb2 = ''
    resultb3 = ''
    resultb4 = ''
    resultb5 = ''
    resultb6 = 0
    object_list = User.objects.all()
    for l in object_list:
        resultb = l.username
        resultb2 += resultb
        resultb2 += ' '
        resultb3 = str(l.id)
        resultb4 += resultb3
        resultb4 += ' '
    resultb2=resultb2.split()
    resultb4=resultb4.split()
    m=int(len(resultb2))
    for n in range(m):
        if (str(resultb2[n])==colaborador2):
            resultb6=int(resultb4[n])


    object_list = User.objects.all()
    AA=''
    BB=[]
    for i in object_list:
        AA+='#'
        AA+=','
        AA+=i.username
        AA+=','
        AA+='#'
        AA+=','
        try:
            CC=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
            BB=RHDT.objects.values_list('ADC22G1').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G1O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=RHDT.objects.values_list('ADC22G2').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G2O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=RHDT.objects.values_list('ADC22G3').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G3O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=RHDT.objects.values_list('ADC22G4').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G4O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=RHDT.objects.values_list('ADC22G5').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G5O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=RHDT.objects.values_list('ADC22G6').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22G7O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            AA+=i.first_name
            AA+=','
            BB=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22E1O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            AA+=i.last_name
            AA+=','
            BB=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+=','
            BB=ADC22.objects.values_list('ADC22E2O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
        except:
            AA+='não tem avaliação de competencia'
            AA+=','
    AA=AA.split(',')
    del AA[-1]
    params = {"UserID":request.user,"time":AA}
    return render(request, "blog/ADC22RHA.html",context=params)

@login_required
def PDI22RH(request):
    
    object_list = User.objects.all()
    AA=''
    BB=[]
    for i in object_list:
        AA+='#'
        AA+=','
        AA+=i.username
        AA+=','
        AA+='#'
        AA+=','      
        try:
            BB=PDI22.objects.values_list('PDI22G1C').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=PDI22.objects.values_list('PDI22G1PD').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=PDI22.objects.values_list('PDI22G1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=PDI22.objects.values_list('PDI22G2C').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=PDI22.objects.values_list('PDI22G2PD').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=PDI22.objects.values_list('PDI22G2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=PDI22.objects.values_list('PDI22G3C').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=PDI22.objects.values_list('PDI22G3PD').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=PDI22.objects.values_list('PDI22G3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=PDI22.objects.values_list('PDI22E1C').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=PDI22.objects.values_list('PDI22E1PD').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=PDI22.objects.values_list('PDI22E1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
            BB=PDI22.objects.values_list('PDI22E2C').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=PDI22.objects.values_list('PDI22E2PD').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            BB=PDI22.objects.values_list('PDI22E2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+=','
            AA+='#'
            AA+=','
        except:
            AA+='não tem PDI'
            AA+=','
    AA=AA.split(',')
    del AA[-1]
    params = {"UserID":request.user,"time":AA}
    return render(request, "blog/PDI22RH.html",context=params)


def MBO22DL(request):
    
    A1=0
    A2=0
    A3=0
    A4=0
    A5=0
    A6=0
    A7=0
    A8=0
    A9=0
    A10=0
    A11=0
    A12=0
    B1=0
    B2=0
    B3=0
    B4=0
    B5=0
    B6=0
    B7=0
    B8=0
    B9=0
    B10=0
    B11=0
    B12=0
    C1=0
    C2=0
    C3=0
    C4=0
    C5=0
    C6=0
    C7=0
    C8=0
    C9=0
    C10=0
    C11=0
    C12=0
    D1=0
    D2=0
    D3=0
    D4=0
    D5=0
    D6=0
    D7=0
    D8=0
    D9=0
    D10=0
    D11=0
    D12=0
    
    test=0
    BB1=''
    BB2=''
    BB3=''
    BB4=''
    CC=''
    object_list = User.objects.all()
#    for k in range(j):
    for i in object_list:
        test=[]
        try :
            test+=MBO22.objects.values_list('MBO22Q1M').get(user=i.id)
            if (test[0]==0):
                BB1+=i.username
                BB1+=','
            if (test[0]==1):
                A1+=1
            if (test[0]==2):
                A2+=1
            if (test[0]==3):
                A3+=1
            if (test[0]==4):
                A4+=1
            if (test[0]==5):
                A5+=1
            if (test[0]==6):
                A6+=1
            if (test[0]==7):
                A7+=1
            if (test[0]==8):
                A8+=1
            if (test[0]==9):
                A9+=1
            if (test[0]==10):
                A10+=1
            if (test[0]==11):
                A11+=1
            if (test[0]==12):
                A12+=1
            test=[]
            test+=MBO22.objects.values_list('MBO22Q2M').get(user=i.id)
            if (test[0]==0):
                BB2+=i.username
                BB2+=','
            if (test[0]==1):
                B1+=1
            if (test[0]==2):
                B2+=1
            if (test[0]==3):
                B3+=1
            if (test[0]==4):
                B4+=1
            if (test[0]==5):
                B5+=1
            if (test[0]==6):
                B6+=1
            if (test[0]==7):
                B7+=1
            if (test[0]==8):
                B8+=1
            if (test[0]==9):
                B9+=1
            if (test[0]==10):
                B10+=1
            if (test[0]==11):
                B11+=1
            if (test[0]==12):
                B12+=1
            test+=MBO22.objects.values_list('MBO22Q3M').get(user=i.id)
            if (test[0]==0):
                BB3+=i.username
                BB3+=','
            if (test[0]==1):
                C1+=1
            if (test[0]==2):
                C2+=1
            if (test[0]==3):
                C3+=1
            if (test[0]==4):
                C4+=1
            if (test[0]==5):
                C5+=1
            if (test[0]==6):
                C6+=1
            if (test[0]==7):
                C7+=1
            if (test[0]==8):
                C8+=1
            if (test[0]==9):
                C9+=1
            if (test[0]==10):
                C10+=1
            if (test[0]==11):
                C11+=1
            if (test[0]==12):
                C12+=1
            test+=MBO22.objects.values_list('MBO22Q4M').get(user=i.id)
            if (test[0]==0):
                BB4+=i.username
                BB4+=','
            if (test[0]==1):
                D1+=1
            if (test[0]==2):
                D2+=1
            if (test[0]==3):
                D3+=1
            if (test[0]==4):
                D4+=1
            if (test[0]==5):
                D5+=1
            if (test[0]==6):
                D6+=1
            if (test[0]==7):
                D7+=1
            if (test[0]==8):
                D8+=1
            if (test[0]==9):
                D9+=1
            if (test[0]==10):
                D10+=1
            if (test[0]==11):
                D11+=1
            if (test[0]==12):
                D12+=1
        except:
            CC+=i.username
            CC+=','
    BB1=BB1.split(',')
    BB2=BB2.split(',')
    BB3=BB3.split(',')
    BB4=BB4.split(',')
    CC=CC.split(',')
    AT=A1+A2+A3+A4+A5+A6+A7+A8+A9+A10+A11+A12
    BT=B1+B2+B3+B4+B5+B6+B7+B8+B9+B10+B11+B12
    CT=C1+C2+C3+C4+C5+C6+C7+C8+C9+C10+C11+C12
    DT=D1+D2+D3+D4+D5+D6+D7+D8+D9+D10+D11+D12
    params = {
        "UserID":request.user,
        "A1":A1,
        "A2":A2,
        "A3":A3,
        "A4":A4,
        "A5":A5,
        "A6":A6,
        "A7":A7,
        "A8":A8,
        "A9":A9,
        "A10":A10,
        "A11":A11,
        "A12":A12,
        "B1":B1,
        "B2":B2,
        "B3":B3,
        "B4":B4,
        "B5":B5,
        "B6":B6,
        "B7":B7,
        "B8":B8,
        "B9":B9,
        "B10":B10,
        "B11":B11,
        "B12":B12,
        "C1":C1,
        "C2":C2,
        "C3":C3,
        "C4":C4,
        "C5":C5,
        "C6":C6,
        "C7":C7,
        "C8":C8,
        "C9":C9,
        "C10":C10,
        "C11":C11,
        "C12":C12,
        "D1":D1,
        "D2":D2,
        "D3":D3,
        "D4":D4,
        "D5":D5,
        "D6":D6,
        "D7":D7,
        "D8":D8,
        "D9":D9,
        "D10":D10,
        "D11":D11,
        "D12":D12,
        "BB1":BB1,
        "BB2":BB2,
        "BB3":BB3,
        "BB4":BB4,
        "CC":CC,
        "AT":AT,
        "BT":BT,
        "CT":CT,
        "DT":DT,
        }
    return render(request, "blog/MBO22DL.html",context=params)


def ADC22DL(request):
    
    A1=0
    A2=0
    A3=0
    A4=0
    A5=0
    A6=0
    A7=0
    A8=0
    A9=0
    A10=0
    A11=0
    A12=0

    B1=0
    B2=0
    B3=0
    B4=0
    B5=0
    B6=0
    B7=0
    B8=0
    B9=0
    B10=0
    B11=0
    B12=0

    test=0
    BB1=''
    BB2=''
    CC1=''
    CC2=''
    object_list = User.objects.all()
#    for k in range(j):
    for i in object_list:
        test=[]
        try :
            test+=ADC22.objects.values_list('ADC22M').get(user=i.id)
            if (test[0]==0):
                BB1+=i.username
                BB1+=','
            if (test[0]==1):
                A1+=1
            if (test[0]==2):
                A2+=1
            if (test[0]==3):
                A3+=1
            if (test[0]==4):
                A4+=1
            if (test[0]==5):
                A5+=1
            if (test[0]==6):
                A6+=1
            if (test[0]==7):
                A7+=1
            if (test[0]==8):
                A8+=1
            if (test[0]==9):
                A9+=1
            if (test[0]==10):
                A10+=1
            if (test[0]==11):
                A11+=1
            if (test[0]==12):
                A12+=1
        except:
            CC1+=i.username
            CC1+=','
        test=[]
        try :
            test+=PDI22.objects.values_list('PDI22M').get(user=i.id)
            if (test[0]==0):
                BB2+=i.username
                BB2+=','
            if (test[0]==1):
                B1+=1
            if (test[0]==2):
                B2+=1
            if (test[0]==3):
                B3+=1
            if (test[0]==4):
                B4+=1
            if (test[0]==5):
                B5+=1
            if (test[0]==6):
                B6+=1
            if (test[0]==7):
                B7+=1
            if (test[0]==8):
                B8+=1
            if (test[0]==9):
                B9+=1
            if (test[0]==10):
                B10+=1
            if (test[0]==11):
                B11+=1
            if (test[0]==12):
                B12+=1
        except:
            CC2+=i.username
            CC2+=','
    BB1=BB1.split(',')
    CC1=CC1.split(',')
    BB2=BB2.split(',')
    CC2=CC2.split(',')
    AT=A1+A2+A3+A4+A5+A6+A7+A8+A9+A10+A11+A12
    BT=B1+B2+B3+B4+B5+B6+B7+B8+B9+B10+B11+B12
    params = {
        "UserID":request.user,
        "A1":A1,
        "A2":A2,
        "A3":A3,
        "A4":A4,
        "A5":A5,
        "A6":A6,
        "A7":A7,
        "A8":A8,
        "A9":A9,
        "A10":A10,
        "A11":A11,
        "A12":A12,
        "B1":B1,
        "B2":B2,
        "B3":B3,
        "B4":B4,
        "B5":B5,
        "B6":B6,
        "B7":B7,
        "B8":B8,
        "B9":B9,
        "B10":B10,
        "B11":B11,
        "B12":B12,
        "BB1":BB1,
        "BB2":BB2,
        "CC1":CC1,
        "CC2":CC2,
        "AT":AT,
        "BT":BT,
        }
    return render(request, "blog/ADC22DL.html",context=params)
