from django.db import models

# Create your models here.
class Menu(models.Model):
    f_name = models.TextField(null="true")
    f_sort = models.TextField(null="true")
    f_modify_time = models.DateTimeField(auto_now=True)
    f_post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tb_menu"

