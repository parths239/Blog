from django.shortcuts import render

posts = [
    {
        'author': 'Parth Sharma',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'Date_Posted': 'August 21, 2024'
    },
    {
        'author': 'Morgan Freeman',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'Date_Posted': 'August 21, 2024'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
