#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.uic import *
import psutil
import platform
from decimal import *

#-------------------------------------------------
    
__author__ = '__Bill__'



class _Window_(QMainWindow):
    """
    -------------------(_Progress Bar_)------------------
    """
    def __init__(self):
        super().__init__()
        print(_Window_.__doc__)


        self.net_io = psutil.net_io_counters(pernic=False)
        print('net_io_counters - ', self.net_io)
        print()
        print('bytes sent: ', self.net_io[0])
        print('bytes recieved: ', self.net_io[1])

        self.disc_io = psutil.disk_io_counters(perdisk=False, nowrap=True)
        print('disc_io_counters - ', self.disc_io)
        print()
        print('byte(s) read: ', self.disc_io[0])
        print('byte(s) write: ', self.disc_io[1])

        #print(self.net_io("read_count"), self.net_io("write_count"))

#---------------create drop shadow-------------------o
        
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setBlurRadius(10)
        self.effect.setXOffset(5)
        self.effect.setYOffset(-5)
        self.effect.setColor(Qt.black)
        #self.taskbar_button = QWinTaskbarButton()


#-------------------read temps for cpu ------------------

        self.temps = psutil.sensors_temperatures()
        self.temp_entrys = self.temps.keys()
        self.core = self.temps['coretemp']

        self.disk = psutil.disk_usage('/')[3]
        print('self.disk ', self.disk)
        
        counter = (0)
        for entry in self.core:
            #print("     %s °C " % (entry.current))
            if counter == (0):
                self.temperatures = entry.current
                counter += (1)

        print('temperatures' , self.temperatures)
        print()
        print('architecture: ', platform.architecture())
        print('node: ', platform.node())
        print('linux_distribution: ', platform.linux_distribution())
        print()


        self.architecture = platform.architecture()
        self.node = platform.node()
        self.linux_distribution = platform.linux_distribution()









     
 #<--------------- set QPalette for label----------------->#

        self.palette = QPalette()
        self.brush = self.palette.setBrush
        self.background = QPalette.Background
        self.brush(self.background, QBrush(QImage("brushed1")))
        self.setPalette(self.palette)

        
#-=----------------- psutil data ------------------------
        
        self.cpu_percentage = psutil.cpu_percent(interval=0.05)
        print('self.cpu_percentage ', self.cpu_percentage ,'%')
        print()
        self.cpu_cores = psutil.cpu_percent(interval=0.05, percpu=True)
        print('cpu_core 1 and 2: ', psutil.cpu_percent(interval=1, percpu=True), '%')
        print()
        self.mem_2 = psutil.virtual_memory()[2]
        self.memory = psutil.virtual_memory()[5]
        self.memory_percent = self.memory / 800000000
        print('self.mem_2', self.mem_2)
        print('memory ', self.memory)
        print()
        print('memory_percent ', self.memory_percent)
        self.disk = psutil.disk_usage('/')[3]
        print('disk_used: ', psutil.disk_usage('/')[3], '%')
        print()
        self.freq = psutil.cpu_freq(percpu=False)[0]/1000*10
        self.cpu_freq = self.freq / 3.2 * 10
        self.boottime = psutil.boot_time() /100000000 




#-------------------------------------------------------------

  
        self.total_physical_memory = 8259145728
        self.percent_mem = 100 / 8.26
        print('percent_mem ', self.percent_mem)
        self.percentage_of_used_memory = self.memory * self.percent_mem
        
        print()
        print('self.percentage_of_used_memory ', self.percentage_of_used_memory / 1000000000)

        
        print(self.cpu_percentage)
        print(self.cpu_cores[0])
        print(self.cpu_cores[1])
        print(psutil.virtual_memory()[2])
        print(psutil.disk_usage('/')[3])
        print(self.cpu_freq)






#--------------------------------------------



        self.move_gui_x = 0
        self.move_gui_y = 0

        self.timer  = QTimer()
        self.timer.timeout.connect(self.update_bar__)
        self.timer.start(100)
        
        self.title__()
        self.labels__()
        self.initGUI()
        



    def title__(self):
 
        _label = QLabel  (self)
        self._label = _label
