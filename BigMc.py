#many things here are recycled
#this is a project that combines some of my python projects


from tkinter import *
from tkinter import messagebox

import random


window = Tk()
window.title("Big ol Mc")

frame = Frame(window)
frame.pack()

window.geometry("400x400")

#setting up all the variables needed for the code to function

name = ""

result =""

mathing = StringVar()

balance = 0

#all games

def typegame():

    for widget in frame.winfo_children():
        widget.destroy()
        #deletes all the widgets so the new widgets can be made

    #here are all the languages
    def eng():
        for widget in frame.winfo_children():
            widget.destroy()
            # re deletes all the widgets so there are no bugs.
        #chooses the language file
        f = open("ukenglish.txt", 'r', encoding="utf8", errors="ignore")
        l = f.readlines()

        words = list(map(lambda x: x.strip(), l))
        #the main loop of the game
        def typegme():
            global time
            global isrunning
            global score

            for widget in frame.winfo_children():
                widget.destroy()

            lbl = Label(frame, text="You have 60 seconds to type the words showing up")
            lbl.grid(column=0, row=0)
            lbl = Label(frame, text="Press space to check and enter to skip/start")
            lbl.grid(column=0, row=1)

            scoree = Label(frame, text="Score:  ")
            scoree.grid(column=0, row=2)

            timelbl = Label(frame, text="time:  ")
            timelbl.grid(column=0, row=3)

            txt1 = Label(frame, text="", font=("Courier", 20))
            txt1.grid(column=0, row=4)

            lbl = Label(frame, text="")
            lbl.grid(column=0, row=5)

            entry = Entry(frame,font=("Courier", 20))
            entry.grid(column=0, row=8)

            backbtn = Button(frame, text="back", height=5, width=30, command=gamechoose)
            backbtn.grid(column=0, row=100)

            time = 60

            isrunning = 0

            score = 0

            def countdown():

                global time

                time = time - 1

                timelbl.after(1000, countdown)

                timelbl.config(text="time:  " + str(time))
                if time == 0:

                    messagebox.showinfo("score:", "In the last 60 seconds you got this many words write :)   score:  "+ str(score))

                    for widget in frame.winfo_children():
                        widget.destroy()

                    backtxt = Label(frame, text="play agair or go back?")
                    backtxt.grid(column=0, row=0)

                    playagainbtn = Button(frame, text="play again", height=20, width=20, command=typegame)
                    playagainbtn.grid(column=99, row=100)

                    backbtn = Button(frame, text="back", height=20, width=20, command=first)
                    backbtn.grid(column=100, row=100)

                    time = -1

            def startgame(num):

                global isrunning
                isrunning = 1

                if score >= 0:
                    next()
                countdown()

            def next():

                global b
                b = random.choice(words)

                txt1.config(text=b)

            def check(num):

                global score

                a = entry.get()
                a = a[:-1]
                d = random.randint(0, 1)

                if (a == b):
                    score = score + 1
                    scoree.config(text="Score:  " + str(score))
                    entry.delete(0, 'end')
                    next()


            if isrunning == 1:
                isrunning = 1

            timelbl.config(text="time:  " + str(time))

            backbtn = Button(frame, text="back", height=5, width=30, command=first)
            backbtn.grid(column=0, row=100)

            window.bind("<Return>", startgame)
            window.bind("<space>", check)

        typegme()

    def esp():

        for widget in frame.winfo_children():
            widget.destroy()

        #chooses the language file
        f = open("espanol.txt", 'r', encoding="utf8", errors="ignore")
        l = f.readlines()

        words = list(map(lambda x: x.strip(), l))

        def typegme():
            global time
            global isrunning
            global score

            for widget in frame.winfo_children():
                widget.destroy()

            lbl = Label(frame, text="Press Enter to Start, and Space to check")
            lbl.grid(column=0, row=0)

            scoree = Label(frame, text="Score:  ")
            scoree.grid(column=0, row=1)

            timelbl = Label(frame, text="time:  ")
            timelbl.grid(column=0, row=2)

            txt1 = Label(frame, text="", font=("Courier", 20))
            txt1.grid(column=0, row=3)

            lbl = Label(frame, text="")
            lbl.grid(column=0, row=5)

            entry = Entry(frame, font=("Courier", 20))
            entry.grid(column=0, row=4)
            time = 60

            isrunning = 0

            score = 0

            def countdown():

                global time

                time = time - 1

                timelbl.after(1000, countdown)

                timelbl.config(text="time:  " + str(time))
                if time == 0:

                    messagebox.showinfo("score:",
                                        "In the last 60 seconds you got this many words write :)   score:  " + str(
                                            score))

                    for widget in frame.winfo_children():
                        widget.destroy()

                    backtxt = Label(frame, text="play agair or go back?")
                    backtxt.grid(column=0, row=0)

                    playagainbtn = Button(frame, text="play again", height=20, width=20, command=typegame)
                    playagainbtn.grid(column=99, row=100)

                    backbtn = Button(frame, text="back", height=20, width=20, command=first)
                    backbtn.grid(column=100, row=100)

                    time = -1

            def startgame(num):

                global isrunning
                isrunning = 1

                if score >= 0:
                    next()
                countdown()

            def next():

                global b
                b = random.choice(words)

                txt1.config(text=b)

            def check(num):

                global score

                a = entry.get()
                a = a[:-1]
                d = random.randint(0, 1)

                if (a == b):
                    score = score + 1
                    scoree.config(text="Score:  " + str(score))
                    entry.delete(0, 'end')
                    next()

            if isrunning == 1:
                isrunning = 1

            timelbl.config(text="time:  " + str(time))

            backbtn = Button(frame, text="back", height=5, width=30, command=first)
            backbtn.grid(column=0, row=100)

            window.bind("<Return>", startgame)
            window.bind("<space>", check)

        typegme()

    def fr():

        for widget in frame.winfo_children():
            widget.destroy()

        #chooses the language file
        f = open("francais.txt", 'r', encoding="utf8", errors="ignore")
        l = f.readlines()

        words = list(map(lambda x: x.strip(), l))

        def typegme():
            global time
            global isrunning
            global score

            for widget in frame.winfo_children():
                widget.destroy()

            lbl = Label(frame, text="Press Enter to Start, and Space to check")
            lbl.grid(column=0, row=0)

            scoree = Label(frame, text="Score:  ")
            scoree.grid(column=0, row=1)

            timelbl = Label(frame, text="time:  ")
            timelbl.grid(column=0, row=2)

            txt1 = Label(frame, text="", font=("Courier", 20))
            txt1.grid(column=0, row=3)

            lbl = Label(frame, text="")
            lbl.grid(column=0, row=5)

            entry = Entry(frame, font=("Courier", 20))
            entry.grid(column=0, row=4)
            time = 60

            isrunning = 0

            score = 0

            def countdown():

                global time

                time = time - 1

                timelbl.after(1000, countdown)

                timelbl.config(text="time:  " + str(time))
                if time == 0:

                    messagebox.showinfo("score:",
                                        "In the last 60 seconds you got this many words write :)   score:  " + str(
                                            score))

                    for widget in frame.winfo_children():
                        widget.destroy()

                    backtxt = Label(frame, text="play agair or go back?")
                    backtxt.grid(column=0, row=0)

                    playagainbtn = Button(frame, text="play again", height=20, width=20, command=typegame)
                    playagainbtn.grid(column=99, row=100)

                    backbtn = Button(frame, text="back", height=20, width=20, command=first)
                    backbtn.grid(column=100, row=100)

                    time = -1

            def startgame(num):

                global isrunning
                isrunning = 1

                if score >= 0:
                    next()
                countdown()

            def next():

                global b
                b = random.choice(words)

                txt1.config(text=b)

            def check(num):

                global score

                a = entry.get()
                a = a[:-1]
                d = random.randint(0, 1)

                if (a == b):
                    score = score + 1
                    scoree.config(text="Score:  " + str(score))
                    entry.delete(0, 'end')
                    next()

            if isrunning == 1:
                isrunning = 1

            timelbl.config(text="time:  " + str(time))

            backbtn = Button(frame, text="back", height=5, width=30, command=first)
            backbtn.grid(column=0, row=100)

            window.bind("<Return>", startgame)
            window.bind("<space>", check)

        typegme()

    def grm():

        for widget in frame.winfo_children():
            widget.destroy()

        #chooses the language file
        f = open("deutsch.txt", 'r', encoding="utf8", errors="ignore")
        l = f.readlines()

        words = list(map(lambda x: x.strip(), l))

        def typegme():
            global time
            global isrunning
            global score

            for widget in frame.winfo_children():
                widget.destroy()

            lbl = Label(frame, text="Press Enter to Start, and Space to check")
            lbl.grid(column=0, row=0)

            scoree = Label(frame, text="Score:  ")
            scoree.grid(column=0, row=1)

            timelbl = Label(frame, text="time:  ")
            timelbl.grid(column=0, row=2)

            txt1 = Label(frame, text="", font=("Courier", 20))
            txt1.grid(column=0, row=3)

            lbl = Label(frame, text="")
            lbl.grid(column=0, row=5)

            entry = Entry(frame, font=("Courier", 20))
            entry.grid(column=0, row=4)
            time = 60

            isrunning = 0

            score = 0

            def countdown():

                global time

                time = time - 1

                timelbl.after(1000, countdown)

                timelbl.config(text="time:  " + str(time))
                if time == 0:

                    messagebox.showinfo("score:",
                                        "In the last 60 seconds you got this many words write :)   score:  " + str(
                                            score))

                    for widget in frame.winfo_children():
                        widget.destroy()

                    backtxt = Label(frame, text="play agair or go back?")
                    backtxt.grid(column=0, row=0)

                    playagainbtn = Button(frame, text="play again", height=20, width=20, command=typegame)
                    playagainbtn.grid(column=99, row=100)

                    backbtn = Button(frame, text="back", height=20, width=20, command=first)
                    backbtn.grid(column=100, row=100)

                    time = -1

            def startgame(num):

                global isrunning
                isrunning = 1

                if score >= 0:
                    next()
                countdown()

            def next():

                global b
                b = random.choice(words)

                txt1.config(text=b)

            def check(num):

                global score

                a = entry.get()
                a = a[:-1]
                d = random.randint(0, 1)

                if (a == b):
                    score = score + 1
                    scoree.config(text="Score:  " + str(score))
                    entry.delete(0, 'end')
                    next()

            if isrunning == 1:
                isrunning = 1

            timelbl.config(text="time:  " + str(time))

            backbtn = Button(frame, text="back", height=5, width=30, command=first)
            backbtn.grid(column=0, row=100)

            window.bind("<Return>", startgame)
            window.bind("<space>", check)

        typegme()

    def itl():

        for widget in frame.winfo_children():
            widget.destroy()

        #chooses the language file
        f = open("italiano.txt", 'r', encoding="utf8", errors="ignore")
        l = f.readlines()

        words = list(map(lambda x: x.strip(), l))

        def typegme():
            global time
            global isrunning
            global score

            for widget in frame.winfo_children():
                widget.destroy()

            lbl = Label(frame, text="Press Enter to Start, and Space to check")
            lbl.grid(column=0, row=0)

            scoree = Label(frame, text="Score:  ")
            scoree.grid(column=0, row=1)

            timelbl = Label(frame, text="time:  ")
            timelbl.grid(column=0, row=2)

            txt1 = Label(frame, text="", font=("Courier", 20))
            txt1.grid(column=0, row=3)

            lbl = Label(frame, text="")
            lbl.grid(column=0, row=5)

            entry = Entry(frame, font=("Courier", 20))
            entry.grid(column=0, row=4)
            time = 60

            isrunning = 0

            score = 0

            def countdown():

                global time

                time = time - 1

                timelbl.after(1000, countdown)

                timelbl.config(text="time:  " + str(time))
                if time == 0:

                    messagebox.showinfo("score:",
                                        "In the last 60 seconds you got this many words write :)   score:  " + str(
                                            score))

                    for widget in frame.winfo_children():
                        widget.destroy()

                    backtxt = Label(frame, text="play agair or go back?")
                    backtxt.grid(column=0, row=0)

                    playagainbtn = Button(frame, text="play again", height=20, width=20, command=typegame)
                    playagainbtn.grid(column=99, row=100)

                    backbtn = Button(frame, text="back", height=20, width=20, command=first)
                    backbtn.grid(column=100, row=100)

                    time = -1

            def startgame(num):

                global isrunning
                isrunning = 1

                if score >= 0:
                    next()
                countdown()

            def next():

                global b
                b = random.choice(words)

                txt1.config(text=b)

            def check(num):

                global score

                a = entry.get()
                a = a[:-1]
                d = random.randint(0, 1)

                if (a == b):
                    score = score + 1
                    scoree.config(text="Score:  " + str(score))
                    entry.delete(0, 'end')
                    next()

            if isrunning == 1:
                isrunning = 1

            timelbl.config(text="time:  " + str(time))

            backbtn = Button(frame, text="back", height=5, width=30, command=first)
            backbtn.grid(column=0, row=100)

            window.bind("<Return>", startgame)
            window.bind("<space>", check)

        typegme()

    def norw():

        for widget in frame.winfo_children():
            widget.destroy()

        #chooses the language file
        f = open("norsk.txt", 'r', encoding="utf8", errors="ignore")
        l = f.readlines()

        words = list(map(lambda x: x.strip(), l))

        def typegme():
            global time
            global isrunning
            global score

            for widget in frame.winfo_children():
                widget.destroy()

            lbl = Label(frame, text="Press Enter to Start, and Space to check")
            lbl.grid(column=0, row=0)

            scoree = Label(frame, text="Score:  ")
            scoree.grid(column=0, row=1)

            timelbl = Label(frame, text="time:  ")
            timelbl.grid(column=0, row=2)

            txt1 = Label(frame, text="", font=("Courier", 20))
            txt1.grid(column=0, row=3)

            lbl = Label(frame, text="")
            lbl.grid(column=0, row=5)

            entry = Entry(frame, font=("Courier", 20))
            entry.grid(column=0, row=4)
            time = 60

            isrunning = 0

            score = 0

            def countdown():

                global time

                time = time - 1

                timelbl.after(1000, countdown)

                timelbl.config(text="time:  " + str(time))
                if time == 0:

                    messagebox.showinfo("score:",
                                        "In the last 60 seconds you got this many words write :)   score:  " + str(
                                            score))

                    for widget in frame.winfo_children():
                        widget.destroy()

                    backtxt = Label(frame, text="play agair or go back?")
                    backtxt.grid(column=0, row=0)

                    playagainbtn = Button(frame, text="play again", height=20, width=20, command=typegame)
                    playagainbtn.grid(column=99, row=100)

                    backbtn = Button(frame, text="back", height=20, width=20, command=first)
                    backbtn.grid(column=100, row=100)

                    time = -1

            def startgame(num):

                global isrunning
                isrunning = 1

                if score >= 0:
                    next()
                countdown()

            def next():

                global b
                b = random.choice(words)

                txt1.config(text=b)

            def check(num):

                global score

                a = entry.get()
                a = a[:-1]
                d = random.randint(0, 1)

                if (a == b):
                    score = score + 1
                    scoree.config(text="Score:  " + str(score))
                    entry.delete(0, 'end')
                    next()

            if isrunning == 1:
                isrunning = 1

            timelbl.config(text="time:  " + str(time))

            backbtn = Button(frame, text="back", height=5, width=30, command=first)
            backbtn.grid(column=0, row=100)

            window.bind("<Return>", startgame)
            window.bind("<space>", check)

        typegme()

    def first():
        for widget in frame.winfo_children():
            widget.destroy()

        #makes the UI for the user to choose the language
        english = Button(frame, text="English", height=6, width=15, command=eng)
        english.grid(column=0, row=2)

        spanish = Button(frame, text="Spanish", height=6, width=15, command=esp)
        spanish.grid(column=1, row=2)

        french = Button(frame, text="French", height=6, width=15, command=fr)
        french.grid(column=0, row=3)

        german = Button(frame, text="German", height=6, width=15, command=grm)
        german.grid(column=1, row=3)

        italian = Button(frame, text="Italian", height=6, width=15, command=itl)
        italian.grid(column=0, row=4)

        norwegian = Button(frame, text="Norwegian", height=6, width=15, command=norw)
        norwegian.grid(column=1, row=4)

        backbtn = Button(frame, text="back", command=gamechoose, height=2, width=31)
        backbtn.grid(column=0, row=999, columnspan=3)

    #class first() to create the UI
    first()

