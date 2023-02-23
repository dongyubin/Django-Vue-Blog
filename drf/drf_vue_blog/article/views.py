from django.http import JsonResponse,Http404
from article.models import Article
from article.serializers import ArticleListSerializer,ArticleDetailSerializer
from article.permissions import IsAdminUserOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework import status,generics

# Create your views here.
# @api_view(['GET', 'POST'])
# def article_list(request):
#   if request.method == 'GET':
#     article = Article.objects.all()
#     serializer = ArticleListSerializer(article, many=True)
#     return Response(serializer.data)
#   elif request.method == 'POST':
#     serializer = ArticleListSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    

# class ArticleDetail(APIView):
#   def get_object(self, pk):
#     try:
#       return Article.objects.get(pk=pk)
#     except:
#       raise Http404
  
#   def get(self, request, pk):
#     article = self.get_object(pk)
#     serializer = ArticleDetailSerializer(article)
#     return Response(serializer.data)
  
#   def put(self, request, pk):
#     article = self.get_object(pk)
#     serializer = ArticleDetailSerializer(article, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   def delete(self, request, pk):
#     article = self.get_object(pk)
#     article.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    