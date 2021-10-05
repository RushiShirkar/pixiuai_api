from rest_framework import generics
from .serializers import IdeaSerializer
from .models import Idea

class IdeaCreate(generics.ListCreateAPIView):
    serializer_class = IdeaSerializer
    queryset = Idea.objects.all()

class IdeaDelete(generics.DestroyAPIView):
    serializer_class = IdeaSerializer
    queryset = Idea.objects.all()

class IdeaUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = IdeaSerializer
    queryset = Idea.objects.all()

class IdeaView(generics.ListAPIView):
    serializer_class = IdeaSerializer
    pagination_class = None
    queryset = Idea.objects.all()