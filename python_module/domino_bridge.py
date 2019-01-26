from bridge_model import BridgeModel
from strat_simpl import StrategyComparer
import json
import sys

n = int(sys.argv[1])
k = int(sys.argv[2])

file_hands = open("bridge_hands.txt", "r")
json_hands = file_hands.readline()
file_hands.close()

hands = json.loads(json_hands)

bridge_model = BridgeModel(n, k, {'board': [-1, -1, -1, -1], 'lefts': [0, 0],
                                  'hands': hands, 'next': 0, 'history': [],
                                  'beginning': 0, 'clock': 0, 'suit': -1})

bridge_model.model.to_subjective([0])

winning = []

state_id = -1

for state in bridge_model.states:
    state_id += 1
    if state['lefts'][0] > state['lefts'][1] and state['lefts'][0] + state['lefts'][1] == k:
        winning.append(state_id)

strategy_comparer = StrategyComparer(bridge_model.model, bridge_model.get_actions()[0])

(result, strategy) = strategy_comparer.generate_strategy_dfs(bridge_model.model.first_state_id, set(winning), [0], strategy_comparer.basic_h)
print(bridge_model.model.js_dump_strategy_subjective(strategy))