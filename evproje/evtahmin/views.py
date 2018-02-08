# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FiyatTahmin
import numpy as np  
import pandas as pd
from sklearn.linear_model import LinearRegression

class EvFiyatTahmin(APIView):
	def get(self , request, metreKare , odaSayisi):
		data = FiyatTahmin.objects.all() ##Veritabanından bilgileri aliyoruz.
		x = np.array(data.values('metreKare','odaSayisi')) 	
		## X degişkenimize columnlardan metrekare ve odasayisini verip bunu np.array biciminde veriyoruz.
		y = np.array(data.values('fiyat')) ## Y degiskenimizede tahmin edecegimiz column u veriyoruz.
		x = pd.DataFrame.from_records(x)  ##Verileri eksiksiz ve düzgün okumak icin pandas kullanıyoruz.
		y = pd.DataFrame.from_records(y)
		
		reg = LinearRegression()   ## sklearn kütüphanesini kullanak LinearRegression Methodunu kullaniyoruz.
		reg.fit(x,y) ## x ve y degiskenlerimizi grafige oturtuyoruz.
		x_new = [[metreKare,odaSayisi]]  ## tahmin edilecek bilgileri alıyoruz.
		x_new = np.array(x_new)
		df1_new= pd.DataFrame(x_new,columns=['metreKare','odaSayisi'])
		tahmin = reg.predict(df1_new)  ## linearregressionun metodunu kullanarak predict metodu ile tahmin ediyoruz.
		tahmin = int(tahmin)
			
		return Response({tahmin})

class Hata(APIView):

	def get(self, request):
		return Response({'status':'error'})
