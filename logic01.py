from gui01 import *
from PyQt6.QtWidgets import *
import re
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.vote_button.clicked.connect(lambda: self.vote())
        self.exit_button.clicked.connect(lambda: self.exit())

        self.__radioValue = 4
        self.cameran_radio.toggled.connect(lambda: self.RadioGaga())
        self.allison_radio.toggled.connect(lambda: self.RadioGaga())
        self.diego_radio.toggled.connect(lambda: self.RadioGaga())
        self.other_radio.toggled.connect(lambda: self.RadioGaga())

        self.__isCandidateMenu = False

        self.__voterMatrix = []
        self.__voterHold = []

    def vote(self) -> None:
        """
        Takes the user to the CANDIDATE MENU or submits correctly entered data and takes user back to the VOTE MENU
        :return:
        """
        if not self.__isCandidateMenu:
            self.__isCandidateMenu = True
            self.top_label.setText(f'----------------------------------\n'
                                   f'CANDIDATE MENU'
                                   f'\n----------------------------------')
            self.vote_button.setText("Submit")
            self.exit_button.setText("Back")
            self.cameran_radio.setEnabled(True)
            self.allison_radio.setEnabled(True)
            self.diego_radio.setEnabled(True)
            self.other_radio.setEnabled(True)
            self.other_input.setEnabled(True)

            self.f_name_input.setEnabled(True)
            self.l_name_input.setEnabled(True)
            self.ssn_input.setEnabled(True)
        else:
            if (self.f_name_input.text() != 'First Name' and self.l_name_input.text() != 'Last Name'
                    and ((self.__radioValue == 4 and self.other_input.text() != '') or self.__radioValue != 4)
                    and re.search('[0-9]{3}-[0-9]{2}-[0-9]{4}', self.ssn_input.text())):
                self.__voterHold.append(self.l_name_input.text())
                self.__voterHold.append(self.f_name_input.text())
                self.__voterHold.append(self.ssn_input.text())
                if self.__radioValue == 1:
                    self.__voterHold.append("Cameron")
                elif self.__radioValue == 2:
                    self.__voterHold.append("Allison")
                elif self.__radioValue == 3:
                    self.__voterHold.append("Diego")
                elif self.__radioValue == 4:
                    self.__voterHold.append(self.other_input.text())

                self.other_radio.setChecked(True)
                self.top_label.setText(f'----------------------------------\n'
                                       f'VOTE MENU'
                                       f'\n----------------------------------')
                self.vote_button.setText("Vote")
                self.exit_button.setText("Exit")

                self.cameran_radio.setEnabled(False)
                self.allison_radio.setEnabled(False)
                self.diego_radio.setEnabled(False)
                self.other_radio.setEnabled(False)
                self.other_input.setEnabled(False)

                self.f_name_input.setEnabled(False)
                self.l_name_input.setEnabled(False)
                self.ssn_input.setEnabled(False)

                self.__isCandidateMenu = False

                self.f_name_input.setText(f'First Name')
                self.l_name_input.setText(f'Last Name')
                self.ssn_input.setText(f'SSN')
                self.other_input.setText('')
                self.botton_label.setText("Ballot Submitted")
                self.__voterMatrix.append(self.__voterHold)
                self.__voterHold = []
            else:
                self.botton_label.setText("Please fill all fields correctly")

    def exit(self) -> None:
        """
        takes the user back to the VOTE MENU or disables all the widgets and saves data to csv
        :return:
        """
        if self.__isCandidateMenu:
            self.top_label.setText(f'----------------------------------\n'
                                   f'VOTE MENU'
                                   f'\n----------------------------------')
            self.vote_button.setText("Vote")
            self.exit_button.setText("Exit")

            self.other_radio.setChecked(True)
            self.cameran_radio.setEnabled(False)
            self.allison_radio.setEnabled(False)
            self.diego_radio.setEnabled(False)
            self.other_radio.setEnabled(False)
            self.other_input.setEnabled(False)

            self.f_name_input.setEnabled(False)
            self.l_name_input.setEnabled(False)
            self.ssn_input.setEnabled(False)

            self.__isCandidateMenu = False

            self.f_name_input.setText(f'First Name')
            self.l_name_input.setText(f'Last Name')
            self.ssn_input.setText(f'SSN')
        else:
            self.top_label.setText(f'----------------------------------\n'
                                   f'RESULTS'
                                   f'\n----------------------------------')
            self.SaveResults()
            self.botton_label.setText(f'RESULTS SAVED TO CSV')

            self.vote_button.setEnabled(False)
            self.exit_button.setEnabled(False)

    def RadioGaga(self) -> None:
        """
        Handles the value checking of the candidate radio buttons
        :return:
        """
        if self.cameran_radio.isChecked():
            self.__radioValue = 1
        elif self.allison_radio.isChecked():
            self.__radioValue = 2
        elif self.diego_radio.isChecked():
            self.__radioValue = 3
        elif self.other_radio.isChecked():
            self.__radioValue = 4

    def SaveResults(self) -> None:
        """
        saves the entered voter data to an existing csv file
        :return:
        """
        with open('voterData.csv', 'a', newline='\n') as csvFile:
            csvWriter = csv.writer(csvFile)
            i = 0
            while i < len(self.__voterMatrix):
                csvWriter.writerow(self.__voterMatrix[i])
                i += 1
