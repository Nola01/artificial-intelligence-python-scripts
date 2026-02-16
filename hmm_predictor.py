import numpy as np
from hmmlearn import hmm

""" 
define number of states. In slides example there are two states: happy and sad
 """
n_states = 2

""" 
define number of observations. In slides example there are two: smile or cry
 """
n_observations = 2

""" 
define the HMM using CategoricalHMM class. It models a variable that
can take on several (qualitative) values with some probabilities.
The number of components is the same as number of states, maximum number of iterations
to perform is set to 100, and no need for initial parameters
 """
model = hmm.CategoricalHMM(n_components=n_states, n_iter=100, init_params="")

""" 
set up initial state, transition and emission probabilities
state prob: 0.45 (happy), 0.55 (sad)
transition prob: 0.7 (from happy to happy), 0.3 (from happy to sad),
                    0.6 (from sad to sad), 0.4 (from sad to happy)
emission prob: 0.8 (happy generates smile), 0.2 (happy generates cry)
                0.35 (sad generates smile), 0.65 (sad generates cry)
 """
start_probability = np.array([0.45, 0.55]) 

transition_probability = np.array([
    [0.7, 0.3],
    [0.6, 0.4]
])

emission_probability = np.array([
    [0.8, 0.2],
    [0.35, 0.65]
])

""" 
assign the probabilities to the HMM model
 """
model.startprob_ = start_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probability

""" 
example observation sequence (0: smile, 1: cry)
 """
observations = np.array([[0], [0], [1], [1], [0]])

""" 
likelihood of the observation sequence
 """
likelihood = model.score(observations)
print(f"Likelihood of the observation sequence: {likelihood}")

""" 
predict the most likely sequence of hidden states
 """
hidden_states = model.predict(observations)
print(f"Most likely hidden states: {hidden_states}")

""" 
map hidden states to their real values
 """
state_mapping = {0: "happy", 1: "sad"}
decoded_states = [state_mapping[state] for state in hidden_states]
print(f"Decoded hidden states: {decoded_states}")