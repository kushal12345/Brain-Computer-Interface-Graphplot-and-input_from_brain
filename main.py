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
        #self.button_gn = '#'

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
        #self. button_clear.clicked.connect(self.button_clickh)



    def button_click1(self):
        #self.textboxValue = self.textbox.text()
        #self.textbox.setText(str(self.button_1n))
        self.QLabel.setText(str(self.button_1n))


    def button_click2(self):
        #self.textboxValue = self.textbox.text()
        #self.textbox.setText(str(self.button_2n))
        self.QLabel.setText(str(self.button_2n))

    def button_click3(self):
        self.QLabel.setText(str(self.button_3n))

    def button_click4(self):
        self.QLabel.setText(str(self.button_4n))

    def button_click5(self):
        self.QLabel.setText(str(self.button_5n))

    def button_click6(self):
        self.QLabel.setText(str(self.button_6n))

    def button_click7(self):
        self.QLabel.setText(str(self.button_7n))

    def button_click8(self):
        self.QLabel.setText(str(self.button_8n))

    def button_click9(self):
        self.QLabel.setText(str(self.button_9n))

    def button_click0(self):
        self.QLabel.setText(str(self.button_0n))

    def button_clicka(self):
        self.QLabel.setText(str(self.button_an))

    def button_clickb(self):
        self.QLabel.setText(str(self.button_bn))

    def button_clickc(self):
        self.QLabel.setText(str(self.button_cn))

    def button_clickd(self):
        self.QLabel.setText(str(self.button_dn))

    def button_clicke(self):
        self.QLabel.setText(str(self.button_en))

    def button_clickf(self):
        self.QLabel.setText(str(self.button_fn))

    def button_clickg(self):
        self.QLabel.setText(str(self.button_gn))

    def button_clickh(self):
        self.QLabel.setText(str(self.button_hn))

    def button_clicki(self):
        self.QLabel.setText(str(self.button_in))

    def button_clickj(self):
        self.QLabel.setText(str(self.button_jn))

    def button_clickk(self):
        self.QLabel.setText(str(self.button_kn))

    def button_clickl(self):
        self.QLabel.setText(str(self.button_ln))

    def button_clickm(self):
        self.QLabel.setText(str(self.button_mn))

    def button_clickn(self):
        self.QLabel.setText(str(self.button_nn))

    def button_clicko(self):
        self.QLabel.setText(str(self.button_on))

    def button_clickp(self):
        self.QLabel.setText(str(self.button_pn))

    def button_clickq(self):
        self.QLabel.setText(str(self.button_qn))

    def button_clickr(self):
        self.QLabel.setText(str(self.button_rn))

    def button_clicks(self):
        self.QLabel.setText(str(self.button_sn))

    def button_clickt(self):
        self.QLabel.setText(str(self.button_tn))

    def button_clicku(self):
        self.QLabel.setText(str(self.button_un))

    def button_clickv(self):
        self.QLabel.setText(str(self.button_vn))

    def button_clickw(self):
        self.QLabel.setText(str(self.button_wn))

    def button_clickx(self):
        self.QLabel.setText(str(self.button_xn))

    def button_clicky(self):
        self.QLabel.setText(str(self.button_yn))

    def button_clickz(self):
        self.QLabel.setText(str(self.button_zn))

    def button_clickspace(self):
        self.QLabel.setText(str(self.button_spacen))
    '''
    def button_click5(self):
        print(self.button_5n)
    '''




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
window . show ()
app . exec_ ()
