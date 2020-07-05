# trying 2
class You:
    J = 'called from class'

    def __init__(self, nums=1):
        J = You.J
        print(J)

j = You(You)

lst = [1,2,3,'a', 'km']

print(lst.index(3))