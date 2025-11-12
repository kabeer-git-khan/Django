from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
            <a href="/posts/{post['id']}/">
            <h1>{post['id']} - {post['title']}</h1></a>
            <p>{post['content']}</p>
        </div>
        """
    return render(request, 'posts/home.html', {"posts": posts})

def post(request, id):
    valid_id = False
    post_dict = None
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        html = f"""
            <div>
                <h1>{post_dict['id']} - {post_dict['title']}</h1>
                <p>{post_dict['content']}</p>
            </div>
        """
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("Post not found")

def google(request, id):
    url = reverse('post', args=[id])
    return HttpResponseRedirect(url)