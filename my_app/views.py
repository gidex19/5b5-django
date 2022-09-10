from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from .models import Message
# Create your views here.


def home(request):

    return render(request, 'my_app/home.html')


def greet(request):
    greeting = ''
    #get current time
    ctime = datetime.now()
    # get current hour and convert to integer 
    hour = int(ctime.strftime("%H"))
    if hour >0 and hour < 12:
        greeting = 'Good Morning'
    elif hour >=12 and hour <= 16:
        greeting = 'Good Afternoon'
    else:
        greeting = 'Good Evening'        
    #context is a dictionary that holds the value to be sent to the frontend    
    context = {'the_greeting': greeting}
    #add context as the third argument of the render function to pass it to the frontend
    return render(request, 'my_app/greet.html', context )


