#Игровой центр


from tkinter import *
import string
import secrets
from tkinter import messagebox
import keyboard
import random
def abd():
    root.destroy()
    print('Вы успешно выйшли!')
def check():
    l=login.get()
    p=pasword.get()
    if l and p:
        global to
        messagebox.showinfo('Succes','Добро пожаловать!')
        root.destroy()
        print('Добро пожаловать',l)
        print('Ваш пароль:',p)
        to=Tk()
        to.resizable(height = False, width = False)
        to.geometry('500x500')
        to.title('Les Pick')
        to['bg']='#d4c2c1'
        bot=Button(to, text='Крестики-Нолики',font='Consolas 16', command=crest)
        bot.pack()
        boot=Button(to, text='К-Н-Б',font='Consolas 16', command=camen)
        boot.pack()
        dot=Button(to, text='Поймай Шар', font='Consolas 16', command=uy)
        dot.pack()
    elif not p and l:
        messagebox.showerror('Error 553','Введите пароль!')
    elif not l and not p:
        messagebox.showerror('Error 553','Введите логин и пароль!')
    elif not l and p:
        messagebox.showerror('Error 553','Введите логин!')

def uy():
    global co
    global p
    print('--------------------------')
    print('Сколько шаров надо поймать')
    print('--------------------------')
    en=int(input(''))
    root=Tk()
    root.title('Поймай Шарик')
    c=Canvas(root, width=600, height=600, bg='white')
    pod=Canvas(root, width=600, height=100, bg='yellow')
    c.pack()
    pod.pack()
    root.resizable(FALSE, FALSE)
    colors=['red', 'blue', 'orange', 'green', 'black', 'brown', '#32a4a8', '#232766', '#7d6a56', 'purple', '#54402c', '#450541', '#780734', '#3b453c', '#e8bc82', '#941dde']
    co=0
    def p(event):
        global co
        co+=1
        pod.delete(ALL)
        pod.create_text(80, 30, font='Arial 18', text='Попаданий:')
        pod.create_text(170, 30, font='Arial 20', text=str(co))
        if en==co:
            
            messagebox.showinfo('Win', 'Ты выйграл')
            root.destroy()
            
    def ball():
        c.delete(ALL)
        x=random.randint(10, 580)
        y=random.randint(10, 580)
        r=30
        jo=c.create_oval(x, y, x+r, y+r, fill=random.choice(colors), width=0)
        c.tag_bind(jo, '<Button-1>', p)
        root.after(750, ball)
    
    ball()
    root.mainloop()

def camen():
    class Main(Frame):
        def __init__(self, root):
            super(Main, self).__init__(root)
            self.start()
        def start(self):
            btn = Button(root, text="Камень", font=("Times New Roman", 15), command=lambda x=1: self.btn_click(x))
            btn2 = Button(root, text="Ножницы", font=("Times New Roman", 15), command=lambda x=2: self.btn_click(x))
            btn3 = Button(root, text="Бумага", font=("Times New Roman", 15), command=lambda x=3: self.btn_click(x))
            btn.place(x=10, y=100, width=120, height=50)
            btn2.place(x=155, y=100, width=120, height=50)
            btn3.place(x=300, y=100, width=120, height=50)
            self.lbl = Label(root, text="Начало игры!", bg="#FFF", font=("Times New Roman", 21, "bold"))
            self.lbl.place(x=150, y=25)
            self.win = self.drow = self.lose = 0
            self.lbl2 = Label(root, justify="left", font=("Times New Roman", 13), text=f"Побед: {self.win}\nПроигрышей:" f" {self.lose}\nНичей: {self.drow}", bg="#FFF")
            self.lbl2.place(x=5, y=5)
        def btn_click(self, choise):
            comp_choise = random.randint(1, 3)
            if choise == comp_choise:
                self.drow += 1
                self.lbl.configure(text="Ничья")
            elif choise == 1 and comp_choise == 2  or choise == 2 and comp_choise == 3  or choise == 3 and comp_choise == 1:
                self.win += 1
                self.lbl.configure(text="Победа")
            else:
                self.lose += 1
                self.lbl.configure(text="Проигрыш")
            self.lbl2.configure(text=f"Побед: {self.win}\nПроигрышей:"f" {self.lose}\nНичей: {self.drow}")
            if self.win==4:
                print('Поздравляю')
                root.destroy()
                messagebox.showinfo('Succes', 'Ты победил Бота')
                
            if self.lose==5:
                root.destroy()
                messagebox.showinfo('Something go wrong', 'Вы исчерпали все попытки')
                
    root = Tk()
    root.geometry("430x160+200+200")
    root.title("Камень, ножницы, бумага")
    root.resizable(False, False)
    root['bg']='#FFF'
    Main(root)
    
