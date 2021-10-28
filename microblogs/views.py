from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.apps import apps
from django.shortcuts import redirect, render
from .forms import LogInForm, SignUpForm, PostForm


def show_user(request, user_id):
    User = get_user_model()
    data = {'user': User.objects.get(id=user_id)}
    return render(request, 'show_user.html', data)


def user_list(request):
    User = get_user_model()
    data = {'user_list': User.objects.all()}
    return render(request, 'user_list.html', data)


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            author = request.user
            if text is not None:
                postFeed = form.save(request.user)
                return redirect('feed')
    form = PostForm()
    return render(request, 'post.html', {'form': form})


def feed(request):
    Feed = apps.get_model('microblogs', 'Post')
    data = {'post_feed': Feed.objects.all()}
    return render(request, 'feed.html', data)


def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed')
        messages.add_message(request, messages.ERROR, "The Credentials provided were invalid!")
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request, 'home.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})