#--------------
        self.setStyleSheet('font-size: 15pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(100,100,100, 95))#<--change label color
        self._label.setPalette(self.palette)
#--------------        
        _label.setText   ('SYSTEM INFO:')
        #self._label.setWordWrap  (True)
        _label.setGeometry(120,0, 150,105)
        self._label.setAlignment (Qt.AlignCenter)
        _label.move(80,0)




    def labels__(self):


        self.architecture = platform.architecture()
        self.node = platform.node()
        self.linux_distribution = platform.linux_distribution()
        
#---------------------------system
        
        self.setStyleSheet('font-size: 15pt; font-family: Ubuntu;')
        self.label_arch = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(25,25,25, 95))#<--change label color
        self.label_arch.setPalette(self.palette)
        
        self.label_arch.setText      ('architecture:' + str(self.architecture))#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_arch.setAlignment (Qt.AlignLeft)
        self.label_arch.move         (40,80)
        self.label_arch.adjustSize ()#<-----------adj label size---o
        self.label_arch.raise_()


#---------------------------NODE
        
        self.setStyleSheet('font-size: 15pt; font-family: Ubuntu;')
        self.label_node = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(25,25,25, 95))#<--change label color
        self.label_node.setPalette(self.palette)
        
        self.label_node.setText      ('node:' + str(self.node))#<---value from psutil:boot
        self.label_node.setWordWrap  (True)#<---------allow more text in label----o
        self.label_node.setAlignment (Qt.AlignLeft)
        self.label_node.move         (100,135)
        self.label_node.adjustSize ()#<-----------adj label size---o
        self.label_node.raise_()

#---------------------------linux_distribution
        
        self.setStyleSheet('font-size: 15pt; font-family: Ubuntu;')
        self.label_dist = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(25,25,25, 95))#<--change label color
        self.label_dist.setPalette(self.palette)
        
        self.label_dist.setText(str(self.linux_distribution))
        self.label_dist.setWordWrap  (False)#<---------allow more text in label----o
        self.label_dist.setAlignment (Qt.AlignLeft)
        self.label_dist.move         (20,175)
        self.label_dist.adjustSize ()#<-----------adj label size---o
        self.label_dist.raise_()        

        
#---------------------------boot
        
        self.setStyleSheet('font-size: 15pt; font-family: Ubuntu;')
        self.text_label_boot = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(25,25,25, 95))#<--change label color
        self.text_label_boot.setPalette(self.palette)
        
        self.text_label_boot.setText      (' bootup time: ' + str(round(self.boottime, 1)) + ' seconds')#<---value from psutil:boot
        
        #self.text_label_boot.setWordWrap  (True)#<---------allow more text in label----o
        self.text_label_boot.setAlignment (Qt.AlignLeft)
        self.text_label_boot.move         (15,235)
        self.text_label_boot.adjustSize ()#<-----------adj label size---o
        self.text_label_boot.raise_()




#----------------net io----------------------o


        self.net_io = psutil.net_io_counters(pernic=False)
        print('net_io_counters - ', self.net_io)
        print()
        print('bytes sent: ', self.net_io[0])
        print('bytes recieved: ', self.net_io[1])
        


        #self.net_io[0] = self.net_io[0]/1000000
        print('self.net_io/1000000  ', self.net_io[0]/1000000)
        
        self.setStyleSheet('font-size: 15pt; font-family: Ubuntu;')
        self.text_label_net = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(102, 0, 204, 95))#<--change label color
        self.text_label_net.setPalette(self.palette)


        
        getcontext().prec = 1
        
        
        self.text_label_net.setText(' bytes sent/recieved: ' + str(round(self.net_io[0]/1000000, 1)) + 'MB  '
                                     + str(round(self.net_io[1]/1000000000, 1)) + 'GB')#<---value from psutil:boot

  
        self.text_label_net.setAlignment (Qt.AlignLeft)
        self.text_label_net.move         (5,300)
        self.text_label_net.adjustSize ()#<-----------adj label size---o
        self.text_label_net.raise_()
        



#----------------disc io----------------------o


        self.disc_io = psutil.disk_io_counters(perdisk=False, nowrap=True)
        print('disc_io_counters - ', self.disc_io)
        print()
        print('byte(s) read: ', self.disc_io[0])
        print('byte(s) write: ', self.disc_io[1])




        #self.net_io[0] = self.net_io[0]/1000000
        print('self.net_io/1000000  ', self.net_io[0]/1000000)
        
        self.setStyleSheet('font-size: 15pt; font-family: Ubuntu;')
        self.text_label_disc_io = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(102, 51, 0, 85))#<--change label color
        self.text_label_disc_io.setPalette(self.palette)


        
        getcontext().prec = 3
        
        
        self.text_label_disc_io.setText(' bytes read/write: ' + str(round(self.disc_io[2]/1000000000, 3)) + 'GB  '
                                     + str(round(self.disc_io[3]/1000000000, 3)) + 'GB')#<---value from psutil:boot

  
        self.text_label_disc_io.setAlignment (Qt.AlignLeft)
        self.text_label_disc_io.move         (5,350)
        self.text_label_disc_io.adjustSize ()#<-----------adj label size---o
        self.text_label_disc_io.raise_()



       
