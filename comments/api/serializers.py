from rest_framework.serializers import ModelSerializer
from comments.models import Comment


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment', 'date_and_hour', 'approved',)
