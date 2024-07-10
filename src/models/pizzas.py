from models import AWS_REGION
from pynamodb.models import Model
from pynamodb.attributes import (UnicodeAttribute, NumberAttribute, ListAttribute, BooleanAttribute)


class Pizza(Model):

    """
    A pizza model
    """

    class Meta:
        table_name = 'pizzas'
        region = AWS_REGION

    pizza_id = NumberAttribute(hash_key=True)
    name = UnicodeAttribute()
    price = NumberAttribute(range_key=True)
    size = NumberAttribute()
    toppings = ListAttribute(null=True)
    available = BooleanAttribute(default=False)
