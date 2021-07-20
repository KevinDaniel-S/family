from django.shortcuts import render
from .models import Family, Membership
from django.contrib.auth.decorators import login_required

@login_required
def family(request) -> render:
    profile = request.user.profile
    
    households = profile.family_set.all()
    if len(households)==0:
        household = None
    else: 
        household = households[0]
    
    return render(request, 'family.html', 
                 {'section':'family', 'family':household})
