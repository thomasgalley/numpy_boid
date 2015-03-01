import numpy as np
boid_positionsx=np.random.rand(1,50)
boid_positionsy=np.random.rand(1,50)
boid_positionsx *= 500 
boid_positionsx -= 50 
boid_positionsy *= 300
boid_positionsy -= 300 
boid_velocities=np.random.rand(2,50)
boid_velocities[0,:] *= 10 
boid_velocities[1,:] *= 40
boid_velocities[1,:] -= 20

boid_position_diff_x=np.add.outer(boid_positionsx,-boid_positionsx)
boid_position_diff_y=np.add.outer(boid_positionsy,-boid_positionsy)

#Fly towards middle

boid_position_diff=(np.add.outer(boid_positionsx,-boid_positionsx))
np.sum(boid_position_diff,axis=1)
new_boid_positions=boid_positionsx+np.sum(boid_position_diff,axis=1)*0.01/50boid_velocities[0,i]+= boid_velocities+np.sum(boid_position_diff_x[i])*0.01/50




"""


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

def position_difference(matrix):
    i=0
    j=0
    l=np.array([50,50,50])
    for i in matrix[0,i]:
        for j in matrix[0,j]:
            l[i,j]=matrix[0,i]-matrix[0,j]
            return l
"""
