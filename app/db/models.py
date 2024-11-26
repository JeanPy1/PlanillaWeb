from tortoise import fields
from tortoise.models import	 Model

class Users(Model):
    
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    
    class Meta:
        table = "users"
        
    def __str__(self):
        return self.name
    