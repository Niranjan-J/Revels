# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from ORM.user import User
import datetime
from ORM.sessions import SessionsManager

# Create your views here.

class SignUp(View):

    def get(self, request):
        return render(request,'Auth/signup.html')

    def post(self, request):
        user = User()
        data = {
            'firstname' : request.POST['firstname'].strip(),
            'lastname' : request.POST['lastname'].strip(),
            'password' : request.POST['password'].strip(),
            'email' : request.POST['email'].strip(),
            'username' : request.POST['username'].strip(),
            'gender' : request.POST['gender'].strip(),
        }

        res = user.createUser(data)

        if res == None :
            return JsonResponse(data)
        else :
            var = {
                'error' : res,
                'data' : data
            }
            return render(request,'Auth/signup.html',var)

class SignIn(View):

    def get(self, request):
        return render(request,'Auth/signin.html')

    def post(self, request):

        data = {
            'password' : request.POST['password'].strip(),
            'email' : request.POST['email'].strip(),
        }

        response = JsonResponse(data)
        sessionM = SessionsManager()

        response = sessionM.createSession(data,response)

        if response != None :
            return response
        else :
            var = {
                'error' : 'res'
            }
            return render(request,'Auth/signin.html',var)

def SignOut(request):
        response =  render(request,'Auth/signin.html')
        try :
            response.delete_cookie('session')
        except :
            pass
        return response

class Home(View):

    def get(self, request):
        sessionM = SessionsManager()
        res = sessionM.checkSession(request)
        if(res != None):
            return JsonResponse("Authenticated",safe=False)
        else :
            return JsonResponse("Not Authenticated",safe=False)
