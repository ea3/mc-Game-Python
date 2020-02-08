from enemy import Enemy, Troll


ugly_troll = Troll("Pug")
print("Ugly Troll - {}". format(ugly_troll))

another_troll = Troll("Ug")
print("Another Troll - {}". format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()

another_troll.grunt()
brother.grunt()

