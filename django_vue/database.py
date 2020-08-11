from django.http import JsonResponse
from django.shortcuts import render
from django.db import models

class Images(models.Model):
    name  = models.CharField(max_length=200)
    