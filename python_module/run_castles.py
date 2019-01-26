from castle_model import CastleModel
import sys

castle1_size = int(sys.argv[1])
castle2_size = int(sys.argv[2])
castle3_size = int(sys.argv[3])
life = int(sys.argv[4])

castle_model = CastleModel([castle1_size, castle2_size, castle3_size], [life, life, life])
print(castle_model.model.js_dump())