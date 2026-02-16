import random

#This class define a room
class Room:
    """ 
    this is the constructor of the class, where we set room's name
    and room's state initial values. 
     """
    def __init__(self, name):
        self.name = name
        self.state = 'clean'

    """ 
    this function set the agent's state value between 'dirty' or
    'clean' with a 50% probability
     """
    def randomly_make_dirty(self):
        if random.random() < 0.5:
            self.state = 'dirty'
        else:
            self.state = 'clean'

#This class define an intelligent agent
class Agent:
    """ 
    this is the constructor of the class, where we set agent's position
    and agent's internal state initial values. 
     """
    def __init__(self):
        self.position = 'A'
        self.internal_state = {'A': 'unknown', 'B': 'unknown'}

    """ 
    this function return the opposite position to the current one
     """
    def transition_model(self):
        if self.position == 'A':
            return 'B'
        else:
            return 'A'
            
    """ 
    this function returns the room's state according to the sensor. If
    it is dirty, returns 'dirty'. If it is 'clean', there is a 2%
    probability that it returns 'dirty', and 98% probability that it
    returns 'clean'
     """
    def sensor_model(self,room):
        if room.state == 'dirty':
            return 'dirty'
        else:
            if random.random() < 0.02:
                return 'dirty'
            else:
                return 'clean'
            
    """ 
    this function change room's state and agent's internal state (for
    a given room) to 'clean' 
     """
    def clean(self, room):
        print(f"Cleaning room {room.name}.")
        room.state = 'Clean'
        self.internal_state[room.name] = 'Clean'

    """ 
    this function change agent's internal state for a given room
    to the perceived state
     """
    def update_internal_state(self, room, perceived_state):
        self.internal_state[room.name] = perceived_state
        print(f"Internal state updated: {self.internal_state}")

    """ 
    this function change  
     """
    def model_based_reflex_agent(self, rooms):
        for _ in range(8):
            current_room = rooms[self.position]
            perceived_state = self.sensor_model(current_room)
            print(f"Sensed {perceived_state} in room {self.position}")

            self.update_internal_state(current_room, perceived_state)
            if perceived_state == 'dirty':
                self.clean(current_room)

            self.position = self.transition_model()
            print(f"Moved to room {self.position}.")

            rooms[self.position].randomly_make_dirty()

# define 2 rooms
room_A = Room('A')
room_B = Room('B')

# list of rooms
rooms = {'A': room_A, 'B': room_B}
agent = Agent()

# set A room's state to 'dirty'
rooms['A'].state = 'dirty'


agent.model_based_reflex_agent(rooms)