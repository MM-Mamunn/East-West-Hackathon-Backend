
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from rest_framework import status
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils  import database 
import json
import re
from django.contrib import messages

# Create your views here.

@api_view(['GET','POST'])
def Dashboard(request):
    if request.method == "GET":
        try:
            page = request.GET.get("page",1)
            limit = request.GET.get("limit", 5)

            database.cur.execute("""
                select dashboard(%s, %s);
            """,(page,limit))
            result = json.loads(json.dumps(database.cur.fetchone()[0]))

            database.conn.commit()
            return Response({
                "data": result
            }
            )


        except(Exception, database.Error) as error:
            database.conn.commit()
            print(error)
            return Response({"message": "GET called but error", "error": error});


@api_view(['GET','POST'])
def driver_view(request):
    if request.method == "GET":
        try:
            page = request.GET.get("page",1)
            limit = request.GET.get("limit", 10)

            database.cur.execute("""
                select driver_view(%s, %s);
            """,(page,limit))
            result = json.loads(json.dumps(database.cur.fetchone()[0]))

            database.conn.commit()
            return Response({
                "data": result
            }
            )


        except(Exception, database.Error) as error:
            database.conn.commit()
            print(error)
            return Response({"message": "GET called but error", "error": error});


@api_view(['GET','POST'])
def driver_insert(request):
    if request.method == "GET":
        return Response({'message':"GET method called"})
    elif request.method == "POST":
        try:
            body = json.dumps(json.loads(request.body))
            print(body)
            
            database.cur.execute("""
                select driver_insert(%s) ;
            """,(body,))
            # result = json.loads(json.dumps(database.cur.fetchone()[0]))
            database.conn.commit()
            

            return Response(
                {
                    "message": "success"
                }
            )
        except(Exception, database.Error) as error:
            database.conn.commit()
            print(error)
            return Response({"message": "Post called but error", "error": error});



