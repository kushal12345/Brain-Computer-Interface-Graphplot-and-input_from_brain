from PyQt5.QtWidgets  import *

from  matplotlib.backends.backend_qt5agg  import  FigureCanvas
from  matplotlib.figure  import  Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

class  MplWidget_5 ( QWidget ):
    def  __init__ ( self ,  parent  =  None ):
        QWidget . __init__ ( self ,  parent )
        self.canvas  =  FigureCanvas ( Figure ())
        self.vertical_layout  =  QVBoxLayout ()
        self.animation= animation
        self.canvas.figure = plt.figure(figsize=(0,0), dpi=80, facecolor='black', edgecolor='k')
        self.canvas.axes  =  self.canvas.figure.add_subplot( 1,1,1 )

    def set_layout(self):
        self.setLayout(self.vertical_layout)
        self.vertical_layout.addWidget ( self . canvas )
        # self.setLayout( vertical_layout )
        #self.show=plt.show()