def crest():
    to.destroy()
    #%s-Строка воспринимаеться пользователем
    #self- это ссылка на сам объект этого класса
    #Еще мы используем random.shuffle - изменяет последовательность
    class Square:
        #Квадратные клетки
        def __init__(self, master, root, num, row, column):
            self.master = master
            self.square_num = num
            #Чтобы изменить текст
            self.msg = StringVar()
            self.lbl = Label(root, textvariable=self.msg, font="Arial 75", bg="white")
            self.lbl.grid(row=row, column=column, sticky=NSEW, padx=5, pady=5)
        
        def unbind(self):
            self.lbl.unbind("<Button-1>")

        def bind(self):
            self.lbl.bind("<Button-1>", self.choice)

        def bind_comp(self):
            self.lbl.bind("<Button-1>", self.choice_comp)

        def set_msg(self, txt):
            self.msg.set(txt)

        def choice(self, event):
            self.master.turn_user(self.square_num)

        def choice_comp(self, event):
            self.master.turn_pc()

        def cfg(self, color):
            self.lbl.configure(bg=color)

    
       

    class Application(Frame):
        def __init__(self, master):
            super(Application, self).__init__(master)
            self.master = master
            #вариации ходов
            self.wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),(1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
            self.board_start = ['_'] * 9
            #скоко макс ходов
            self.free_squares_start = [x for x in range(9)]
            self.choice_pc1 = [0, 2, 6, 8]
            self.choice_pc2 = [1, 3, 5, 7]
            # статистика игры
            self.drawn_game = 0
            self.user1_win = 0
            self.user2_win = 0
            self.pc1_win = 0
            self.pc2_win = 0
            self.create_widgets()

        def create_widgets(self):
            # блок статистики
            stat_frame = Frame(self.master)
            stat_frame.grid(row=0, column=0, padx=5, pady=5, sticky=N)
            # статистика
            statistics = LabelFrame(stat_frame, text=" Статистика ")
            statistics.grid()
            #Чтобы изменить текст
            self.stat_msg = StringVar()
            stat_lbl = Label(statistics, textvariable=self.stat_msg, justify=LEFT, width=20)
            stat_lbl.grid(padx=0)

            # блок игрока 1
            gamer1_frame = Frame(self.master)
            gamer1_frame.grid(row=1, column=0, padx=5, pady=5, sticky=W)
            step_choice = LabelFrame(gamer1_frame, text=" Игрок 1 ")
            step_choice.grid(ipadx=26)
            #чтобы изменить цыфры
            self.gamer1_step = IntVar()
            self.gamer1_step.set(0)
            gamer1_step0 = Radiobutton(step_choice, text='Игрок', variable=self.gamer1_step, value=0)
            gamer1_step1 = Radiobutton(step_choice, text='Компьютер', variable=self.gamer1_step, value=1)
            gamer1_step0.grid(ipady=2, sticky=W)
            gamer1_step1.grid(ipady=3, sticky=W)
            # блок игрока 2
            gamer2_frame = Frame(self.master)
            gamer2_frame.grid(row=1, column=1, padx=5, pady=5, sticky=W)
            step_choice = LabelFrame(gamer2_frame, text=" Игрок 2 ")
            step_choice.grid(ipadx=26)
            self.gamer2_step = IntVar()
            self.gamer2_step.set(1)
            gamer2_step0 = Radiobutton(step_choice, text='Игрок', variable=self.gamer2_step, value=0)
            gamer2_step1 = Radiobutton(step_choice, text='Компьютер', variable=self.gamer2_step, value=1)
            gamer2_step0.grid(ipady=2, sticky=W)
            gamer2_step1.grid(ipady=3, sticky=W)
            # блок выбора хода
            step_frame = Frame(self.master)
            step_frame.grid(row=0, column=1, padx=10, pady=5, sticky=N)
            step_choice = LabelFrame(step_frame, text=" Ходит первым ")
            step_choice.grid(ipadx=20, ipady=25)
            self.first_step = IntVar()
            self.first_step.set(0)
            first_step0 = Radiobutton(step_choice, text='Игрок 1', variable=self.first_step, value=0)
            first_step1 = Radiobutton(step_choice, text='Игрок 2', variable=self.first_step, value=1)
            first_step0.grid(ipady=3, sticky=W)
            first_step1.grid(ipady=2, sticky=W)
            # блок выбора знака
            sign_frame = Frame(self.master)
            sign_frame.grid(row=0, column=2, padx=5, pady=5)
            # выбор знака
            sign_choice = LabelFrame(sign_frame, text=" Выбор знака ")
            sign_choice.grid(ipadx=20)
            self.gamer1_choice = StringVar()
            self.gamer1_choice.set('0')
            gamer1_sign0 = Radiobutton(sign_choice, text='Игрок 1 "0"', variable=self.gamer1_choice, value='0')
            gamer1_sign1 = Radiobutton(sign_choice, text='Игрок 1 "X"', variable=self.gamer1_choice, value='X')
            gamer1_sign0.grid()
            gamer1_sign1.grid()
            
            # кнопка старт
            self.btn = Button(sign_frame, text="Старт", command=self.start)
            self.btn.grid(pady=6, ipady=10, sticky=NSEW)
            # игровое поле
            self.squares = {}
            num = 0
            for row in range(2, 5):
                for column in range(0, 3):
                    self.squares[num] = Square(self, self.master, num, row, column)
                    num += 1
            self.widgets = [gamer1_sign0, gamer1_sign1, gamer1_step0, gamer1_step1, gamer2_step0, gamer2_step1, first_step0,
                            first_step1, self.btn]
            
        
            
        def start(self, *args):
            self.choice_pc = None
            self.flag_end = False
            self.flag_choice_user = False
            self.flag_choice_pc = False
            self.free_squares = self.free_squares_start[:]
            self.board = self.board_start[:]
            for square_num in range(9):
                square = self.squares[square_num]
                if self.gamer1_step.get() == 1 and self.gamer2_step.get() == 1:
                    square.bind_comp()
                else:
                    square.bind()
                square.set_msg('')
                square.cfg('white')
            gs1 = self.gamer1_step.get()
            gs2 = self.gamer2_step.get()
            if self.gamer1_choice.get() == '0':
                if gs1 == 0 and gs2 == 1:
                    self.user_sign, self.pc_sign = '0', 'X'
                elif gs1 == 1 and gs2 == 0:
                    self.pc_sign, self.user_sign = '0', 'X'
                elif gs1 == 0 and gs2 == 0:
                    self.user1_sign, self.user2_sign = '0', 'X'
                elif gs1 == 1 and gs2 == 1:
                    self.pc1_sign, self.pc2_sign = '0', 'X'
            else:
                if gs1 == 0 and gs2 == 1:
                    self.user_sign, self.pc_sign = 'X', '0'
                elif gs1 == 1 and gs2 == 0:
                    self.pc_sign, self.user_sign = 'X', '0'
                elif gs1 == 0 and gs2 == 0:
                    self.user1_sign, self.user2_sign = 'X', '0'
                elif gs1 == 1 and gs2 == 1:
                    self.pc1_sign, self.pc2_sign = 'X', '0'
            fs = self.first_step.get()
            if fs == 0:
                if gs1 == 1:
                    self.turn_pc()
            elif fs == 1:
                if gs2 == 1:
                    self.flag_choice_pc = True
                    self.turn_pc()
            self.widget_state()
            

        def widget_state(self, wst=DISABLED):
            for widget in self.widgets:
                widget.config(state=wst)

        def unbind_squares(self):
            for square_num in self.free_squares:
                self.squares[square_num].unbind()

        def greet_winner(self, sign):
            #поздравления 
            if self.gamer1_step.get() == 0 and self.gamer2_step.get() == 0:
                if sign == self.user1_sign and self.gamer1_step.get() == 0:
                    self.user1_win += 1
                if sign == self.user2_sign and self.gamer2_step.get() == 0:
                    self.user2_win += 1
            elif self.gamer1_step.get() == 1 and self.gamer2_step.get() == 1:
                if sign == self.pc1_sign and self.gamer1_step.get() == 1:
                    self.pc1_win += 1
                elif sign == self.pc2_sign and self.gamer2_step.get() == 1:
                    self.pc2_win += 1
            else:
                if sign == self.user_sign and self.gamer1_step.get() == 0:
                    self.user1_win += 1
                if sign == self.pc_sign and self.gamer1_step.get() == 1:
                    self.pc1_win += 1
                if sign == self.user_sign and self.gamer2_step.get() == 0:
                    self.user2_win += 1
                if sign == self.pc_sign and self.gamer2_step.get() == 1:
                    self.pc2_win += 1
            self.flag_end = True

        def show_win(self, win, sign):
            if self.gamer1_step.get() == 0 and self.gamer2_step.get() == 0:
                if sign == self.user1_sign:
                    color = 'green'
                    messagebox.showinfo('Big Win!', 'You Win!')
                else:
                    color = 'red'
                    messagebox.showinfo('Big Lose!', 'You Lose(')
            elif self.gamer1_step.get() == 1 and self.gamer2_step.get() == 1:
                if sign == self.pc1_sign:
                    color = 'green'
                    messagebox.showinfo('Big Win!', 'You win!')
                else:
                    color = 'red'
                    messagebox.showinfo('Big Lose!', 'You Lose(')
            else:
                if sign == self.user_sign:
                    color = 'green'
                    messagebox.showinfo('Big Win!', 'You win!')
                else:
                    color = 'red'
                    messagebox.showinfo('Big Lose!', 'You Lose(')
            for square_num in win:
                square = self.squares[square_num]
                square.cfg(color)

        def game_over(self):
            #окончание игры
            self.stat_msg.set('Сыграно игр: %s\nИз них:\n  побед игрока 1: %s\n  побед игрока 2: %s\n  побед компьютера 1: %s\n  побед компьютера 2: %s\n  ничьих: %s' %(self.user1_win + self.user2_win + self.pc1_win + self.pc2_win + self.drawn_game,self.user1_win, self.user2_win, self.pc1_win, self.pc2_win, self.drawn_game))
            # widget_state надо для того чтобы мы могли заново задавать параметры игры после ее окончания
            self.widget_state(NORMAL)
            

        def test_win(self, sign):
            for a, b, c in self.wins:
                if self.board[a] == sign and self.board[b] == sign and self.board[c] == sign:
                    self.show_win((a, b, c), sign)
                    self.unbind_squares()
                    self.greet_winner(sign)
                    self.game_over()
                    return
            if not self.free_squares:
                self.flag_end = True
                self.drawn_game += 1
                messagebox.showinfo('Big Draw!', 'It is Draw')
                for square_num in range(9):
                    square = self.squares[square_num]
                    square.cfg('yellow')
                    
                self.game_over()

        def is_win(self, sign, iboard):
            for a, b, c in self.wins:
                if iboard[a] == sign and iboard[b] == sign and iboard[c] == sign:
                    return True
            return False

        def find_best_turn(self, sign):
            #ищем место для поставки знака
            for iturn in self.free_squares:
                iboard = self.board[:]
                iboard[iturn] = sign
                res = self.is_win(sign, iboard)
                if res:
                    return iturn
            return None

        def default_choice(self):
            if not self.choice_pc:
                self.choice_pc = [4]
                random.shuffle(self.choice_pc1)
                random.shuffle(self.choice_pc2)
                self.choice_pc.extend(self.choice_pc1)
                self.choice_pc.extend(self.choice_pc2)
            for iturn in self.choice_pc:
                if iturn in self.free_squares:
                    return iturn

        def turn_pc(self):
            #Ход пк
            if self.gamer1_step.get() == 1 and self.gamer2_step.get() == 1:
                if not self.flag_choice_pc:
                    square_num = self.find_best_turn(self.pc1_sign)
                    if square_num is None:
                        square_num = self.find_best_turn(self.pc2_sign)
                        if square_num is None:
                            square_num = self.default_choice()
                    self.turn(square_num, self.pc1_sign)
                    self.flag_choice_pc = True
                else:
                    square_num = self.find_best_turn(self.pc2_sign)
                    if square_num is None:
                        square_num = self.find_best_turn(self.pc1_sign)
                        if square_num is None:
                            square_num = self.default_choice()
                    self.turn(square_num, self.pc2_sign)
                    self.flag_choice_pc = False
            else:
                square_num = self.find_best_turn(self.pc_sign)
                if square_num is None:
                    square_num = self.find_best_turn(self.user_sign)
                    if square_num is None:
                        square_num = self.default_choice()
                self.turn(square_num, self.pc_sign)

        def change_board(self, square_num, sign):
            #заполнение клетки знаком
            self.board[square_num] = sign
            self.free_squares.remove(square_num)
            if self.gamer1_step.get() == 0 and self.gamer2_step.get() == 0:
                self.flag_choice_user = True

        def turn(self, square_num, sign):
            square = self.squares[square_num]
            square.unbind()
            square.set_msg(sign)
            self.change_board(square_num, sign)
            self.test_win(sign)

        def turn_user(self, square_num):
            #Ход игрока
            if self.gamer1_step.get() == 0 and self.gamer2_step.get() == 0:
                if self.first_step.get() == 0:
                    if not self.flag_choice_user:
                        self.turn(square_num, self.user1_sign)
                    else:
                        self.turn(square_num, self.user2_sign)
                        self.flag_choice_user = False
                elif self.first_step.get() == 1:
                    if not self.flag_choice_user:
                        self.turn(square_num, self.user2_sign)
                    else:
                        self.turn(square_num, self.user1_sign)
                        self.flag_choice_user = False
            elif (self.gamer1_step.get() == 0 and self.gamer2_step.get() == 1) or (
                    self.gamer1_step.get() == 1 and self.gamer2_step.get() == 0):
                self.turn(square_num, self.user_sign)
                if not self.flag_end:
                    self.turn_pc()



    root = Tk()
    root.title('Крестики - Нолики')
    root.resizable(False, False)
    Vit_Great = Application(root)
    root['bg']='#c7c3c1'
    root.mainloop()
def gen():
    #apl = герерируем рандом буквы + цифры 
    apl=string.ascii_letters + string.digits
    #password = записываем secrets - генерируем код с числами for i - на скоко символов
    password=''.join(secrets.choice(apl) for i in range(10))
    messagebox.showinfo(' Your Password', password)
    pasword.insert(0, password)
keyboard.add_hotkey('ctrl + shift', abd)    
root=Tk()
root.resizable(height = False, width = False)
root.geometry('500x500')
root.title('Reservation')
root['bg']='#d4c2c1'

text_login=Label(text='login', font='Comfortaa 20')
login=Entry(root, font='Consolas 15', relief='groove', justify='center')
text_password=Label(text='Password', font='Comfortaa 20')
pasword=Entry(root, font='Consolas 15', relief='groove', justify='center', show='*')
enter=Button(text='Войти', font='Consolas 16', command=check, bg='lightgray',activebackground='red')
gener=Button(text='Сгенерировать пароль', font='Comfortaa 12', bg='lightgray',activebackground='red', command=gen)
bap=Label(text='Вы можете выйти Для етого нажмите Ctrl + Shist', font='Comfortaa 12', bg='lightgray',activebackground='red')

text_login.pack()
login.pack()
text_password.pack()
pasword.pack()
bap.pack()
gener.pack()
enter.pack()

root.mainloop()
