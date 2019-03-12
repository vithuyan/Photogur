from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import Picture, Comment
from django.urls import path

def pictures_page(request):
    context = {'pictures': Picture.objects.all()}
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)


def picture_show(request, id):
	picture = Picture.objects.get(pk=id)
	context = {'picture': picture}
	return render(request, 'picture.html', context)
