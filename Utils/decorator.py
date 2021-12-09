from django.shortcuts import redirect, render

def login_required(view):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/auth/signin/?status=403')
        return view(request, *args, **kwargs)
    return wrapper