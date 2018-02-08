from django.db import models

class FiyatTahmin(models.Model):
	metreKare = models.IntegerField(default = 0)
	odaSayisi = models.IntegerField(default = 0) 
	fiyat = models.IntegerField(default = 0)