def colorgame():
    global time
    global isrunning
    global colors
    global score



    for widget in frame.winfo_children():
        #deletes all the widgets so the new widgets can be made
        widget.destroy()

    #creating all the UI and resetting all the variables

    lbl = Label(frame, text="You have 60 seconds to guess the color")
    lbl.grid(column=0, row=0)
    lbl = Label(frame, text="Press space to check and enter to skip/start")
    lbl.grid(column=0, row=1)

    scoree = Label(frame, text="Score:  ")
    scoree.grid(column=0, row=2)

    timelbl = Label(frame, text="time:  ")
    timelbl.grid(column=0, row=3)

    txt1 = Label(frame, text="", font=("Courier", 20))
    txt1.grid(column=0, row=4)

    lbl = Label(frame, text="")
    lbl.grid(column=0, row=5)

    entry = Entry(frame, font=("Courier", 20))
    entry.grid(column=0, row=8)

    backbtn = Button(frame, text="back", height=5, width=30, command=gamechoose)
    backbtn.grid(column=0, row=100)

    time = 60

    isrunning = 0

    score = 0


    #the countdown
    def countdown():

        global time

        time = time - 1

        timelbl.after(1000, countdown)

        timelbl.config(text="time:  " + str(time))
        if time == 0:

            messagebox.showinfo("Ya NOOOB", "UR sCoRe WaS" + str(score))
            for widget in frame.winfo_children():
                widget.destroy()

            backtxt = Label(frame, text="play agair or go back?")
            backtxt.grid(column=0, row=0)

            playagainbtn = Button(frame, text="play again", height=20, width=20, command=colorgame)
            playagainbtn.grid(column=99, row=100)

            backbtn = Button(frame, text="back", height=20, width=20, command=gamechoose)
            backbtn.grid(column=100, row=100)
            time = -1


    def startgame(num):

        global isrunning
        isrunning = 1

        next()
        countdown()

    def next():

        global colors

        colors = ["Red", "Blue", "Black", "Yellow", "Green", "Brown", "Orange"]
        random.shuffle(colors)

        txt1.config(fg=str(colors[1]), text=str(colors[0]))

    def check(num):

        global score

        a = entry.get()
        a = a[:-1]
        d = random.randint(0, 1)

        if (a == colors[1]):

            score = score + 1
            scoree.config(text="Score:  " + str(score))
            entry.delete(0, 'end')
            next()
        else:
            entry.delete(0, 'end')
            score = score - 1
            scoree.config(text="Score:  " + str(score))
            next()

    if isrunning == 1:
        isrunning = 1

    timelbl.config(text="time:  " + str(time))

    window.bind("<Return>", startgame)
    window.bind("<space>", check)

