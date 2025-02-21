from django.db import models


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.username 
    
    def as_dict(self):
        return {
            "id": self.id,
            "username": self.username,
        }
    
class Leaderboard(models.Model):
    user=models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.user.username} - {self.score}'

    def as_dict(self):
        return{
            "id": self.id,
            "user": self.user.username,
            "score": self.score,
        }