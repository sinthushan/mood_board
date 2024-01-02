from django.db import models
from creator.models import Creator
from board.models import Board


class Gallery(models.Model):
    # an instance of this model should be created when a new creator is created
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE, related_name="gallery")

    def upload_img(self, file):
        with open(f"media/{file.name}", 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        new_img = Inspo(gallery_ID = self, image_url = f'media/{file.name}')
        new_img.save()

class Inspo(models.Model):
    gallery_ID =  models.ForeignKey(Gallery, on_delete=models.CASCADE)
    board_ID =  models.ForeignKey(Board, on_delete=models.CASCADE, blank=True, null=True)
    image_url = models.URLField()
    column_coordinate = models.IntegerField(blank=True, null=True)
    row_coordiantes = models.IntegerField(blank=True, null=True)
    column_length = models.IntegerField(blank=True, null=True)
    row_length = models.IntegerField(blank=True, null=True)
