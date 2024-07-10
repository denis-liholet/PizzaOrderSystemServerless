from commons.pos_exception import POSNotFoundException
from commons.utils import get_today_date, get_beginning_of_the_day_ts, get_current_ts
from models.orders import Order
from services.ssm_service import SSMService


class OrderService:

    def __init__(self):
        self._ssm_service = SSMService()

    @staticmethod
    def get_order(order_id: int) -> Order:
        order = Order.get(hash_key=order_id)
        if not order:
            raise POSNotFoundException(
                f"Order with ID {order_id} not found")
        return order

    @staticmethod
    def get_today_orders() -> list:
        # todo add list of orders in typing
        start_ts = get_beginning_of_the_day_ts()
        hk = get_today_date()
        result = Order.order_date_index.query(
            hash_key=hk,
            range_key_condition=Order.order_ts > start_ts)
        return list(result)

    def place_order(self, order_date: str, order_info: list) -> int:
        order_id = self._ssm_service.get_pk_increment()
        new_order = Order()
        new_order.order_id = order_id
        new_order.order_ts = get_current_ts()
        new_order.order_date = order_date
        new_order.order_info = order_info
        new_order.save()
        return order_id

    @staticmethod
    def place_ready_status(order_id: int):
        current_order = Order.get(hash_key=order_id)
        if not current_order:
            raise POSNotFoundException(
                f"Order with ID {order_id} not found")
        current_order.update(actions=[Order.ready.set(True)])

    @staticmethod
    def issue_order(order_id: int):
        current_order = Order.get(hash_key=order_id)
        current_order.update(actions=[Order.issued.set(True)])
