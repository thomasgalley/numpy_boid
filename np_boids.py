import numpy as np
boid_positions=np.random.rand(2,50)
boid_positions[0,:] *= 500 
boid_positions[0,:] -= 50 
boid_positions[1,:] *= 300
boid_positions[1,:] -= 300 
boid_velocities=np.random.rand(2,50)
boid_velocities[0,:] *= 10 
boid_velocities[1,:] *= 40
boid_velocities[1,:] -= 20
