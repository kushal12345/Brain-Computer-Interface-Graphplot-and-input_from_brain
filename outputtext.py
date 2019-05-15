from PyQt5.QtWidgets  import *

from  matplotlib.backends.backend_qt5agg  import  FigureCanvas
from  matplotlib.figure  import  Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

class  OutputText ( QFrame ):
    def __init__ (self , parent = None):
        QFrame. __init__(self, parent)
        
