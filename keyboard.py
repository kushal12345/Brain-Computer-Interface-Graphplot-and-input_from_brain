import time
from matplotlib import pyplot as plt
class Keyboard():

    def loopkey(self,buttons, outputs,t):
        print("{0} sec delay".format(t))

        for button,output  in zip(buttons,outputs):
            button.setStyleSheet("background-color: red")
            #button.clicked.connect(output)
            '''
            if(headset.single_eyeblink):
                button.connect(output)
            elif(headet.double_eyeblink):
                #restart loop from top        
            '''
            time.sleep(t)
            button.setStyleSheet("background-color: white")
