#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from PyQt5.QtMultimedia import *
#from PyQt5.QtQuick import *
from PyQt5.uic import *
#from PyQt5.QtQml import *
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QEvent
import psutil
import platform



#-------------------------------------------------
    
__author__ = '__Bill__'



class _Window_(QMainWindow):
    """
    -------------------(_Progress Bar_)------------------
    """
    def __init__(self):
        super().__init__()
        print(_Window_.__doc__)


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

        self.red = (255, 0, 0)
        self.orange = (255, 128, 0, 0)
        self.yellow = (255, 255, 0, 20)
        self.green = (2, 75, 15, 70)
        self.violet = (126, 104, 255, 10)
        self.hex_green = ('#024913')
        self.blue = (100, 149, 237, 99)


        self.radius = """QProgressBar{
                            border: 2px solid grey;
                            border-radius: 5px;
                            text-align: center;
                            chunk {background: rgba(0, 0, 255, 60);
                        }"""


        self.DEFAULT_STYLE =  """QProgressBar::chunk {background-color: #ff0000; }"""

        self.new_style = """QProgressBar {
                              border: 1px solid grey;
                              border-radius: 10px;
                              text-align: center;
                              background-color: #00000000;
                              chunk: rgba(100, 149, 237, 50);
                              }
                              """



        self.chunk = """QProgressBar:vertical
                        {
                        border: 0px solid gray;
                        border-radius: 10px;
                        background: #00000000;
                        padding: 1px;
                        }
                        QProgressBar::chunk:vertical {
                        background: qlineargradient(x1: 1, y1: 1, x2: 1,
                        y2: 0, stop: 0 yellow, stop: 1 orange, stop: 2 red);
                       
                        }"""


        self.chunk_vertical = """QProgressBar:vertical
                        {
                        border: 0px solid gray;
                        border-radius: 10px;
                        background: #00000000;
                        padding: 1px;
                        }
                        QProgressBar::chunk:vertical {
                        background: qlineargradient(x1: 1, y1: 1, x2: 1,
                        y2: 0, stop: 0 rgba(2, 75, 15, 80), stop: 1 rgba(255, 128, 0, 25), stop: 2 purple);
                       
                        }"""


        self.chunk_horizontal_1 = """QProgressBar:horizontal
                                {
                                    border: 0px solid gray;
                                    border-radius: 3px;
                                    background: #00000000;
                                    padding: 1px;
                                }
                                    QProgressBar::chunk:horizontal
                                {
                                    background: qlineargradient(x1: 0, y1: 1, x2: 1, y2: 1,
                                    stop: 0 rgba(55, 128, 100, 85),
                                    stop: 1 rgba(255, 28, 0, 85));
                                }"""




        self.chunk_horizontal_2 = """QProgressBar:horizontal
                                {
                                    border: 0px solid gray;
                                    border-radius: 3px;
                                    background: #00000000;
                                    padding: 1px;
                                }
                                    QProgressBar::chunk:horizontal
                                {
                                    background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5,
                                    stop: 0 rgba(55, 18, 180, 85),
                                    stop: 1 rgba(239, 231, 115, 85));
                                }"""


        self.chunk_horizontal_3 = """QProgressBar:horizontal
                                {
                                    border: 0px solid gray;
                                    border-radius: 10px;
                                    background: #00000000;
                                    padding: 0px;
                                }
                                    QProgressBar::chunk:horizontal
                                {
                                    background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5,
                                    stop: 0 rgba(5, 118, 50, 85),
                                    stop: 1 rgba(25, 188, 190, 85));
                                }"""


        # mess with border-radius, thatDarklordGuy!
        self.sheet = ( """
                                color: rgba(237,174,28,70%);
                                background-color: rgba(0,0,0,100%);
                                text-align: center;
                                border-radius: 150px;
                                border: 1px solid rgba(237,174,28,70%);
                                padding: 0px;
                                """)
                        

        self.violet = """QProgressBar::chunk {background: rgba(0, 0, 255, 60);}"""
        self.cornflower_blue = """QProgressBar::chunk {background: rgba(100, 149, 237, 50);}"""
                           

        self.move_bar_1 = 0
        self.move_bar_2 = 0
        self.move_bar_3 = 0

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
        self.setStyleSheet('font-size: 18pt; font-family: Cronyx;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(125,125,125, 95))#<--change label color
        self._label.setPalette(self.palette)
#--------------        
        _label.setText   ('SYSTEM INFO:')
        #self._label.setWordWrap  (True)
        _label.setGeometry(120,0, 150,105)




    def labels__(self):


        self.architecture = platform.architecture()
        self.node = platform.node()
        self.linux_distribution = platform.linux_distribution()
        
#---------------------------system
        
        self.setStyleSheet('font-size: 15pt; font-family: Cronyx;')
        self.label_arch = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(25,25,25, 95))#<--change label color
        self.label_arch.setPalette(self.palette)
        
        self.label_arch.setText      ('architecture:' + str(self.architecture))#<---value from psutil:boot
        self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_arch.setAlignment (Qt.AlignLeft)
        self.label_arch.move         (120,75)
        self.label_arch.adjustSize ()#<-----------adj label size---o
        self.label_arch.raise_()


