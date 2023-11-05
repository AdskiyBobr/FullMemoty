#Glava
from layout import *
from data import *
from windows import *
from menu_layout import *

from time import sleep

from random import choice, shuffle

ans_buttons = [ans1_button, ans2_button, ans3_button, ans4_button]
shuffle(ans_buttons)

q1 = Form("Яка нинішня ціна Опрессора МК2?", "6 000 000 - 8 000 000", "2 275 000 - 3 750 000", "8 000 000 - 10 000 000", "1 000 000 - 2 000 000")
q2 = Form('Коли вийшла Гта 5?','2013','2020','2010','2015')
q3 = Form('Скільки головних героїв у Гта 5?','3','4','1','2')
q4 = Form('Чи є у сюжетній лінії гта 5 ограблення Fleeca bank?','Ні','Так','Такого банку немає у грі','Я не знаю')
q5 = Form('Чи є у останній місії Гта 5 вбивство Франклина?','Ні','Так','Такого герою не існує','Я не знаю')
q6 = Form('Який город у грі гта 5?','Лос-Антос','Лондон','Київ','Франція')
q7 = Form('Чи є у онлайні гта 5 бойовий літак F-160?','Так','Ні','Можливо','Я не знаю')


que_list = [q1,q2,q3,q4,q5,q6,q7]
def random_answer():
    global frm_card
    cur_q = choice(que_list)
    frm_card = FormView(cur_q, question_label, ans_buttons[0], ans_buttons[1], ans_buttons[2], ans_buttons[3])
    frm_card.show()
    
showQuestion()
random_answer()


def new_question():
    global question_list
    new_q = Form(txt_question.text(),
                 txt_answer.text(),
                 txt_wrong1.text(),
                 txt_wrong2.text(),
                 txt_wrong3.text())
    que_list.append(new_q)
    txt_question.clear()
    txt_answer.clear()
    txt_wrong1.clear()
    txt_wrong2.clear()
    txt_wrong3.clear()

def clear_inputs_func():
    txt_question.clear()
    txt_answer.clear()
    txt_wrong1.clear()
    txt_wrong2.clear()
    txt_wrong3.clear()
#add_question.clicked.connect(new_question)

frm_card = 0

frm_card = FormView(q1, question_label, ans_buttons[0], ans_buttons[1], ans_buttons[2], ans_buttons[3])

def randomAnswer():
    global frm_card
    cur_q = choice(que_list)
    cur_q_label = cur_q.question
    cur_q_answer = cur_q.answer
    question_label.setText(cur_q_label)
    correct_label.setText(cur_q_answer)
    
    frm_card = FormView(cur_q, question_label, ans_buttons[0], ans_buttons[1], ans_buttons[2], ans_buttons[3])
    frm_card.show()


randomAnswer()
showQuestion()
def check_result():
    if ans_button.text() == "Ответить":
        correct = frm_card.answer_W.isChecked()
        incorrect = frm_card.wrong_answer1_W.isChecked() or frm_card.wrong_answer2_W.isChecked() or frm_card.wrong_answer3_W.isChecked()

        if correct:
            print("Правильно!")
            showAnswer()
        
        if incorrect:
            print("Неправильно!")
            showAnswer()
    
    else:
        randomAnswer()
        showQuestion()

def show_menu():
    wdgt_main.hide()
    wdgt_menu.show()

def show_main():
    wdgt_menu.hide()
    wdgt_main.show()

def go_sleep():
    sleep(rest_spinbox.value() * 60)



ans_button.clicked.connect(check_result)

back_button.clicked.connect(show_main)
menu_button.clicked.connect(show_menu)
back_button.clicked.connect(show_main)
add_question.clicked.connect(new_question)
clear_inputs.clicked.connect(clear_inputs_func)
rest_button.clicked.connect(go_sleep)

show_main()
main_window = QWidget() # Виджет "Окно"
main_window.resize(640, 480)
main_window.setLayout(layout_main) # Расставить єлементі
main_window.show() # Показать окно
app.exec() # Запуск