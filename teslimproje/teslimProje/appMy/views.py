from django.shortcuts import render
from appMy.models import *
from django.db.models import Q

def indexPage(request):
    context = {}
    return render(request, 'index.html', context)


def blogPage(request, slug=None):
    if slug:
        blog_list = Blog.objects.filter(category__slug=slug).order_by("-id")
    else:
        blog_list = Blog.objects.all().order_by("-id")
    category_list = Category.objects.all()
    
    query = request.GET.get("query")
    if query:
        blog_list = blog_list.filter(Q(title__icontains=query) | Q(text__icontains=query) | Q(author__icontains=query) | Q(category__title__icontains=query))
    context = {
        "blog_list": blog_list,
        "category_list": category_list,
    }
    return render(request, 'bloglar.html', context)
    
def detailPage(request, bid):
    # kullanıcı ya da frontend'den bilgi alabilmenin 2 yöntemi vardır.
    # 1) url adresinden
    # 2) Formlardan
    if bid.isnumeric():
        
        blog = Blog.objects.get(id=bid) # getirmediği durumda hata verir
    else:
          blog = Blog.objects.get(slug=bid)
    comment_list = Comment.objects.filter(blog=blog)
    
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        text = request.POST.get("comment")
        comment = Comment(fullname=fullname, text=text, blog=blog)
        comment.save()
    
    context = {
        "blog":blog,
        "comment_list":comment_list,
    }
    return render(request, 'detail.html', context)



def iletisimPage(request):
    if request.method == "POST":
        finame = request.POST.get("firstname")
        laname = request.POST.get("lastname")
        company = request.POST.get("companyname")
        adress = request.POST.get("adres")
        mail = request.POST.get("email")
        phone = request.POST.get("phonenumber")
        subject = request.POST.get("title")
        textsubject = request.POST.get("text")
        iletisim = Contact(firstname=finame, lastname=laname, companyname=company, adres=adress, email=mail, phonenumber=phone, title=subject, text=textsubject)
        iletisim.save()
    context = {}
    return render(request, 'iletisim.html', context)
def hakkimizdaPage(request):
    context = {}
    return render(request, 'hakkimizda.html', context)


