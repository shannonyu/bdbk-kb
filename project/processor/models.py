from django.db import models

# every time version number is updated, 
# data migration must be performed
# version: 1

class SimilarNamedEntity(models.Model):
    bdbk_id = models.IntegerField(db_index=True)
    zhwiki_id = models.IntegerField(db_index=True)