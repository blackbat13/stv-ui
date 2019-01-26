from simple_voting_model import SimpleVotingModel
import sys

no_voters = int(sys.argv[1])
no_candidates = int(sys.argv[2])

simple_voting = SimpleVotingModel(no_candidates, no_voters)
print(simple_voting.model.js_dump())