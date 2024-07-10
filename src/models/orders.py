from models import AWS_REGION
from pynamodb.models import Model
from pynamodb.attributes import (NumberAttribute, ListAttribute, BooleanAttribute,
                                 UnicodeAttribute)
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection


class OrderDateIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = 'order-date-index'
        projection = AllProjection()

    order_date = UnicodeAttribute(hash_key=True)
    order_ts = NumberAttribute(range_key=True)


class Order(Model):

    """
    An order model
    """

    class Meta:
        table_name = 'orders'
        region = AWS_REGION

    order_id = NumberAttribute(hash_key=True)
    order_date = UnicodeAttribute()
    order_ts = NumberAttribute()
    order_info = ListAttribute()
    ready = BooleanAttribute(default=False)
    issued = BooleanAttribute(default=False)

    order_date_index = OrderDateIndex()
