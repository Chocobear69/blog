from rest_framework.serializers import ModelSerializer

from post.models import Post
from customer.models import Customer


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def validate(self, attrs):
        customer = Customer.objects.first()
        attrs["author"] = customer
        return attrs
