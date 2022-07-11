from rest_framework.generics import ListCreateAPIView

from post.models import Post
from post.serializers import PostSerializer
from customer.permissions import ReadOnlyPermission
from post.paginators import StandardPaginator
from post.filters import PostFilters


class ListPostView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [ReadOnlyPermission]
    pagination_class = StandardPaginator
    filter = PostFilters
