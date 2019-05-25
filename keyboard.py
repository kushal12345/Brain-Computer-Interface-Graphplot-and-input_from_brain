import time

class keyboard:
    def round():
        x  = [1,2,3,4,5]
        for i in x:
            print(i)
            time.sleep(1)

    def loopkey(button,output):
        print("button of keyboard ",button)
        print("output of keyboard",output)
        for i in button:
            for j in output:
                i.setStyleSheet("background-color: red")
                i.clicked.connect(j)
                print(j)
                time.sleep(0.5)
