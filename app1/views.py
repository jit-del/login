from django.shortcuts import render,redirect
from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'app/home.html')

class CustomerRegiistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()#blank form
        return render(request, 'app/customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulation!! Registered Successflly")
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})


class ProfileView(View):
    def get(self,request):
        return render(request, 'app/profile.html',)
