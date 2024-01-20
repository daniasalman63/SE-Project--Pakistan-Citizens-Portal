from django.db import models

class Candidate(models.Model):
    product_id=models.AutoField
    candidate_name=models.CharField(max_length=50)
    number_of_votes=models.IntegerField()

    def __str__(self):
        return self.candidate_name
