from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Habit(models.Model):
    owner = models.ForeignKey(to=User,
                              on_delete=models.CASCADE,
                              related_name="habits")
    verb = models.CharField(max_length=255)
    noun = models.CharField(max_length=255)
    daily_goal = models.PositiveIntegerField()
    started_on = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['verb', 'noun'], name="verb_noun")
        ]

    def __str__(self):
        if not (self.verb and self.noun and self.daily_goal):
            return super().__str__()

        return f"{self.verb} {self.daily_goal} {self.noun}"


class DailyRecord(models.Model):
    habit = models.ForeignKey(to=Habit,
                              on_delete=models.CASCADE,
                              related_name="daily_records")
    date = models.DateField()
    quantity = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['habit', 'date'], name="habit_date")
        ]
