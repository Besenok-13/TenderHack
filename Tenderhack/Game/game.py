class Gamer:
    def __init__(self, min_cost, products):
        self.min_cost = min_cost
        self.products = products

    def check(self, cost):
        if self.min_cost > cost:
            return False
        return True

    def action_out(self):
        return False

    def action_low(self):
        return True


def game(
    gamers: list[Gamer], cost: float,
):
    to_dell = []
    for i, gamer in enumerate(gamers):
        if gamer.check():
            to_dell.append(i)

    for i in to_dell:
        gamers.pop(i)
