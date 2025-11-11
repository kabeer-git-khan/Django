from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'id': 1,
        'title': 'Explore Python',
        'content': 'Python is a versatile programming language that can be used for web development, data science, and artificial intelligence.',
    },
    {
        'id': 2,
        'title': 'Explore Django',
        'content': 'Django is a web framework for building web applications using Python.',
    },
    {
        'id': 3,
        'title': 'Explore JavaScript',
        'content': 'JavaScript is a programming language that can be used for web development.',
    },
]


def home(request):
    html = ""
    for post in posts:
        html += f"""
        <div>
            <h1>{post['id']} - {post['title']}</h1>
            <p>{post['content']}</p>
        </div>
        """
    return HttpResponse(html)

def post(request, id):
    return HttpResponse(f"Post {id}")