def atm1():

    for widget in frame.winfo_children():
        #deletes all the widgets so the new widgets can be made
        widget.destroy()

    global balance

    #goes back
    def clearF1():

        gamechoose()

    #withdraws
    def withdraw():
        global balance

        a = float(amount)
        balance = balance - float(amount)

        messagebox.showinfo("blance", "ur money" + str(balance))
        makefirst()

    #adds to the balance
    def add():
        global balance

        a = float(amount)
        balance = a + balance
        messagebox.showinfo("balance", "ur money" + str(balance))
        makefirst()

    #makes the UI for the Bank
    def makesecond():
        global amount
        amount = moneyinput.get()
        moneyinput.destroy()

        for widget in frame.winfo_children():
            widget.destroy()

        welcome = Label(frame, text="Welcome To WDSUM (WeDontStealUrMoney)")
        welcome.grid(column=1, row=1)

        moneyamount = Label(frame, text=amount)
        moneyamount.grid(column=1, row=2)

        submitButton = Button(frame, text="Take Da Money", height=5, width=20, command=withdraw)
        submitButton.grid(column=1, row=3)

        emptyl = Label(frame, text="")
        emptyl.grid(column=1, row=4)

        submitButton = Button(frame, text="Give Da Money", height=5, width=20, command=add)
        submitButton.grid(column=1, row=5)

        emptyl = Label(frame, text="")
        emptyl.grid(column=1, row=6)

        submitButton = Button(frame, text="go back", height=5, width=20, command=makefirst)
        submitButton.grid(column=1, row=7)

    #makes the UI for the Bank
    def makefirst():

        for widget in frame.winfo_children():
            widget.destroy()

        global moneyinput
        moneyinput = Entry(frame, width=50)
        moneyinput.grid(column=1, row=0)

        emptyl = Label(frame, text="")
        emptyl.grid(column=1, row=1)

        submitButton = Button(frame, text="Submit", height=5, width=20, command=makesecond)
        submitButton.grid(column=1, row=2)

        emptyl1 = Label(frame, text="")
        emptyl1.grid(column=1, row=3)

        submitButton1 = Button(frame, text="cancel", height=5, width=20, command=clearF1)
        submitButton1.grid(column=1, row=4)

    makefirst()

