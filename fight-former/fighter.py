

class Fighter(object):
    """docstring for Fighter."""

    # def __init__(self, name, height, weight, reach, stance, age):
    def __init__(self, name, height, weight, reach, stance, dob):
        super(Fighter, self).__init__()
        self.name = name
        # self.height = self.heightToInches(height)
        self.height = height
        self.weight = weight
        self.reach = reach
        self.stance = stance
        self.dob = dob

        def print():
            print("name: " + self.name)
            # print()
