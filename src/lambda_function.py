from commons.utils import get_current_ts, get_today_date
from services.response_service import Response
from commons.pos_exception import POSValidationException
from services.order_service import OrderService


ORDER_SERVICE = OrderService


def place_order(info: list) -> dict:
    order_date = get_today_date()
    order_id = ORDER_SERVICE().place_order(
        order_date=order_date,
        order_info=[info]
    )
    return Response(
        status_code=200,
        message='Order accepted',
        meta={
            'id': order_id,
            'date': order_date
        }
    ).get_response()


def complete_order():
    pass


def lambda_handler(event: dict, context: dict) -> dict:

    try:
        action_map = {
            'order': place_order,
            'produce': complete_order
        }
        event_type = event.get('event_type')
        if event_type.lower() not in action_map.keys():
            raise POSValidationException(
                message='Unsupported event type')
        event_meta = event.get('meta')
        processor = action_map.get(event_type)
        response = processor(event_meta)
    except POSValidationException as e:
        return Response(
            status_code=e.code,
            message=e.message
        ).get_response()
    except Exception as e:
        return Response(
            status_code=500,
            message=repr(e)
        ).get_response()
    return response


event = {
    'event_type': "order",
    'meta': [
        "5 Here is an order description"
    ]
}

lambda_handler(event=event, context={})
