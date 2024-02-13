from rest_framework import viewsets
from .models import Item, Category, Tag
from .serializers import ItemSerializer, CategorySerializer, TagSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ItemFilter
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.http import HttpResponse
import markdown
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
import os


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilter
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

class ObtainAuthToken(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'message': 'Authentication failed'}, status=400)
    
class ReadmeView(View):
    def get(self, request, *args, **kwargs):
        readme_path = os.path.join(settings.BASE_DIR, 'README.md')
        with open(readme_path, 'r') as readme_file:
            readme_content = readme_file.read()
        html_content = markdown.markdown(readme_content)
        return HttpResponse(html_content)
    


