import tkinter
from tkinter import *
import random
from tkinter import messagebox

rook=tkinter.Tk()
rook.geometry("800x700")
rook.configure(background="#512E5F")
answer = [
        "python",
        "java",
        "hello",
        "love",
        "india",
        "turtle",
        "shalini",
        "house",
        "army",
        "minster",
        "aircraft",
    ]
words = [
        "ptynoh",
        "vaja",
        "lloeh",
        "veol",
        "diani",
        "tutrle",
        " inilash",
        "sehou",
        "ramy",
        "nsimter",
        "raftcair",
    ]
clues = [
        "clue 1 :from where you listen gossip \n clue 2 :what you were in engagment in hand",
        "clue 1:beside the beech where people take sun bath \n clue 2: word is similar when girl cant say to her rival a bitch",
        "clue 1:top of yor head long /short all  types of \n clue 2: associated with word  silence in respect to class refer by teacher",
        "clue 1:name of a body part \n clue 2: round/ and also taught to 1 students during abcd lesson",
        "clue 1:the place you sleep \n clue 2: from which you cover it ",
        "clue 1:opposite of comming together\n clue 2:opposite of down",
        "clue 1:it is seen after rain it is bit colourfull  ",
        "clue 1:greeting words used when people met other people",
        "clue 1:the day we born is celebrated as",
        "clue 1:it is used to feed to new born infant",
        "clue 1:it is used to amplify the sound/music",
        "clue 1:man has a new born baby boy and who is boy to that man?"
    ]
answers = ["earring", "sandwich", "hair pin", "football", "bed sheet","split up","rainbow","hello","birthday","milk" ,"speaker","son"]

def sps():


    root1 = tkinter.Tk()
    root1.geometry("500x500+920+250")

    # function call
    def quit():
        sys.exit()

    def stone():
        text.delete(0.0, "end")
        num = random.randrange(1, 4)
        if (num == 2):
            text.insert(0.0, "stone")
            messagebox.showinfo("result", "DRAW")
            text.delete(0.0, "end")
            return
        if (num == 3):
            text.insert(0.0, "paper")
            messagebox.showinfo("result", "LOOSE")
            text.delete(0.0, "end")
            return
        else:
            text.insert(0.0, "scissors")
            messagebox.showinfo("result", "YOU WIN")
            text.delete(0.0, "end")
        return

    def paper():
        text.delete(0.0, "end")
        num = random.randrange(1, 4)
        if (num == 3):
            text.insert(0.0, "paper")
            messagebox.showinfo("result", "DRAW");
            text.delete(0.0, "end")
            return
        if (num == 2):
            text.insert(0.0, "stone")
            messagebox.showinfo("result", "YOU WIN")
            text.delete(0.0, "end")
            return
        else:
            text.insert(0.0, "scissors")
            messagebox.showinfo("result", "YOU LOOSE")
            text.delete(0.0, "end")
        return

    def scissors():
        text.delete(0.0, "end")
        num = random.randrange(1, 4)
        if (num == 1):
            text.insert(0.0, "scissors")
            messagebox.showinfo("result", "DRAW")
            text.delete(0.0, "end")
            return
        if (num == 2):
            text.insert(0.0, "paper")
            messagebox.showinfo("result", "YOU WIN")
            text.delete(0.0, "end")
            return
        else:
            text.insert(0.0, "stone")
            messagebox.showinfo("result", "YOU LOOSE")
            text.delete(0.0, "end")
        return

    def help():
        root12 = tkinter.Tk()

        root12.configure(background="black")

        def return1():
            sys.exit()

        label5 = Label(root12,
                       text="\tRULES\n\n\n1:their are three rock paper scissors in this game \n\n  2:if you got scissors and computer got stone then you LOSES!!\n\n3:if computer got paper you got stone you LOSES!!\n\n4:you got scissor and computer got stone you WON!!",
                       font=("comic sans", 15), bg="black", fg="grey")
        label5.pack()
        but = Button(root12, text="return", fg="black", command=return1)
        but.pack()
        root12.mainloop()

    # heading
    root1.configure(background="black")
    label = Label(root1, text="rOcK paPer sCissoRs", font=("comic sans", 20), fg="cyan", bg="black")
    label.pack()
    label1 = Label(root1, text="Wellcome to the Game", fg="light green", bg="black", font=("verdence", 12))
    label1.pack()

    # button for help and quit
    button1 = Button(root1, text="help", command=help, width=9, fg="black", bg="#C39BD3")
    button1.place(x=160, y=80)
    button2 = Button(root1, text="quit game", command=quit, fg="black", bg="#C39BD3",)
    button2.place(x=270, y=80)
    # tag
    label2 = Label(root1, text="sTonE", fg="grey", bg="black", font=("verdance", 15))
    label2.place(x=140, y=160)
    label3 = Label(root1, text="paPer", fg="grey", bg="black", font=("verdence", 15))
    label3.place(x=270, y=160)
    label3 = Label(root1, text="sCissOrs", fg="grey", bg="black", font=("verdence", 15))
    label3.place(x=200, y=250)

    # for option choose
    button1 = Button(root1, text="stone", width=15, command=stone, fg="black", bg="#A3E4D7")
    button1.place(x=110, y=200)
    button2 = Button(root1, text="paper", width=15, command=paper, fg="black", bg="#E6B0AA")
    button2.place(x=270, y=200)
    button3 = Button(root1, text="scissors", width=15, command=scissors, fg="black", bg="#7FB3D5")
    button3.place(x=190, y=290)

    # computer move
    label4 = Label(root1, text="computer move", fg="light blue", bg="black", font=("comic sans", 15))
    text = Text(root1, width=30, height=2, wrap=WORD, font=("verdence", 15))
    text.pack(side=BOTTOM)
    label4.pack(side=BOTTOM)

    root1.mainloop()


