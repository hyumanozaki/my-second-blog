from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import MBO22,ADC22,RHDT,PDI22#, PDI22G
#from .models import MBO
from .forms import PostForm
from .forms import MBO22Q1Form,MBO22Q2Form,MBO22Q3Form,MBO22Q4Form,ADC22CForm,ADC22AOForm,PDI22Form,DeptForm,uploadForm, readForm
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
from django.views.generic import CreateView
from django.urls import reverse_lazy
import sys
import os
#import numpy as np
#import pandas as pd
#from user.models import User, Order

User = get_user_model()


Y1 = 2022
Q1 = 10
Q2 = 11
Q3 = 12

def upload(request):
    data='nothing'
#    f = open('C:/Users/hyuma.nozaki/djangoboys/psw.txt','r', encoding='UTF-8')
#    f = open('/Users/hyuma.nozaki/djangoboys/psw.txt','r', encoding='UTF-8')
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER,'psw.txt')
    f = open(my_file,'r', encoding='UTF-8')
#    f = open('psw.txt','r', encoding='UTF-8')
    data = f.read()
    data = data.replace('\n',',')
    data = data.split(',')
    BB = len(data)
    CC = int(BB/5)
    if request.method == 'POST':
        for i in range(CC) :
            j=5*i
            k=j+1
            l=j+2
            m=j+3
            n=j+4
            AA = User()
            AA.username = data[j]
            AA.email = data[k]
            AA.first_name = data[l]
            AA.last_name = data[m]
            AA.password = data[n]
            AA.save()
#        class uploadview(CreateView):
#            form_class = uploadForm
#        template_name = "blog/upload.html"
#    success_url = reverse_lazy("blog:RH")
#        def form_valid(self,form):
#            user = form.save()
#            return redirect(to='/RH')
    params = {"form":data,"BB":BB}
    return render(request, 'blog/upload.html', params)

#    if request.method == 'POST':
#        read = readForm(request.POST, request.FILES)
#        sys.stderr.write("*** file_upload *** aaa ***\n")
#        handle(request.FILES['file'])
#        file_obj = request.FILES['file']
#        sys.stderr.write(file_obj.name + "\n")
#    def handle(file_obj):
#        sys.stderr.write("*** handle *** aaa ***\n")
#        sys.stderr.write(file_obj.name + "\n")
#        file_path = 'blog/' + file_obj.name
#        sys.stderr.write(file_path + "\n")
#        with open (file_path, 'b+') as destination:
#            for chunk in file_obj.chunks():
#                sys.stderr.write("*** handle *** ccc ***\n")
#                destination.write(chunk)
#                sys.stderr.wirte("*** handle *** eee ***\n")

    



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
            return HttpResponse("endereço de email ou senha está errado")
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
    result2=result2.split()#email de todos
    result4=result4.split()#name de todos
    result7=result7.split()#id de tods
    k=int(len(result2))
    for j in range(k):
        if (str(result2[j])==str(request.user)):
            result5+=str(result4[j])
            result5+=' '
            result8+=str(result7[j])
            result8+=' '
    result5=result5.split()
    result8=result8.split()
    params = {"C1":result5,"A":result4,"C3":result4,"UserID":request.user}
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
            subject = "seu PDI foi aprovado pelo avaliador/a, parabens!"
            message = "seu PDI foi aprovado pelo avaliador/a, parabens!"
            from_email = 'hyuma2331@gmail.com'  # 送信
            recipient_list = [colaborador]  # 宛先リスト
            send_mail(subject, message, from_email, recipient_list)

        if (order == 'pede corrigir'):
            new_status = 0
            task.PDI22C = new_status
            task.save()
            time=0
            subject = "seu avaliador/a pediu te para corrigir seu PDI"
            message = "seu avaliador/a pediu te para corrigir seu PDI, talvez tenha algo errado e tenha que corrigir, entre o sistema e corrija"
            from_email = 'hyuma2331@gmail.com'  # 送信
            recipient_list = [colaborador]  # 宛先リスト
            send_mail(subject, message, from_email, recipient_list)


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
        if (PDI22.objects.values_list('PDI22G1C').get(user=result6)==Glist[j]):
            G1C+=Glist[k]
            G1A+=Glist[l]
        if (PDI22.objects.values_list('PDI22G2C').get(user=result6)==Glist[j]):
            G2C+=Glist[k]
            G2A+=Glist[l]
        if (PDI22.objects.values_list('PDI22G3C').get(user=result6)==Glist[j]):
            G3C+=Glist[k]
            G3A+=Glist[l]

    E1C+=ADC22.objects.values_list('ADC22E1C').get(user=result6)
    E1A+=ADC22.objects.values_list('ADC22E1A').get(user=result6)
    E2C+=ADC22.objects.values_list('ADC22E2C').get(user=result6)
    E2A+=ADC22.objects.values_list('ADC22E2A').get(user=result6)

    if (G1C==[]):
        data11=''
    else :
        data11=str(G1C[0])
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
            if (MBO22TIME==1):
                task.MBO22Q1A = new_status
                task.MBO22Q1Y = Y
                task.MBO22Q1M = M
                task.MBO22Q1D = D
                task.save()
            if (MBO22TIME==2):
                task.MBO22Q2A = new_status
                task.MBO22Q2Y = Y
                task.MBO22Q2M = M
                task.MBO22Q2D = D
                task.save()
            if (MBO22TIME==3):
                task.MBO22Q3A = new_status
                task.MBO22Q3Y = Y
                task.MBO22Q3M = M
                task.MBO22Q3D = D
                task.save()
            if (MBO22TIME==4):
                task.MBO22Q4A = new_status
                task.MBO22Q4Y = Y
                task.MBO22Q4M = M
                task.MBO22Q4D = D
                task.save()
            subject = "seu MBO foi aprovado pelo avaliador/a, parabens!"
            message = "seu MBO foi aprovado pelo avaliador/a, parabens!"
            from_email = 'hyuma2331@gmail.com'  # 送信
            recipient_list = [colaborador]  # 宛先リスト
            send_mail(subject, message, from_email, recipient_list)
        if (order == 'pede corrigir'):
            task = get_object_or_404(MBO22, user=result6)
            new_status = 0
            if (MBO22TIME==1):
                task.MBO22Q1 = new_status
                task.save()
            if (MBO22TIME==2):
                task.MBO22Q2 = new_status
                task.save()
            if (MBO22TIME==3):
                task.MBO22Q3 = new_status
                task.save()
            if (MBO22TIME==4):
                task.MBO22Q4 = new_status
                task.save()
            subject = "seu avaliador/a pediu te para corrigir seu MBO"
            message = "seu avaliador/a pediu te para corrigir seu MBO, talvez tenha algo errado e tenha que corrigir, entre o sistema e corrija"
            from_email = 'hyuma2331@gmail.com'  # 送信
            recipient_list = [colaborador]  # 宛先リスト
            send_mail(subject, message, from_email, recipient_list)


    porta=MBO22.objects.values_list('MBO22Q1').get(user=result6)+MBO22.objects.values_list('MBO22Q2').get(user=result6)+MBO22.objects.values_list('MBO22Q3').get(user=result6)+MBO22.objects.values_list('MBO22Q4').get(user=result6)
    porta2=MBO22.objects.values_list('MBO22Q1A').get(user=result6)+MBO22.objects.values_list('MBO22Q2A').get(user=result6)+MBO22.objects.values_list('MBO22Q3A').get(user=result6)+MBO22.objects.values_list('MBO22Q4A').get(user=result6)
    if (MBO22TIME==1):
        if (int(porta[0])==1):
            if (int(porta2[0])==0):
                    time=1
            else:
                time=10
        else :
            time=0
    if (MBO22TIME==2):
        if (int(porta[1])==1):
            if (int(porta2[1])==0):
                time=2
            else:
                time=10
        else :
            time=0
    if (MBO22TIME==3):
        if (int(porta[2])==1):
            if (int(porta2[2])==0):
                time=3
            else:
                time=10
        else :
            time=0
    if (MBO22TIME==4):
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

    porta=[]
    porta+=MBO22.objects.values_list('MBO22Q1').get(user=request.user)
    porta+=MBO22.objects.values_list('MBO22Q2').get(user=request.user)
    porta+=MBO22.objects.values_list('MBO22Q3').get(user=request.user)
    porta+=MBO22.objects.values_list('MBO22Q4').get(user=request.user)
    if (MBO22TIME==1):
        if (int(porta[0])==0):
            time=1
        else :
            time=0
    if (MBO22TIME==2):
        if (int(porta[1])==0):
            time=2
        else :
            time=0
    if (MBO22TIME==3):
        if (int(porta[2])==0):
            time=3
        else :
            time=0
    if (MBO22TIME==4):
        if (int(porta[3])==0):
            time=4
        else :
            time=0

    if (request.method == 'POST'):
        if (time==1):
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
        if (time==2):
            task = get_object_or_404(MBO22, user=request.user)
            new_status = 1
            task.MBO22Q2 = new_status
            task.save()
        if (time==3):
            task = get_object_or_404(MBO22, user=request.user)
            new_status = 1
            task.MBO22Q3 = new_status
            task.save()
        if (time==4):
            task = get_object_or_404(MBO22, user=request.user)
            new_status = 1
            task.MBO22Q4 = new_status
            task.save()
        if (time!=5):
            time=0
            params = {"UserID":request.user,"data1":MBO22.objects.values_list('MBO22A1','MBO22B1','MBO22C1','MBO22D1','MBO22E1','MBO22F1','MBO22G1').get(user=request.user),"data2":MBO22.objects.values_list('MBO22AP','MBO22BP','MBO22CP','MBO22DP','MBO22EP','MBO22FP','MBO22GP').get(user=request.user),"data3":MBO22.objects.values_list('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2').get(user=request.user),"data4":MBO22.objects.values_list('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3').get(user=request.user),"data5":MBO22.objects.values_list('MBO22A4','MBO22B4','MBO22C4','MBO22D4','MBO22E4','MBO22F4','MBO22G4').get(user=request.user),"data6":MBO22.objects.values_list('MBO22AR','MBO22BR','MBO22CR','MBO22DR','MBO22ER','MBO22FR','MBO22GR').get(user=request.user),"data7":request.user.email,"time":time}
            subject = request.user.username
            subject += " submeteru MBO, entre o sistema e aprove ou peça corrigir"
            message = request.user.username
            message += " submeteru MBO, entre o sistema e aprove ou peça corrigir"
            from_email = 'hyuma2331@gmail.com'  # 送信
            recipient_list = [request.user.email]  # 宛先リスト
            send_mail(subject, message, from_email, recipient_list)
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
        subject = request.user.username
        subject += " submeteru avaliação de competencia, entre o sistema e aprove ou peça corrigir"
        message = request.user.username
        message += " submeteru avaliação de competencia, entre o sistema e aprove ou peça corrigir"
        from_email = 'hyuma2331@gmail.com'  # 送信
        recipient_list = [request.user.email]  # 宛先リスト
        send_mail(subject, message, from_email, recipient_list)


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
        "data3B":ADC22.objects.values_list('ADC22G1OC','ADC22G2OC','ADC22G3OC','ADC22G4OC','ADC22G5OC','ADC22G6OC','ADC22G7OC','ADC22E1OC','ADC22E2OC').get(user=request.user),
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
        subject = "sua avaliação de competencia foi aprovado, parabens!"
        message = "sua avaliação de competencia foi aprovado, parabens!"
        from_email = 'hyuma2331@gmail.com'  # 送信
        recipient_list = [colaborador]  # 宛先リスト
        send_mail(subject, message, from_email, recipient_list)

            

    params = {"UserID":request.user,
        "data1":RHDT.objects.values_list('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7').get(user=resultb6),
        "data2":ADC22.objects.values_list('ADC22G1C','ADC22G2C','ADC22G3C','ADC22G4C','ADC22G5C','ADC22G6C','ADC22G7C').get(user=result6),
        "data3":ADC22.objects.values_list('ADC22G1A','ADC22G2A','ADC22G3A','ADC22G4A','ADC22G5A','ADC22G6A','ADC22G7A').get(user=result6),
        "data4B":ADC22.objects.values_list('ADC22G1OC','ADC22G2OC','ADC22G3OC','ADC22G4OC','ADC22G5OC','ADC22G6OC','ADC22G7OC','ADC22E1OC','ADC22E2OC').get(user=result6),
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
        subject = request.user.username
        subject += " submeteru plano de desenvolvimento individual, entre o sistema e aprove ou peça corrigir"
        message = request.user.username
        message += " submeteru plano de desenvolvimento individual, entre o sistema e aprove ou peça corrigir"
        from_email = 'hyuma2331@gmail.com'  # 送信
        recipient_list = [request.user.email]  # 宛先リスト
        send_mail(subject, message, from_email, recipient_list)


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

    colaborador=name

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
        'form1': RHDT.objects.values_list('ADC22G1D').get(user=resultb6),
        'avaliado' : colaborador,
            }
    return render(request, 'blog/G1D2.html', params)

