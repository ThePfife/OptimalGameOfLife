board_routes = { 'college' : ['a'],
                 'highschool' : ['a'],
                 'a' : ['family', 'tv'],
                 'family' : ['b'],
                 'tv' : ['b'],
                 'b' : ['ball', 'play'],
                 'ball' : ['c'],
                 'play' : ['c']
}

# routes
route_college = [None] * 11
route_highschool = [None] * 3
route_a = [None] * 34
route_family = [None] * 7
route_tv = [None] * 6
route_b = [None] * 23
route_ball = [None] * 4
route_play = [None] * 7
route_c = [None] * 52

SPACE_INVALID = 0
SPACE_PAYDAY = 1 # amount = -1 for lose payday
SPACE_PAY_COLLECT = 2 # amount is money to gain (or lose if negative)
SPACE_LIFE_TILE = 3 # amount is for child
SPACE_LOSE_TURN = 4
SPACE_HARD_CODE = 6 # amount corresponds to another enum for hard coded stuff

class Space:
    def __init__(self, space_type, stopping, amount, func):
        self.space_type = space_type
        self.stopping = stopping
        self.amount = amount
        self.func = func

route_highschool[0] = Space(SPACE_PAYDAY, False, 0, None)

print(route_highschool)

