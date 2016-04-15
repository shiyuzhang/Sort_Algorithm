list = [74, 92, 69, 13, 19, 81, 98, 61, 56, 90, 75, 24, 11, 3, 37, 76, 42, 66, 43, 10, 35, 8, 41, 26, 29, 18, 99, 68, 65, 34, 59, 50, 71, 89, 51, 53, 78, 54,
 97, 55, 85, 57, 25, 14, 7, 64, 22, 48, 1, 17, 95, 63, 20, 70, 4, 88, 39, 87, 36, 38, 93, 21, 79, 46, 86, 44, 47, 0, 84, 16, 32, 45, 23, 30, 9, 62, 28,
91, 73, 5, 67, 31, 94, 77, 12, 40, 33, 52, 83, 80, 6, 58, 49, 15, 2, 27, 96, 82, 72, 60]


def draw_scatter (list):
    x = range(len(list))
    import matplotlib.pyplot as plt
    plt.scatter (list, x)
    plt.show()

def bubble (list):

    length = len(list)
    steps = 0

    for i in range (0, length):
        for j in range (i, length):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]
                steps += 1
                draw_scatter (list)
                
    print list
    print steps
    
    
    
    
    
#bubble1 (list)

#bubble (list)

'''
import numpy as np   
from matplotlib import pyplot as plt   
from matplotlib import animation   
  
# first set up the figure, the axis, and the plot element we want to animate   
fig = plt.figure()   
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))   
line, = ax.plot([], [], lw=2)   
  
# initialization function: plot the background of each frame   
def init():   
    line.set_data([], [])   
    return line,   
  
# animation function.  this is called sequentially   
def animate(i):   
    x = np.linspace(0, 2, 1000)   
    y = np.sin(2 * np.pi * (x - 0.01 * i))   
    line.set_data(x, y)   
    return line,   
  
# call the animator.  blit=true means only re-draw the parts that have changed.   
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)   
  
# save the animation as an mp4.  this requires ffmpeg or mencoder to be   
# installed.  the extra_args ensure that the x264 codec is used, so that   
# the video can be embedded in html5.  you may need to adjust this for   
# your system: for more information, see   
# http://matplotlib.sourceforge.net/api/animation_api.html   
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])   
  
plt.show() 

'''

import matplotlib.pyplot as plt  
import numpy as np  
import matplotlib.animation as animation  
  
def main():  
 numframes = 100  
 numpoints = 10  
 color_data = np.random.random((numframes, numpoints))  
 x, y, c = np.random.random((3, numpoints))  
  
 fig = plt.figure()  
 scat = plt.scatter(x, y, c=c, s=100)  
  
 ani = animation.FuncAnimation(fig, update_plot, frames=xrange(numframes),  
         fargs=(color_data, scat))  
 plt.show()  
  
def update_plot(i, data, scat):  
 scat.set_array(data[i])  
 return scat,  
  
main()  
