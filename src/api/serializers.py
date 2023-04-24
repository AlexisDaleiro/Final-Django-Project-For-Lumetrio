from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'liked']

        def __str__(self):
            return str(self.author)
        
