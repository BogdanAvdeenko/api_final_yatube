from django.contrib.auth import get_user_model
from django.db import models

FIRST_SYMBOLS_OF_POST = 15

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Группа', max_length=200)
    slug = models.SlugField('Адрес', unique=True)
    description = models.TextField('Описание',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Post(models.Model):
    text = models.TextField('Текст поста',)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    image = models.ImageField(
        'Картинка', upload_to='posts/', null=True, blank=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name='Группа',
        blank=True, null=True
    )

    def __str__(self):
        return self.text[:FIRST_SYMBOLS_OF_POST]

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментируемый пост'
    )
    text = models.TextField('Текст комментария',)
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        return '"{}" to post "{}" by author "{}"'.format(
            self.text, self.post, self.author
        )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор на которого подписываются'
    )

    def __str__(self):
        return '{} follows {}'.format(self.user, self.following)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_subscribers'
            )
        ]
