# here i will create and abstract my Monster class
#     as

class Monster():
    def __init__(self, name= 'munchy'):
        self.name = name
        self.skills = []

    def sleep(self):
        return 'zzz'
    def eat (self,food ='cheese pizza'):
        return ' eats '+food+ ' nom nom '
        
    def scare_attack(self):
        return 'RAHHH'
    def add_skill(self, skill_arg):
        self.skills.append(skill_arg)
    # def shout_out_