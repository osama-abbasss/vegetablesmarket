from django.shortcuts import render, redirect
from accounts.forms import SignUpForm, ProfileForm
from django.contrib.auth import login, authenticate
from accounts.models import Profile



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('accounts:profile')


    else:
        form = SignUpForm()


    template_name = "registration/signup.html"
    context = {'form':form}
    return render(request, template_name, context)



def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return redirect('accounts:signup')
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                try:
                    if request.POST['terms_and_conditions']:
                        profile = form.save(commit=False)
                        profile.terms_and_conditions = True
                        profile.save()
                except:
                    profile = form.save(commit=False)
                    profile.terms_and_conditions = False
                    profile.save()  

                return redirect("/")
        template_name = 'registration/profile.html'
        context = {}
        return render(request, template_name, context)

    else:
        return redirect('accounts:signup')