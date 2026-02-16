class SimpleReflexAgent:
    # this is the constructor of the class, in this case default
    def __init__(self):
        pass

    """ 
    this function receive a percept. It return 3 different
    actions depending on the given percept ('dirty'-'suck', 
    'clean'-'move right', 'Otherwise'-'No action')
     """
    def perceive(self, percept):
        if percept == 'dirty':
            return 'suck'
        elif percept == 'clean':
            return 'move right'
        else:
            return 'No action'
        
""" 
we define a new 'SimpleReflexAgent' object and 
print the action for each given percept
 """
agent = SimpleReflexAgent()
print(agent.perceive('dirty'))
print(agent.perceive('clean'))