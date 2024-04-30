from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model) :
    user                    = models.ForeignKey(User , on_delete = models.CASCADE)
    title                   = models.CharField(max_length = 200 , blank = False , null = False)
    completed               = models.BooleanField(default = False)
    description             = models.TextField(max_length = 500 , blank = True , null = True)
    
    def __str__(self) :
        return f"{self.title[:20]} : {self.completed}"
    
    