from django.db import models


class Teachers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Teachers'


class Tests(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    creator_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Tests'


class Library(models.Model):
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Tests, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Library'


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    test_id = models.ForeignKey(Tests, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Questions'


class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    is_correct = models.BooleanField()
    question_id = models.ForeignKey("Questions", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Answers'


class Students(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    session_id = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Students'