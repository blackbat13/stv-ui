from drone_model import DroneModel, CracowMap
import sys

n = int(sys.argv[1])
k = int(sys.argv[2])
v = int(sys.argv[3])

energies = []
for _ in range(0, n):
    energies.append(k)

drone_model = DroneModel(n, energies, CracowMap())
drone_model.listify_states()
if v == 1:
    atl_model = drone_model.model.to_atl_imperfect(drone_model.get_actions())
else:
    atl_model = drone_model.model.to_atl_perfect(drone_model.get_actions())

winning = []

state_id = -1

for state in drone_model.states:
    state_id += 1
    if len(state['visited'][0]) >= 2:#len(drone_model.graph):
        winning.append(state_id)

agents = []
for i in range(0, n):
    agents.append(i)

result = atl_model.minimum_formula_many_agents(agents, winning)
if 0 in result:
    print(1)
else:
    print(0)
print(len(result))
print(drone_model.model.js_dump_strategy_objective(atl_model.strategy))