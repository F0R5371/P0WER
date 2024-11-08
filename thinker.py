# Start with symbols (propositions)
class Prop:
    def __init__(self, prop):
        self.prop = prop

# Then with connectives
class Not:
    def __init__(self, negated):
        self.negated = negated

class Or:
    def __init__(self, *connected):
        self.connected = connected

class And:
    def __init__(self, *connected):
        self.connected = connected

class Imply:
    def __init__(self, cause, result):
        self.cause = cause
        self.result = result

class Bidir:
    def __init__(self, left, right):
        self.left = left
        self.right = right

# These by default will always be True
raining = Prop('Raining')
sunny = Prop('Sunny')
snowy = Prop('Snowing')
inside = Prop('Inside')
programming = Prop('Programming')

not_raining = Not(raining)
weather = Or(raining, sunny, snowy)



