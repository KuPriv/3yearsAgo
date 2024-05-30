from datetime import datetime, timedelta
import time
import ctypes
import winsound
import os
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

# получаем путь до логов
path = os.getenv("AppData") + r"\.vimeworld\minigames\logs\latest.log"
time_11 = "00:00:00"
time_12 = "00:00:00"
time_13 = "00:00:00"
time_14 = "00:00:00"
time_15 = "00:00:00"
time_16 = "00:00:00"
time_17 = "00:00:00"
time_18 = "00:00:00"
time_19 = "00:00:00"
time_110 = "00:00:00"
time_111 = "00:00:00"
time_112 = "00:00:00"
der = "Фрака_Деревни"
der_time = "00:00:00"
centr = "Фрака_Центр"
centr_time = "00:00:00"
#fam_time = "00:00:00"
#fam_time2 = "00:00:00"
# Надо ли спешку уведомления
global call_msgbox
call_msgbox = True


def alarm():
    global call_msgbox
    q = ["12:52:00", "18:52:00", "00:52:00", "06:52:00", ]
    if call_msgbox:
        if str((QDateTime.currentDateTime().toString())[-13:-5]) in q:
            time.sleep(0.1)
            winsound.Beep(800, 600)
            if call_msgbox:
                ctypes.windll.user32.MessageBoxW(0, "Спешка будет через 3 минуты", "", 0x00010000)


def get_time_boss():
    with open(r'for_checker/123.txt', "r", encoding='utf-8') as F:
        data = F.readlines()
    global notification
    global time_11, time_12, time_13, time_14, time_15, time_16, time_17, time_18, time_19, time_110, time_111, time_112
    if data[0][0] != "q":
        time_11 = str(datetime.strptime(data[0][1:9], "%H:%M:%S") + timedelta(hours=0, minutes=20))[11:]
    if data[1][0] != "w":
        time_12 = str(datetime.strptime(data[1][1:9], "%H:%M:%S") + timedelta(hours=0, minutes=47))[11:]
    if data[2][0] != "e":
        time_13 = str(datetime.strptime(data[2][1:9], "%H:%M:%S") + timedelta(hours=1, minutes=00))[11:]
    if data[3][0] != "r":
        time_14 = str(datetime.strptime(data[3][1:9], "%H:%M:%S") + timedelta(hours=1, minutes=27))[11:]
    if data[4][0] != "t":
        time_15 = str(datetime.strptime(data[4][1:9], "%H:%M:%S") + timedelta(hours=1, minutes=30))[11:]
    if data[5][0] != "y":
        time_16 = str(datetime.strptime(data[5][1:9], "%H:%M:%S") + timedelta(hours=1, minutes=50))[11:]
    if data[6][0] != "u":
        time_17 = str(datetime.strptime(data[6][1:9], "%H:%M:%S") + timedelta(hours=2, minutes=35))[11:]
    if data[7][0] != "i":
        time_18 = str(datetime.strptime(data[7][1:9], "%H:%M:%S") + timedelta(hours=3, minutes=20))[11:]
    if data[8][0] != "o":
        time_19 = str(datetime.strptime(data[8][1:9], "%H:%M:%S") + timedelta(hours=2, minutes=40))[11:]
    if data[9][0] != "p":
        time_110 = str(datetime.strptime(data[9][1:9], "%H:%M:%S") + timedelta(hours=4, minutes=55))[11:]
    if data[10][0] != "a":
        time_111 = str(datetime.strptime(data[10][1:9], "%H:%M:%S") + timedelta(hours=5, minutes=55))[11:]
    if data[11][0] != "s":
        time_112 = str(datetime.strptime(data[11][1:9], "%H:%M:%S") + timedelta(hours=4, minutes=00))[11:]
    F.close()


def zna4_derev(line, s):
    global der
    der = s
    global der_time
    if s == "Азиаты":
        der = "Деревня,Азиаты:"
        der_time = str(datetime.strptime(line[1:9], "%H:%M:%S") + timedelta(hours=2, minutes=0))[11:]
    if s == "Белые":
        der = "Деревня,Белые:"
        der_time = str(datetime.strptime(line[1:9], "%H:%M:%S") + timedelta(hours=2, minutes=0))[11:]
    if s == "Ниггеры":
        der = "Деревня, Ниггеры:"
        der_time = str(datetime.strptime(line[1:9], "%H:%M:%S") + timedelta(hours=2, minutes=0))[11:]


