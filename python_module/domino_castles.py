from castle_model import CastleModel
from strat_simpl import StrategyComparer
import sys

castle1_size = int(sys.argv[1])
castle2_size = int(sys.argv[2])
castle3_size = int(sys.argv[3])
life = int(sys.argv[4])

castle_model = CastleModel([castle1_size, castle2_size, castle3_size], [life, life, life])

winning = []

state_id = -1

for state in castle_model.states:
    state_id += 1
    if state['lifes'][2] == 0:
        winning.append(state_id)
        print(state)

agents = []
for i in range(0, castle1_size):
    agents.append(i)

strategy_comparer = StrategyComparer(castle_model.model, castle_model.get_actions()[0])

(result, strategy) = strategy_comparer.generate_strategy_dfs(0, set(winning), agents, strategy_comparer.basic_h)
castle_model.listify_states()
print(castle_model.model.js_dump_strategy(strategy))