from rest_framework.viewsets import ModelViewSet
from api.serializers import PostSerializer
from posts.models import Post

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()