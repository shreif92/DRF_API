# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404, render
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import  ModelViewSet
# from rest_framework import status
from .serializers import *
from .models import *
from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filter import *
from rest_framework.pagination import PageNumberPagination



# ------------------==>>function based view<<==--------------------
# @api_view(['GET','POST'])
# # def books_api(request):
#     if request.method == 'GET':
#         books =  Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#     elif  request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     return Response(serializer.data)


# # @api_view(['GET','PUT','DELETE'])
# def book_api(request, pk):
    # book_id = get_object_or_404(Book,id=pk)
    # if  request.method == 'GET':
    #     serializer = BookSerializer(book_id)
    #     return Response(serializer.data)
    # elif request.method == 'PUT':
    #     serializer = BookSerializer(book_id,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    # elif  request.method == 'DELETE':
    #     book_id.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PUT', 'DELETE'])
# def book_api(request, pk):
    # book_id = get_object_or_404(Book, id=pk)

    # if request.method == 'GET':
    #     serializer = BookSerializer(book_id)
    #     return Response(serializer.data)

    # elif request.method == 'PUT':
    #     try:
    #         serializer = BookSerializer(book_id, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # elif request.method == 'DELETE':
    #     book_id.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------
# @api_view(['GET','POST'])
# def categorys_api(request):
#     if request.method == 'GET':
#         categorys =  Category.objects.all()
#         serializer = Categoryserializers(categorys, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = Categoryserializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     return Response(serializer.data)

# # @api_view(['GET','PUT','DELETE'])
# def category_api(request, pk):
    # categorys_id = get_object_or_404(Category,id=pk)
    # if request.method == 'GET':
    #     serializer = Categoryserializers(categorys_id)
    #     return Response(serializer.data)
    # elif request.method == 'PUT':
    #     serializer = Categoryserializers(categorys_id, data=request.data)
    #     if  serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    # elif request.method == 'DELETE':
    #     categorys_id.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# # ---------------------==>> class based view <<==--------------------

# # class ApiBooks(APIView):
# #     def  get(self, request):
# #         books =  Book.objects.all()
# #         serializer = BookSerializer(books, many=True)
# #         return Response(serializer.data)
# #     def  post(self, request):
# #         serializer = BookSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
        

# # class ApiBook(APIView):
# #     def get(self, request, pk):
# #         book_id = get_object_or_404(Book, id=pk)
# #         serializer = BookSerializer(book_id)
# #         return Response(serializer.data)
# #     def  put(self, request, pk):
# #         book_id = get_object_or_404(Book, id=pk)
# #         serializer = BookSerializer(book_id, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #     def delete(self, request, pk):
# #         book_id = get_object_or_404(Book, id=pk)
# #         book_id.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)


# # class ApiCategorys(APIView):
# #     def get(self,request):
# #         categorys =  Category.objects.all()
# #         serializer = Categoryserializers(categorys, many=True)
# #         return Response(serializer.data)
# #     def  post(self, request):
# #         serializer = Categoryserializers(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)


# # class ApiCategory(APIView):
# #     def get (self, request, pk):
# #         categorys_id = get_object_or_404(Category, id=pk)
# #         serializer = Categoryserializers(categorys_id)
# #         return Response(serializer.data)
# #     def   put(self, request, pk):
# #         categorys_id = get_object_or_404(Category, id=pk)
# #         serializer = Categoryserializers(categorys_id, data=request.data)
# #         if  serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
        
# #     def  delete(self, request, pk):
# #         categorys_id = get_object_or_404(Category, id=pk)
# #         categorys_id.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)


# # --------------------==>> generics based view <<==--------------------

# # class ApiBooks(ListCreateAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer


# # class ApiBook(RetrieveUpdateDestroyAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer


# # class ApiCategorys(ListCreateAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer


# # class ApiCategory(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = Categoryserializers




# -----------------------==>> viewsets <<==-----------------------
class Booksviewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_class = BooksFilter
    filterset_fields = ['category', 'published_date','available','title']
    search_fields = ['title']
    ordering_fields = ['published_date']
    pagination_class = PageNumberPagination


class CategorysViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categoryserializers