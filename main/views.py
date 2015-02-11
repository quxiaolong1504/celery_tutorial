# encoding:utf-8

from django.http import HttpResponse
from django.views.generic import View

from main.tasks import _do_kground_work

class Hello(View):

    def get(self, request, *args, **kwargs):
        _do_kground_work.delay('GreenPine')
        return HttpResponse('Hello, World!')


