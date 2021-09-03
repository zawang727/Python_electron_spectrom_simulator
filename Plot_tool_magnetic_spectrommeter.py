# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:14:11 2021

@author: JennanWang
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Box():
    def __init__(self):
       self.xyzmin = [0.0,0.0,0.0]
       self.xyzmax = [1.0,1.0,1.0]
       
class Curve():
    def __init__(self):
       self.path = []
    
def list_of_cor_2_3_cor_list(list_of_cor):
    newCurve = Curve()
    arr = np.array(list_of_cor)
    arr = arr.transpose(1,0)
    newCurve.path.append(arr[0].copy())
    newCurve.path.append(arr[1].copy())
    newCurve.path.append(arr[2].copy())
    return newCurve
       
def plot_Box3D(ax,model,_color,_label): #ax is fig.gca(projection='3d') model is Box
    ax.plot([model.xyzmin[0],model.xyzmin[0]], [model.xyzmin[1],model.xyzmin[1]], [model.xyzmin[2],model.xyzmax[2]], color=_color, label=_label)
    ax.plot([model.xyzmin[0],model.xyzmin[0]], [model.xyzmin[1],model.xyzmax[1]], [model.xyzmin[2],model.xyzmin[2]], color=_color, label=_label)
    ax.plot([model.xyzmin[0],model.xyzmax[0]], [model.xyzmin[1],model.xyzmin[1]], [model.xyzmin[2],model.xyzmin[2]], color=_color, label=_label)
    ax.plot([model.xyzmax[0],model.xyzmax[0]], [model.xyzmax[1],model.xyzmax[1]], [model.xyzmax[2],model.xyzmin[2]], color=_color, label=_label)
    ax.plot([model.xyzmax[0],model.xyzmax[0]], [model.xyzmax[1],model.xyzmin[1]], [model.xyzmax[2],model.xyzmax[2]], color=_color, label=_label)
    ax.plot([model.xyzmax[0],model.xyzmin[0]], [model.xyzmax[1],model.xyzmax[1]], [model.xyzmax[2],model.xyzmax[2]], color=_color, label=_label)
    ax.plot([model.xyzmax[0],model.xyzmax[0]], [model.xyzmax[1],model.xyzmin[1]], [model.xyzmin[2],model.xyzmin[2]], color=_color, label=_label)
    ax.plot([model.xyzmax[0],model.xyzmax[0]], [model.xyzmin[1],model.xyzmin[1]], [model.xyzmax[2],model.xyzmin[2]], color=_color, label=_label)
    ax.plot([model.xyzmin[0],model.xyzmin[0]], [model.xyzmax[1],model.xyzmin[1]], [model.xyzmax[2],model.xyzmax[2]], color=_color, label=_label)
    ax.plot([model.xyzmin[0],model.xyzmin[0]], [model.xyzmax[1],model.xyzmax[1]], [model.xyzmax[2],model.xyzmin[2]], color=_color, label=_label)
    ax.plot([model.xyzmin[0],model.xyzmax[0]], [model.xyzmin[1],model.xyzmin[1]], [model.xyzmax[2],model.xyzmax[2]], color=_color, label=_label)
    ax.plot([model.xyzmin[0],model.xyzmax[0]], [model.xyzmax[1],model.xyzmax[1]], [model.xyzmin[2],model.xyzmin[2]], color=_color, label=_label)
    
def plot_Curve3D(ax,model,_color,_label): #ax is fig.gca(projection='3d') model is Curve
    ax.plot(model.path[0],model.path[1],model.path[2], color=_color, label=_label)
    
    
def plot_Curve2D(ax,model,_color,_label): #ax is fig.gca(projection='2d') model is Curve
    ax.plot(model.path[0],model.path[1], color=_color, label=_label)
    
    
def plot_Box2D(ax,model,_color,_label): #ax is fig.gca(projection='2d') model is Box
    ax.plot([model.xyzmin[0],model.xyzmin[0]], [model.xyzmin[1],model.xyzmin[1]],  color=_color, label=_label)
    ax.plot([model.xyzmin[0],model.xyzmin[0]], [model.xyzmin[1],model.xyzmax[1]],  color=_color, label=_label)
    ax.plot([model.xyzmin[0],model.xyzmax[0]], [model.xyzmin[1],model.xyzmin[1]],  color=_color, label=_label)
    ax.plot([model.xyzmax[0],model.xyzmax[0]], [model.xyzmax[1],model.xyzmax[1]],  color=_color, label=_label)
    ax.plot([model.xyzmax[0],model.xyzmax[0]], [model.xyzmax[1],model.xyzmin[1]],  color=_color, label=_label)
    ax.plot([model.xyzmax[0],model.xyzmin[0]], [model.xyzmax[1],model.xyzmax[1]],  color=_color, label=_label)
    ax.plot([model.xyzmax[0],model.xyzmax[0]], [model.xyzmax[1],model.xyzmin[1]],  color=_color, label=_label)
    ax.plot([model.xyzmax[0],model.xyzmax[0]], [model.xyzmin[1],model.xyzmin[1]],  color=_color, label=_label)
    ax.plot([model.xyzmin[0],model.xyzmin[0]], [model.xyzmax[1],model.xyzmin[1]],  color=_color, label=_label)
    ax.plot([model.xyzmin[0],model.xyzmin[0]], [model.xyzmax[1],model.xyzmax[1]],  color=_color, label=_label)
    ax.plot([model.xyzmin[0],model.xyzmax[0]], [model.xyzmin[1],model.xyzmin[1]], color=_color, label=_label)
    ax.plot([model.xyzmin[0],model.xyzmax[0]], [model.xyzmax[1],model.xyzmax[1]], color=_color, label=_label)
    

def plot_model3D(Frame,paths):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    plot_Box3D(ax,Frame,'red','Magnetic')
    for i in paths:
        plot_Curve3D(ax,i,'blue','Curve')
    ax.set_xlim3d(0, 0.4)
    ax.set_ylim3d(-0.2, 0.2)
    ax.set_zlim3d(-0.2, 0.2)
    plt.show()
    
def plot_model2D(Frame,paths):
    fig = plt.figure()
    ax = fig.gca()
    plot_Box2D(ax,Frame,'red','Magnetic')
    for i in paths:
        plot_Curve2D(ax,i,'blue','Curve')
    plt.show()
    