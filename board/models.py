from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Board(models.Model):
    # we wont be setting a primary key as django will automatically 
    # create an ID field and set it as the primary key
    board_name = models.CharField(max_length=250)
    creator = models.ForeignKey(User, on_delete=models.CASCADE) 
    number_of_columns = models.IntegerField()
    number_of_rows = models.IntegerField()


class Inspo(models.Model):
    board_ID =  models.ForeignKey(Board, on_delete=models.CASCADE)
    image_url = models.URLField()
    column_coordinate = models.IntegerField()
    row_coordiantes = models.IntegerField()
    column_length = models.IntegerField()
    row_length = models.IntegerField()

    