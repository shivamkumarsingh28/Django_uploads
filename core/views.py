from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import HotelForm
from .models import Hotel

def index(request):
    return HttpResponse("Hello world!")
 
def hotel_image_view(request):
 
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'form.html', {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')

def display_hotel_images(request):
 
    if request.method == 'GET':
 
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all()
        return render(request, 'display_image.html', {'hotel_images': Hotels})