def G2D2(request, name):
    colaborador=name

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
        'avaliado' : colaborador,
            }
    return render(request, 'blog/G2D2.html', params)

def G3D2(request, name):
    colaborador=name

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
        'avaliado' : colaborador,
            }
    return render(request, 'blog/G3D2.html', params)

def G4D2(request, name):
    colaborador=name

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
        'avaliado' : colaborador,
            }
    return render(request, 'blog/G4D2.html', params)

def G5D2(request, name):
    colaborador=name

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
        'avaliado' : colaborador,
            }
    return render(request, 'blog/G5D2.html', params)

def G6D2(request, name):
    colaborador=name

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
        'avaliado' : colaborador,
            }
    return render(request, 'blog/G6D2.html', params)

def G7D2(request, name):
    colaborador=name

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
        'avaliado' : colaborador,
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

    params = {
        'UserID':request.user,
        'form1': RHDT.objects.values_list('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7').get(user=resultb6),
        'form11': ADC22.objects.values_list('ADC22E1','ADC22E2').get(user=result6),
        'form2': ADC22.objects.values_list('ADC22G1C','ADC22G2C','ADC22G3C','ADC22G4C','ADC22G5C','ADC22G6C','ADC22G7C','ADC22E1C','ADC22E2C').get(user=result6),
        'form2B': ADC22.objects.values_list('ADC22G1OC','ADC22G2OC','ADC22G3OC','ADC22G4OC','ADC22G5OC','ADC22G6OC','ADC22G7OC','ADC22E1OC','ADC22E2OC').get(user=result6),
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

    MBO23TIME=[]
    MBO23TIME+=RHDT.objects.values_list('MBOTIME23').get(user=resultb6)

    MBO24TIME=[]
    MBO24TIME+=RHDT.objects.values_list('MBOTIME24').get(user=resultb6)

    ADC23TIME=[]
    ADC23TIME+=RHDT.objects.values_list('ADCTIME23').get(user=resultb6)

    ADC24TIME=[]
    ADC24TIME+=RHDT.objects.values_list('ADCTIME24').get(user=resultb6)


    obj = MBO22.objects.get(user=request.user)
    if (request.method == 'POST'):
        friend = DeptForm(request.POST, instance=obj)
        friend.save()

    dept=[]
    dept+=MBO22.objects.values_list('DEPT').get(user=request.user)
    dept1=str(dept[0])
    if dept1 == '':
        time=0
    else:
        time=1

    params = {
        "UserID":request.user,
        "MBO23TIME" : int(MBO23TIME[0]),
        "MBO24TIME" : int(MBO24TIME[0]),
        "ADC23TIME" : int(ADC23TIME[0]),
        "ADC24TIME" : int(ADC24TIME[0]),
        "time" : time,
        "dept": DeptForm(instance=obj),
        }
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
        BB=[]
        try:
            BB+=MBO22.objects.values_list('DEPT').get(user=i.id)
            ES+=str(BB[0])
            ES+=','
        except:
            ES+='departamento não definido'
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
            ES+='sem MBO'
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
            ES+='sem MBO'
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
            ES+='sem MBO'
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
            ES+='sem MBO'
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
            ES+='sem ADC'
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
            ES+='sem PDI'
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
        AA+='^'
        AA+=i.username
        AA+='^'
        AA+='#'
        AA+='^'
        try :
            BB=MBO22.objects.values_list('DEPT').get(user=i.id)
            AA+=BB[0]
            BB=[]
        except :
            AA+='dept não definido'
        AA+='^'
        AA+='#'
        AA+='^'
        try:
            BB=MBO22.objects.values_list('MBO22A1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22AP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22A2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22A3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22A4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22AR').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=MBO22.objects.values_list('MBO22B1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22BP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22B2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22B3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22B4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22BR').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=MBO22.objects.values_list('MBO22C1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22CP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22C2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22C3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22C4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22CR').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=MBO22.objects.values_list('MBO22D1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22DP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22D2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22D3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22D4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22DR').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=MBO22.objects.values_list('MBO22E1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22EP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22E2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22E3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22E4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22ER').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=MBO22.objects.values_list('MBO22F1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22FP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22F2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22F3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22F4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22FR').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=MBO22.objects.values_list('MBO22G1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22GP').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22G2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22G3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22G4').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=MBO22.objects.values_list('MBO22GR').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
        except:
            AA+='não tem MBO'
            AA+='^'
    AA=AA.split('^')
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
        AA+='^'
        AA+=i.username
        AA+='^'
        AA+='#'
        AA+='^'
        try :
            BB=MBO22.objects.values_list('DEPT').get(user=i.id)
            AA+=BB[0]
            BB=[]
        except :
            AA+='dept não definido'
        AA+='^'
        AA+='#'
        AA+='^'
        try:
            CC=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
            BB=RHDT.objects.values_list('ADC22G1').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G1OC').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G1O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=RHDT.objects.values_list('ADC22G2').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G2OC').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G2O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=RHDT.objects.values_list('ADC22G3').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G3OC').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G3O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=RHDT.objects.values_list('ADC22G4').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G4OC').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G4O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=RHDT.objects.values_list('ADC22G5').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G5OC').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G5O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=RHDT.objects.values_list('ADC22G6').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G6OC').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G6O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=RHDT.objects.values_list('ADC22G7').get(user=resultb6)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G7OC').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22G7O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            AA+=i.first_name
            AA+='^'
            BB=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22E1OC').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22E1O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            AA+=i.last_name
            AA+='^'
            BB=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
            AA+=str(BB[0])
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22E2OC').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=ADC22.objects.values_list('ADC22E2O').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
        except:
            AA+='não tem avaliação de competencia'
            AA+='^'
    AA=AA.split('^')
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
        AA+='^'
        AA+=i.username
        AA+='^'
        AA+='#'
        AA+='^'
        try :
            BB=MBO22.objects.values_list('DEPT').get(user=i.id)
            AA+=BB[0]
            BB=[]
        except :
            AA+='dept não definido'
        AA+='^'
        AA+='#'
        AA+='^'      
        try:
            BB=PDI22.objects.values_list('PDI22G1C').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=PDI22.objects.values_list('PDI22G1PD').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=PDI22.objects.values_list('PDI22G1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=PDI22.objects.values_list('PDI22G2C').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=PDI22.objects.values_list('PDI22G2PD').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=PDI22.objects.values_list('PDI22G2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=PDI22.objects.values_list('PDI22G3C').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=PDI22.objects.values_list('PDI22G3PD').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=PDI22.objects.values_list('PDI22G3').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=PDI22.objects.values_list('PDI22E1C').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=PDI22.objects.values_list('PDI22E1PD').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=PDI22.objects.values_list('PDI22E1').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
            BB=PDI22.objects.values_list('PDI22E2C').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=PDI22.objects.values_list('PDI22E2PD').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            BB=PDI22.objects.values_list('PDI22E2').get(user=i.id)
            AA+=BB[0]
            BB=[]
            AA+='^'
            AA+='#'
            AA+='^'
        except:
            AA+='não tem PDI'
            AA+='^'
    AA=AA.split('^')
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


@login_required
def ADC22ESTA(request):

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
    Elist+=RHDT.objects.values_list('ADC22E2C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E3C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E4C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E5C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E6C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E7C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E8C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E9C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E10C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E11C').get(user=resultb6)
    Elist+=RHDT.objects.values_list('ADC22E12C').get(user=resultb6)

    object_list = User.objects.all()
    
    G1C=0.0
    G2C=0.0
    G3C=0.0
    G4C=0.0
    G5C=0.0
    G6C=0.0
    G7C=0.0

    G1A=0.0
    G2A=0.0
    G3A=0.0
    G4A=0.0
    G5A=0.0
    G6A=0.0
    G7A=0.0

    G1CN=0
    G2CN=0
    G3CN=0
    G4CN=0
    G5CN=0
    G6CN=0
    G7CN=0

    G1AN=0
    G2AN=0
    G3AN=0
    G4AN=0
    G5AN=0
    G6AN=0
    G7AN=0

    G1F=0
    G2F=0
    G3F=0
    G4F=0
    G5F=0
    G6F=0
    G7F=0

    G1FC=0
    G2FC=0
    G3FC=0
    G4FC=0
    G5FC=0
    G6FC=0
    G7FC=0

    G1FA=0
    G2FA=0
    G3FA=0
    G4FA=0
    G5FA=0
    G6FA=0
    G7FA=0

    D1G1=0
    D1G1C=0
    D1G1A=0
    D1G2=0
    D1G2C=0
    D1G2A=0
    D1G3=0
    D1G3C=0
    D1G3A=0
    D1G4=0
    D1G4C=0
    D1G4A=0
    D1G5=0
    D1G5C=0
    D1G5A=0
    D1G6=0
    D1G6C=0
    D1G6A=0
    D1G7=0
    D1G7C=0
    D1G7A=0

    D2N=0
    D2G1C=0
    D2G1A=0
    D2G2C=0
    D2G2A=0
    D2G3C=0
    D2G3A=0
    D2G4C=0
    D2G4A=0
    D2G5C=0
    D2G5A=0
    D2G6C=0
    D2G6A=0
    D2G7C=0
    D2G7A=0

    D3N=0
    D3G1C=0
    D3G1A=0
    D3G2C=0
    D3G2A=0
    D3G3C=0
    D3G3A=0
    D3G4C=0
    D3G4A=0
    D3G5C=0
    D3G5A=0
    D3G6C=0
    D3G6A=0
    D3G7C=0
    D3G7A=0

    D4N=0
    D4G1C=0
    D4G1A=0
    D4G2C=0
    D4G2A=0
    D4G3C=0
    D4G3A=0
    D4G4C=0
    D4G4A=0
    D4G5C=0
    D4G5A=0
    D4G6C=0
    D4G6A=0
    D4G7C=0
    D4G7A=0

    D5N=0
    D5G1C=0
    D5G1A=0
    D5G2C=0
    D5G2A=0
    D5G3C=0
    D5G3A=0
    D5G4C=0
    D5G4A=0
    D5G5C=0
    D5G5A=0
    D5G6C=0
    D5G6A=0
    D5G7C=0
    D5G7A=0

    D6N=0
    D6G1C=0
    D6G1A=0
    D6G2C=0
    D6G2A=0
    D6G3C=0
    D6G3A=0
    D6G4C=0
    D6G4A=0
    D6G5C=0
    D6G5A=0
    D6G6C=0
    D6G6A=0
    D6G7C=0
    D6G7A=0

    D7N=0
    D7G1C=0
    D7G1A=0
    D7G2C=0
    D7G2A=0
    D7G3C=0
    D7G3A=0
    D7G4C=0
    D7G4A=0
    D7G5C=0
    D7G5A=0
    D7G6C=0
    D7G6A=0
    D7G7C=0
    D7G7A=0

    D8N=0
    D8G1C=0
    D8G1A=0
    D8G2C=0
    D8G2A=0
    D8G3C=0
    D8G3A=0
    D8G4C=0
    D8G4A=0
    D8G5C=0
    D8G5A=0
    D8G6C=0
    D8G6A=0
    D8G7C=0
    D8G7A=0

    D9N=0
    D9G1C=0
    D9G1A=0
    D9G2C=0
    D9G2A=0
    D9G3C=0
    D9G3A=0
    D9G4C=0
    D9G4A=0
    D9G5C=0
    D9G5A=0
    D9G6C=0
    D9G6A=0
    D9G7C=0
    D9G7A=0

    D10N=0
    D10G1C=0
    D10G1A=0
    D10G2C=0
    D10G2A=0
    D10G3C=0
    D10G3A=0
    D10G4C=0
    D10G4A=0
    D10G5C=0
    D10G5A=0
    D10G6C=0
    D10G6A=0
    D10G7C=0
    D10G7A=0

    D11N=0
    D11G1C=0
    D11G1A=0
    D11G2C=0
    D11G2A=0
    D11G3C=0
    D11G3A=0
    D11G4C=0
    D11G4A=0
    D11G5C=0
    D11G5A=0
    D11G6C=0
    D11G6A=0
    D11G7C=0
    D11G7A=0

    D12N=0
    D12G1C=0
    D12G1A=0
    D12G2C=0
    D12G2A=0
    D12G3C=0
    D12G3A=0
    D12G4C=0
    D12G4A=0
    D12G5C=0
    D12G5A=0
    D12G6C=0
    D12G6A=0
    D12G7C=0
    D12G7A=0

    D13N=0
    D13G1C=0
    D13G1A=0
    D13G2C=0
    D13G2A=0
    D13G3C=0
    D13G3A=0
    D13G4C=0
    D13G4A=0
    D13G5C=0
    D13G5A=0
    D13G6C=0
    D13G6A=0
    D13G7C=0
    D13G7A=0

    D14N=0
    D14G1C=0
    D14G1A=0
    D14G2C=0
    D14G2A=0
    D14G3C=0
    D14G3A=0
    D14G4C=0
    D14G4A=0
    D14G5C=0
    D14G5A=0
    D14G6C=0
    D14G6A=0
    D14G7C=0
    D14G7A=0

    D15N=0
    D15G1C=0
    D15G1A=0
    D15G2C=0
    D15G2A=0
    D15G3C=0
    D15G3A=0
    D15G4C=0
    D15G4A=0
    D15G5C=0
    D15G5A=0
    D15G6C=0
    D15G6A=0
    D15G7C=0
    D15G7A=0

    D16N=0
    D16G1C=0
    D16G1A=0
    D16G2C=0
    D16G2A=0
    D16G3C=0
    D16G3A=0
    D16G4C=0
    D16G4A=0
    D16G5C=0
    D16G5A=0
    D16G6C=0
    D16G6A=0
    D16G7C=0
    D16G7A=0

    D1=''
    D2=''
    D3=''
    D4=''
    D5=''
    D6=''
    D7=''
    D8=''
    D9=''
    D10=''
    D11=''
    D12=''
    D13=''
    D14=''
    D15=''
    D16=''

    E1C=0.0
    E1N=0
    E2C=0.0
    E2N=0
    E3C=0.0
    E3N=0
    E4C=0.0
    E4N=0
    E5C=0.0
    E5N=0
    E6C=0.0
    E6N=0
    E7C=0.0
    E7N=0
    E8C=0.0
    E8N=0
    E9C=0.0
    E9N=0
    E10C=0.0
    E10N=0
    E11C=0.0
    E11N=0
    E12C=0.0
    E12N=0
    E13C=0.0
    E13N=0
    E14C=0.0
    E14N=0
    E15C=0.0
    E15N=0
    E16C=0.0
    E16N=0
    E1A=0.0
    E2A=0.0
    E3A=0.0
    E4A=0.0
    E5A=0.0
    E6A=0.0
    E7A=0.0
    E8A=0.0
    E9A=0.0
    E10A=0.0
    E11A=0.0
    E12A=0.0
    E13A=0.0
    E14A=0.0
    E15A=0.0
    E16A=0.0

    for i in object_list:
        try:
            CE1=[]
            CE1+=ADC22.objects.values_list('ADC22E1').get(user=i.id)
            if Elist[0]==CE1[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
                E1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
                E1A+=float(AA[1])
                E1N+=1
            if Elist[1]==CE1[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
                E2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
                E2A+=float(AA[1])
                E2N+=1
            if Elist[2]==CE1[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
                E3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
                E3A+=float(AA[1])
                E3N+=1
            if Elist[3]==CE1[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
                E4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
                E4A+=float(AA[1])
                E4N+=1
            if Elist[4]==CE1[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
                E5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
                E5A+=float(AA[1])
                E5N+=1
            if Elist[5]==CE1[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
                E6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
                E6A+=float(AA[1])
                E6N+=1
            if Elist[6]==CE1[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
                E7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
                E7A+=float(AA[1])
                E7N+=1
            if Elist[7]==CE1[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
                E8C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
                E8A+=float(AA[1])
                E8N+=1
            if Elist[8]==CE1[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
                E9C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
                E9A+=float(AA[1])
                E9N+=1
            if Elist[9]==CE1[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
                E10C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
                E10A+=float(AA[1])
                E10N+=1
            if Elist[10]==CE1[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
                E11C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
                E11A+=float(AA[1])
                E11N+=1
            if Elist[11]==CE1[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E1C').get(user=i.id)
                E12C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E1A').get(user=i.id)
                E12A+=float(AA[1])
                E12N+=1
            CE2=[]
            CE2+=ADC22.objects.values_list('ADC22E2').get(user=i.id)
            if Elist[0]==CE2[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
                E1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
                E1A+=float(AA[1])
                E1N+=1
            if Elist[1]==CE2[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
                E2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
                E2A+=float(AA[1])
                E2N+=1
            if Elist[2]==CE2[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
                E3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
                E3A+=float(AA[1])
                E3N+=1
            if Elist[3]==CE2[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
                E4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
                E4A+=float(AA[1])
                E4N+=1
            if Elist[4]==CE2[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
                E5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
                E5A+=float(AA[1])
                E5N+=1
            if Elist[5]==CE2[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
                E6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
                E6A+=float(AA[1])
                E6N+=1
            if Elist[6]==CE2[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
                E7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
                E7A+=float(AA[1])
                E7N+=1
            if Elist[7]==CE2[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
                E8C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
                E8A+=float(AA[1])
                E8N+=1
            if Elist[8]==CE2[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
                E9C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
                E9A+=float(AA[1])
                E9N+=1
            if Elist[9]==CE2[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
                E10C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
                E10A+=float(AA[1])
                E10N+=1
            if Elist[10]==CE2[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
                E11C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
                E11A+=float(AA[1])
                E11N+=1
            if Elist[11]==CE2[0]:
                AA=[]
                AA+=ADC22.objects.values_list('ADC22E2C').get(user=i.id)
                E12C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22E2A').get(user=i.id)
                E12A+=float(AA[1])
                E12N+=1
        except :
            AA=[]


    for i in object_list:
        try:
            
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
            G1C+=float(AA[0])
            G1CN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
            G1A+=float(AA[0])
            G1AN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
            G2C+=float(AA[0])
            G2CN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
            G2A+=float(AA[0])
            G2AN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
            G3C+=float(AA[0])
            G3CN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
            G3A+=float(AA[0])
            G3AN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
            G4C+=float(AA[0])
            G4CN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
            G4A+=float(AA[0])
            G4AN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
            G5C+=float(AA[0])
            G5CN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
            G5A+=float(AA[0])
            G5AN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
            G6C+=float(AA[0])
            G6CN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
            G6A+=float(AA[0])
            G6AN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
            G7C+=float(AA[0])
            G7CN+=1
            AA=[]
            AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
            G7A+=float(AA[0])
            G7AN+=1
            if PDI22.objects.values_list('PDI22G1C').get(user=i.id)==RHDT.objects.values_list('ADC22G1').get(user=resultb6):
                G1F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                G1FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                G1FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G1C').get(user=i.id)==RHDT.objects.values_list('ADC22G2').get(user=resultb6):
                G2F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                G2FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                G2FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G1C').get(user=i.id)==RHDT.objects.values_list('ADC22G3').get(user=resultb6):
                G3F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                G3FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                G3FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G1C').get(user=i.id)==RHDT.objects.values_list('ADC22G4').get(user=resultb6):
                G4F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                G4FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                G4FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G1C').get(user=i.id)==RHDT.objects.values_list('ADC22G5').get(user=resultb6):
                G5F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                G5FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                G5FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G1C').get(user=i.id)==RHDT.objects.values_list('ADC22G6').get(user=resultb6):
                G6F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                G6FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                G6FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G1C').get(user=i.id)==RHDT.objects.values_list('ADC22G7').get(user=resultb6):
                G7F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                G7FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                G7FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G2C').get(user=i.id)==RHDT.objects.values_list('ADC22G1').get(user=resultb6):
                G1F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                G1FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                G1FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G2C').get(user=i.id)==RHDT.objects.values_list('ADC22G2').get(user=resultb6):
                G2F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                G2FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                G2FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G2C').get(user=i.id)==RHDT.objects.values_list('ADC22G3').get(user=resultb6):
                G3F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                G3FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                G3FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G2C').get(user=i.id)==RHDT.objects.values_list('ADC22G4').get(user=resultb6):
                G4F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                G4FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                G4FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G2C').get(user=i.id)==RHDT.objects.values_list('ADC22G5').get(user=resultb6):
                G5F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                G5FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                G5FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G2C').get(user=i.id)==RHDT.objects.values_list('ADC22G6').get(user=resultb6):
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                G6FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                G6FA+=float(AA[1])
                G6F+=1
            if PDI22.objects.values_list('PDI22G2C').get(user=i.id)==RHDT.objects.values_list('ADC22G7').get(user=resultb6):
                G7F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                G7FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                G7FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G3C').get(user=i.id)==RHDT.objects.values_list('ADC22G1').get(user=resultb6):
                G1F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                G1FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                G1FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G3C').get(user=i.id)==RHDT.objects.values_list('ADC22G2').get(user=resultb6):
                G2F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                G2FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                G2FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G3C').get(user=i.id)==RHDT.objects.values_list('ADC22G3').get(user=resultb6):
                G3F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                G3FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                G3FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G3C').get(user=i.id)==RHDT.objects.values_list('ADC22G4').get(user=resultb6):
                G4F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                G4FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                G4FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G3C').get(user=i.id)==RHDT.objects.values_list('ADC22G5').get(user=resultb6):
                G5F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                G4FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                G4FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G3C').get(user=i.id)==RHDT.objects.values_list('ADC22G6').get(user=resultb6):
                G6F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                G5FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                G5FA+=float(AA[1])
            if PDI22.objects.values_list('PDI22G3C').get(user=i.id)==RHDT.objects.values_list('ADC22G7').get(user=resultb6):
                G7F+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                G7FC+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                G7FA+=float(AA[1])
            test=[]
            test+=MBO22.objects.values_list('DEPT').get(user=i.id)
            if test[0]=='MARKETING':
                D1=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D1G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D1G1A+=float(AA[1])
                D1G1+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D1G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D1G2A+=float(AA[1])
                D1G2+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D1G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D1G3A+=float(AA[1])
                D1G3+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D1G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D1G4A+=float(AA[1])
                D1G4+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D1G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D1G5A+=float(AA[1])
                D1G5+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D1G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D1G6A+=float(AA[1])
                D1G6+=1
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D1G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D1G7A+=float(AA[1])
                D1G7+=1
            if test[0]=='GERENCIA DE PRODUTOS E FORNECEDORES':
                D2N+=1
                D2=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D2G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D2G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D2G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D2G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D2G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D2G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D2G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D2G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D2G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D2G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D2G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D2G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D2G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D2G7A+=float(AA[1])
            if test[0]=='COMERCIAL':
                D3N+=1
                D3=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D3G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D3G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D3G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D3G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D3G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D3G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D3G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D3G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D3G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D3G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D3G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D3G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D3G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D3G7A+=float(AA[1])
            if test[0]=='OPERACIONAL':
                D4N+=1
                D4=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D4G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D4G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D4G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D4G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D4G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D4G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D4G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D4G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D4G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D4G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D4G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D4G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D4G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D4G7A+=float(AA[1])
            if test[0]=='ADMINISTRATIVO':
                D5N+=1
                D5=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D5G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D5G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D5G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D5G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D5G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D5G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D5G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D5G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D5G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D5G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D5G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D5G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D5G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D5G7A+=float(AA[1])

            if test[0]=='COMERCIAL EXPRESS':
                D6N+=1
                D6=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D6G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D6G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D6G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D6G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D6G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D6G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D6G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D6G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D6G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D6G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D6G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D6G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D6G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D6G7A+=float(AA[1])

            if test[0]=='CUSTOMER SERVICE':
                D7N+=1
                D7=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D7G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D7G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D7G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D7G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D7G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D7G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D7G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D7G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D7G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D7G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D7G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D7G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D7G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D7G7A+=float(AA[1])

            if test[0]=='GARANTIA DA QUALIDADE':
                D8N+=1
                D8=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D8G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D8G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D8G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D8G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D8G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D8G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D8G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D8G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D8G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D8G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D8G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D8G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D8G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D8G7A+=float(AA[1])

            if test[0]=='LOGISTICA':
                D9N+=1
                D9=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D9G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D9G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D9G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D9G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D9G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D9G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D9G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D9G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D9G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D9G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D9G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D9G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D9G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D9G7A+=float(AA[1])

            if test[0]=='PESQUISA E DESENVOLVIMENTO':
                D10N+=1
                D10=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D10G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D10G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D10G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D10G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D10G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D10G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D10G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D10G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D10G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D10G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D10G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D10G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D10G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D10G7A+=float(AA[1])

            if test[0]=='PLANEJAMENTO DE MATERIAIS':
                D11N+=1
                D11=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D11G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D11G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D11G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D11G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D11G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D11G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D11G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D11G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D11G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D11G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D11G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D11G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D11G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D11G7A+=float(AA[1])

            if test[0]=='PLANEJAMENTO FINANCEIRO - FP&A':
                D12N+=1
                D12=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D12G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D12G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D12G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D12G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D12G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D12G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D12G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D12G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D12G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D12G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D12G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D12G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D12G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D12G7A+=float(AA[1])

            if test[0]=='RECURSOS HUMANOS':
                D13N+=1
                D13=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D13G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D13G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D13G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D13G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D13G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D13G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D13G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D13G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D13G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D13G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D13G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D13G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D13G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D13G7A+=float(AA[1])


            if test[0]=='TECNOLOGIA DA INFORMACAO':
                D14N+=1
                D14=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D14G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D14G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D14G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D14G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D14G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D14G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D14G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D14G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D14G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D14G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D14G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D14G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D14G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D14G7A+=float(AA[1])

            if test[0]=='UNIDADE FRAGRANCIAS':
                D15N+=1
                D15=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D15G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D15G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D15G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D15G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D15G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D15G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D15G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D15G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D15G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D15G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D15G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D15G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D15G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D15G7A+=float(AA[1])


            if test[0]=='Financeiro':
                D16N+=1
                D16=test[0]
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G1C').get(user=i.id)
                D16G1C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G1A').get(user=i.id)
                D16G1A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G2C').get(user=i.id)
                D16G2C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G2A').get(user=i.id)
                D16G2A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G3C').get(user=i.id)
                D16G3C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G3A').get(user=i.id)
                D16G3A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G4C').get(user=i.id)
                D16G4C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G4A').get(user=i.id)
                D16G4A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G5C').get(user=i.id)
                D16G5C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G5A').get(user=i.id)
                D16G5A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G6C').get(user=i.id)
                D16G6C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G6A').get(user=i.id)
                D16G6A+=float(AA[1])
                AA=[]
                AA+=ADC22.objects.values_list('ADC22G7C').get(user=i.id)
                D16G7C+=float(AA[0])
                AA+=ADC22.objects.values_list('ADC22G7A').get(user=i.id)
                D16G7A+=float(AA[1])


        except:
            AA=1

    if E1N!=0:
        E1C=round(E1C/E1N,1)
        E1A=round(E1A/E1N,1)
    if E2N!=0:
        E2C=round(E2C/E2N,1)
        E2A=round(E2A/E2N,1)
    if E3N!=0:
        E3C=round(E3C/E3N,1)
        E3A=round(E3A/E3N,1)
    if E4N!=0:
        E4C=round(E4C/E4N,1)
        E4A=round(E4A/E4N,1)
    if E5N!=0:
        E5C=round(E5C/E5N,1)
        E5A=round(E5A/E5N,1)
    if E6N!=0:
        E6C=round(E6C/E6N,1)
        E6A=round(E6A/E6N,1)
    if E7N!=0:
        E7C=round(E7C/E7N,1)
        E7A=round(E7A/E7N,1)
    if E8N!=0:
        E8C=round(E8C/E8N,1)
        E8A=round(E8A/E8N,1)
    if E9N!=0:
        E9C=round(E9C/E9N,1)
        E9A=round(E9A/E9N,1)
    if E10N!=0:
        E10C=round(E10C/E10N,1)
        E10A=round(E10A/E10N,1)
    if E11N!=0:
        E11C=round(E11C/E11N,1)
        E11A=round(E11A/E11N,1)
    if E12N!=0:
        E12C=round(E12C/E12N,1)
        E12A=round(E12A/E12N,1)


    G1C=round(G1C/G1CN,1)
    G1A=round(G1A/G1AN,1)
    G2C=round(G2C/G2CN,1)
    G2A=round(G2A/G2AN,1)
    G3C=round(G3C/G3CN,1)
    G3A=round(G3A/G3AN,1)
    G4C=round(G4C/G4CN,1)
    G4A=round(G4A/G4AN,1)
    G5C=round(G5C/G5CN,1)
    G5A=round(G5A/G5AN,1)
    G6C=round(G6C/G6CN,1)
    G6A=round(G6A/G6AN,1)
    G7C=round(G7C/G7CN,1)
    G7A=round(G7A/G7AN,1)

    if G1F!=0:
        G1FC=round(G1FC/G1F,1)
        G1FA=round(G1FA/G1F,1)
    if G2F!=0:
        G2FC=round(G2FC/G2F,1)
        G2FA=round(G2FA/G2F,1)
    if G3F!=0:
        G3FC=round(G3FC/G3F,1)
        G3FA=round(G3FA/G3F,1)
    if G4F!=0:
        G4FC=round(G4FC/G4F,1)
        G4FA=round(G4FA/G4F,1)
    if G5F!=0:
        G5FC=round(G5FC/G5F,1)
        G5FA=round(G5FA/G5F,1)
    if G6F!=0:
        G6FC=round(G6FC/G6F,1)
        G6FA=round(G6FA/G6F,1)
    if G7F!=0:
        G7FC=round(G7FC/G7F,1)
        G7FA=round(G7FA/G7F,1)

    if D1G1==0:
        D1G1=0
        D1G1C=0
        D1G1A=0
    else:
        D1G1C=round(D1G1C/D1G1,1)
        D1G1A=round(D1G1A/D1G1,1)
    if D1G2==0:
        D1G2=0
        D1G2C=0
        D1G2A=0
    else:
        D1G2C=round(D1G2C/D1G2,1)
        D1G2A=round(D1G2A/D1G2,1)
    if D1G3==0:
        D1G3=0
        D1G3C=0
        D1G3A=0
    else:
        D1G3C=round(D1G3C/D1G3,1)
        D1G3A=round(D1G3A/D1G3,1)
    if D1G4==0:
        D1G4=0
        D1G4C=0
        D1G4A=0
    else:
        D1G4C=round(D1G4C/D1G4,1)
        D1G4A=round(D1G4A/D1G4,1)
    if D1G5==0:
        D1G5=0
        D1G5C=0
        D1G5A=0
    else:
        D1G5C=round(D1G5C/D1G5,1)
        D1G5A=round(D1G5A/D1G5,1)
    if D1G6==0:
        D1G6=0
        D1G6C=0
        D1G6A=0
    else:
        D1G6C=round(D1G6C/D1G6,1)
        D1G6A=round(D1G6A/D1G6,1)
    if D1G7==0:
        D1G7=0
        D1G7C=0
        D1G7A=0
    else:
        D1G7C=round(D1G7C/D1G7,1)
        D1G7A=round(D1G7A/D1G7,1)

    if D2N!=0:
        D2G1C=round(D2G1C/D2N,1)
        D2G1A=round(D2G1A/D2N,1)
        D2G2C=round(D2G2C/D2N,1)
        D2G2A=round(D2G2A/D2N,1)
        D2G3C=round(D2G3C/D2N,1)
        D2G3A=round(D2G3A/D2N,1)
        D2G4C=round(D2G4C/D2N,1)
        D2G4A=round(D2G4A/D2N,1)
        D2G5C=round(D2G5C/D2N,1)
        D2G5A=round(D2G5A/D2N,1)
        D2G6C=round(D2G6C/D2N,1)
        D2G6A=round(D2G6A/D2N,1)
        D2G7C=round(D2G7C/D2N,1)
        D2G7A=round(D2G7A/D2N,1)

    if D3N!=0:
        D3G1C=round(D3G1C/D3N,1)
        D3G1A=round(D3G1A/D3N,1)
        D3G2C=round(D3G2C/D3N,1)
        D3G2A=round(D3G2A/D3N,1)
        D3G3C=round(D3G3C/D3N,1)
        D3G3A=round(D3G3A/D3N,1)
        D3G4C=round(D3G4C/D3N,1)
        D3G4A=round(D3G4A/D3N,1)
        D3G5C=round(D3G5C/D3N,1)
        D3G5A=round(D3G5A/D3N,1)
        D3G6C=round(D3G6C/D3N,1)
        D3G6A=round(D3G6A/D3N,1)
        D3G7C=round(D3G7C/D3N,1)
        D3G7A=round(D3G7A/D3N,1)

    if D4N!=0:
        D4G1C=round(D4G1C/D4N,1)
        D4G1A=round(D4G1A/D4N,1)
        D4G2C=round(D4G2C/D4N,1)
        D4G2A=round(D4G2A/D4N,1)
        D4G3C=round(D4G3C/D4N,1)
        D4G3A=round(D4G3A/D4N,1)
        D4G4C=round(D4G4C/D4N,1)
        D4G4A=round(D4G4A/D4N,1)
        D4G5C=round(D4G5C/D4N,1)
        D4G5A=round(D4G5A/D4N,1)
        D4G6C=round(D4G6C/D4N,1)
        D4G6A=round(D4G6A/D4N,1)
        D4G7C=round(D4G7C/D4N,1)
        D4G7A=round(D4G7A/D4N,1)

    if D5N!=0:
        D5G1C=round(D5G1C/D5N,1)
        D5G1A=round(D5G1A/D5N,1)
        D5G2C=round(D5G2C/D5N,1)
        D5G2A=round(D5G2A/D5N,1)
        D5G3C=round(D5G3C/D5N,1)
        D5G3A=round(D5G3A/D5N,1)
        D5G4C=round(D5G4C/D5N,1)
        D5G4A=round(D5G4A/D5N,1)
        D5G5C=round(D5G5C/D5N,1)
        D5G5A=round(D5G5A/D5N,1)
        D5G6C=round(D5G6C/D5N,1)
        D5G6A=round(D5G6A/D5N,1)
        D5G7C=round(D5G7C/D5N,1)
        D5G7A=round(D5G7A/D5N,1)


    if D6N!=0:
        D6G1C=round(D6G1C/D6N,1)
        D6G1A=round(D6G1A/D6N,1)
        D6G2C=round(D6G2C/D6N,1)
        D6G2A=round(D6G2A/D6N,1)
        D6G3C=round(D6G3C/D6N,1)
        D6G3A=round(D6G3A/D6N,1)
        D6G4C=round(D6G4C/D6N,1)
        D6G4A=round(D6G4A/D6N,1)
        D6G5C=round(D6G5C/D6N,1)
        D6G5A=round(D6G5A/D6N,1)
        D6G6C=round(D6G6C/D6N,1)
        D6G6A=round(D6G6A/D6N,1)
        D6G7C=round(D6G7C/D6N,1)
        D6G7A=round(D6G7A/D6N,1)

    if D7N!=0:
        D7G1C=round(D7G1C/D7N,1)
        D7G1A=round(D7G1A/D7N,1)
        D7G2C=round(D7G2C/D7N,1)
        D7G2A=round(D7G2A/D7N,1)
        D7G3C=round(D7G3C/D7N,1)
        D7G3A=round(D7G3A/D7N,1)
        D7G4C=round(D7G4C/D7N,1)
        D7G4A=round(D7G4A/D7N,1)
        D7G5C=round(D7G5C/D7N,1)
        D7G5A=round(D7G5A/D7N,1)
        D7G6C=round(D7G6C/D7N,1)
        D7G6A=round(D7G6A/D7N,1)
        D7G7C=round(D7G7C/D7N,1)
        D7G7A=round(D7G7A/D7N,1)

    if D8N!=0:
        D8G1C=round(D8G1C/D8N,1)
        D8G1A=round(D8G1A/D8N,1)
        D8G2C=round(D8G2C/D8N,1)
        D8G2A=round(D8G2A/D8N,1)
        D8G3C=round(D8G3C/D8N,1)
        D8G3A=round(D8G3A/D8N,1)
        D8G4C=round(D8G4C/D8N,1)
        D8G4A=round(D8G4A/D8N,1)
        D8G5C=round(D8G5C/D8N,1)
        D8G5A=round(D8G5A/D8N,1)
        D8G6C=round(D8G6C/D8N,1)
        D8G6A=round(D8G6A/D8N,1)
        D8G7C=round(D8G7C/D8N,1)
        D8G7A=round(D8G7A/D8N,1)

    if D9N!=0:
        D9G1C=round(D9G1C/D9N,1)
        D9G1A=round(D9G1A/D9N,1)
        D9G2C=round(D9G2C/D9N,1)
        D9G2A=round(D9G2A/D9N,1)
        D9G3C=round(D9G3C/D9N,1)
        D9G3A=round(D9G3A/D9N,1)
        D9G4C=round(D9G4C/D9N,1)
        D9G4A=round(D9G4A/D9N,1)
        D9G5C=round(D9G5C/D9N,1)
        D9G5A=round(D9G5A/D9N,1)
        D9G6C=round(D9G6C/D9N,1)
        D9G6A=round(D9G6A/D9N,1)
        D9G7C=round(D9G7C/D9N,1)
        D9G7A=round(D9G7A/D9N,1)

    if D10N!=0:
        D10G1C=round(D10G1C/D10N,1)
        D10G1A=round(D10G1A/D10N,1)
        D10G2C=round(D10G2C/D10N,1)
        D10G2A=round(D10G2A/D10N,1)
        D10G3C=round(D10G3C/D10N,1)
        D10G3A=round(D10G3A/D10N,1)
        D10G4C=round(D10G4C/D10N,1)
        D10G4A=round(D10G4A/D10N,1)
        D10G5C=round(D10G5C/D10N,1)
        D10G5A=round(D10G5A/D10N,1)
        D10G6C=round(D10G6C/D10N,1)
        D10G6A=round(D10G6A/D10N,1)
        D10G7C=round(D10G7C/D10N,1)
        D10G7A=round(D10G7A/D10N,1)

    if D11N!=0:
        D11G1C=round(D11G1C/D11N,1)
        D11G1A=round(D11G1A/D11N,1)
        D11G2C=round(D11G2C/D11N,1)
        D11G2A=round(D11G2A/D11N,1)
        D11G3C=round(D11G3C/D11N,1)
        D11G3A=round(D11G3A/D11N,1)
        D11G4C=round(D11G4C/D11N,1)
        D11G4A=round(D11G4A/D11N,1)
        D11G5C=round(D11G5C/D11N,1)
        D11G5A=round(D11G5A/D11N,1)
        D11G6C=round(D11G6C/D11N,1)
        D11G6A=round(D11G6A/D11N,1)
        D11G7C=round(D11G7C/D11N,1)
        D11G7A=round(D11G7A/D11N,1)

    if D12N!=0:
        D12G1C=round(D12G1C/D12N,1)
        D12G1A=round(D12G1A/D12N,1)
        D12G2C=round(D12G2C/D12N,1)
        D12G2A=round(D12G2A/D12N,1)
        D12G3C=round(D12G3C/D12N,1)
        D12G3A=round(D12G3A/D12N,1)
        D12G4C=round(D12G4C/D12N,1)
        D12G4A=round(D12G4A/D12N,1)
        D12G5C=round(D12G5C/D12N,1)
        D12G5A=round(D12G5A/D12N,1)
        D12G6C=round(D12G6C/D12N,1)
        D12G6A=round(D12G6A/D12N,1)
        D12G7C=round(D12G7C/D12N,1)
        D12G7A=round(D12G7A/D12N,1)

    if D13N!=0:
        D13G1C=round(D13G1C/D13N,1)
        D13G1A=round(D13G1A/D13N,1)
        D13G2C=round(D13G2C/D13N,1)
        D13G2A=round(D13G2A/D13N,1)
        D13G3C=round(D13G3C/D13N,1)
        D13G3A=round(D13G3A/D13N,1)
        D13G4C=round(D13G4C/D13N,1)
        D13G4A=round(D13G4A/D13N,1)
        D13G5C=round(D13G5C/D13N,1)
        D13G5A=round(D13G5A/D13N,1)
        D13G6C=round(D13G6C/D13N,1)
        D13G6A=round(D13G6A/D13N,1)
        D13G7C=round(D13G7C/D13N,1)
        D13G7A=round(D13G7A/D13N,1)

    if D14N!=0:
        D14G1C=round(D14G1C/D14N,1)
        D14G1A=round(D14G1A/D14N,1)
        D14G2C=round(D14G2C/D14N,1)
        D14G2A=round(D14G2A/D14N,1)
        D14G3C=round(D14G3C/D14N,1)
        D14G3A=round(D14G3A/D14N,1)
        D14G4C=round(D14G4C/D14N,1)
        D14G4A=round(D14G4A/D14N,1)
        D14G5C=round(D14G5C/D14N,1)
        D14G5A=round(D14G5A/D14N,1)
        D14G6C=round(D14G6C/D14N,1)
        D14G6A=round(D14G6A/D14N,1)
        D14G7C=round(D14G7C/D14N,1)
        D14G7A=round(D14G7A/D14N,1)

    if D15N!=0:
        D15G1C=round(D15G1C/D15N,1)
        D15G1A=round(D15G1A/D15N,1)
        D15G2C=round(D15G2C/D15N,1)
        D15G2A=round(D15G2A/D15N,1)
        D15G3C=round(D15G3C/D15N,1)
        D15G3A=round(D15G3A/D15N,1)
        D15G4C=round(D15G4C/D15N,1)
        D15G4A=round(D15G4A/D15N,1)
        D15G5C=round(D15G5C/D15N,1)
        D15G5A=round(D15G5A/D15N,1)
        D15G6C=round(D15G6C/D15N,1)
        D15G6A=round(D15G6A/D15N,1)
        D15G7C=round(D15G7C/D15N,1)
        D15G7A=round(D15G7A/D15N,1)

    if D16N!=0:
        D16G1C=round(D16G1C/D16N,1)
        D16G1A=round(D16G1A/D16N,1)
        D16G2C=round(D16G2C/D16N,1)
        D16G2A=round(D16G2A/D16N,1)
        D16G3C=round(D16G3C/D16N,1)
        D16G3A=round(D16G3A/D16N,1)
        D16G4C=round(D16G4C/D16N,1)
        D16G4A=round(D16G4A/D16N,1)
        D16G5C=round(D16G5C/D16N,1)
        D16G5A=round(D16G5A/D16N,1)
        D16G6C=round(D16G6C/D16N,1)
        D16G6A=round(D16G6A/D16N,1)
        D16G7C=round(D16G7C/D16N,1)
        D16G7A=round(D16G7A/D16N,1)

    GG=[]
    GG+=RHDT.objects.values_list('ADC22G1').get(user=resultb6)
    GG+=RHDT.objects.values_list('ADC22G2').get(user=resultb6)
    GG+=RHDT.objects.values_list('ADC22G3').get(user=resultb6)
    GG+=RHDT.objects.values_list('ADC22G4').get(user=resultb6)
    GG+=RHDT.objects.values_list('ADC22G5').get(user=resultb6)
    GG+=RHDT.objects.values_list('ADC22G6').get(user=resultb6)
    GG+=RHDT.objects.values_list('ADC22G7').get(user=resultb6)

    params = {
        "test":test,
        "UserID":request.user,
        "G1":GG[0],
        "G2":GG[1],
        "G3":GG[2],
        "G4":GG[3],
        "G5":GG[4],
        "G6":GG[5],
        "G7":GG[6],
        "G1C":G1C,
        "G1A":G1A,
        "G1CN":G1CN,
        "G1AN":G1AN,
        "G2C":G2C,
        "G2A":G2A,
        "G2CN":G2CN,
        "G2AN":G2AN,
        "G3C":G3C,
        "G3A":G3A,
        "G3CN":G3CN,
        "G3AN":G3AN,
        "G4C":G4C,
        "G4A":G4A,
        "G4CN":G4CN,
        "G4AN":G4AN,
        "G5C":G5C,
        "G5A":G5A,
        "G5CN":G5CN,
        "G5AN":G5AN,
        "G6C":G6C,
        "G6A":G6A,
        "G6CN":G6CN,
        "G6AN":G6AN,
        "G7C":G7C,
        "G7A":G7A,
        "G7CN":G7CN,
        "G7AN":G7AN,
        "G1FC":G1FC,
        "G2FC":G2FC,
        "G3FC":G3FC,
        "G4FC":G4FC,
        "G5FC":G5FC,
        "G6FC":G6FC,
        "G7FC":G7FC,
        "G1FA":G1FA,
        "G2FA":G2FA,
        "G3FA":G3FA,
        "G4FA":G4FA,
        "G5FA":G5FA,
        "G6FA":G6FA,
        "G7FA":G7FA,
        "G1F":G1F,
        "G2F":G2F,
        "G3F":G3F,
        "G4F":G4F,
        "G5F":G5F,
        "G6F":G6F,
        "G7F":G7F,
        "D1":D1,
        "D1N":D1G1,
        "D1G1C":D1G1C,
        "D1G1A":D1G1A,
        "D1G2C":D1G2C,
        "D1G2A":D1G2A,
        "D1G3C":D1G3C,
        "D1G3A":D1G3A,
        "D1G4C":D1G4C,
        "D1G4A":D1G4A,
        "D1G5C":D1G5C,
        "D1G5A":D1G5A,
        "D1G6C":D1G6C,
        "D1G6A":D1G6A,
        "D1G7C":D1G7C,
        "D1G7A":D1G7A,
        "D2":D2,
        "D2N":D2N,
        "D2G1C":D2G1C,
        "D2G1A":D2G1A,
        "D2G2C":D2G2C,
        "D2G2A":D2G2A,
        "D2G3C":D2G3C,
        "D2G3A":D2G3A,
        "D2G4C":D2G4C,
        "D2G4A":D2G4A,
        "D2G5C":D2G5C,
        "D2G5A":D2G5A,
        "D2G6C":D2G6C,
        "D2G6A":D2G6A,
        "D2G7C":D2G7C,
        "D2G7A":D2G7A,
        "D3":D3,
        "D3N":D3N,
        "D3G1C":D3G1C,
        "D3G1A":D3G1A,
        "D3G2C":D3G2C,
        "D3G2A":D3G2A,
        "D3G3C":D3G3C,
        "D3G3A":D3G3A,
        "D3G4C":D3G4C,
        "D3G4A":D3G4A,
        "D3G5C":D3G5C,
        "D3G5A":D3G5A,
        "D3G6C":D3G6C,
        "D3G6A":D3G6A,
        "D3G7C":D3G7C,
        "D3G7A":D3G7A,
        "D4":D4,
        "D4N":D4N,
        "D4G1C":D4G1C,
        "D4G1A":D4G1A,
        "D4G2C":D4G2C,
        "D4G2A":D4G2A,
        "D4G3C":D4G3C,
        "D4G3A":D4G3A,
        "D4G4C":D4G4C,
        "D4G4A":D4G4A,
        "D4G5C":D4G5C,
        "D4G5A":D4G5A,
        "D4G6C":D4G6C,
        "D4G6A":D4G6A,
        "D4G7C":D4G7C,
        "D4G7A":D4G7A,
        "D5":D5,
        "D5N":D5N,
        "D5G1C":D5G1C,
        "D5G1A":D5G1A,
        "D5G2C":D5G2C,
        "D5G2A":D15G2A,
        "D5G3C":D5G3C,
        "D5G3A":D5G3A,
        "D5G4C":D5G4C,
        "D5G4A":D5G4A,
        "D5G5C":D5G5C,
        "D5G5A":D5G5A,
        "D5G6C":D5G6C,
        "D5G6A":D5G6A,
        "D5G7C":D5G7C,
        "D5G7A":D5G7A,
        "D6":D6,
        "D6N":D6N,
        "D6G1C":D6G1C,
        "D6G1A":D6G1A,
        "D6G2C":D6G2C,
        "D6G2A":D6G2A,
        "D6G3C":D6G3C,
        "D6G3A":D6G3A,
        "D6G4C":D6G4C,
        "D6G4A":D6G4A,
        "D6G5C":D6G5C,
        "D6G5A":D6G5A,
        "D6G6C":D6G6C,
        "D6G6A":D6G6A,
        "D6G7C":D6G7C,
        "D6G7A":D6G7A,
        "D7":D7,
        "D7N":D7N,
        "D7G1C":D7G1C,
        "D7G1A":D7G1A,
        "D7G2C":D7G2C,
        "D7G2A":D7G2A,
        "D7G3C":D7G3C,
        "D7G3A":D7G3A,
        "D7G4C":D7G4C,
        "D7G4A":D7G4A,
        "D7G5C":D7G5C,
        "D7G5A":D7G5A,
        "D7G6C":D7G6C,
        "D7G6A":D7G6A,
        "D7G7C":D7G7C,
        "D7G7A":D7G7A,
        "D8":D8,
        "D8N":D8N,
        "D8G1C":D8G1C,
        "D8G1A":D8G1A,
        "D8G2C":D8G2C,
        "D8G2A":D8G2A,
        "D8G3C":D8G3C,
        "D8G3A":D8G3A,
        "D8G4C":D8G4C,
        "D8G4A":D8G4A,
        "D8G5C":D8G5C,
        "D8G5A":D8G5A,
        "D8G6C":D8G6C,
        "D8G6A":D8G6A,
        "D8G7C":D8G7C,
        "D8G7A":D8G7A,
        "D9":D9,
        "D9N":D9N,
        "D9G1C":D9G1C,
        "D9G1A":D9G1A,
        "D9G2C":D9G2C,
        "D9G2A":D9G2A,
        "D9G3C":D9G3C,
        "D9G3A":D9G3A,
        "D9G4C":D9G4C,
        "D9G4A":D9G4A,
        "D9G5C":D9G5C,
        "D9G5A":D9G5A,
        "D9G6C":D9G6C,
        "D9G6A":D9G6A,
        "D9G7C":D9G7C,
        "D9G7A":D9G7A,
        "D10":D10,
        "D10N":D10N,
        "D10G1C":D10G1C,
        "D10G1A":D10G1A,
        "D10G2C":D10G2C,
        "D10G2A":D10G2A,
        "D10G3C":D10G3C,
        "D10G3A":D10G3A,
        "D10G4C":D10G4C,
        "D10G4A":D10G4A,
        "D10G5C":D10G5C,
        "D10G5A":D10G5A,
        "D10G6C":D10G6C,
        "D10G6A":D10G6A,
        "D10G7C":D10G7C,
        "D10G7A":D10G7A,

        "D11":D11,
        "D11N":D11N,
        "D11G1C":D11G1C,
        "D11G1A":D11G1A,
        "D11G2C":D11G2C,
        "D11G2A":D11G2A,
        "D11G3C":D11G3C,
        "D11G3A":D11G3A,
        "D11G4C":D11G4C,
        "D11G4A":D11G4A,
        "D11G5C":D11G5C,
        "D11G5A":D11G5A,
        "D11G6C":D11G6C,
        "D11G6A":D11G6A,
        "D11G7C":D11G7C,
        "D11G7A":D11G7A,
        "D12":D12,
        "D12N":D12N,
        "D12G1C":D12G1C,
        "D12G1A":D12G1A,
        "D12G2C":D12G2C,
        "D12G2A":D12G2A,
        "D12G3C":D12G3C,
        "D12G3A":D12G3A,
        "D12G4C":D12G4C,
        "D12G4A":D12G4A,
        "D12G5C":D12G5C,
        "D12G5A":D12G5A,
        "D12G6C":D12G6C,
        "D12G6A":D12G6A,
        "D12G7C":D12G7C,
        "D12G7A":D12G7A,
        "D13":D13,
        "D13N":D13N,
        "D13G1C":D13G1C,
        "D13G1A":D13G1A,
        "D13G2C":D13G2C,
        "D13G2A":D13G2A,
        "D13G3C":D13G3C,
        "D13G3A":D13G3A,
        "D13G4C":D13G4C,
        "D13G4A":D13G4A,
        "D13G5C":D13G5C,
        "D13G5A":D13G5A,
        "D13G6C":D13G6C,
        "D13G6A":D13G6A,
        "D13G7C":D13G7C,
        "D13G7A":D13G7A,
        "D14":D14,
        "D14N":D14N,
        "D14G1C":D14G1C,
        "D14G1A":D14G1A,
        "D14G2C":D14G2C,
        "D14G2A":D14G2A,
        "D14G3C":D14G3C,
        "D14G3A":D14G3A,
        "D14G4C":D14G4C,
        "D14G4A":D14G4A,
        "D14G5C":D14G5C,
        "D14G5A":D14G5A,
        "D14G6C":D14G6C,
        "D14G6A":D14G6A,
        "D14G7C":D14G7C,
        "D14G7A":D14G7A,
        "D15":D15,
        "D15N":D15N,
        "D15G1C":D15G1C,
        "D15G1A":D15G1A,
        "D15G2C":D15G2C,
        "D15G2A":D15G2A,
        "D15G3C":D15G3C,
        "D15G3A":D15G3A,
        "D15G4C":D15G4C,
        "D15G4A":D15G4A,
        "D15G5C":D15G5C,
        "D15G5A":D15G5A,
        "D15G6C":D15G6C,
        "D15G6A":D15G6A,
        "D15G7C":D15G7C,
        "D15G7A":D15G7A,
        "D16":D10,
        "D16N":D16N,
        "D16G1C":D16G1C,
        "D16G1A":D16G1A,
        "D16G2C":D16G2C,
        "D16G2A":D16G2A,
        "D16G3C":D16G3C,
        "D16G3A":D16G3A,
        "D16G4C":D16G4C,
        "D16G4A":D16G4A,
        "D16G5C":D16G5C,
        "D16G5A":D16G5A,
        "D16G6C":D16G6C,
        "D16G6A":D16G6A,
        "D16G7C":D16G7C,
        "D16G7A":D16G7A,
        "E1N":E1N,
        "E1C":E1C,
        "E1A":E1A,
        "E2N":E2N,
        "E2C":E2C,
        "E2A":E2A,
        "E3N":E3N,
        "E3C":E3C,
        "E3A":E3A,
        "E4N":E4N,
        "E4C":E4C,
        "E4A":E4A,
        "E5N":E5N,
        "E5C":E5C,
        "E5A":E5A,
        "E6N":E6N,
        "E6C":E6C,
        "E6A":E6A,
        "E7N":E7N,
        "E7C":E7C,
        "E7A":E7A,
        "E8N":E8N,
        "E8C":E8C,
        "E8A":E8A,
        "E9N":E9N,
        "E9C":E9C,
        "E9A":E9A,
        "E10N":E10N,
        "E10C":E10C,
        "E10A":E10A,
        "E11N":E11N,
        "E11C":E11C,
        "E11A":E11A,
        "E12N":E12N,
        "E12C":E12C,
        "E12A":E12A,
        "E1":Elist[0],
        "E2":Elist[1],
        "E3":Elist[2],
        "E4":Elist[3],
        "E5":Elist[4],
        "E6":Elist[5],
        "E7":Elist[6],
        "E8":Elist[7],
        "E9":Elist[8],
        "E10":Elist[9],
        "E11":Elist[10],
        "E12":Elist[11],
        "test":CE1

        }
    return render(request, "blog/ADC22ESTA.html",context=params)


