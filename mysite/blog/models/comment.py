from django.db import models

from blog.models import Post

class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=88)
    email = models. EmailField()
    body = models.TextField()
    created_on  = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["created_on"]
    
    def str_(self):
        return "Comment {} by {}".format(self.body, self.name)  