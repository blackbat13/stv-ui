
from tian_ji_model import TianJiModel
import json
import sys

horses = int(sys.argv[1])

tian_ji_model = TianJiModel(horses)
print(tian_ji_model.model.js_dump())