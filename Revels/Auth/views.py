# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
# Create your views here.

class SignUp(View):
    def get(self, request):
        return render(request,'Auth/signup.html')
