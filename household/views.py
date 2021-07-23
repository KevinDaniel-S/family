from django.shortcuts import render
from .models import Family, Membership
from django.contrib.auth.decorators import login_required

def family(request) -> render:
    user = request.user
    if user.is_authenticated:
        families = user.profile.family_set.all()
        return render(request, "family.html", 
                      {"families":families})
    else:
        return render(request, "webapp_info.html")

@login_required
def register(request) -> render:
    return render()
