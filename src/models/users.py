from models import AWS_REGION
from pynamodb.models import Model
from pynamodb.attributes import (UnicodeAttribute, NumberAttribute,
                                 ListAttribute, BooleanAttribute)


class User(Model):

    """
    The user model
    """

    class Meta:
        table_name = 'users'
        region = AWS_REGION

    user_id = NumberAttribute(hash_key=True)
    first_name = UnicodeAttribute()
    second_name = UnicodeAttribute()
    role = UnicodeAttribute(null=True)
    created = NumberAttribute(range_key=True)
    order_history = ListAttribute(null=True)
    deleted = BooleanAttribute(default=False)
