from django.shortcuts import render
from uploadpic.models import IMG
from media.upload.pj import pinjie
from django.http import HttpResponse
# Create your views here.


def upload(request):
    return render(request, 'upload.html')


def show(request):
    new_img_1 = IMG(img=request.FILES.get('img1'))
    new_img_1.save()
    new_img_2 = IMG(img=request.FILES.get('img2'))
    new_img_2.save()

    s = pinjie()
    return HttpResponse(s.getvalue(), content_type='image/png')

