# The Functions Approach

initial_state = {"population": 100, 'growth_rate': 0.05}
def update_population(state):
    new_state = state.copy()
    new_state["population"] *= (1 + state["growth_rate"])
    return new_state

new_state = update_population(initial_state)
print(new_state)

# Object Oriented Progrmming Approach
class PopulationSim:
    def __init__(self, population, growth_rate): #State is held as instance
        #attribute in self.population
        self._population = population
        self._growth_rate = growth_rate
    def update(self):
        self._population *= (1 + self._growth_rate)

new_ss = PopulationSim(150, 0.05)
new_ss.update()
print(new_ss._population)

