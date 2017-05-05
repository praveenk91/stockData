from django.shortcuts import render
from django.http import HttpResponse
from books.models import Stockdata
import datetime 


def index(request):
	

	stock_data = Stockdata.objects.order_by('-id')[0]
	now = datetime.datetime.now()
	

	#return render(request, 'current_datetime.html', {'stocks':stock_data})
	return render(request, 'current_datetime.html', {'stocks': stock_data , 'Curr_time' : now})


def hello(request):
    return HttpResponse("Hello world")

