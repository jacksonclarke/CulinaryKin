from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from user_profile.models import Profile

# Create your views here.
def home(request):
    return render(request, "core/home.html", {"title": "Home"})


def temp(request):
    return render(request, "core/temp.html", {"title": "Sorry!"})


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentails
            auth.login(request, user)
            messages.success(request, "Login Successful. Welcome Back!")
            return redirect("core:temp")
        else:
            # Not able to authenticate
            messages.error(request, "Invalid Credentails. Please try again.")
            # print("Invalid Credentails. Please try again.")
            return redirect("core:signin")
    return render(request, "core/signin.html", {"title": "Signin"})


def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:  # Check if passwords match.
            if User.objects.filter(
                email=email
            ).exists():  # Check if email is already registered
                messages.warning(
                    request, "Email already in use, Please try signing in!"
                )
                # print("Email already in use, Please try signing in!")
                return redirect("core:signin")
            elif User.objects.filter(
                username=username
            ).exists():  # Check if username is taken
                messages.warning(request, "Username already taken!")
                # print("Username already taken!")
                return redirect("core:signup")
            else:  
                # Create the user
                new_user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )
                new_user.save()
                # Log the user in using the given credentails.
                user_credentails = auth.authenticate(
                    username=username, password=password
                )
                auth.login(request, user_credentails)
                
                # Create Profile for new user
                get_new_user = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=get_new_user)
                new_profile.save()

                # Redirect User
                messages.success(request, "Account created Successfully! Welcome!")
                # print(f"Account created Successfully! Welcome {first_name}!")
                return redirect("core:temp")
        else:
            messages.error(request, "Passwords don't match!")
            print("Passwords don't match")
            return redirect("core:signup")
    return render(request, "core/signup.html", {"title": "Signup"})


def signout(request):
    auth.logout(request)
    messages.success(request, "Logout Successful! Have a great day!")
    print("Logout Successful!")
    return redirect("core:signin")
