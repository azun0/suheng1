from django.shortcuts import redirect, render

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.base import View
from django.http import HttpResponseForbidden, HttpResponseRedirect
from urllib.parse import urlparse

from .models import Photo

class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'

class PhotoCreate(CreateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_create'
    success_url='/'

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_update'
    success_url='/'

class PhotoDelete(DeleteView):
    model = Photo

    template_name_suffix = '_delete'
    success_url='/'

class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'

class PhotoLike(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user
                if user in photo.like.all():
                    photo.like.remove(user)
                else:
                    photo.like.add(user)
            referer_url = request.META.get('HTTP-REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)

class PhotoFavorite(View) :
    def get(self, request, *args, **kwargs) :
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user
                if user in photo.favorite.all():
                    photo.favorite.remove(user)
                else:
                    photo.favorite.add(user)
            return HttpResponseRedirect('/')


def form_valid(self,form):
    form.instance.author_id = self.request.user.id
    if form.is_valid():
        form.instance.save()
        return redirect('/')
    else:
        return self.render_to_response({'form':form})