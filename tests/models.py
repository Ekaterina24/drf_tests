from django.contrib.auth.models import User
from django.db import models
# from django.contrib.auth import get_user_model


class Answer(models.Model):
    text = models.CharField(verbose_name='Текст ответа', max_length=100)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Question(models.Model):
    text = models.CharField(verbose_name='Текст вопроса', max_length=100)
    answer = models.ManyToManyField(Answer, verbose_name='Ответы', default='')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Test(models.Model):
    title = models.CharField(verbose_name='Название теста', max_length=100)
    questions = models.ManyToManyField(
        Question, verbose_name='Вопросы', default='')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_tests')
    readers = models.ManyToManyField(User, through='UserTestRelation', related_name='tests')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Category(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=100)
    description = models.TextField(verbose_name='Описание категории')
    test = models.ManyToManyField(Test, verbose_name='Тесты', default='')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class UserTestRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'{self.user.username}: {self.test.title}, RATE {self.rate}'


# class UserAnswers(models.Model):
#     user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
#     test = models.ForeignKey(Test, verbose_name='Тест', on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE)
#     answer = models.ForeignKey(Answer, verbose_name='Ответ', on_delete=models.CASCADE)


# class Feedback(models.Model):
#     user = models.CharField(verbose_name='Имя', max_length=100)
#     text = models.TextField(verbose_name='Текст отзыва', blank=True)
#
#     def __str__(self):
#         return f'{self.user}'
#
#     class Meta:
#         verbose_name = 'Отзыв'
#         verbose_name_plural = 'Отзывы'