#---------------------------NODE
        
        self.setStyleSheet('font-size: 15pt; font-family: Cronyx;')
        self.label_node = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(25,25,25, 95))#<--change label color
        self.label_node.setPalette(self.palette)
        
        self.label_node.setText      ('node:' + str(self.node))#<---value from psutil:boot
        self.label_node.setWordWrap  (True)#<---------allow more text in label----o
        self.label_node.setAlignment (Qt.AlignLeft)
        self.label_node.move         (120,135)
        self.label_node.adjustSize ()#<-----------adj label size---o
        self.label_node.raise_()

#---------------------------linux_distribution
        
        self.setStyleSheet('font-size: 15pt; font-family: Cronyx;')
        self.label_dist = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(25,25,25, 95))#<--change label color
        self.label_dist.setPalette(self.palette)
        
        self.label_dist.setText      ('linux_distribution:' + str(self.linux_distribution))#<---value from psutil:boot
        self.label_dist.setWordWrap  (True)#<---------allow more text in label----o
        self.label_dist.setAlignment (Qt.AlignLeft)
        self.label_dist.move         (70,175)
        self.label_dist.adjustSize ()#<-----------adj label size---o
        self.label_dist.raise_()        

        
#---------------------------boot
        
        self.setStyleSheet('font-size: 15pt; font-family: Cronyx;')
        self.text_label_boot = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(25,25,25, 95))#<--change label color
        self.text_label_boot.setPalette(self.palette)
        
        self.text_label_boot.setText      (' bootup time: ' + str(self.boottime) + ' seconds')#<---value from psutil:boot
        
        self.text_label_boot.setWordWrap  (True)#<---------allow more text in label----o
        self.text_label_boot.setAlignment (Qt.AlignLeft)
        self.text_label_boot.move         (120,235)
        self.text_label_boot.adjustSize ()#<-----------adj label size---o
        self.text_label_boot.raise_()

       
#---------------------------cpu temp
        
        self.setStyleSheet('font-size: 15pt; font-family: Cronyx;')
        self.text_label_cpu = QLabel (self)
        text_label_cpu = self.text_label_cpu
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(95,25,25, 95))
        self.text_label_cpu.setPalette(self.palette)
        
        text_label_cpu.setText      ("\r\n" + ' CPU temps: ' + str(self.temperatures) + '°C')
        text_label_cpu.setWordWrap  (True)
        text_label_cpu.setAlignment (Qt.AlignLeft)
        text_label_cpu.move         (120,375)
        text_label_cpu.adjustSize   ()
        text_label_cpu.raise_()



#---------------------------disk usage
        
        self.setStyleSheet('font-size: 15pt; font-family: Cronyx;')
        self.text_label_disc = QLabel (self)
        text_label_disc = self.text_label_disc
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(0,0,125, 95))
        text_label_disc.setPalette(self.palette)
        
        text_label_disc.setText      ("\r\n" + ' disc usage: ' + str(self.disk) + '%')
        text_label_disc.setWordWrap  (True)
        text_label_disc.setAlignment (Qt.AlignLeft)
        text_label_disc.move         (120,425)
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
##
##        print('temperatures' , self.temperatures)
##        print()  


#--------------------update labels with info each tick----------

        self.text_label_cpu.setText      ("\r\n" + ' CPU temps: ' + str(self.temperatures) + '°C')
        self.text_label_disc.setText      ("\r\n" + ' disc usage: ' + str(self.disk) + '%')
     





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
                | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
                        #position  #size
        self.setGeometry(1560,50, 350,525)
        self.setWindowTitle('Conky Like Widget')
        self.setVisible(False)
        self.exitOnClose = False


        self.show()





        

if __name__ == '__main__':
    app = QApplication([])
    #tray = SystemTrayIcon()
    _Win_ = _Window_()
    app.exec_()
