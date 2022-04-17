class Kot:
    def __init__(self, start, perc):
        self.start_price = start
        self.current_price = start
        self.percent = perc
        self.last = ""
        self.moves = 0
        self.isEnded = False
        self.step = self.start_price * self.percent / 100
        self.bots = []
        self.history = []
        self.in_book = dict()  # {'stop_percent': bots[], ...}

    def low(self, lst):
        if self.last == lst:
            return 0
        self.history.append([self.moves, self.current_price])
        self.last = lst
        self.moves += 1
        self.current_price -= self.start_price * (self.percent / 100)
        return self.current_price

    def addBot(self, ID, floor):
        self.bots.append(Bot(ID, floor, self))

    def get_current(self):
        return self.current_price

    def get_last(self):
        return self.last

    def isStopped(self):
        return self.isEnded

    def update(self):
        if self.isEnded:
            return 0
        if self.current_price <= 0:
            self.stop()
        for bot in self.bots:
            bot.update(self)

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
        self.fl = fl
        self.floor = fl * kt.start_price / 100
        self.timer = 300  # FOR DELAY
        self.awaiting = False
        if f"{fl}" in kt.in_book.keys():
            temp = kt.in_book[f"{fl}"] + [self]
        else:
            temp = [self]
        kt.in_book[f"{fl}"] = temp

    def PRESS_FUCKING_BUTTON(self, kot):
        kot.low(self.login)

    def update(self, kot):
        next_price = kot.current_price - kot.step
        if next_price - kot.step < self.floor and not self.awaiting:
            if len(kot.in_book[f"{self.fl}"]) > 2:
                if kot.in_book[f"{self.fl}"][0] == self and self.login != kot.last:
                    self.timer = 300
                elif kot.in_book[f"{self.fl}"][0] == self:
                    self.timer = 300
                else:
                    self.timer = 1000
                self.awaiting = True

        if next_price < self.floor:
            return 0
        else:
            if self.delay():
                self.PRESS_FUCKING_BUTTON(kot)

    def delay(self):
        self.timer -= 1
        if self.timer <= 0:
            self.timer = 150
            self.awaiting = False
            return True
        return False


# kts = []
# kts.append(Kot(10000, 2))

# kts[0].addBot("bot N1", 88)
# kts[0].addBot("bot N2", 88)
# kts[0].addBot("bot N3", 88)
# for kt in kts:
#    kt.update()


""" 
TODO  
 
Queue for bots to prevent permanent losses 
last step must be booked for first bot(but not for humans) 
also there should be delay for last step 
 
"""


class Test:
    def __init__(self, x, y):
        self.x = []
        self.y = []
        self.kts = [Kot()]
        self.kts[0].addBot("bot N1", 30)
        self.kts[0].addBot("bot N2", 30)

    def test_play(self):

        for kt in self.kts:
            kt.update()
            # self.y.append(kt.current_price)
            self.y.append(kt.current_price)
            if len(self.x):
                self.x.append(self.x[-1] + 1)
            else:
                self.x.append(1)

    def generate_pict(self):
        import json

        import numpy as np
        import plotly
        import plotly.express as px

        xx = np.array(self.x)
        yy = np.array(self.y)

        # def f(x):
        #    return x ** 2
        if len(xx) and len(yy):
            fig = px.scatter(x=xx, y=yy)
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            return graphJSON
