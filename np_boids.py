import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random


boid_positionsx=np.random.rand(1,50)
boid_positionsy=np.random.rand(1,50)
boid_positionsx *= 500 
boid_positionsx -= 50 
boid_positionsy *= 300
boid_positionsy -= 300 
boid_velocitiesx=np.random.rand(1,50)
boid_velocitiesy=np.random.rand(1,50)
boid_velocitiesx *= 10 
boid_velocitiesy *= 40
boid_velocitiesy -= 20






def boid_position_diff(boid_positions):
    boid_position_diff=np.add.outer(boid_positions,-boid_positions)
    return boid_position_diff

boid_position_diff_x=boid_position_diff(boid_positionsx)
boid_position_diff_y=boid_position_diff(boid_positionsy)
boids=(boid_positionsx,boid_positionsy,boid_velocitiesx,boid_velocitiesy)


def update_boids(boid_positionsx,boid_positionsy,boid_velocitiesx,boid_velocitiesy,boid_position_diff_x,boid_position_diff_y):
    
    #Fly towards middle

    boid_velocitiesx+=np.sum(boid_position_diff_x,axis=1)[0]*0.01/50
    boid_velocitiesy+=np.sum(boid_position_diff_y,axis=1)[0]*0.01/50

   # Fly away from nearby boids

    test=(boid_position_diff_x**2+boid_position_diff_y**2)<100
    boid_velocitiesx+=test[:,0][0][0]*boid_position_diff_x[:,0][0][0]
    boid_velocitiesy+=test[:,0][0][0]*boid_position_diff_y[:,0][0][0]

    # Try to match speed with nearby boids

    test2=(boid_position_diff_x**2+boid_position_diff_y**2)<10000
    boid_velocitiesx+=test2[:,0][0][0]*boid_position_diff_x[:,0][0][0]
    boid_velocitiesy+=test2[:,0][0][0]*boid_position_diff_y[:,0][0][0]

    # Move according to velocities

    boid_positionsx+=boid_velocitiesx[0]
    boid_positionsy+=boid_velocitiesy[0]


    

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boid_positionsx,boid_positionsy,boid_velocitiesx,boid_velocitiesy,boid_position_diff_x,boid_position_diff_y)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
"""

new_boid_velocitiesx=boid_velocitiesx+np.sum(boid_position_diffx,axis=1)*0.01/50
test=boid_position_diffx**2+boid_position_diffy**2
test=(boid_position_diffx**2+boid_position_diffy**2)<100
new_boid_velocitiesx=boid_velocitiesx
boid_velocitiesx+=test[:,0]*boid_position_diffx[:,0] #if the test is true (=1) the new velocity will update,otherwise it will not (since false=0)
test2=(boid_position_diffx**2+boid_position_diffy**2)<10000
new_boid_velocitiesx+=test[:,0]*boid_velocities_diffx[:,0]
boid_positionsx+=new_boid_velocitiesx[0]

boid_velocities_diffx=boid_position_diff(boid_velocitiesx)
boid_velocities_diffy=boid_position_diff(boid_velocitiesy)


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
