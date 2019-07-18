# Run all the code in this file.3.12
#
# import needed classes


from monster_class import*
from workshop_class import*

Monster1 = Monster("Mike Wozniaki")

print(Monster1.sleep())
print(Monster1.name + Monster1.eat())# create some workshops #
Monster1.add_skill('Kill')
Monster1.add_skill('Seek')
Monster1.add_skill('destroy')
print(Monster1.skills)
print(Monster1.sleep())

Monster2 = Monster("Scully")#
print(Monster2.sleep())
print(Monster2.name + Monster2.eat())
Monster3 = Monster()  #
print(Monster3.sleep())
print(Monster3.name + Monster3.eat())


# create somme monsters
#
#
# make monsters make a noise or do  something