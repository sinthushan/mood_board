from django.db import models
from creator.models import Creator



class Board(models.Model):
    # we wont be setting a primary key as django will automatically 
    # create an ID field and set it as the primary key
    board_name = models.CharField(max_length=250)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    board_height_px = models.IntegerField()
    board_width_px = models.IntegerField() 
    number_of_columns = models.IntegerField()
    number_of_rows = models.IntegerField()




    