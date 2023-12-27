from django.db import models
from creator.models import Creator



class Gallery(models.Model):
    # an instance of this model should be created when a new creator is created
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE, related_name="gallery")

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


class Inspo(models.Model):
    gallery_ID =  models.ForeignKey(Gallery, on_delete=models.CASCADE)
    board_ID =  models.ForeignKey(Board, on_delete=models.CASCADE, blank=True, null=True)
    image_url = models.URLField()
    column_coordinate = models.IntegerField()
    row_coordiantes = models.IntegerField()
    column_length = models.IntegerField()
    row_length = models.IntegerField()

    