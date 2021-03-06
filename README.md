# RACCY-ORM

### OVERVIEW

Raccy-ORM is a small lightweight ORM, inspired by Django-ORM.

### REQUIREMENTS

- Python 3.7+
- Works on Linux, Windows, and Mac

### INSTALL

```shell script
pip install raccy-orm
```

### EXAMPLE

```python
from datetime import datetime as dt
import ro as model

config = model.Config()
config.DATABASE = model.SQLiteDatabase(':memory:')


class Author(model.Model):
    author_id = model.PrimaryKeyField()
    name = model.CharField(max_length=75)
    age = model.IntegerField()
    lucky_number = model.IntegerField(default=90)
    salary = model.FloatField(default=50000)
    date = model.DateField()
    datetime = model.DateTimeField()
    adult = model.BooleanField(default=False)


class Post(model.Model):
    author_id = model.ForeignKeyField(Author, 'author_id')
    post = model.TextField(null=False)


Author.objects.bulk_insert(
    dict(name='Kwame', age=45, date=dt.now().date(), datetime=dt.now(), lucky_number=99, salary=6400),
    dict(name='Yaw', age=32, date=dt.now().date(), datetime=dt.now(), lucky_number=56, salary=6400),
    dict(name='Fiifi', age=23, date=dt.now().date(), datetime=dt.now(), lucky_number=34),
    dict(name='Navas', age=21, date=dt.now().date(), datetime=dt.now()),
    dict(name='Jesus', age=34, date=dt.now().date(), datetime=dt.now(), salary=6400, adult=True)
)
Post.objects.insert(post="This is Kojo's post", author_id=1)
Post.objects.insert(post="This is Kwabena's post", author_id=2)
Post.objects.insert(post="This is Baffour's post", author_id=3)
Post.objects.insert(post="This is Derrick's post", author_id=1)


for d in Author.objects.all():
    print(d.pk, d.name)
```

```shell script
1 Kwame
2 Yaw
3 Fiifi
4 Navas
5 Jesus
```