def guess():
    from tkinter import messagebox
    rooto = tkinter.Tk()
    rooto.geometry('500x100+900+500')
    rooto.title("word guessing game")

    rooto.configure(background="black")

    global no

    def stop():
        sys.exit()

    def game():

        root2 = tkinter.Tk()
        root2.geometry('1000x500+700+100')
        root2.title("word guessing game")
        root2.configure(background="black")

        def default():
            global no
            label.config(text=clues[no])

        def changeclue():
            global no, clue, answers
            no = random.randrange(0, 12)
            label.config(text=clues[no])
            entry1.delete(0, END)

        def check():
            global clue, answers, no
            an = entry1.get()
            if (an == answers[no]):
                messagebox.showinfo("Sucess", "correct guess")
                changeclue()
            else:
                messagebox.showinfo("error", "incorrect guess")
                entry1.delete(0, END)

        global no
        no = random.randrange(0, 12)
        # label for clues
        label = Label(root2, text="you are here", fg="white", bg="black", font=("verdence", 18), )
        label.pack(side=TOP)
        # for entry the guess
        ans = StringVar()
        entry1 = Entry(root2, font=("comic sans", 20), textvariable=ans, )
        entry1.pack(pady=20)
        # checking button
        button = Button(root2, text="CHECK", fg="black", bg="light green", width=10, command=check, )
        button.pack()
        # for reseting
        button1 = Button(root2, text="RESET", fg="black", bg="light green", width=10, command=changeclue)
        button1.pack(pady=20)

        default()
        root2.mainloop()

    # label tag
    lbl1 = Label(rooto, text="Do You Want To play This Game", font=("verdence", 20), )
    lbl1.pack(side=TOP, pady=10)

    # button tag for yes
    but = Button(rooto, text="YES", bg="light blue", fg="black", width=24, command=game, )
    but.pack(padx=10)

    # button tag for no
    but1 = Button(rooto, text="NO", bg="light blue", fg="black", width=24, command=stop, )
    but1.pack(padx=10)

    rooto.mainloop()




def jumb():

    root = tkinter.Tk()
    root.geometry('800x500+700+200')
    root.title("jumbbled")
    root.configure(background="black")

    num = random.randrange(0, 11, 1)
    def res():
        global num, words, answer
        num = random.randrange(0, 11, 1)
        lbl.config(text=words[num])
        e1.delete


    def default():
        global num, words, answer
        num = random.randrange(0, 11, 1)
        lbl.config(text=words[num])
    def checkans():
        global num, words, answer
        var = e1.get()
        if (var == answer[num]):
            nam = e2.get()
            messagebox.showinfo("sucess", nam + " correct answer")
            e1.delete(0, END)
            res()
        else:
            nam = e2.get()
            messagebox.showinfo("incorrect answer", nam + " incorrect answer")
            e1.delete(0, END)

    label = Label(root, text="JUMMBLED WORDS", fg="yellow", bg="black", font=("verdence", 15))
    label.pack(pady=20)
    lbl1 = Label(
        root,
        text="name",
        font=("comic sans", 14),
        fg="cyan",
        bg="black",
    )
    lbl1.pack()

    # for entry name
    e2 = Entry(root, font=("comic sans", 15), )
    e2.pack()

    # to show the jumbbled words
    lbl = Label(
        root,
        text="your here",
        font=("verdence", 18),
        width=18,
        fg="white",
        bg="black",
    )
    lbl.pack(pady=40, padx=10)

    # to take entry from text box
    ans1 = StringVar()
    e1 = Entry(
        root,
        font=("verdence", 18),
        textvariable=ans1,
    )
    e1.pack()

    # checking button
    btnvheck = Button(
        root,
        text="CHECK",
        font=("comic sans ms", 16),
        width=10,
        bg="light green",
        fg="black",
        relief=GROOVE,
        command=checkans,
    )
    btnvheck.pack(pady=30)

    # reseting button
    btnvheck = Button(
        root,
        text="RESET",
        font=("comic sans ms", 16),
        width=10,
        bg="light green",
        fg="black",
        relief=GROOVE,
        command=res,
    )
    btnvheck.pack(pady=10)

    default()
    root.mainloop()



label=Label(rook,text="gAmEs  tO pLaY",font=("comic sans",40),width=50,fg="cyan",bg="black")
label.pack(pady=10)
label_1=Label(rook,text="JUMBBLED WORDS",font=("comic sans",22),width=90,fg="light green",bg="black")
label_1.pack(pady=30)
button_1=Button(rook,text="click",width=15,borderwidth=3,relief="raised",command=jumb,bg="light green")
button_1.pack()

label_2=Label(rook,text="GUESS THE WORD",width=90,font=("comic sans",22),fg="yellow",bg="black")
label_2.pack(pady=30)
button_2=Button(rook,text="click",width=15,borderwidth=3,relief="raised",command=guess,bg="yellow")
button_2.pack()
label_3=Label(rook,text="STONE PAPER SCISSORS",width=90,font=("comic sans",22),fg="light blue",bg="black")


button_3=Button(rook,text="click",width=15,borderwidth=3,relief="raised",command=sps,bg="light blue")
label_3.pack(pady=30)
button_3.pack()

label=Label(rook,text="Quit Window",font=("comic sans",40),width=50,fg="cyan",bg="black",)
label.pack(side="bottom")
button_4=Button(rook,text="click",width=15,borderwidth=3,relief="raised",bg="cyan",command=sys.exit)

button_4.pack(side="bottom")


rook.mainloop()