from drone_model import DroneModel, CracowMap
import sys

n = int(sys.argv[1])
k = int(sys.argv[2])

energies = []
for _ in range(0, n):
    energies.append(k)

drone_model = DroneModel(n, energies, CracowMap())
drone_model.listify_states()
print(drone_model.model.js_dump())