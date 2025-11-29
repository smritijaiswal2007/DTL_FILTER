from django.shortcuts import render

# Create your views here.
def landing(req):
    # data = {'name':'rohit','age':'2','city':'bhopal'}
    l = {'smriti','rohit','priyesh','shubh','mom''dad'}
    return render(req,'landing.html')