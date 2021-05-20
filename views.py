from django.shortcuts import render
from . import second

def home(request):
    return render(request , 'index.html')

def result(request):
    user_input = int(request.GET['user_name'])
    prediction = second.fake_prediction(user_input)
    return render(request , 'result.html' , {'home_input':prediction})