def zna4_centr(line, s):
    global centr
    centr = s
    global centr_time
    if s == "Азиаты":
        centr = "Точка,Азиаты:"
        centr_time = str(datetime.strptime(line[1:9], "%H:%M:%S") + timedelta(hours=2, minutes=0))[11:]
    if s == "Белые":
        centr = "Точка,Белые:"
        centr_time = str(datetime.strptime(line[1:9], "%H:%M:%S") + timedelta(hours=2, minutes=0))[11:]
    if s == "Ниггеры":
        centr = "Точка, Ниггеры:"
        centr_time = str(datetime.strptime(line[1:9], "%H:%M:%S") + timedelta(hours=2, minutes=0))[11:]


"""def famka(line):
    global fam_time
    fam_time = str(datetime.strptime(line[1:9], "%H:%M:%S") + timedelta(hours=6, minutes=0))

def famka2(line):
    global fam_time2
    fam_time2 = str(datetime.strptime(line[1:9], "%H:%M:%S") + timedelta(hours=6, minutes=0))"""

def read_path():
    if os.path.exists(path):
        file = open(path, "r", encoding="utf-8")
        with open(r'for_checker/123.txt', 'r', encoding="utf-8") as f:
            data = f.readlines()
        while True:
            where = file.tell()
            line = file.readline()
            if len(line) == 0:
                data[12] = g
                f.close()
                save_changes = open(r'for_checker/123.txt', 'w', encoding="utf-8")
                save_changes.writelines(data)
                save_changes.close()
                break
            if line[0] == "[":
                g = line[1:9]
            if not line:
                try:
                    time.sleep(0.1)
                except KeyboardInterrupt:
                    os.kill(os.getpid(), 9)
                file.seek(where)
            else:
                """if " [Client thread/INFO]: Setting user:" in line:
                    if line.count("Koowang63") == 1 or line.count("Koowang") == 1:
                        None
                    else:
                        sys.exit()"""
                if " [Client thread/INFO]: [CHAT] Королевский зомби был повержен за" in line:
                    if line.count("[CHAT]") == 1:
                        data[0] = line
                if " [Client thread/INFO]: [CHAT] Холуй был повержен за" in line:
                    if line.count("[CHAT]") == 1:
                        data[1] = line
                if " [Client thread/INFO]: [CHAT] Сточный слизень был повержен за" in line:
                    if line.count("[CHAT]") == 1:
                        data[2] = line
                if " [Client thread/INFO]: [CHAT] Фенрир был повержен за" in line:
                    if line.count("[CHAT]") == 1:
                        data[3] = line
                if " [Client thread/INFO]: [CHAT] Все Всадники апокалипсиса были повержены за" in line:
                    if line.count("[CHAT]") == 1:
                        data[4] = line
                if " [Client thread/INFO]: [CHAT] Матка была повержена за" in line:
                    if line.count("[CHAT]") == 1:
                        data[5] = line
                if " [Client thread/INFO]: [CHAT] Коровка из Коровёнки была повержена за" in line:
                    if line.count("[CHAT]") == 1:
                        data[6] = line
                if " [Client thread/INFO]: [CHAT] Йети был повержен за" in line:
                    if line.count("[CHAT]") == 1:
                        data[7] = line
                if " [Client thread/INFO]: [CHAT] Левиафан был повержен за " in line:
                    if line.count("[CHAT]") == 1:
                        data[8] = line
                if " [Client thread/INFO]: [CHAT] Хранитель подводного мира был повержен за" in line:
                    if line.count("[CHAT]") == 1:
                        data[9] = line
                if " [Client thread/INFO]: [CHAT] Небесный владыка был повержен за" in line:
                    if line.count("[CHAT]") == 1:
                        data[10] = line
                if " [Client thread/INFO]: [CHAT] Житель края был повержен за" in line:
                    if line.count("[CHAT]") == 1:
                        data[11] = line
                if " [Client thread/INFO]: [CHAT] Точка в деревне Люфония была захвачена фракцией Азиатов" in line:
                    if line.count("[CHAT]") == 1:
                        zna4_derev(line, "Азиаты")
                if " [Client thread/INFO]: [CHAT] Точка в деревне Люфония была захвачена фракцией Белых" in line:
                    if line.count("[CHAT]") == 1:
                        zna4_derev(line, "Белые")
                if " [Client thread/INFO]: [CHAT] Точка в деревне Люфония была захвачена фракцией Ниггеров" in line:
                    if line.count("[CHAT]") == 1:
                        zna4_derev(line, "Ниггеры")
                if " [Client thread/INFO]: [CHAT] Центральная точка была захвачена фракцией Азиатов" in line:
                    if line.count("[CHAT]") == 1:
                        zna4_centr(line, "Азиаты")
                if " [Client thread/INFO]: [CHAT] Центральная точка была захвачена фракцией Белых" in line:
                    if line.count("[CHAT]") == 1:
                        zna4_centr(line, "Белые")
                if " [Client thread/INFO]: [CHAT] Центральная точка была захвачена фракцией Ниггеров" in line:
                    if line.count("[CHAT]") == 1:
                        zna4_centr(line, "Ниггеры")
                """if (" [Client thread/INFO]: [CHAT] Семья > Наша семья отбила атаку семьи игрока" in line) and "10 Звезд" in line:
                    if line.count("[CHAT]") == 1:
                        famka(line)
                if (" [Client thread/INFO]: [CHAT] Семья > Наша семья отбила атаку семьи игрока" in line) and "20 Звезд" in line:
                    if line.count("[CHAT]") == 1:
                        famka2(line)"""
                get_time_boss()
    else:
        print(f"Чел хорош)")

