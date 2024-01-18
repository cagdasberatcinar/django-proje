from django.db import models


class Category(models.Model):
    title = models.CharField(("Kategori Başlığı"), max_length=50)
    slug = models.SlugField(("Slug"))
    def __str__(self) -> str: 
        return self.title

class Blog(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Başlık"), max_length=150) 
    text = models.TextField(verbose_name="İçerik")
    date_now = models.DateTimeField(("Tarih - Saat"), auto_now=False, auto_now_add=False)
    author = models.CharField(("Yazar"), max_length=50)
    image = models.ImageField(("Blok Resmi"), upload_to="", max_length=300, null=True)
    subtitle = models.CharField(("Alt Başlık"), max_length=50, null=True, blank=True)
    isactive = models.BooleanField(("Sayfada Göster"),  default=False)
    slug=models.SlugField(("Slug"), blank=True)
    
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name=("Blog"), on_delete=models.CASCADE, null=True) 
    fullname = models.CharField(("Ad - Soyad"), max_length=50) # AD KISMINI GÖSTERİYOR
    text = models.TextField(("Yorum")) # YORUM KISMINI GÖSTERİYOR
    date_now = models.DateTimeField(("Tarih - Saat"), auto_now=False, auto_now_add=True) # YORUMUN NE ZAMAN YAPILDIĞINI GÖSTERİR
    def __str__(self) -> str: 
        return self.blog.title

class Contact(models.Model):
    firstname = models.CharField(("Adı"), max_length=50)
    lastname = models.CharField(("Soyadı"), max_length=50)
    companyname = models.CharField(("Şirket Adı"), max_length=150)
    adres = models.CharField(("Adresi"), max_length=150)
    title = models.CharField(("Konu"), max_length=150)
    email = models.EmailField(("E-mail Adresi"), max_length=254)
    phonenumber = models.CharField(("Telefon Numarası"), max_length=50)
    text = models.TextField(("İletişim Mesajı"))
    def __str__(self) -> str:
        return self.title