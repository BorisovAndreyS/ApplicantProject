from django.db import models


# Create your models here.
# Абитуриент, его модель надо будет еще добавить Статус
class Applicant(models.Model):
    STATUS_CHOICES = [

        ('new', 'Новый'),

        ('in_progress', 'В процессе'),

        ('accepted', 'Зачислен'),

        ('rejected', 'Отклонено'),

    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    contact_phone = models.IntegerField(null=True)
    contact_email = models.EmailField(null=True)
    address = models.TextField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['first_name', 'last_name', 'middle_name', 'birth_date'] #Пробуем запретить дубли Физ Лиц



# Модель образовательной программы

class Programm(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField()
    description = models.TextField(default=None)
    budget_seats = models.IntegerField()
    paid_seats = models.IntegerField()


# Модель заявлений

class Applications(models.Model):
    STATUS_CHOICES = [

        ('submitted', 'Подано'),

        ('in_review', 'В рассмотрении'),

        ('accepted', 'Принято'),

        ('rejected', 'Отклонено'),

    ]
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    programm_id = models.ForeignKey(Programm, on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now=True)  # Дата подачи заявления
    updated_at = models.DateTimeField(auto_now=True)  # Дата обновления
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    # Подумать куда лучше добавить оценки за экзамены


class ExamResult(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=255)
    score = models.PositiveIntegerField()
    exam_date = models.DateField()
