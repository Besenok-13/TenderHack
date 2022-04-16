class Kot:
    def __init__(self):
        self.current_price = 10000
        self.start_price = 10000
        self.percent = 2
        self.last = 0
        self.moves = 1000
        self.isEnded = False
        self.step = self.start_price * self.percent / 100

    def low(self, lst):
        self.last = lst
        self.moves -= 1
        self.current_price -= self.start_price * (self.percent / 100)
        print(self.last, "lowed!", self.current_price, self.moves)
        return self.current_price

    def get_current(self):
        return self.current_price

    def get_last(self):
        return self.last

    def isStopped(self):
        return self.isEnded

    def update(self):
        if self.isEnded:
            return 0
        if self.current_price < 0:
            self.stop()

    def imhere():
        print("imhere")

    def stop(self):
        self.isEnded = True
        print(self.current_price)
        print(self.last)
        print("ENDED!")


class Bot:
    def __init__(self, ID, fl, kt):
        self.login = ID
        self.floor = fl * kt.start_price / 100
        self.timer = 300  # FOR DELAY

    def PRESS_FUCKING_BUTTON(self, kot):
        kot.low(self.login)
        kot.update()

    def update(self, kot):
        if kot.isStopped():
            return 0
        curr_price = kot.get_current()
        next_price = curr_price - kot.step
        if next_price < self.floor:
            pass
        else:
            self.PRESS_FUCKING_BUTTON(kot)


kt = Kot()
bot1 = Bot("bot N1", 30, kt)
bot2 = Bot("bot N2", 30, kt)
for i in range(30):
    bot1.update(kt)
    bot2.update(kt)
    print(kt.current_price)
kt.low("me")
print(kt.current_price)
