# This class define an intelligent agent
class TableDrivenAgent:
    """ 
    this is the constructor of the class, where we set agent's table
    and agent's percept history list initial values. 
     """
    def __init__(self, table):
        self.table = table
        self.percept_history = []

    """ 
    this function add a percept to the percept history list.
    Then convert the list to a tuple and look for it in the
    dictionary. If it is in, it returns the action. Otherwise,
    it returns 'No action'
    """
    def perceive(self, percept):
        self.percept_history.append(percept)
        action = self.table.get(tuple(self.percept_history), 'No action')
        return action

""" 
we define a dictionary called 'table'.
The key ('clean') has the value ('right'). This means that when the state is only 'clean',
the action to be taken is to move 'right'.
The key ('clean', 'clean') has the value ('down'). This indicates that when both states are
'clean', the corresponding action is to move 'down'.
The key ('clean','clean','dirty') has the value 'suck', meaning that when the first and second
states are 'clean' but the third is 'dirty', the action to take is 'suck'
 """
table = {
    ('clean',):'right',
    ('clean', 'clean'): 'down',
    ('clean', 'clean', 'dirty'): 'suck'
}

""" 
we define a new 'TableDrivenAgent' object and 
print the action for each given percept
 """
agent = TableDrivenAgent(table)
print(agent.perceive('clean'))
print(agent.perceive('clean'))
print(agent.perceive('dirty'))