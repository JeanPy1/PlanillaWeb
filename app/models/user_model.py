from tortoise import fields
from tortoise.models import Model


class UserModel(Model):

    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=40)
    email = fields.CharField(max_length=50, unique=True)
    username = fields.CharField(max_length=10, unique=True)
    password = fields.CharField(max_length=10)
    created_at = fields.DateField(auto_now_add=True)

    class Meta:
        table = "user"

    def __str__(self):
        return self.name
