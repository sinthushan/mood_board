from django.db import models
from creator.models import Creator
from board.models import Board


class Gallery(models.Model):
    # an instance of this model should be created when a new creator is created
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE, related_name="gallery")

class Inspo(models.Model):
    gallery_ID =  models.ForeignKey(Gallery, on_delete=models.CASCADE)
    board_ID =  models.ForeignKey(Board, on_delete=models.CASCADE, blank=True, null=True)
    image_url = models.URLField()
    column_coordinate = models.IntegerField()
    row_coordiantes = models.IntegerField()
    column_length = models.IntegerField()
    row_length = models.IntegerField()
