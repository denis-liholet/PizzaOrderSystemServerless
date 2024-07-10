from models.pizzas import Pizza


class PizzaService:

    @staticmethod
    def get_pizza(pizza_id: int):
        return Pizza.get(hash_key=pizza_id)
