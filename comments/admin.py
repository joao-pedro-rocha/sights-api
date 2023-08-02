from django.contrib import admin
from .models import Comment
from .actions import disapprove_comment, approve_comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'approved']
    # Actions personalizados para o admin
    actions = [disapprove_comment, approve_comment]
    list_editable = ['approved']


admin.site.register(Comment, CommentAdmin)
