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


class Kot:
    def __init__(self):
        self.current_price = 10000
        self.start_price = 10000
        self.percent = 2
        self.last = 0
        self.steps = 5
        self.isEnded = False

    def low(self, lst):
        self.last = lst
        self.steps -= 1
        self.current_price -= self.start_price * (self.percent / 100)
        print("lowed!", self.current_price, self.steps)
        return self.current_price

    def get_current(self):
        return self.current_price

    def get_last(self):
        return self.last

    def update(self):
        if self.steps < 1:
            self.stop()

    def stop(self):
        self.isEnded = True
        print(self.current_price)
        print(self.last)
        print("ENDED!")


kt = Kot()
while not kt.isEnded:
    kt.update()
    a = int(input())
    if a > 0:
        kt.low(a)
