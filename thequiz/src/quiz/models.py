from django.db import models

class Quiz(models.Model):
    author = models.CharField(("Author"), max_length=50)
    title = models.CharField(("Quiz title"), max_length=250,default="Random quiz")
    date_created = models.DateTimeField(auto_now_add=True)

    QUIZ_LEVELS = {
        "HR" : "HARD",
        "MD" : "INTERMIDATE",
        "EZ" : "EASY"  
              }
    quiz_level = models.CharField(verbose_name="level", max_length=3, choices= QUIZ_LEVELS)

    @property
    def keep_count(self):
        return self.question.count()
    
    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
        ordering = ['id']

    def __str__(self):
        return self.title


class Questions(models.Model):
    quiz =models.ForeignKey(Quiz, related_name = 'question', on_delete = models.CASCADE)
    title = models.CharField( max_length=250,default = "")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['id']

    def __str__(self):
        return self.title
    

class Answer(models.Model):
    question =models.ForeignKey(Questions, related_name = 'answers', on_delete = models.CASCADE)
    answers = models.CharField( max_length=250, null=True, blank=True)
    is_right = models.BooleanField(default=False,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        ordering = ['id']

    def __str__(self):
        return self.answers


