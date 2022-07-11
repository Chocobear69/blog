from rest_framework.generics import ListAPIView

from post.models import Post
from post.serializers import PostSerializer


class ListPostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return super(ListPostView, self).get(request, args, kwargs)
