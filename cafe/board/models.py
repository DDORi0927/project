from django.db import models
from django.utils import timezone

class Board(models.Model):
    CATEGORY_CHOICES = [("free", "자유"), ("question", "문의"),]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="free")
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    writer = models.CharField(max_length=30)
    date_create = models.DateTimeField(default=timezone.now)
    data_update = models.DateTimeField(default=timezone.now)
    status_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Reply(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    writer = models.CharField(max_length=30)
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(default=timezone.now)
    status_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.content

class Good(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    writer = models.CharField(max_length=30)
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.writer