def quizgame():


    #this is the code for the quizgame

    global score
    global current
    global question
    global awnser

    for widget in frame.winfo_children():
        #deletes all the widgets so the new widgets can be made
        widget.destroy()

    current = 0

    score = 0

    list = [["Are oompa loompas serial killers?\nYES\nNO\nyEs\n,nO\n", "3"],
            ["Are oompa loompas controlling the stock market?\nYES\nNO", "1"],
            ["Are oompa loompas going to kill you while you sleep?\nYES\nno", "2"],
            ["Are oompa loompas cryptomining?\nYES\nNO", "1"],
            ["Are oompa loompas controlling the stock market?\nYES\nNO\nMAYBE", "3"],
            ["Are oompa loompas watching you ?\nYES\nNO\nMAYBE", "1"]]

    question = ""
    awnser = ""

    question = list[current][0]

    awnser = list[current][1]

    lbl = Label(frame, text="score:  " + str(score))
    lbl.grid(column=0, row=1)

    lbl1 = Label(frame, text=question)
    lbl1.grid(column=0, row=2)

    entry = Entry(frame, font=("Courier", 20))
    entry.grid(column=0, row=4)

    backbtn = Button(frame, text="back", height=5, width=30, command=gamechoose)
    backbtn.grid(column=0, row=100)



    def Check(num):
        global score
        global current
        global question
        global awnser

        pplawnser = entry.get()

        if pplawnser == list[current][1]:
            score = score + 1

            if current <= 4:
                current = current + 1

                question = list[current][0]
                lbl.config(text="Score:  " + str(score))

                lbl1.config(text=list[current][0])

                awnser = list[current][1]
            else:
                messagebox.showinfo("Ya NOOOB", "UR sCoRe WaS  " + str(score - 1) + "  /5")

                for widget in frame.winfo_children():


                    widget.destroy()

                backtxt = Label(frame, text = "play agair or go back?" )
                backtxt.grid(column = 0 , row = 0)

                playagainbtn = Button(frame, text="play again",height = 20, width = 20, command = quizgame)
                playagainbtn.grid(column=99, row=100)

                backbtn = Button(frame, text="back", height = 20, width = 20,command = gamechoose)
                backbtn.grid(column=100, row=100)
        else:
            score = score - 1

            lbl.config(text="Score:  " + str(score))


    window.bind("<Return>", Check)

