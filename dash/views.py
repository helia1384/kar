from django.shortcuts import render

def index(request):
    return render(request, 'dash/index.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def edit_profile(request):
    return render(request, 'accounts/edit_profile.html')
