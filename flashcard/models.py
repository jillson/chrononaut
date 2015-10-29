from django.db import models
import flashcard.dsl
import random

class CardGenerator(models.Model):
    Level = models.IntegerField(default=1)
    Name = models.CharField(max_length=100)
    Formula = models.TextField()
    Question = models.TextField()
    def __unicode__(self):
        return self.Name
    def get_json(self):
        dd = dsl.build_vars(self.Formula)
        question = self.Question % dd
        return { "level": self.Level,
                 "question": question,
                 "correctAnswer": dd["correct"],
                 "wrongAnswer1": dd["wrong1"],
                 "wrongAnswer2": dd["wrong2"],
                 "wrongAnswer3": dd["wrong3"] }


