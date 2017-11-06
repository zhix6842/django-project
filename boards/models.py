from django.db import models

# Create your models here.
class Board(models.Model):
    f_name = models.TextField(null="false")
    f_content = models.TextField(null="false")
    f_email =  models.TextField(null="false")
    f_modify_time = models.DateTimeField(auto_now=True)
    f_post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tb_board"