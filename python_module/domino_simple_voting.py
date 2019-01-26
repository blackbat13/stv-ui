from simple_voting_model import SimpleVotingModel
from strat_simpl import StrategyComparer
import sys

no_voters = int(sys.argv[1])
no_candidates = int(sys.argv[2])

simple_voting = SimpleVotingModel(no_candidates, no_voters)
print(simple_voting.model.js_dump())

winning = []

state_id = -1
voter_number = 1

for state in simple_voting.states:
    state_id += 1
    if state['finish'][voter_number] == 1 and state['coercer_actions'][voter_number] != 'pun' and state['voted'][
            voter_number] != 1:
        winning.append(state_id)

agents = [1]

strategy_comparer = StrategyComparer(simple_voting.model, simple_voting.get_actions()[1])

(result, strategy) = strategy_comparer.generate_strategy_dfs(0, set(winning), agents, strategy_comparer.basic_h)
print(simple_voting.model.js_dump_strategy(strategy))