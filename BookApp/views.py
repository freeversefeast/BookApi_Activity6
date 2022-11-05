from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BookApp.models import Books
from BookApp.serializers import BookSerializer
# Create your views here.
@csrf_exempt
def bookApi(request,id=0):
    if request.method=='GET':
        books = Books.objects.all()
        books_serializer=BookSerializer(books,many=True)
        return JsonResponse(books_serializer.data,safe=False)
    elif request.method=='POST':
        book_data = JSONParser().parse(request)
        books_serializer=BookSerializer(data=book_data)
        if books_serializer.is_valid():
           books_serializer.save()   
           return JsonResponse( "Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        book_data=JSONParser().parse(request)
        book=Books.objects.get(BookId=book_data['BookId'])
        books_serializer=BookSerializer(book,data=book_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse( "Updated Successfully",safe=False)
        return JsonResponse( "Failed to Update")
    elif request.method=='DELETE':
        book=Books.objects.get(BookId=id)
        book.delete()
        return JsonResponse("Deleted Successfully",safe=False)
