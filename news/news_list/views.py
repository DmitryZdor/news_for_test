from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404

from news_list.models import News
from .serializers import NewsSerializer


def index(request):
    news = News.objects.all()
    template = 'news_list/index.html'
    title = 'NEWS'
    return render(request, template, context={'news': news,
                                                  'title': title, })


@api_view(['GET', 'POST'])
def news_list(request):
    if request.method == 'POST':
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def news_detail(request, pk):
    new = get_object_or_404(News, pk=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = NewsSerializer(new, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = NewsSerializer(new)
    return Response(serializer.data)