def func():
    print(1)
    global time_11
    global time_12
    global time_13
    global time_14
    global time_15
    global time_16
    global time_17
    global time_18
    global time_19
    global time_110
    global time_111
    global time_112
    global centr_time
    global der_time
    time_11 = "00:00:00"
    time_12 = "00:00:00"
    time_13 = "00:00:00"
    time_14 = "00:00:00"
    time_15 = "00:00:00"
    time_16 = "00:00:00"
    time_17 = "00:00:00"
    time_18 = "00:00:00"
    time_19 = "00:00:00"
    time_110 = "00:00:00"
    time_111 = "00:00:00"
    time_112 = "00:00:00"
    centr_time = "00:00:00"
    der_time = "00:00:00"
class Window(QMainWindow):
    global time_11
    global time_12
    global time_13
    global time_14
    global time_15
    global time_16
    global time_17
    global time_18
    global time_19
    global time_110
    global time_111
    global time_112
    global der
    global centr
    global der_time
    global centr_time
    global fam_time
    global fam_time2
    global call_msgbox
    global s

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Meow Meow")
        self.window
        self.setGeometry(1300, 100, 620, 540)
        self.setFixedSize(620, 540)
        self.setWindowIcon(QIcon(r'for_checker/LOGO.png'))
        self.setWindowIcon(QtGui.QIcon(r'for_checker/LOGO.png'))
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()
        self.setDisabled(True)
        self.editor = QTextEdit(self)
        self.editor.resize(620, 560)
        self.editor.setStyleSheet('QTextEdit{background-image:url("./for_checker/WIND.png");}')
        self.time_1 = QtWidgets.QLabel(self)
        self.time_2 = QtWidgets.QLabel(self)
        self.time_3 = QtWidgets.QLabel(self)
        self.time_4 = QtWidgets.QLabel(self)
        self.time_5 = QtWidgets.QLabel(self)
        self.time_6 = QtWidgets.QLabel(self)
        self.time_7 = QtWidgets.QLabel(self)
        self.time_8 = QtWidgets.QLabel(self)
        self.time_9 = QtWidgets.QLabel(self)
        self.time_10 = QtWidgets.QLabel(self)
        self.time_11 = QtWidgets.QLabel(self)
        self.time_12 = QtWidgets.QLabel(self)
        self.derev = QtWidgets.QLabel(self)
        self.derev_time = QtWidgets.QLabel(self)
        self.cent = QtWidgets.QLabel(self)
        self.cent_time = QtWidgets.QLabel(self)
        self.w = QtWidgets.QLabel(self)
        self.w2 = QtWidgets.QLabel(self)
        self.w3 = QtWidgets.QLabel(self)
        #self.f_time = QtWidgets.QLabel(self)
        #self.f_time2 = QtWidgets.QLabel(self)
        self.boss_1()
        self.boss_2()
        self.boss_3()
        self.boss_4()
        self.boss_5()
        self.boss_6()
        self.boss_7()
        self.boss_8()
        self.boss_9()
        self.boss_10()
        self.boss_11()
        self.boss_12()
        self.okno()
        self.top()
        self.txt_speh()
        self.chitaem()
        self.vrem2()
        #self.knopk()
        self.time_boss_1()
        self.time_boss_2()
        self.time_boss_3()
        self.time_boss_4()
        self.time_boss_5()
        self.time_boss_6()
        self.time_boss_7()
        self.time_boss_8()
        self.time_boss_9()
        self.time_boss_110()
        self.time_boss_111()
        self.time_boss_112()
        self.dereva_time()
        self.centa_time()
        self.fraca_d()
        self.fraca_c()
        self.real_time()
        #self.fam()
        #self.fam2()
        #self.famk_time()
        #self.famk_time2()

    def chitaem(self):
        format = "%H:%M:%S"
        if int(QDateTime.currentDateTime().toString()[-7:-4]) % 10 == 0:
            read_path()
            alarm()

        """if fam_time == "00:00:00":
            self.f_time.setText("Attack/no logs")
        else:
            self.f_time.setText(fam_time)

        if fam_time2 == "00:00:00":
            self.f_time2.setText("Attack/no logs")
        else:
            self.f_time2.setText(fam_time2)"""

        if time_11 == "00:00:00":
            self.time_1.setText("NO LOGS")
        else:
            self.time_1.setText(str(time_11))
            z = str(datetime.strptime(str(time_11), format) - datetime.strptime(
                str(QDateTime.currentDateTime().toString())[-13:-5], format))
            if z[1] == ":":
                z = "0" + z[0] + ":" + z[2:4] + ":" + z[5:7]
            if str(z) < "00:05:00" or str(z[0:2]) == "-1":
                self.time_1.setStyleSheet("color: rgb(140, 140, 140);")
        if time_12 == "00:00:00":
            self.time_2.setText("NO LOGS")
        else:
            self.time_2.setText(str(time_12))
            z = str(datetime.strptime(str(time_12), format) - datetime.strptime(
                str(QDateTime.currentDateTime().toString())[-13:-5], format))
            if z[1] == ":":
                z = "0" + z[0] + ":" + z[2:4] + ":" + z[5:7]
            if str(z) < "00:05:00" or str(z[0:2]) == "-1":
                self.time_2.setStyleSheet("color: rgb(140, 140, 140);")
        if time_13 == "00:00:00":
            self.time_3.setText("NO LOGS")
        else:
            self.time_3.setText(str(time_13))
            z = str(datetime.strptime(str(time_13), format) - datetime.strptime(
                str(QDateTime.currentDateTime().toString())[-13:-5], format))
            if z[1] == ":":
                z = "0" + z[0] + ":" + z[2:4] + ":" + z[5:7]
            if str(z) < "00:05:00" or str(z[0:2]) == "-1":
                self.time_3.setStyleSheet("color: rgb(140, 140, 140);")
        if time_14 == "00:00:00":
            self.time_4.setText("NO LOGS")
        else:
            self.time_4.setText(str(time_14))
            z = str(datetime.strptime(str(time_14), format) - datetime.strptime(
                str(QDateTime.currentDateTime().toString())[-13:-5], format))
            if z[1] == ":":
                z = "0" + z[0] + ":" + z[2:4] + ":" + z[5:7]
            if str(z) < "00:05:00" or str(z[0:2]) == "-1":
                self.time_4.setStyleSheet("color: rgb(140, 140, 140);")
        if time_15 == "00:00:00":
            self.time_5.setText("NO LOGS")
        else:
            self.time_5.setText(str(time_15))
            z = str(datetime.strptime(str(time_15), format) - datetime.strptime(
                str(QDateTime.currentDateTime().toString())[-13:-5], format))
            if z[1] == ":":
                z = "0" + z[0] + ":" + z[2:4] + ":" + z[5:7]
            if str(z) < "00:05:00" or str(z[0:2]) == "-1":
                self.time_5.setStyleSheet("color: rgb(140, 140, 140);")
        if time_16 == "00:00:00":
            self.time_6.setText("NO LOGS")
        else:
            self.time_6.setText(str(time_16))
            z = str(datetime.strptime(str(time_16), format) - datetime.strptime(
                str(QDateTime.currentDateTime().toString())[-13:-5], format))
            if z[1] == ":":
                z = "0" + z[0] + ":" + z[2:4] + ":" + z[5:7]
            if str(z) < "00:05:00" or str(z[0:2]) == "-1":
                self.time_6.setStyleSheet("color: rgb(140, 140, 140);")
        if time_17 == "00:00:00":
            self.time_7.setText("NO LOGS")
        else:
            self.time_7.setText(str(time_17))
            z = str(datetime.strptime(str(time_17), format) - datetime.strptime(
                str(QDateTime.currentDateTime().toString())[-13:-5], format))
            if z[1] == ":":
                z = "0" + z[0] + ":" + z[2:4] + ":" + z[5:7]
            if str(z) < "00:05:00" or str(z[0:2]) == "-1":
                self.time_7.setStyleSheet("color: rgb(140, 140, 140);")
        if time_18 == "00:00:00":
            self.time_8.setText("NO LOGS")
        else:
            self.time_8.setText(str(time_18))
            z = str(datetime.strptime(str(time_18), format) - datetime.strptime(
                str(QDateTime.currentDateTime().toString())[-13:-5], format))
            if z[1] == ":":
                z = "0" + z[0] + ":" + z[2:4] + ":" + z[5:7]
            if str(z) < "00:05:00" or str(z[0:2]) == "-1":
                self.time_8.setStyleSheet("color: rgb(140, 140, 140);")
        if time_19 == "00:00:00":
            self.time_9.setText("NO LOGS")
        else:
            self.time_9.setText(str(time_19))
            z = str(datetime.strptime(str(time_19), format) - datetime.strptime(
                str(QDateTime.currentDateTime().toString())[-13:-5], format))
            if z[1] == ":":
                z = "0" + z[0] + ":" + z[2:4] + ":" + z[5:7]
            if str(z) < "00:05:00" or str(z[0:2]) == "-1":
                self.time_9.setStyleSheet("color: rgb(140, 140, 140);")
        if time_110 == "00:00:00":
            self.time_10.setText("NO LOGS")
        else:
            self.time_10.setText(str(time_110))
            z = str(datetime.strptime(str(time_110), format) - datetime.strptime(
                str(QDateTime.currentDateTime().toString())[-13:-5], format))
            if z[1] == ":":
                z = "0" + z[0] + ":" + z[2:4] + ":" + z[5:7]
            if str(z) < "00:05:00" or str(z[0:2]) == "-1":
                self.time_10.setStyleSheet("color: rgb(140, 140, 140);")
        if time_111 == "00:00:00":
            self.time_11.setText("NO LOGS")
        else:
            self.time_11.setText(str(time_111))
            z = str(datetime.strptime(str(time_111), format) - datetime.strptime(
                str(QDateTime.currentDateTime().toString())[-13:-5], format))
            if z[1] == ":":
                z = "0" + z[0] + ":" + z[2:4] + ":" + z[5:7]
            if str(z) < "00:05:00" or str(z[0:2]) == "-1":
                self.time_11.setStyleSheet("color: rgb(140, 140, 140);")
        if time_112 == "00:00:00":
            self.time_12.setText("NO LOGS")
        else:
            self.time_12.setText(str(time_112))
            z = str(datetime.strptime(str(time_112), format) - datetime.strptime(
                str(QDateTime.currentDateTime().toString())[-13:-5], format))
            if z[1] == ":":
                z = "0" + z[0] + ":" + z[2:4] + ":" + z[5:7]
            if str(z) < "00:05:00" or str(z[0:2]) == "-1":
                self.time_12.setStyleSheet("color: rgb(140, 140, 140);")
        self.derev.setText(der)
        self.cent.setText(centr)
        if der_time == "00:00:00":
            self.derev_time.setText("NO LOGS")
        else:
            self.derev_time.setText(der_time)
        if centr_time == "00:00:00":
            self.cent_time.setText("NO LOGS")
        else:
            self.cent_time.setText(centr_time)
        self.vrem()

    """def knopk(self):
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(450, 290)
        self.btn.setText("Чистка кд")
        #self.btn.setStyleSheet("color: rgb(140, 140, 140);")
        #self.btn.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.btn.setFixedWidth(120)
        self.btn.setFixedHeight(50)
        self.btn.clicked.connect(func)"""

    def top(self):
        self.w.move(450, 510)
        self.w.setText("Made by MeowGL")
        self.w.setStyleSheet("color: rgb(140, 140, 140);")
        self.w.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.w.adjustSize()

    def dereva_time(self):
        self.derev_time.setText(der_time)
        self.derev_time.setStyleSheet("color: rgb(140, 140, 140);")
        self.derev_time.move(515, 150)
        self.derev_time.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.derev_time.adjustSize()

    def centa_time(self):
        self.cent_time.setText(centr_time)
        self.cent_time.setStyleSheet("color: rgb(140, 140, 140);")
        self.cent_time.move(515, 190)
        self.cent_time.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.cent_time.adjustSize()

    def fraca_d(self):
        self.derev.setText(der)
        self.derev.setStyleSheet("color: rgb(140, 140, 140);")
        self.derev.move(345, 150)
        self.derev.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.derev.adjustSize()

    def fraca_c(self):
        self.cent.setText(centr)
        self.cent.setStyleSheet("color: rgb(140, 140, 140);")
        self.cent.move(345, 190)
        self.cent.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.cent.adjustSize()

    """def fam(self):
        self.f = QtWidgets.QLabel(self)
        self.f.setStyleSheet("color: rgb(140, 140, 140);")
        self.f.setText("След атака_1:")
        self.f.move(345, 350)
        self.f.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.f.adjustSize()

    def fam2(self):
        self.f2 = QtWidgets.QLabel(self)
        self.f2.setStyleSheet("color: rgb(140, 140, 140);")
        self.f2.setText("След атака_2:")
        self.f2.move(345, 410)
        self.f2.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.f2.adjustSize()

    def famk_time(self):
        self.f_time.setText(fam_time)
        self.f_time.setStyleSheet("color: rgb(140, 140, 140);")
        self.f_time.move(345, 375)  
        self.f_time.setFont(QtGui.QFont("Times", 9, QtGui.QFont.Bold))
        self.f_time.setFixedWidth(210)
        self.f_time.adjustSize()

    def famk_time2(self):
        self.f_time2.setText(fam_time2)
        self.f_time2.setStyleSheet("color: rgb(140, 140, 140);")
        self.f_time2.move(345, 435)
        self.f_time2.setFont(QtGui.QFont("Times", 9, QtGui.QFont.Bold))
        self.f_time2.setFixedWidth(210)
        self.f_time2.adjustSize()"""

    def txt_speh(self):
        self.p = QtWidgets.QLabel(self)
        self.p.setStyleSheet("color: rgb(140, 140, 140);")
        self.p.setText("Время до спешки:")
        self.p.move(345, 250)
        self.p.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.p.adjustSize()

    def boss_1(self):
        self.boss_1 = QtWidgets.QLabel(self)
        self.boss_1.setStyleSheet("color: rgb(140, 140, 140);")
        self.boss_1.setText("Королевский Зомби")
        self.boss_1.move(10, 70)
        self.boss_1.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.boss_1.adjustSize()

    def time_boss_1(self):
        self.time_1.setText(str(time_11))
        self.time_1.setStyleSheet("color: rgb(140, 140, 140);")
        self.time_1.move(250, 70)
        self.time_1.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.time_1.adjustSize()

    def boss_2(self):
        self.boss_2 = QtWidgets.QLabel(self)
        self.boss_2.setStyleSheet("color: rgb(140, 140, 140);")
        self.boss_2.setText("Холуй")
        self.boss_2.move(10, 110)
        self.boss_2.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.boss_2.adjustSize()

    def time_boss_2(self):
        self.time_2.setText(str(time_12))
        self.time_2.setStyleSheet("color: rgb(140, 140, 140);")
        self.time_2.move(250, 110)
        self.time_2.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.time_2.adjustSize()

    def boss_3(self):
        self.boss_3 = QtWidgets.QLabel(self)
        self.boss_3.setStyleSheet("color: rgb(140, 140, 140);")
        self.boss_3.setText("Слайм")
        self.boss_3.move(10, 150)
        self.boss_3.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.boss_3.adjustSize()

    def time_boss_3(self):
        self.time_3.setText(str(time_13))
        self.time_3.setStyleSheet("color: rgb(140, 140, 140);")
        self.time_3.move(250, 150)
        self.time_3.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.time_3.adjustSize()

    def boss_4(self):
        self.boss_4 = QtWidgets.QLabel(self)
        self.boss_4.setStyleSheet("color: rgb(140, 140, 140);")
        self.boss_4.setText("Фенрир")
        self.boss_4.move(10, 190)
        self.boss_4.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.boss_4.adjustSize()

    def time_boss_4(self):
        self.time_4.setText(str(time_14))
        self.time_4.setStyleSheet("color: rgb(140, 140, 140);")
        self.time_4.move(250, 190)
        self.time_4.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.time_4.adjustSize()

    def boss_5(self):
        self.boss_5 = QtWidgets.QLabel(self)
        self.boss_5.setStyleSheet("color: rgb(140, 140, 140);")
        self.boss_5.setText("Всадники")
        self.boss_5.move(10, 230)
        self.boss_5.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.boss_5.adjustSize()

    def time_boss_5(self):
        self.time_5.setText(str(time_15))
        self.time_5.setStyleSheet("color: rgb(140, 140, 140);")
        self.time_5.move(250, 230)
        self.time_5.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.time_5.adjustSize()

    def boss_6(self):
        self.boss_6 = QtWidgets.QLabel(self)
        self.boss_6.setStyleSheet("color: rgb(140, 140, 140);")
        self.boss_6.setText("Матка")
        self.boss_6.move(10, 270)
        self.boss_6.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.boss_6.adjustSize()

    def time_boss_6(self):
        self.time_6.setText(str(time_16))
        self.time_6.setStyleSheet("color: rgb(140, 140, 140);")
        self.time_6.move(250, 270)
        self.time_6.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.time_6.adjustSize()

    def boss_7(self):
        self.boss_7 = QtWidgets.QLabel(self)
        self.boss_7.setStyleSheet("color: rgb(140, 140, 140);")
        self.boss_7.setText("Коровка")
        self.boss_7.move(10, 310)
        self.boss_7.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.boss_7.adjustSize()

    def time_boss_7(self):
        self.time_7.setText(str(time_17))
        self.time_7.setStyleSheet("color: rgb(140, 140, 140);")
        self.time_7.move(250, 310)
        self.time_7.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.time_7.adjustSize()

    def boss_8(self):
        self.boss_8 = QtWidgets.QLabel(self)
        self.boss_8.setStyleSheet("color: rgb(140, 140, 140);")
        self.boss_8.setText("Йети")
        self.boss_8.move(10, 350)
        self.boss_8.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.boss_8.adjustSize()

    def time_boss_8(self):
        self.time_8.setText(str(time_18))
        self.time_8.setStyleSheet("color: rgb(140, 140, 140);")
        self.time_8.move(250, 350)
        self.time_8.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.time_8.adjustSize()

    def boss_9(self):
        self.boss_9 = QtWidgets.QLabel(self)
        self.boss_9.setStyleSheet("color: rgb(140, 140, 140);")
        self.boss_9.setText("Левиафан")
        self.boss_9.move(10, 390)
        self.boss_9.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.boss_9.adjustSize()

    def time_boss_9(self):
        self.time_9.setText(str(time_19))
        self.time_9.setStyleSheet("color: rgb(140, 140, 140);")
        self.time_9.move(250, 390)
        self.time_9.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.time_9.adjustSize()

    def boss_10(self):
        self.boss_10 = QtWidgets.QLabel(self)
        self.boss_10.setStyleSheet("color: rgb(140, 140, 140);")
        self.boss_10.setText("Хранитель")
        self.boss_10.move(10, 430)
        self.boss_10.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.boss_10.adjustSize()

    def time_boss_110(self):
        self.time_10.setText(str(time_110))
        self.time_10.setStyleSheet("color: rgb(140, 140, 140);")
        self.time_10.move(250, 430)
        self.time_10.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.time_10.adjustSize()

    def boss_11(self):
        self.boss_11 = QtWidgets.QLabel(self)
        self.boss_11.setStyleSheet("color: rgb(140, 140, 140);")
        self.boss_11.setText("Небесный Владыка")
        self.boss_11.move(10, 470)
        self.boss_11.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.boss_11.adjustSize()

    def time_boss_111(self):
        self.time_11.setText(str(time_111))
        self.time_11.setStyleSheet("color: rgb(140, 140, 140);")
        self.time_11.move(250, 470)
        self.time_11.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.time_11.adjustSize()

    def boss_12(self):
        self.boss_12 = QtWidgets.QLabel(self)
        self.boss_12.setStyleSheet("color: rgb(140, 140, 140);")
        self.boss_12.setText("Житель Края")
        self.boss_12.move(10, 510)
        self.boss_12.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.boss_12.adjustSize()

    def time_boss_112(self):
        self.time_12.setText(str(time_112))
        self.time_12.setStyleSheet("color: rgb(140, 140, 140);")
        self.time_12.move(250, 510)
        self.time_12.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.time_12.adjustSize()

    def displayTime(self):
        self.ikonka.setText(str(QDateTime.currentDateTime().toString())[-13:-5])
        self.chitaem()

    def okno(self):
        self.ikonka2 = QtWidgets.QLabel(self)
        self.ikonka2.setStyleSheet("color: rgb(140, 140, 140);")
        self.ikonka2.move(510, 252)
        self.ikonka2.setText(str(QDateTime.currentDateTime().toString())[-13:-5])
        self.ikonka2.setFont(QtGui.QFont("Times", 9, QtGui.QFont.Bold))
        self.ikonka2.adjustSize()

    def vrem(self):
        # здесь менять время под часовой пояс
        w = ["00:55:00", "06:55:00", "12:55:00", "18:55:00"]
        format = "%H:%M:%S"
        if  str(QDateTime.currentDateTime().toString())[-13:-5] not in w:
            if "00:00:00" <= str(QDateTime.currentDateTime().toString())[-13:-5] <= "00:55:00":
                time = datetime.strptime("00:55:00", format) - datetime.strptime(
                    str(QDateTime.currentDateTime().toString())[-13:-5], format)
            elif str(QDateTime.currentDateTime().toString())[-13:-5] <= "18:55:00":
                for i in range(1, 4):
                    if w[i - 1] <= str(QDateTime.currentDateTime().toString())[-13:-5] <= w[i]:
                        z = str(w[i])
                        time = datetime.strptime(z, format) - datetime.strptime(
                            str(QDateTime.currentDateTime().toString())[-13:-5], format)
                        break
            else:
                z = "00:56:00"
                time1 = datetime.strptime(str(QDateTime.currentDateTime().toString())[-13:-5], format) - datetime.strptime(
                    z, format)
                time1 = str(time1)
                time = datetime.strptime("23:59:00", format) - datetime.strptime(time1, format)
            self.ikonka2.setText(str(time))

    def real_time(self):
        self.ikonka = QtWidgets.QLabel(self)
        self.ikonka.setStyleSheet("color: rgb(140, 140, 140);")
        self.ikonka.setText(str(QDateTime.currentDateTime().toString())[-13:-5])
        self.ikonka.move(490, 90)
        self.ikonka.setFont(QtGui.QFont("Times", 9, QtGui.QFont.Bold))
        self.ikonka.adjustSize()

    def vrem2(self):
        self.ikonka4 = QtWidgets.QLabel(self)
        self.ikonka4.setStyleSheet("color: rgb(140, 140, 140);")
        self.ikonka4.setText("Ваше время:")
        self.ikonka4.move(370, 88)
        self.ikonka4.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.ikonka4.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
