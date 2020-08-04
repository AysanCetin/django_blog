from django.db import models
from django.utils import timezone

# Gonderi isimli model oluşturduk
# Bu modelin kendina ait 
# attribute leri olsun --> baslik, icerik, yazar, y_tarihi, tag

class Gonderi(models.Model): 
    # models.Model --> Gonderi nin bir django modeli olduğunu belirtir.
    # Ayrıca veritabanı işlemlerimizi bu Model e göre yapmasını django'ya söylüyoruz.
    baslik = models.CharField(max_length=200) # baslik attribute' u --> CharField --> kısıtlı olan metinleri ifade eden bir fonksiyondur.
    icerik = models.TextField() # TextField --> kısıtlı olmayan metinleri ifade eden bir fonksiyondur.  
    yazar = models.ForeignKey('auth.User', on_delete=models.CASCADE,) #ForeignKey --> başka modelden alınması gerektiğini söyleyen, ifade eden bir fonksiyondur. 'auth.User' --> 'User' isimli başka modelimiz var   
    y_tarihi = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=300, blank=True, null=True)

    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik