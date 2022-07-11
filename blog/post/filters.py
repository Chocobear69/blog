import django_filters

from post.models import Post


class PostFilters(django_filters.FilterSet):
    is_hidden = django_filters.BooleanFilter(field_name="is_hidden")
    author = django_filters.NumberFilter(field_name="author")
    title = django_filters.CharFilter(method="search_by_title")

    def search_by_title(self, queryset, name, value):
        return Post.object.filter(title=value)

    class Meta:
        model = Post
        fields = ["author", "is_hidden", "title"]
