from  PyQt5.QtWidgets  import *
from  PyQt5.uic  import  loadUi
import sys
from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )
import matplotlib.animation as animation
import matplotlib as plt
from matplotlib.figure import Figure
import  numpy  as  np
import  random
from lineEdit import QLabel
import time
from keyboard import Keyboard
import threading
#import mindwave, time, subprocess

#headset = mindwave.Headset('')
#time.sleep(2)
#headset.connect()
#print("connecting")

#while headset.status != 'connected':
#    time.sleep(3)
#    print ("Trying to Connect to headset")
#    if(headset.status=='standby'):
#        headset.connect()
#        print("retrying")
#    print("connected")


n=200 #frames
interval=60

global init
init = ""


class  MatplotlibWidget ( QMainWindow ):

    def  __init__ ( self ):
        QMainWindow . __init__ ( self )
        loadUi ( "qt_desginer.ui" , self )
        self.setWindowTitle ( "Brain Input processer" )
        #self . pushButton_generate_random_signal . clicked . connect ( self . update_graph )
        self.update_graph()
        self.addToolBar ( NavigationToolbar(self.MplWidget.canvas,self))


        self.button_1n = 1
        self.button_2n = 2
        self.button_3n = 3
        self.button_4n = 4
        self.button_5n = 5
        self.button_6n = 6
        self.button_7n = 7
        self.button_8n = 8
        self.button_9n = 9
        self.button_0n = 0

        self.button_an = 'a'
        self.button_bn = 'b'
        self.button_cn = 'c'
        self.button_dn = 'd'
        self.button_en = 'e'
        self.button_fn = 'f'
        self.button_gn = 'g'
        self.button_hn = 'h'
        self.button_in = 'i'
        self.button_jn = 'j'
        self.button_kn = 'k'
        self.button_ln = 'l'
        self.button_mn = 'm'
        self.button_nn = 'n'
        self.button_on = 'o'
        self.button_pn = 'p'
        self.button_qn = 'q'
        self.button_rn = 'r'
        self.button_sn = 's'
        self.button_tn = 't'
        self.button_un = 'u'

        self.button_vn = 'v'
        self.button_wn = 'w'
        self.button_xn = 'x'
        self.button_yn = 'y'
        self.button_zn = 'z'
        self.button_spacen = ' '

        '''
        self. button_1.clicked.connect(self.button_click1)
        self. button_2.clicked.connect(self.button_click2)
        self. button_3.clicked.connect(self.button_click3)
        self. button_4.clicked.connect(self.button_click4)
        self. button_5.clicked.connect(self.button_click5)
        self. button_6.clicked.connect(self.button_click6)
        self. button_7.clicked.connect(self.button_click7)
        self. button_8.clicked.connect(self.button_click8)
        self. button_9.clicked.connect(self.button_click9)
        self. button_0.clicked.connect(self.button_click0)

        self. button_a.clicked.connect(self.button_clicka)
        self. button_b.clicked.connect(self.button_clickb)
        self. button_c.clicked.connect(self.button_clickc)
        self. button_d.clicked.connect(self.button_clickd)
        self. button_e.clicked.connect(self.button_clicke)
        self. button_f.clicked.connect(self.button_clickf)
        self. button_g.clicked.connect(self.button_clickg)
        self. button_h.clicked.connect(self.button_clickh)
        self. button_i.clicked.connect(self.button_clicki)
        self. button_j.clicked.connect(self.button_clickj)

        self. button_k.clicked.connect(self.button_clickk)
        self. button_l.clicked.connect(self.button_clickl)
        self. button_m.clicked.connect(self.button_clickm)
        self. button_n.clicked.connect(self.button_clickn)
        self. button_o.clicked.connect(self.button_clicko)
        self. button_p.clicked.connect(self.button_clickp)
        self. button_q.clicked.connect(self.button_clickq)
        self. button_r.clicked.connect(self.button_clickr)
        self. button_s.clicked.connect(self.button_clicks)
        self. button_t.clicked.connect(self.button_clickt)

        self. button_u.clicked.connect(self.button_clicku)
        self. button_v.clicked.connect(self.button_clickv)
        self. button_w.clicked.connect(self.button_clickw)
        self. button_x.clicked.connect(self.button_clickx)
        self. button_y.clicked.connect(self.button_clicky)
        self. button_z.clicked.connect(self.button_clickz)
        self. button_space.clicked.connect(self.button_clickspace)
        self. button_clear.clicked.connect(self.button_clickclear)
        '''
        self.button = [ self.button_1,self.button_2,self.button_3,self.button_4,self.button_5,self.button_6,self.button_7,self.button_8,self.button_9,self.button_0,
                        self.button_a,self.button_b,self.button_c,self.button_d,self.button_e,self.button_f,self.button_g,self.button_h,self.button_i,self.button_j,
                        self.button_k,self.button_l,self.button_m,self.button_n,self.button_o,self.button_p,self.button_q,self.button_r,self.button_s,self.button_t,
                        self.button_u,self.button_v,self.button_w,self.button_x,self.button_y,self.button_z,self.button_space,self.button_clear]
        self.output = [ self.button_click1,self.button_click2,self.button_click3,self.button_click4,self.button_click5,
                        self.button_click6,self.button_click7,self.button_click8,self.button_click9,self.button_click0,
                        self.button_clicka,self.button_clickb,self.button_clickc,self.button_clickd,self.button_clicke,
                        self.button_clickf,self.button_clickg,self.button_clickh,self.button_clicki,self.button_clickj,
                        self.button_clickk,self.button_clickl,self.button_clickm,self.button_clickn,self.button_clicko,
                        self.button_clickp,self.button_clickq,self.button_clickr,self.button_clicks,self.button_clickt,
                        self.button_clicku,self.button_clickv,self.button_clickw,self.button_clickx,self.button_clicky,
                        self.button_clickz,self.button_clickspace,self.button_clickclear]

    def keyboardinput(self,output):
        a = output
        global init
        concat =  init + a
        self.QLabel.setText(concat)
        init = concat

    def keyboardinputclear(self):
        self.QLabel.clear()


    def button_click1(self):
        self.keyboardinput(str(self.button_1n))
        #self.QLabel.setText(str(self.button_1n))


    def button_click2(self):
        self.keyboardinput(str(self.button_2n))
        #self.QLabel.setText(str(self.button_2n))

    def button_click3(self):
        self.keyboardinput(str(self.button_3n))
        #self.QLabel.setText(str(self.button_3n))

    def button_click4(self):
        self.keyboardinput(str(self.button_4n))
        #self.QLabel.setText(str(self.button_4n))

    def button_click5(self):
        self.keyboardinput(str(self.button_5n))
        #self.QLabel.setText(str(self.button_5n))

    def button_click6(self):
        self.keyboardinput(str(self.button_6n))
        #self.QLabel.setText(str(self.button_6n))

    def button_click7(self):
        self.keyboardinput(str(self.button_7n))
        #self.QLabel.setText(str(self.button_7n))

    def button_click8(self):
        self.keyboardinput(str(self.button_8n))
        #self.QLabel.setText(str(self.button_8n))

    def button_click9(self):
        self.keyboardinput(str(self.button_9n))
        #self.QLabel.setText(str(self.button_9n))

    def button_click0(self):
        self.keyboardinput(str(self.button_0n))
        #self.QLabel.setText(str(self.button_0n))

    def button_clicka(self):
        self.keyboardinput(str(self.button_an))
        #self.QLabel.setText(str(self.button_an))

    def button_clickb(self):
        self.keyboardinput(str(self.button_bn))
        #self.QLabel.setText(str(self.button_bn))

    def button_clickc(self):
        self.keyboardinput(str(self.button_cn))
        #self.QLabel.setText(str(self.button_cn))

    def button_clickd(self):
        self.keyboardinput(str(self.button_dn))
        #self.QLabel.setText(str(self.button_dn))

    def button_clicke(self):
        self.keyboardinput(str(self.button_en))
        #self.QLabel.setText(str(self.button_en))

    def button_clickf(self):
        self.keyboardinput(str(self.button_fn))
        #self.QLabel.setText(str(self.button_fn))

    def button_clickg(self):
        self.keyboardinput(str(self.button_gn))
        #self.QLabel.setText(str(self.button_gn))

    def button_clickh(self):
        self.keyboardinput(str(self.button_hn))
        #self.QLabel.setText(str(self.button_hn))

    def button_clicki(self):
        self.keyboardinput(str(self.button_in))
        #self.QLabel.setText(str(self.button_in))

    def button_clickj(self):
        self.keyboardinput(str(self.button_jn))
        #self.QLabel.setText(str(self.button_jn))

    def button_clickk(self):
        self.keyboardinput(str(self.button_kn))
        #self.QLabel.setText(str(self.button_kn))

    def button_clickl(self):
        self.keyboardinput(str(self.button_ln))
        #self.QLabel.setText(str(self.button_ln))

    def button_clickm(self):
        self.keyboardinput(str(self.button_mn))
        #self.QLabel.setText(str(self.button_mn))

    def button_clickn(self):
        self.keyboardinput(str(self.button_nn))
        #self.QLabel.setText(str(self.button_nn))

    def button_clicko(self):
        self.keyboardinput(str(self.button_on))
        #self.QLabel.setText(str(self.button_on))

    def button_clickp(self):
        self.keyboardinput(str(self.button_pn))
        #self.QLabel.setText(str(self.button_pn))

    def button_clickq(self):
        self.keyboardinput(str(self.button_qn))
        #self.QLabel.setText(str(self.button_qn))

    def button_clickr(self):
        self.keyboardinput(str(self.button_rn))
        #self.QLabel.setText(str(self.button_rn))

    def button_clicks(self):
        self.keyboardinput(str(self.button_sn))
        #self.QLabel.setText(str(self.button_sn))

    def button_clickt(self):
        self.keyboardinput(str(self.button_tn))
        #self.QLabel.setText(str(self.button_tn))

    def button_clicku(self):
        self.keyboardinput(str(self.button_un))
        #self.QLabel.setText(str(self.button_un))

    def button_clickv(self):
        self.keyboardinput(str(self.button_vn))
        #self.QLabel.setText(str(self.button_vn))

    def button_clickw(self):
        self.keyboardinput(str(self.button_wn))
        #self.QLabel.setText(str(self.button_wn))

    def button_clickx(self):
        self.keyboardinput(str(self.button_xn))
        #self.QLabel.setText(str(self.button_xn))

    def button_clicky(self):
        self.keyboardinput(str(self.button_yn))
        #self.QLabel.setText(str(self.button_yn))

    def button_clickz(self):
        self.keyboardinput(str(self.button_zn))
        #self.QLabel.setText(str(self.button_zn))

    def button_clickspace(self):
        self.keyboardinput(str(self.button_spacen))
        #self.QLabel.setText(str(self.button_spacen))

    def button_clickclear(self):
        self.keyboardinputclear()

    def  update_graph ( self ):
        self.animation = self.MplWidget.animation.FuncAnimation(self.MplWidget.canvas.axes.figure, self.animate, frames=n, interval=interval)
        self.MplWidget.show()
        self.MplWidget.set_layout()

        self.animation_2 = self.MplWidget_2.animation.FuncAnimation(self.MplWidget_2.canvas.axes.figure, self.animate_meditation, frames=n, interval=interval)
        self.MplWidget_2.show()
        self.MplWidget_2.set_layout()

        self.animation_3 = self.MplWidget_3.animation.FuncAnimation(self.MplWidget_3.canvas.axes.figure, self.animate_alpha, frames=n, interval=interval)
        self.MplWidget_3.show()
        self.MplWidget_3.set_layout()

        self.animation_4 = self.MplWidget_4.animation.FuncAnimation(self.MplWidget_4.canvas.axes.figure, self.animate_delta, frames=n, interval=interval)
        self.MplWidget_4.show()
        self.MplWidget_4.set_layout()

        self.animation_5 = self.MplWidget_5.animation.FuncAnimation(self.MplWidget_5.canvas.axes.figure, self.animate_theta, frames=n, interval=interval)
        self.MplWidget_5.show()
        self.MplWidget_5.set_layout()

    def animate(self, data):
        x_time = np.arange(0+data, 50 + data, 0.1)
        y_attention  = np.sin (x_time )

        self . MplWidget . canvas . axes . clear ()
        self . MplWidget . canvas . axes . plot ( x_time ,  y_attention)
        self . MplWidget . canvas . axes . legend (( 'Attention' ),loc = 'upper right' )
        self . MplWidget . canvas . axes . set_title ( 'Attention Signal' )
        self . MplWidget . canvas . draw()

        return self.animation

    def animate_meditation(self, data):
        x_time = np.arange(0+data, 50 + data, 0.1)
        y_meditation  = np.cos (x_time )

        self . MplWidget_2 . canvas . axes . clear ()
        self . MplWidget_2 . canvas . axes . plot ( x_time ,  y_meditation)
        self . MplWidget_2 . canvas . axes . legend (( 'Meditation' ),loc = 'upper right' )
        self . MplWidget_2 . canvas . axes . set_title ( 'Meditation Signal' )
        self . MplWidget_2 . canvas . draw()

        return self.animation_2

    def animate_alpha(self, data):
        x_time = np.arange(0+data, 50 + data, 0.1)
        y_meditation  = np.cos (x_time )

        self . MplWidget_3 . canvas . axes . clear ()
        self . MplWidget_3 . canvas . axes . plot ( x_time ,  y_meditation)
        self . MplWidget_3 . canvas . axes . legend (( 'Alpha' ),loc = 'upper right' )
        self . MplWidget_3 . canvas . axes . set_title ( 'Alpha Signal' )
        self . MplWidget_3 . canvas . draw()

        return self.animation_3

    def animate_delta(self, data):
        x_time = np.arange(0+data, 50 + data, 0.1)
        y_meditation  = np.cos (x_time )

        self . MplWidget_4 . canvas . axes . clear ()
        self . MplWidget_4 . canvas . axes . plot ( x_time ,  y_meditation)
        self . MplWidget_4 . canvas . axes . legend (( 'Delta' ),loc = 'upper right' )
        self . MplWidget_4 . canvas . axes . set_title ( 'Delta Signal' )
        self . MplWidget_4 . canvas . draw()

        return self.animation_4

    def animate_theta(self, data):
        x_time = np.arange(0+data, 50 + data, 0.1)
        y_meditation  = np.cos (x_time )

        self . MplWidget_5 . canvas . axes . clear ()
        self . MplWidget_5 . canvas . axes . plot ( x_time ,  y_meditation)
        self . MplWidget_5 . canvas . axes . legend (( 'Theta' ),loc = 'upper right' )
        self . MplWidget_5 . canvas . axes . set_title ( 'Theta Signal' )
        self . MplWidget_5 . canvas . draw()

        return self.animation_5



app  =  QApplication ([])
window  =  MatplotlibWidget ()
# window.show ()
buttonpass=window.button
outputpass=window.output
keyboardobj=Keyboard()
t = threading.Thread(target = keyboardobj.loopkey, args=(buttonpass,outputpass,1),daemon=True)
w = threading.Thread(target=window.show())
w.start()
t.start()
app . exec_ ()
