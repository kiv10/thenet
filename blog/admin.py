from django.contrib import admin
from blog.models import Post, Comment, Collab


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Collab)

