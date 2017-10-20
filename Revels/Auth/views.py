# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from Auth.user import UserManager
import datetime
from ORM.sessions import SessionsManager

# Create your views here.

class SignUp(View):

    def get(self, request):
        return render(request,'Auth/signup.html')

    def post(self, request):

        data = {
            'firstname' : request.POST['firstname'].strip(),
            'lastname' : request.POST['lastname'].strip(),
            'password' : request.POST['password'].strip(),
            'email' : request.POST['email'].strip(),
            'username' : request.POST['username'].strip(),
            'gender' : request.POST['gender'].strip(),
        }
        userm = UserManager()
        errors = userm.validate(data)
        if(len(errors) == 0) :
            userm.createUser(data)
            return JsonResponse(data)
        else :
            var = {
                'errors' : errors,
                'data' : data
            }
            print(var)
            return render(request,'Auth/signup.html',var)

class SignIn(View):

    def get(self, request):
        return render(request,'Auth/signin.html')

    def post(self, request):

        data = {
            'password' : request.POST['password'].strip(),
            'username' : request.POST['username'].strip(),
        }
        userm = UserManager()
        userm.signInUser(data)
        response = JsonResponse(data)
        sessionM = ORM.sessions.SessionsManager()
        session_id = sessionM.createSession(data)
        response.set_cookie('session', session_id)
        return response
