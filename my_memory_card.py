#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Национальное блюдо Беларуси', 'картошка', 'круассан', 'сосиски', 'пончик'))
questions_list.append(Question('Год основания Кревской Унии', '1486', '1480', '1501', '1386'))
questions_list.append(Question('Между кем была заключена Кревская Уния', 'Польша и ВКЛ', 'СССР и Англия', 'ВКЛ и Беларусь', 'Польша и Польша'))
questions_list.append(Question('Как расшивровывается Гиппопотомонстросескипедалофобия','боязнь длинных слов и предложений', 'боязнь людей', 'боязнь Максимов', 'боязнь геометрии'))
questions_list.append(Question('Как звали человека который убил жёлтого в сериале Слово Пацана.Кровь на Асфальте', 'Вова Адидас', 'Никита лох', 'Петя Найк', 'МаратПальтоАйгуль'))
questions_list.append(Question('День Октябрьской Революции', '7 ноября', '7 октября', '1 сентября', '29 октября'))
questions_list.append(Question('hfrbhrburnbrub', 'btr', 'rhth', 'rhrh', 'rthtrh'))
questions_list.append(Question('Аксиома параллельных прямых', 'паралельные прямые имеют одну общую точку', 'агугага', 'мяу', 'выгувыгу'))
questions_list.append(Question('Кто круче?', 'Максимы', 'квадроберы', 'лапкеры', 'хобхорсеры'))


app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(400, 200)
window.move(100, 100)


lb_Question = QLabel('Ваш вопрос')
btn_OK = QPushButton('Ответить')


RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Ответ 1')
rbtn_2 = QRadioButton('Ответ 2')
rbtn_3 = QRadioButton('Ответ 3')
rbtn_4 = QRadioButton('Ответ 4')


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)


layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)





AnsGroupBox = QGroupBox('Результаты теста')
lb_Result = QLabel('Правльно\неправильно')
lb_Correct = QLabel('Правильный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()


layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(2)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(2)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q:Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()


def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-всего вопросов: ',window.total, '\n-правильных ответов: ', window.score)
        print('Рейтинг: ', window.score/window.total*100, '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', window.score/window.total*100, '%')


def next_question():
    window.total += 1
    print('Статистика\n-всего вопросов: ',window.total, '\n-правильных ответов: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)


def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window.setLayout(layout_card)
window.cur_question = -1
btn_OK.clicked.connect(click_OK)
window.total = 0
window.score = 0








window.cur_question = -1
btn_OK.clicked.connect(click_OK)
next_question()
window.show()
app.exec()