# Actions para admin que reprovam ou aprovam comentários
def disapprove_comment(modeladmin, request, queryset):
    queryset.update(approved=False)


def approve_comment(modeladmin, request, queryset):
    queryset.update(approved=True)


disapprove_comment.short_description = 'Disapprove comment'
approve_comment.short_description = 'Approve comment'
