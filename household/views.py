from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Family, Membership
from .forms import FamilyCreationForm

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
    if request.method=='POST':
        family_form = FamilyCreationForm(request.POST)
        if family_form.is_valid():
            new_family = family_form.save()
            user = request.user.profile
            new_family.members.add(user, through_defaults={'command_level':2})
            return render(request, "household/register_done.html",
                                  {'new_family':new_family})
    else:
        family_form = FamilyCreationForm()
    return render(request, "household/register.html",
                          {'family_form':family_form})
