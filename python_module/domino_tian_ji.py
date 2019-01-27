from tian_ji_model import TianJiModel
from strat_simpl import StrategyComparer
import json
import sys

horses = int(sys.argv[1])

tian_ji_model = TianJiModel(horses)

winning = []

state_id = -1

for state in tian_ji_model.states:
    state_id += 1
    if state['tian_ji_score'] > state['king_score'] and len(state['tian_ji_horses']) == 0:
        winning.append(state_id)

strategy_comparer = StrategyComparer(tian_ji_model.model, tian_ji_model.get_actions()[0])

(result, strategy) = strategy_comparer.generate_strategy_dfs(0, set(winning), [0], strategy_comparer.basic_h)
if result:
    print("1")
else:
    print("0")
print(tian_ji_model.model.js_dump_strategy(strategy))