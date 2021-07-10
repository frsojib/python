class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("I am making a call")
    def play_game(self):
        print("I am playing a game")

p2 = Phone()
p3 = Phone()
p2.set_color("red")
p2.set_cost(5000)
p3.set_color("blue")
p3.set_cost(10000)
print(p3.show_color())
print(p3.show_cost())
print(p2.show_color())
print(p2.show_cost())