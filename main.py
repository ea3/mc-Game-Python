from enemy import Enemy, Troll, Vampire, VampireKing


ugly_troll = Troll("Pug")
print("Ugly Troll - {}". format(ugly_troll))
ugly_troll.take_damage(3)

another_troll = Troll("Ug")
print("Another Troll - {}". format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()

another_troll.grunt()
brother.grunt()

big_Vampire = Vampire("Draculator")
print(big_Vampire)
big_Vampire.take_damage(7)

small_Vampire = Vampire("Draculin")
print(small_Vampire)
small_Vampire.take_damage(2)

print("*" * 80)
while big_Vampire.alive:
    big_Vampire.take_damage(1)

dracula = VampireKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)