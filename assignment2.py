import numpy as np

class WeatherSimulation:
    def __init__(self, data1, data2):
    
        #Initialize the class with the transition probabilities and holding time data.

        self.transition_probabilities = data1
        self.holding_time = data2

        for i in data1.values():
            val=i.values()
            values=list(val)
            value=sum(values)
            if value != 1:
                raise RuntimeError("RuntimeError")
        
        self._currentState = 'sunny'
        self.completedhors = 0

    def get_states(self):
        
        #Returns the keys of the transition probabilities dictionary.
        
        self.transition_probabilities.keys()
        return self.transition_probabilities.keys()

    def current_state(self):
        
        #Returns the current state of the simulation.
        
        self._currentState
        return self._currentState

    def next_state(self):
        
        #Changes the current state to the next state according to the transition probabilities and the holding time.
        
        if self.completedhors <= 0:
            trans_prob = self.transition_probabilities[self._currentState]
            trans_prob_keys=list(self.transition_probabilities.keys())
            self._currentState = np.random.choice(
                trans_prob_keys, p=list(trans_prob.values()))
            self.completedhors = self.holding_time[self._currentState]
            self.completedhors -= 1
        else:
            self.completedhors -= 1

    def set_state(self, new_state):
        #
        #Set the current state to a new state.
        
        self._currentState = new_state

    def current_state_remaining_hours(self):
        
        #Returns the remaining hours in the current state.
        
        completedhours=self.completedhors
        return completedhours

    def iterable(self):
    
        #Iterable function to yield the current state of the simulation.
        
        while True:
            currentstate= self._currentState
            yield currentstate
            self.next_state()

    def simulate(self, hours):
        
        #Runs the simulation for a given number of hours and returns the percentage of time spent in each state.
        
        count_states = {k: 0 for k in self.transition_probabilities.keys()}

        for i in range(hours):
            count_states[self.current_state()] += 1
            self.next_state()
        count_state_values= count_states.values()
        count_states_list = list(count_state_values)
        count_states_percents = []
        lenght_of_state=len(count_states_list)
        for j in range(lenght_of_state):
            list_count_per_hour=count_states_list[j]/hours
            count_states_percents.append(list_count_per_hour*100)
        return (count_states_percents)
