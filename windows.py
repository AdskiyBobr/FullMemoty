#потомучто понабирают всяяких

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from menu_layout import form_layout
from layout import main_layout

wdgt_main = QWidget()
wdgt_menu = QWidget()


menu_layout = QVBoxLayout()

buttons_layout = QHBoxLayout()

add_question = QPushButton('Додати питання')
clear_inputs = QPushButton('Прибрати')
back_button = QPushButton('Повернутись')

buttons_layout.addWidget(add_question)
buttons_layout.addWidget(clear_inputs)
menu_layout.addLayout(form_layout)
menu_layout.addLayout(buttons_layout)
menu_layout.addWidget(back_button, alignment=Qt.AlignCenter)

wdgt_main.setLayout(main_layout)
wdgt_menu.setLayout(menu_layout)

layout_main = QVBoxLayout()
layout_main.addWidget(wdgt_main)
layout_main.addWidget(wdgt_menu)