def calculatorgame():

    #idk what this does tbh
    def Bpress(numba):
        global mathing
        global result

        result = result + str(numba)
        mathing.set(result)

    #clears all the input
    def clear():
        global mathing
        global result

        result = ""
        mathing.set("")

    #here all the calculations are done for the programm
    def calculate():
        global mathing
        try:
            finnalresult = str(eval(result))

            mathing.set(finnalresult)

        except:

            clear()

    #creates all the UI
    def creatUI():

        global mathing, numrenderer

        for widget in frame.winfo_children():
            # deletes all the widgets so the new widgets can be made
            widget.destroy()

        numrenderer = Entry(frame, text=mathing)
        numrenderer.grid(column=1, row=0)

        btn1 = Button(frame, text="1", width=7, command=lambda: Bpress(1))
        btn1.grid(column=1, row=1)

        btn2 = Button(frame, text="2", width=7, command=lambda: Bpress(2))
        btn2.grid(column=2, row=1)

        btn3 = Button(frame, text="3", width=7, command=lambda: Bpress(3))
        btn3.grid(column=1, row=2)

        btn4 = Button(frame, text="4", width=7, command=lambda: Bpress(4))
        btn4.grid(column=2, row=2)

        btn5 = Button(frame, text="5", width=7, command=lambda: Bpress(5))
        btn5.grid(column=1, row=3)

        btn6 = Button(frame, text="6", width=7, command=lambda: Bpress(6))
        btn6.grid(column=2, row=3)

        btn8 = Button(frame, text="7", width=7, command=lambda: Bpress(7))
        btn8.grid(column=1, row=4)

        btn9 = Button(frame, text="8", width=7, command=lambda: Bpress(8))
        btn9.grid(column=2, row=4)

        btn10 = Button(frame, text="9", width=7, command=lambda: Bpress(9))
        btn10.grid(column=1, row=5)

        btn11 = Button(frame, text="0", width=7, command=lambda: Bpress(0))
        btn11.grid(column=2, row=5)

        plus = Button(frame, text="+", width=7, command=lambda: Bpress("+"))
        plus.grid(column=0, row=1)

        minus = Button(frame, text="-", width=7, command=lambda: Bpress("-"))
        minus.grid(column=0, row=2)

        slash = Button(frame, text="/", width=7, command=lambda: Bpress("/"))
        slash.grid(column=0, row=3)

        dot = Button(frame, text=",", width=7, command=lambda: Bpress("."))
        dot.grid(column=0, row=3)

        dhnamh = Button(frame, text="**", width=7, command=lambda: Bpress("**"))
        dhnamh.grid(column=0, row=0)

        par1 = Button(frame, text=")", width=7, command=lambda: Bpress(")"))
        par1.grid(column=2, row=0)

        doit = Button(frame, text="=", width=7, command=calculate)
        doit.grid(column=0, row=4)

        clearit = Button(frame, text="C", width=7, command=clear)
        clearit.grid(column=0, row=5)

        backbtn = Button(frame, text="back", height=5, width=30, command=gamechoose)
        backbtn.grid(column=1, row=100)

        clear()

    creatUI()


