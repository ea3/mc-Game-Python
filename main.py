from enemy import Enemy, Troll


ugly_troll = Troll()
print("Ugly Troll - {}". format(ugly_troll))

another_troll = Troll("Ug", 18, 1)
print("Another Troll - {}". format(another_troll), end='')

brother = Troll("Urg", 23)
print(brother)