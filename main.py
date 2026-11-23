'''
Main voting app
'''

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from gui import Ui_Form
from logic import VoteManager

class Window(QWidget):
    '''
    Voting application window.
    '''

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.manager = VoteManager()

        self.ui.btnSubmit.clicked.connect(self.submit)
        self.ui.btnClear.clicked.connect(self.clear)

        def submit(self) -> None:
            '''
            Process vote
            '''

            try:
                voter_id = self.ui.txtID.text().strip()

                if not self.manager.validate_id(voter_id):
                    self.ui.lblMessage.setStyleSheet(
                        'color:red;'
                    )

                    self.ui.lblMessage.setText(
                        'Enter valid ID'
                    )

                    return