#basic first 2 screens
def gamechoose():

    for widget in frame.winfo_children():
        #deletes all the widgets so the new widgets can be made
        widget.destroy()

    lbl = Label(frame, text="Choose Game ur game " + name, font = ("Courier", 14))
    lbl.grid(column=0, row=0,columnspan=3)

    lbl2 = Label(frame, text=" ")
    lbl2.grid(column=1, row=1)

    quizbtn = Button(frame, text = "Quiz Game", height = 8 , width = 15, command = quizgame)
    quizbtn.grid(column = 0 ,row = 2)

    colorbtn = Button(frame, text = "Color Game", height = 8 , width = 15, command = colorgame)
    colorbtn.grid(column = 0 ,row = 3)

    calcualtor = Button(frame, text = "Calculator", height = 8 , width = 15 , command = calculatorgame)
    calcualtor.grid(column = 1,row = 2)

    paradox = Button(frame, text = "bank", height = 8, width = 15 , command = atm1)
    paradox.grid(column = 1 ,row = 3)

    typegmee = Button(frame, text = "FastType", command = typegame, height = 2, width = 31)
    typegmee.grid(column = 0 , row = 100,columnspan=3)

    backbtn = Button(frame, text = "back", command = welcomescr, height = 2, width = 31)
    backbtn.grid(column = 0 , row = 999,columnspan=3)

