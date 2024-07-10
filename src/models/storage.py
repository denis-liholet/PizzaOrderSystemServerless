from models import AWS_REGION
from pynamodb.models import Model
from pynamodb.attributes import (UnicodeAttribute, NumberAttribute, BooleanAttribute)


class Storage(Model):

    """
    A storage model
    """

    class Meta:
        table_name = 'storage'
        region = AWS_REGION

    ingredient_id = NumberAttribute(hash_key=True)
    name = UnicodeAttribute()
    price = NumberAttribute(range_key=True)
    amount = NumberAttribute(default=0)
    available = BooleanAttribute(default=False)
