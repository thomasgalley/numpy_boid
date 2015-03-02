import numpy as np
boid_positionsx=np.random.rand(1,50)
boid_positionsy=np.random.rand(1,50)
boid_positionsx *= 500 
boid_positionsx -= 50 
boid_positionsy *= 300
boid_positionsy -= 300 
boid_velocities=np.random.rand(2,50)
boid_velocitiesx *= 10 
boid_velocitiesy *= 40
boid_velocitiesy -= 20


boids=(boid_positionsx,boid_positionsy,boid_velocitiesx,boid_velocitiesy)

boid_velocities_diffx=(np.add.outer(boid_positionsx,-boid_positionsx))

def velocity_change(velocity1,parameter1,parameter2,change_magnitude):
   velocitynew=velocity1+(parameter2-parameter1)*change_magnitude
   return velocitynew

def position_diff(boid_positions):
    boid_position_diff=np.add.outer(boid_positions,-boid_positions)
    return boid_position_diff

boid_position_diff_x=boid_position_diff(boid_positionsx)
boid_position_diff_y=boid_position_diff(boid_positionsy)

def update_boids(boids):
    #Fly towards middle

    boid_velocitiesx+=np.sum(boid_position_diff_x,axis=1)*0.01/50
    boid_velocitiesy+=np.sum(boid_position_diff_x,axis=1)*0.01/50

    # Fly away from nearby boids

    test=(boid_position_diffx**2+boid_position_diffy**2)<100
    boid_velocitiesx+=test[:,0]*boid_position_diffx[:,0]
    boid_velocitiesy+=test[:,0]*boid_position_diffy[:,0]

    # Try to match speed with nearby boids

    test2=(boid_position_diffx**2+boid_position_diffy**2)<10000
    boid_velocitiesx+=test2[:,0]*boid_position_diffx[:,0]
    boid_velocitiesy+=test2[:,0]*boid_position_diffy[:,0]

    # Move according to velocities

    boid_positionsx+=new_boid_velocitiesx[0]
    boid_positionsy+=new_boid_velocitiesy[0]


"""

new_boid_velocitiesx=boid_velocitiesx+np.sum(boid_position_diffx,axis=1)*0.01/50
test=boid_position_diffx**2+boid_position_diffy**2
test=(boid_position_diffx**2+boid_position_diffy**2)<100
new_boid_velocitiesx=boid_velocitiesx
boid_velocitiesx+=test[:,0]*boid_position_diffx[:,0] #if the test is true (=1) the new velocity will update,otherwise it will not (since false=0)
test2=(boid_position_diffx**2+boid_position_diffy**2)<10000
new_boid_velocitiesx+=test[:,0]*boid_velocities_diffx[:,0]
boid_positionsx+=new_boid_velocitiesx[0]




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