def welcomescr():
    global name
    global logo
    global label2

    for widget in frame.winfo_children():
        #deletes all the widgets so the new widgets can be made and that there are no bugs later on
        widget.destroy()

    lbl = Label(frame, text = "Welcome to Big Mc",font = ("Courier", 20))
    lbl.grid(column = 0, row = 0)

    lbl = Label(frame, text = " ")
    lbl.grid(column = 0, row = 1)

    lbl = Label(frame, text = " ")
    lbl.grid(column = 0, row = 2)

    entry = Entry(frame, width = 38)
    entry.grid(column = 0 , row = 2, ipady=3)

    lbl = Label(frame, text = " ")
    lbl.grid(column = 0, row = 3)

    lbl = Label(frame, text = " ")
    lbl.grid(column = 0, row = 4)

    lbl1 = Label(frame, text="Press BackSpace to exit", font = ("Courier", 10))
    lbl1.grid(column=0, row=5)

    lbl = Label(frame, text = " ")
    lbl.grid(column = 0, row = 6)

    lbl = Label(frame, text = " ")
    lbl.grid(column = 0, row = 7)

    lbl1 = Label(frame, text = "Press Enter to continue", font = ("Courier", 10))
    lbl1.grid(column = 0, row = 8)

    logo = PhotoImage(file="hz.png")

    label2 = Label(frame, image=logo)
    label2.grid(column = 0, row = 9)


    def Check(num):
        global name
        name  = entry.get()

        gamechoose()
    window.bind("<Return>", Check)
    window.bind("<BackSpace>", SystemExit)

#calls the first screen that makes the program work
welcomescr()

window.mainloop()