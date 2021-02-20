from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel
from random import randint
from time import sleep


def format_number(value: int) -> str:
    """
        Function to format decimal numbers in BR pattern.
    """
    value = str(value)
    cont = 0
    new_str = ''
    for i in value[::-1]:
        cont += 1
        if cont % 3 == 0:
            new_str += i + '.' 
        else:
            new_str += i
    if new_str[len(new_str)-1] == '.':
        try:
            new_str = new_str[:len(new_str)-1]
        except IndexError:
            pass    
    return new_str[::-1]

class App():
    """
        Main class:

        start -> interface, buttons, labels, combobox and logic.

    """
    total = 0
    method = ''
    numbers = 0
    n_game = 0

    def __init__(self: object):
        self.app = QApplication([])
        self.form = uic.loadUi('sena.ui')
        self.list_withdrawn = []
        self.bt_1 = True
        self.bt_2 = True
        self.bt_3 = True
        self.bt_4 = True
        self.bt_5 = True
        self.bt_6 = True
        self.bt_7 = True
        self.bt_8 = True
        self.bt_9 = True
        self.bt_10 = True
        self.bt_11 = True
        self.bt_12 = True
        self.bt_13 = True
        self.bt_14 = True
        self.bt_15 = True
        self.bt_16 = True
        self.bt_17 = True
        self.bt_18 = True
        self.bt_19 = True
        self.bt_20 = True
        self.bt_21 = True
        self.bt_22 = True
        self.bt_23 = True
        self.bt_24 = True
        self.bt_25 = True
        self.bt_26 = True
        self.bt_27 = True
        self.bt_28 = True
        self.bt_29 = True
        self.bt_30 = True
        self.bt_31 = True
        self.bt_32 = True
        self.bt_33 = True
        self.bt_34 = True
        self.bt_35 = True
        self.bt_36 = True
        self.bt_37 = True
        self.bt_38 = True
        self.bt_39 = True
        self.bt_40 = True
        self.bt_41 = True
        self.bt_42 = True
        self.bt_43 = True
        self.bt_44 = True
        self.bt_45 = True
        self.bt_46 = True
        self.bt_47 = True
        self.bt_48 = True
        self.bt_49 = True
        self.bt_50 = True
        self.bt_51 = True
        self.bt_52 = True
        self.bt_53 = True
        self.bt_54 = True
        self.bt_55 = True
        self.bt_56 = True
        self.bt_57 = True
        self.bt_58 = True
        self.bt_59 = True
        self.bt_60 = True
        self.form.comboBox.activated[str].connect(lambda: self.check_modality(self.form.comboBox.currentText()))
        self.check_modality(self.form.comboBox.currentText())
        self.numbers_pad()
        self.status_withdrawn(App.total)
        self.calc_combinations(App.total)
        self.form.pushButton.clicked.connect(lambda: self.generate_result(self.form.lineEdit.text()))
        self.form.show()
        self.app.exec()
        
    def status_withdrawn(self, value: int):
        """
            Increment and Decrement counter based in values receive, refresh status about combinations e probability.
        """
        App.total += value
        self.form.lb_withdraw.setText(str(App.total))
        self.form.lb_comb.setText(str(self.calc_combinations(App.total)))

    def verify_number(self, value: str):
        """
            Check what button was clickead and call two function search_number and status_withdrawn.
        """
        if value == '01' and self.bt_1 == True:
            self.form.bt_1.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_1 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '01' and self.bt_1 == False:
            self.form.bt_1.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_1 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '02' and self.bt_2 == True:
            self.form.bt_2.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_2 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '02' and self.bt_2 == False:
            self.form.bt_2.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_2 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '03' and self.bt_3 == True:
            self.form.bt_3.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_3 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '03' and self.bt_3 == False:
            self.form.bt_3.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_3 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '04' and self.bt_4 == True:
            self.form.bt_4.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_4 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '04' and self.bt_4 == False:
            self.form.bt_4.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_4 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '05' and self.bt_5 == True:
            self.form.bt_5.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_5 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '05' and self.bt_5 == False:
            self.form.bt_5.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_5 = True
            self.status_withdrawn(-1) 
            self.search_number(value)
        elif value == '06' and self.bt_6 == True:
            self.form.bt_6.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_6 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '06' and self.bt_6 == False:
            self.form.bt_6.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_6 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '07' and self.bt_7 == True:
            self.form.bt_7.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_7 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '07' and self.bt_7 == False:
            self.form.bt_7.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_7 = True
            self.status_withdrawn(-1)  
            self.search_number(value)
        elif value == '08' and self.bt_8 == True:
            self.form.bt_8.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_8 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '08' and self.bt_8 == False:
            self.form.bt_8.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_8 = True
            self.status_withdrawn(-1) 
            self.search_number(value)
        elif value == '09' and self.bt_9 == True:
            self.form.bt_9.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_9 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '09' and self.bt_9 == False:
            self.form.bt_9.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_9 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '10' and self.bt_10 == True:
            self.form.bt_10.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_10 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '10' and self.bt_10 == False:
            self.form.bt_10.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_10 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '11' and self.bt_11 == True:
            self.form.bt_11.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_11 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '11' and self.bt_11 == False:
            self.form.bt_11.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_11 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '12' and self.bt_12 == True:
            self.form.bt_12.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_12 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '12' and self.bt_12 == False:
            self.form.bt_12.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_12 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '13' and self.bt_13 == True:
            self.form.bt_13.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_13 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '13' and self.bt_13 == False:
            self.form.bt_13.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_13 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '14' and self.bt_14 == True:
            self.form.bt_14.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_14 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '14' and self.bt_14 == False:
            self.form.bt_14.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_14 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '15' and self.bt_15 == True:
            self.form.bt_15.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_15 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '15' and self.bt_15 == False:
            self.form.bt_15.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_15 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '16' and self.bt_16 == True:
            self.form.bt_16.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_16 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '16' and self.bt_16 == False:
            self.form.bt_16.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_16 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '17' and self.bt_17 == True:
            self.form.bt_17.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_17 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '17' and self.bt_17 == False:
            self.form.bt_17.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_17 = True
            self.status_withdrawn(-1) 
            self.search_number(value)
        elif value == '18' and self.bt_18 == True:
            self.form.bt_18.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_18 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '18' and self.bt_18 == False:
            self.form.bt_18.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_18 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '19' and self.bt_19 == True:
            self.form.bt_19.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_19 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '19' and self.bt_19 == False:
            self.form.bt_19.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_19 = True
            self.status_withdrawn(-1) 
            self.search_number(value)
        elif value == '20' and self.bt_20 == True:
            self.form.bt_20.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_20 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '20' and self.bt_20 == False:
            self.form.bt_20.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_20 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '21' and self.bt_21 == True:
            self.form.bt_21.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_21 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '21' and self.bt_21 == False:
            self.form.bt_21.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_21 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '22' and self.bt_22 == True:
            self.form.bt_22.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_22 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '22' and self.bt_22 == False:
            self.form.bt_22.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_22 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '23' and self.bt_23 == True:
            self.form.bt_23.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_23 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '23' and self.bt_23 == False:
            self.form.bt_23.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_23 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '24' and self.bt_24 == True:
            self.form.bt_24.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_24 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '24' and self.bt_24 == False:
            self.form.bt_24.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_24 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '25' and self.bt_25 == True:
            self.form.bt_25.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_25 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '25' and self.bt_25 == False:
            self.form.bt_25.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_25 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '26' and self.bt_26 == True:
            self.form.bt_26.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_26 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '26' and self.bt_26 == False:
            self.form.bt_26.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_26 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '27' and self.bt_27 == True:
            self.form.bt_27.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_27 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '27' and self.bt_27 == False:
            self.form.bt_27.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_27 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '28' and self.bt_28 == True:
            self.form.bt_28.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_28 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '28' and self.bt_28 == False:
            self.form.bt_28.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_28 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '29' and self.bt_29 == True:
            self.form.bt_29.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_29 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '29' and self.bt_29 == False:
            self.form.bt_29.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_29 = True
            self.status_withdrawn(-1) 
            self.search_number(value)
        elif value == '30' and self.bt_30 == True:
            self.form.bt_30.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_30 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '30' and self.bt_30 == False:
            self.form.bt_30.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_30 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '31' and self.bt_31 == True:
            self.form.bt_31.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_31 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '31' and self.bt_31 == False:
            self.form.bt_31.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_31 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '32' and self.bt_32 == True:
            self.form.bt_32.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_32 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '32' and self.bt_32 == False:
            self.form.bt_32.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_32 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '33' and self.bt_33 == True:
            self.form.bt_33.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_33 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '33' and self.bt_33 == False:
            self.form.bt_33.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_33 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '34' and self.bt_34 == True:
            self.form.bt_34.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_34 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '34' and self.bt_34 == False:
            self.form.bt_34.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_34 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '35' and self.bt_35 == True:
            self.form.bt_35.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_35 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '35' and self.bt_35 == False:
            self.form.bt_35.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_35 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '36' and self.bt_36 == True:
            self.form.bt_36.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_36 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '36' and self.bt_36 == False:
            self.form.bt_36.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_36 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '37' and self.bt_37 == True:
            self.form.bt_37.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_37 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '37' and self.bt_37 == False:
            self.form.bt_37.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_37 = True
            self.status_withdrawn(-1) 
            self.search_number(value)
        elif value == '38' and self.bt_38 == True:
            self.form.bt_38.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_38 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '38' and self.bt_38 == False:
            self.form.bt_38.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_38 = True
            self.status_withdrawn(-1) 
            self.search_number(value)
        elif value == '39' and self.bt_39 == True:
            self.form.bt_39.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_39 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '39' and self.bt_39 == False:
            self.form.bt_39.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_39 = True
            self.status_withdrawn(-1) 
            self.search_number(value)
        elif value == '40' and self.bt_40 == True:
            self.form.bt_40.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_40 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '40' and self.bt_40 == False:
            self.form.bt_40.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_40 = True
            self.status_withdrawn(-1) 
            self.search_number(value)
        elif value == '41' and self.bt_41 == True:
            self.form.bt_41.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_41 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '41' and self.bt_41 == False:
            self.form.bt_41.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_41 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '42' and self.bt_42 == True:
            self.form.bt_42.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_42 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '42' and self.bt_42 == False:
            self.form.bt_42.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_42 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '43' and self.bt_43 == True:
            self.form.bt_43.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_43 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '43' and self.bt_43 == False:
            self.form.bt_43.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_43 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '44' and self.bt_44 == True:
            self.form.bt_44.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_44 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '44' and self.bt_44 == False:
            self.form.bt_44.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_44 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '45' and self.bt_45 == True:
            self.form.bt_45.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_45 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '45' and self.bt_45 == False:
            self.form.bt_45.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_45 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '46' and self.bt_46 == True:
            self.form.bt_46.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_46 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '46' and self.bt_46 == False:
            self.form.bt_46.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_46 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '47' and self.bt_47 == True:
            self.form.bt_47.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_47 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '47' and self.bt_47 == False:
            self.form.bt_47.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_47 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '48' and self.bt_48 == True:
            self.form.bt_48.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_48 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '48' and self.bt_48 == False:
            self.form.bt_48.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_48 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '49' and self.bt_49 == True:
            self.form.bt_49.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_49 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '49' and self.bt_49 == False:
            self.form.bt_49.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_49 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '50' and self.bt_50 == True:
            self.form.bt_50.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_50 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '50' and self.bt_50 == False:
            self.form.bt_50.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_50 = True
            self.status_withdrawn(-1) 
            self.search_number(value)
        elif value == '51' and self.bt_51 == True:
            self.form.bt_51.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_51 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '51' and self.bt_51 == False:
            self.form.bt_51.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_51 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '52' and self.bt_52 == True:
            self.form.bt_52.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_52 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '52' and self.bt_52 == False:
            self.form.bt_52.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_52 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '53' and self.bt_53 == True:
            self.form.bt_53.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_53 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '53' and self.bt_53 == False:
            self.form.bt_53.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_53 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '54' and self.bt_54 == True:
            self.form.bt_54.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_54 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '54' and self.bt_54 == False:
            self.form.bt_54.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_54 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '55' and self.bt_55 == True:
            self.form.bt_55.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_55 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '55' and self.bt_55 == False:
            self.form.bt_55.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_55 = True
            self.status_withdrawn(-1) 
            self.search_number(value)
        elif value == '56' and self.bt_56 == True:
            self.form.bt_56.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_56 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '56' and self.bt_56 == False:
            self.form.bt_56.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_56 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '57' and self.bt_57 == True:
            self.form.bt_57.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_57 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '57' and self.bt_57 == False:
            self.form.bt_57.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_57 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '58' and self.bt_58 == True:
            self.form.bt_58.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_58 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '58' and self.bt_58 == False:
            self.form.bt_58.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_58 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '59' and self.bt_59 == True:
            self.form.bt_59.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_59 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '59' and self.bt_59 == False:
            self.form.bt_59.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_59 = True
            self.status_withdrawn(-1)
            self.search_number(value)
        elif value == '60' and self.bt_60 == True:
            self.form.bt_60.setStyleSheet("QToolButton {background-color: red;}")
            self.bt_60 = False
            self.status_withdrawn(1)
            self.search_number(value)
        elif value == '60' and self.bt_60 == False:
            self.form.bt_60.setStyleSheet("QToolButton {background-color: rgb(0,85,0);}")
            self.bt_60 = True
            self.status_withdrawn(-1)
            self.search_number(value)

    def numbers_pad(self):
        """
            Start click events in alll buttons;
        """
        self.form.bt_1.clicked.connect(lambda: self.verify_number(self.form.bt_1.text()))
        self.form.bt_2.clicked.connect(lambda: self.verify_number(self.form.bt_2.text()))
        self.form.bt_3.clicked.connect(lambda: self.verify_number(self.form.bt_3.text()))
        self.form.bt_4.clicked.connect(lambda: self.verify_number(self.form.bt_4.text()))
        self.form.bt_5.clicked.connect(lambda: self.verify_number(self.form.bt_5.text()))
        self.form.bt_6.clicked.connect(lambda: self.verify_number(self.form.bt_6.text()))
        self.form.bt_7.clicked.connect(lambda: self.verify_number(self.form.bt_7.text()))
        self.form.bt_8.clicked.connect(lambda: self.verify_number(self.form.bt_8.text()))
        self.form.bt_9.clicked.connect(lambda: self.verify_number(self.form.bt_9.text()))
        self.form.bt_10.clicked.connect(lambda: self.verify_number(self.form.bt_10.text()))
        self.form.bt_11.clicked.connect(lambda: self.verify_number(self.form.bt_11.text()))
        self.form.bt_12.clicked.connect(lambda: self.verify_number(self.form.bt_12.text()))
        self.form.bt_13.clicked.connect(lambda: self.verify_number(self.form.bt_13.text()))
        self.form.bt_14.clicked.connect(lambda: self.verify_number(self.form.bt_14.text()))
        self.form.bt_15.clicked.connect(lambda: self.verify_number(self.form.bt_15.text()))
        self.form.bt_16.clicked.connect(lambda: self.verify_number(self.form.bt_16.text()))
        self.form.bt_17.clicked.connect(lambda: self.verify_number(self.form.bt_17.text()))
        self.form.bt_18.clicked.connect(lambda: self.verify_number(self.form.bt_18.text()))
        self.form.bt_19.clicked.connect(lambda: self.verify_number(self.form.bt_19.text()))
        self.form.bt_20.clicked.connect(lambda: self.verify_number(self.form.bt_20.text()))
        self.form.bt_21.clicked.connect(lambda: self.verify_number(self.form.bt_21.text()))
        self.form.bt_22.clicked.connect(lambda: self.verify_number(self.form.bt_22.text()))
        self.form.bt_23.clicked.connect(lambda: self.verify_number(self.form.bt_23.text()))
        self.form.bt_24.clicked.connect(lambda: self.verify_number(self.form.bt_24.text()))
        self.form.bt_25.clicked.connect(lambda: self.verify_number(self.form.bt_25.text()))
        self.form.bt_26.clicked.connect(lambda: self.verify_number(self.form.bt_26.text()))
        self.form.bt_27.clicked.connect(lambda: self.verify_number(self.form.bt_27.text()))
        self.form.bt_28.clicked.connect(lambda: self.verify_number(self.form.bt_28.text()))
        self.form.bt_29.clicked.connect(lambda: self.verify_number(self.form.bt_29.text()))
        self.form.bt_30.clicked.connect(lambda: self.verify_number(self.form.bt_30.text()))
        self.form.bt_31.clicked.connect(lambda: self.verify_number(self.form.bt_31.text()))
        self.form.bt_32.clicked.connect(lambda: self.verify_number(self.form.bt_32.text()))
        self.form.bt_33.clicked.connect(lambda: self.verify_number(self.form.bt_33.text()))
        self.form.bt_34.clicked.connect(lambda: self.verify_number(self.form.bt_34.text()))
        self.form.bt_35.clicked.connect(lambda: self.verify_number(self.form.bt_35.text()))
        self.form.bt_36.clicked.connect(lambda: self.verify_number(self.form.bt_36.text()))
        self.form.bt_37.clicked.connect(lambda: self.verify_number(self.form.bt_37.text()))
        self.form.bt_38.clicked.connect(lambda: self.verify_number(self.form.bt_38.text()))
        self.form.bt_39.clicked.connect(lambda: self.verify_number(self.form.bt_39.text()))
        self.form.bt_40.clicked.connect(lambda: self.verify_number(self.form.bt_40.text()))
        self.form.bt_41.clicked.connect(lambda: self.verify_number(self.form.bt_41.text()))
        self.form.bt_42.clicked.connect(lambda: self.verify_number(self.form.bt_42.text()))
        self.form.bt_43.clicked.connect(lambda: self.verify_number(self.form.bt_43.text()))
        self.form.bt_44.clicked.connect(lambda: self.verify_number(self.form.bt_44.text()))
        self.form.bt_45.clicked.connect(lambda: self.verify_number(self.form.bt_45.text()))
        self.form.bt_46.clicked.connect(lambda: self.verify_number(self.form.bt_46.text()))
        self.form.bt_47.clicked.connect(lambda: self.verify_number(self.form.bt_47.text()))
        self.form.bt_48.clicked.connect(lambda: self.verify_number(self.form.bt_48.text()))
        self.form.bt_49.clicked.connect(lambda: self.verify_number(self.form.bt_49.text()))
        self.form.bt_50.clicked.connect(lambda: self.verify_number(self.form.bt_50.text()))
        self.form.bt_51.clicked.connect(lambda: self.verify_number(self.form.bt_51.text()))
        self.form.bt_52.clicked.connect(lambda: self.verify_number(self.form.bt_52.text()))
        self.form.bt_53.clicked.connect(lambda: self.verify_number(self.form.bt_53.text()))
        self.form.bt_54.clicked.connect(lambda: self.verify_number(self.form.bt_54.text()))
        self.form.bt_55.clicked.connect(lambda: self.verify_number(self.form.bt_55.text()))
        self.form.bt_56.clicked.connect(lambda: self.verify_number(self.form.bt_56.text()))
        self.form.bt_57.clicked.connect(lambda: self.verify_number(self.form.bt_57.text()))
        self.form.bt_58.clicked.connect(lambda: self.verify_number(self.form.bt_58.text()))
        self.form.bt_59.clicked.connect(lambda: self.verify_number(self.form.bt_59.text()))
        self.form.bt_60.clicked.connect(lambda: self.verify_number(self.form.bt_60.text()))

    def factorial(self, number: int) -> int:
        """
            Return factorial of number
        """
        factor = 1
        for i in range (1, number+1):
            factor = factor * i
        return factor
        
    def calc_combinations(self, number: int) -> int:
        """
            Return a calc of probability based in game modality choosed
        """
        reduct_posb = App.numbers - int(number)
        max_posb = self.factorial(reduct_posb)
        div_posb = self.factorial(App.n_game) * self.factorial(reduct_posb - App.n_game)
        return format_number(int(max_posb / div_posb))

    def generate_result(self, value: int):
        """
            Generate games based in modality choosed and how much games you did choose.
        """
        self.form.pushButton.setEnabled(False)
        self.form.pushButton.setStyleSheet('QPushButton {background-color: red;}')
        games = []
        while len(games) < int(value) and int(value) > 0:
            self.form.progressBar.setValue(0)
            game = []
            while len(game) < App.n_game:
                result = randint(1, App.numbers)
                if result < 10:
                    result = '0' + str(result)
                else:
                    result = str(result)    
                if result not in game and result not in self.list_withdrawn:
                    game.append(result)
            games.append(game)
            percent = len(games)/int(value)
            self.form.progressBar.setValue(int(percent * 100))
            sleep(2)
        self.form.textBrowser.setText('')
        for i in games:
            i.sort()
            cont = 0
            game_str = ''
            for n in i:
                cont += 1
                if cont < App.n_game:
                    game_str += str(n) + '-'
                else:
                    game_str += str(n)
            self.form.textBrowser.append(game_str)
        sleep(10)
        self.form.pushButton.setEnabled(True)
        self.form.pushButton.setStyleSheet('QPushButton {color: rgb(255, 255, 255);background-color: rgb(0, 170, 0);}')
            
    def search_number(self, value: int):
        """
            Check if number received already in list withdrawn, if yes withdraw, else add.
        """
        if value not in self.list_withdrawn:
            self.list_withdrawn.append(value)
        else:
            for i in self.list_withdrawn:
                if value == i:
                    self.list_withdrawn.remove(i)          

    def check_modality(self, text: str):
        """
            Define based in modality, which are they numbers and what range the modality play.
        """
        
        self.form.label_2.setText(text)
        if text == 'Mega-Sena':
            App.n_game = 6
            App.numbers = 60
            if len(self.list_withdrawn) > 0:
                for i in range(26, 61):
                    self.verify_number(str(i))
            App.total = 0    
            
        else:
            App.n_game = 15
            App.numbers = 25
            for i in range(26, 61):
                self.verify_number(str(i))

            App.total = 0    

        self.status_withdrawn(App.total)
        print(self.list_withdrawn)
teste = App()
