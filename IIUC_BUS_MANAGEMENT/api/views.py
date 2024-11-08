
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





@api_view(['GET','POST','PATCH'])
def bus_update(request):
    if request.method == "PATCH":
        try:
                
                body = json.dumps(json.loads(request.body))
                print(body)
                
                database.cur.execute("""
                    select bus_update(%s) ;
                """,(body,))
                #result = json.loads(json.dumps(database.cur.fetchone()[0]))
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





@api_view(['GET','POST'])
def driver_view(request):
    if request.method == "GET":
        try:
            page = request.GET.get("page",1)
            limit = request.GET.get("limit", 5)

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
def search_trip(request):
    if request.method == "GET":
        try:
            page = request.GET.get("page",1)
            limit = request.GET.get("limit", 5)
            driver_id = request.GET.get("driver_id",3)

            database.cur.execute("""
                select search_trip(%s);
            """,(driver_id,))
            # print(database.cur.fetchone()[0])
            result = json.loads(json.dumps(database.cur.fetchone()[0]))
            print(result)
            database.conn.commit()
            return Response({
                "data": result
            }
            )


        except(Exception, database.Error) as error:
            database.conn.commit()
            print(error)
            return Response({"message": "GET called but error", "error": error});

