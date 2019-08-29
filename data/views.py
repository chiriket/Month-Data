from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import requests


# Create your views here.
#........
def index(request):
    title = 'Home'
    date = Date.objects.all()
   
    return render(request, 'index.html', {'title':title})


def date(request):
   url = 'https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.dataur
   response = requests.get(url)

   date = response.json()
    
   return render(request,  'date.html',{
       'search': date'searchedByName')
     
   })

def get_date():
   '''
   Fetches and returns date from api
   '''

   url = 'https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data'
   response = requests.get(url)

   date = response.json()

   return date


    



