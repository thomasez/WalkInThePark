#!/usr/bin/env python
 
import os
import sys
import platform
import argparse
 
import PySide
from PySide.QtGui import QApplication, QMainWindow, QTextEdit,\
                         QPushButton,  QMessageBox

sys.path.append('./lib/')

__version__ = '0.1.0'
from score_ui  import Ui_MainWindow
from score_lib import Player, Course, Walk, saveScore
 
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.course = Course('Ekeberg');
        self.walk = Walk(self.course)
        self.player = Player();
        self.player.setName('ez')
        self.walk.setPlayer(self.player)
        self.setupUi(self)
        # Hard coding debug! Wonder how long time this one will last.
        if os.environ['USER'] != 'thomasez':
            self.showFullScreen()
        self.actionShow_GPL.triggered.connect(self.showGPL)
        self.actionAbout.triggered.connect(self.about)        
        self.Plus.clicked.connect(self.plus)        
        self.Minus.clicked.connect(self.minus)        
        self.Next.clicked.connect(self.next)        
        self.Done.clicked.connect(self.done)        
        self.Previous.clicked.connect(self.previous)        
        self.Throws.display(0)
        self.Done.setEnabled(True)

    def setPebble(self, pebble):
        self.pebble = pebble
        if self.pebble:
            def music_control_handler(endpoint, resp):
                if resp == "PLAYPAUSE":
                    self.next()
                    #print 'PLAYPAUSE!'
                elif resp == "PREVIOUS":
                    self.minus()
                    #print 'PREVIOUS!'
                elif resp == "NEXT":
                    self.plus()
                    #print 'NEXT!'

            self.pebble.getPebble().register_endpoint("MUSIC_CONTROL", music_control_handler)
            #print 'waiting for control events'

    def redraw(self):
        bnum = self.walk.getBasket()
        par = self.course.getPar(bnum)
        btxt = str(self.course.getName()) +  " - Basket " + str(bnum) + " - Par " + str(par)
        self.Basketnum.setText(btxt)
        self.Playername.setText("Player 1")
        throws = self.walk.getThrows()
        self.Throws.display(throws)
        total = self.walk.getResult()
        totaltxt = "Total:\t" + str(total['score']) + "\nPar:\t" + str(total['par']) + "\n"
        totaltxt += "Res:\t" + str(total['result'])
        totaltxt += "  (FH:" + str(total['res_first']) + " / "
        totaltxt += str(total['par_first']) + " )"
        totaltxt += " (SH:" + str(total['res_second']) + " / "
        totaltxt += str(total['par_second']) + " )"
        self.Total.setText(totaltxt)
        if self.walk.isDone():
            self.Done.setText('Done')
        else:
            self.Done.setText('Save')
        # print "Pebble:" + str(self.pebble)
        if self.pebble:
            btxt = "Basket " + str(bnum)
            rtxt = "Res:\t" + str(total['result']) + "\nPar:\t" + str(total['par']) + "\n"
            self.pebble.update_screen(btxt, throws, rtxt)

    def next(self):
        self.walk.nextBasket()
        self.redraw()
       
    def previous(self):
        self.walk.previousBasket()
        self.redraw()
       
    def plus(self):
        self.walk.addThrow(1)
        self.redraw()
       
    def minus(self):
        self.walk.subtractThrow(1)
        self.redraw()
       
    def done(self):
        saveScore(self.walk)
        total = self.walk.getScoreTotal()
        txt = "have saved?, Total:" + str(total['score'] + " Par:" + total['par'])
        QMessageBox.about(self, "Done!", txt)

    def showGPL(self):
        '''Read and display GPL licence.'''
        self.textEdit.setText(open('COPYING.txt').read())
       
    def about(self):
        '''Popup a box with about message.'''
        QMessageBox.about(self, "About the Golf scor app",
                """<b> About this program </b> v %s
               <p>Copyright 2013 Thomas Lundquist</p>
               <p>All rights reserved in accordance with
               GPL v2 or later - NO WARRANTIES!</p>
               <p>This app was coocked from Joe Biggs PuSide exaples.
               <p>Python %s -  PySide version %s - Qt version %s on %s""" % \
                (__version__, platform.python_version(), PySide.__version__,\
                 PySide.QtCore.__version__, platform.system()))      
       
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scorecard for your golf round')
    parser.add_argument('--pebble', help='Turn on Pebble support', action='store_true')
    parser.add_argument('--pebble_id', type=str, help='the last 4 digits of the target Pebble\'s MAC address. \nNOTE: if \
                        --lightblue is set, providing a full MAC address (ex: "A0:1B:C0:D3:DC:93") won\'t require the pebble \
                        to be discoverable and will be faster')
    parser.add_argument('--lightblue', action="store_true", help='use LightBlue bluetooth API')
    parser.add_argument('--pair', action="store_true", help='pair to the pebble from LightBlue bluetooth API before connecting.')
    args = parser.parse_args()
    pebble = False
    if args.pebble:
        from pebble_buttons import PebbleButtons
        pebble_id = args.pebble_id
        if pebble_id is None and "PEBBLE_ID" in os.environ:
            pebble_id = os.environ["PEBBLE_ID"]
        pebble = PebbleButtons(pebble_id, args.lightblue, args.pair)

    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.setPebble(pebble)
    frame.redraw()
    frame.show()
    app.exec_()

