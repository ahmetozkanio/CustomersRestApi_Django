from django.contrib import admin

from .models import Customer

# Register your models here.

@admin.register(Customer)
class ArticleAdmin(admin.ModelAdmin):#Django Tarafindan Soylenen Class Admin PaneliniOzellestirmek icin gerekli
    
    #bu bize admin panelindeki Article basliginda hangi bilgilerin gosterilmesini istiyorsak onu belirtiyoruz
    list_display = ["first_name","last_name","email","tel"]

    #bu ise bize basliktaki yine o bilgiye bastigimizda icerigin acilmasini saglar 
    list_display_link = ["first_name","last_name"]

    #first_name Bilgisine gore arama ozelligini koyduk Admin paneline Yani search bar ekledik
    search_fields = ["first_name","last_name","email","tel"]

    #Filtre olusturma yani tarih siralamasi ekledik admin paneline hangi tarihe gore bilgileri gosterdik
    list_filter = ["created_date"]
    class Meta:
        model = Customer