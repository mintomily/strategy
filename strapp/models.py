from django.db import models

from account.models import CustomUser

class Bulletin(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )

    text = models.TextField(
        verbose_name='コメント'
    )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    def __str__ (self):
        return self.user

class Characters(models.Model):
    CATEGORY = (('millennium', 'ミレニアム'),
                ('trinity', 'トリニティ'),
                ('gehenna', 'ゲヘナ'),
                ('abydos', 'アビドス'),
                ('hyakki', '百鬼夜行'),
                ('redwinter', 'レッドウィンター'),
                ('valkyrie', 'ヴァルキューレ'),
                ('srt', 'SRT'),
                ('sengaikyo', '山海経'),
                ('arius', 'アリウス'))

    category = models.CharField(
        verbose_name='学園',
        max_length=50,
        choices = CATEGORY
    )

    name = models.CharField(
        verbose_name='名前',
        max_length=200
    )

    image = models.ImageField(
        verbose_name='立ち絵',
        upload_to = 'photos'
    )

    age = models.IntegerField(
        verbose_name='年齢',
        null=True,
        blank=True
    )
    
    birthday = models.DateField(
        verbose_name='誕生日'
    )

    height = models.IntegerField(
        verbose_name='身長'
    )
    
    hobby = models.CharField(
        verbose_name='趣味',
        max_length=50
    )

    voice = models.CharField(
        verbose_name='CV',
        max_length=20
    )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    def __str__ (self):
        return self.name