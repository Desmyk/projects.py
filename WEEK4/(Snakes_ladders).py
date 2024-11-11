class GamePlayer:
    # initializing the game player properties 
     
    def __init__(self, _id):
        # initial dummy rank -1
        self._id = _id
        # starting position for every player is 1
        self.rank = -1
        self.position = 1
 
    def set_position(self, pos):
        self.position = pos
 
    def set_rank(self, rank):
        self.rank = rank
 
    def get_pos(self):
        return self.position
 
    def get_rank(self):
        return self.rank
    
class MovingEntity:
    # initialize properties of the entity
 
    def __init__(self, end_pos=None):
        # end pos where player would be send on board
        self.end_pos = end_pos  
        # description of moving entity
        self.desc = None  
 
    def set_description(self, desc):
        self.desc = None
 
    def get_end_pos(self):
        if self.end_pos is None:
            raise Exception("no_end_position_defined")
        return self.end_pos
    
 
class Snake(MovingEntity):
    # define Snake Entity
 
    def __init__(self, end_pos=None):
        super(Snake, self).__init__(end_pos)
        # set description to snake
        self.desc = "Snake"
 
 
class Ladder(MovingEntity):
    # define Ladder entity
 
    def __init__(self, end_pos=None):
        super(Ladder, self).__init__(end_pos)
        # set description to Ladder
        self.desc = "Ladder"
        
 
class Board:
    
    # define board with size and moving entities
    
    def __init__(self, size):
        self.size = size
        # instead of using list, we can use map of {pos:moving_entity} to save space
        self.board = {} 
    
    def get_size(self):
        return self.size
 
    def set_moving_entity(self, pos, moving_entity):
        # set moving entity to pos
        self.board[pos] = moving_entity
 
    def get_next_pos(self, player_pos):
        # get next pos given a specific position player is on
        if player_pos > self.size:
            return player_pos
        if player_pos not in self.board:
            return player_pos
        return self.board[player_pos].get_end_pos()
 
    def at_last_pos(self, pos):
        if pos == self.size:
            return True
        return False
    

class Dice:
    def __init__(self, sides):
      # no of sides in the dice
        self.sides = sides  
 
    def roll(self):
        # return random number between 1 to sides
        import random
        ans = random.randrange(1, self.sides + 1)
        return ans
