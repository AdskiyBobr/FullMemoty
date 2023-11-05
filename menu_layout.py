#Interface layout
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

txt_question = QLineEdit()
txt_answer = QLineEdit()
txt_wrong1 = QLineEdit()
txt_wrong2= QLineEdit()
txt_wrong3 = QLineEdit()

form_layout = QFormLayout()

form_layout.addRow('Питання:', txt_question)
form_layout.addRow('Відповідь:', txt_answer)
form_layout.addRow('Неправильна відповідь 1:', txt_wrong1)
form_layout.addRow('Неправильна відповідь 2:', txt_wrong2)
form_layout.addRow('Неправильна відповідь 3:', txt_wrong3)