#---------------------------cpu temp
        
        self.setStyleSheet('font-size: 15pt; font-family: Ubuntu;')
        self.text_label_cpu = QLabel (self)
        text_label_cpu = self.text_label_cpu
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(95,25,25, 95))
        self.text_label_cpu.setPalette(self.palette)
        
        text_label_cpu.setText      ("\r\n" + ' CPU temps: ' + str(self.temperatures) + '°C')
        text_label_cpu.setWordWrap  (True)
        text_label_cpu.setAlignment (Qt.AlignLeft)
        text_label_cpu.move         (80,375)
        text_label_cpu.adjustSize   ()
        text_label_cpu.raise_()



#---------------------------disk usage
        
        self.setStyleSheet('font-size: 15pt; font-family: Ubuntu;')
        self.text_label_disc = QLabel (self)
        text_label_disc = self.text_label_disc
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(0,0,125, 95))
        text_label_disc.setPalette(self.palette)
        
        text_label_disc.setText      ("\r\n" + ' disc usage: ' + str(self.disk) + '%')
        text_label_disc.setWordWrap  (True)
        text_label_disc.setAlignment (Qt.AlignLeft)
        text_label_disc.move         (90,425)
        text_label_disc.adjustSize   ()
        text_label_disc.raise_()





    def update_bar__(self):
        
        
        
        for proc in psutil.process_iter():
            pass        
        
        self.cpu_percentage = psutil.cpu_percent(interval=0.25)
        self.cpu_cores = psutil.cpu_percent(interval=0.25, percpu=True)
        self.memory = psutil.virtual_memory()[2]
        self.disk = psutil.disk_usage('/')[3]
        self.freq = psutil.cpu_freq(percpu=False)[0]/1000*10
        self.cpu_freq = self.freq / 3.2 * 10

        self.disc_io = psutil.disk_io_counters(perdisk=False)
        self.net_io = psutil.net_io_counters(pernic=False)

#---------------------boot time----------------------------
                    
        #self.boottime = psutil.boot_time() /10000000
        #print('boot time: ', self.boottime, ' seconds')


    

#-------------------read temps for cpu ------------------

        temps = psutil.sensors_temperatures()
        temp_entrys = temps.keys()
        core = temps['coretemp']


        counter = (0)
        for entry in core:
            #print("     %s °C " % (entry.current))
            if counter == (0):
                self.temperatures = entry.current
                counter += (1)

##        print('temperatures' , self.temperatures)
##        print()  



#--------------------update labels with info each tick----------

        self.text_label_cpu.setText      ("\r\n" + ' CPU temps: ' + str(self.temperatures) + '°C')
        self.text_label_disc.setText      ("\r\n" + ' disc usage: ' + str(self.disk) + '%')




###----------------------------update net label -------------------------o
##        
        self.text_label_net.setText(' net sent/recieved: ' + str(round(self.net_io[0]/1000000, 1)) + 'MB  '
                                     + str(round(self.net_io[1]/1000000000, 1)) + 'GB')#<---value from psutil:boot



###----------------------------update disc label -------------------------o
##
        self.text_label_disc_io.setText(' disk read/write: ' + str(round(self.disc_io[0]/1000, 1)) + 'kB  '
                                     + str(round(self.disc_io[1]/1000, 1)) + 'kB')#<---value from psutil:boot





    def mousePressEvent(self, event):
        self.oPos = event.globalPos()
        
        if event.buttons() == Qt.NoButton:
            self.raise_()
##        elif event.buttons() == Qt.LeftButton:
##            self.raise_()
##        elif event.buttons() == Qt.RightButton:
##            self.raise_()
##        print('pressevent')
        
        elif event.buttons() == (Qt.RightButton): 
            #quit()
            print('mouse')
        else:
            pass





    def initGUI(self):

        self.setWindowFlags(Qt.FramelessWindowHint # hides the window controls     
                                | Qt.ToolTip
                                | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
                        #position  #size
        self.setGeometry(1560,50, 350,525)#x,y  size,size
        self.setWindowTitle('Conky Like Widget')
        
        self.setVisible(False)
        self.exitOnClose = False
        
        self.setGraphicsEffect(self.effect)
        self.trayIcon = QSystemTrayIcon(QIcon(), self)
        self.trayIcon.show()
        
        self.lower()
        self.show()





        

if __name__ == '__main__':
    app = QApplication([])
    #tray = SystemTrayIcon()
    _Win_ = _Window_()
    app.exec_()
