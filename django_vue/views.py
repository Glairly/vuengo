from django.http import JsonResponse
from django.shortcuts import render
import torchvision
import torchvision.transforms as transforms
from PIL import Image

def index(request):
    return render(request, template_name='index.html')


def simple_api_view(request):
    response = JsonResponse({
        'data': [
            'You get an phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
        ]
    })
    return response

def shakehand(request):
    return JsonResponse({
        'data' : "Hi !! I'm Glairly 😀"
    })

