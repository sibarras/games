# trying 2
class You:
    J = 'called from class'

    @classmethod
    def __init__(cls, nums=1):
        print(cls.J)
        cls.J += ' plus one'

You()
You()
You()
You()


lst = [1,2,3,'a', 'km']

print(lst.index(3))