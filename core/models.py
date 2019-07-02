from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Habit(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    daily_goal = models.PositiveIntegerField()
    started_on = models.DateField(auto_now_add=True)


class DailyRecord(models.Model):
    habit = models.ForeignKey(to=Habit, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['habit', 'date'], name="habit_date")
        ]
