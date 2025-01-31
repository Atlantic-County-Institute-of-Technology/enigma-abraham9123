import tkinter as tk
from random import randint
from tkinter import PhotoImage
class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("diepoker")
        self.root.geometry("800x800")
        self.root.configure(background='black')
        self.period_count = 0
        self.rolls = 3
        self.blind = 0
        self.keeplist = []
        self.dicelist = []
        self.keepLabelList = []
        self.bg = PhotoImage(file="images/bg.png")
        self.bgLabel = tk.Label(
            root,
            image=self.bg
        )
        self.bgLabel.place(
            x=0,
            y=0,
        )
        self.label = tk.Label(
            root,
            text="diepoker",
            font=("comic sans", 50),
            fg="black"
        )
        self.label.pack(pady=25)
        self.blindtxt = tk.Label(
            root,
            text="",
            font=("comic sans",20)

        )
        self.start = tk.Button(
            root,
            text="start",
            font=("comic sans", 30),
            command=self.difficulties
        )
        self.start.pack(pady=50)
        self.rollingLabel = tk.Label(
            root,
            text="",
            font=("comic sans",30)
        )
        self.easy = tk.Button()
        self.difficulties_frame = tk.Frame(
            root,
            bg="black"
        )
        self.difficulties_frame.pack(pady=50)
        self.easy = tk.Button(
            self.difficulties_frame,
            text="easy",
            font=("comic sans",30)
        )

        self.normal = tk.Button(
            self.difficulties_frame,
            text="normal",
            font=("comic sans", 30)
        )
        self.hard = tk.Button(
            self.difficulties_frame,
            text="hard",
            font=("comic sans", 30)
        )
        self.keep_frame = tk.Frame(
            root,
            bg="black"
        )
        self.keep_frame.pack(pady=50)
        self.dice_frame = tk.Frame(
            root,
            bg="black"
        )
        self.keepButton_frame = tk.Frame(
            root,
            bg="black"
        )
        for _ in range(6):
            self.dicelist.append(tk.Label(self.dice_frame, bg="black"))
        for _ in range(6):
            self.keeplist.append(tk.Button(self.keepButton_frame,text="keep",command=self.keep))
        self.dice_frame.pack()
        self.keepButton_frame.pack()
        for _ in range(6):
            self.keepLabelList.append(tk.Label(self.keep_frame, bg="black"))
        self.image_label = tk.Label(root)
        self.keep_images = {
            1: PhotoImage(file="images/WhiteSquare1.png"),
            2: PhotoImage(file="images/WhiteSquare2.png"),
            3: PhotoImage(file="images/WhiteSquare3.png"),
            4: PhotoImage(file="images/WhiteSquare4.png"),
            5: PhotoImage(file="images/WhiteSquare5.png"),
            6: PhotoImage(file="images/WhiteSquare6.png"),
        }

        self.image_paths = {
            1: "images/dice1.png",
            2: "images/dice2.png",
            3: "images/dice3.png",
            4: "images/dice4.png",
            5: "images/dice5.png",
            6: "images/dice6.png"
        }


        self.dice_images = {
            1: PhotoImage(file=self.image_paths[1]),
            2: PhotoImage(file=self.image_paths[2]),
            3: PhotoImage(file=self.image_paths[3]),
            4: PhotoImage(file=self.image_paths[4]),
            5: PhotoImage(file=self.image_paths[5]),
            6: PhotoImage(file=self.image_paths[6]),
        }
    def rolling(self):
        self.rollingLabel.config(text="rollin the dice")
        self.period_count = 0
        self.animate_periods()
    def animate_periods(self):
        if self.period_count < 3:
            self.rollingLabel.config(text=f"Rolling{'.' * (self.period_count + 1)}")
            self.period_count += 1
            self.root.after(250, self.animate_periods)
        else:
            self.rollingLabel.pack_forget()
            self.blindtxt.pack()
            self.diceRoll()
    def diceRoll(self):
        for button in self.keeplist:
            button.pack(side=tk.LEFT, padx=33.4)
        for label in self.keepLabelList:
            label.pack(side=tk.LEFT, padx=10)
        for label in self.dicelist:
            label.pack(side=tk.LEFT, padx=10)
    # Roll six dice and update the images

        for label in self.keepLabelList:
            roll = randint(1, 6)
            label.configure(image=self.keep_images[roll])
            label.pack()
        for label in self.dicelist:
            roll = randint(1, 6)  # Randomly select a number between 1 and 6
            label.configure(image=self.dice_images[roll])
            label.pack()
    def keep(self):
        for x in range(1,7):
            if self.keeplist[x-1] == self.keepLabelList[x-1]:
                self.keepLabelList[x-1].config(image=self.dice_images.get(x))
    def difficulties(self):
        self.start.pack_forget()
        self.easy.configure(command=self.easydif)
        self.normal.configure(command=self.normaldif)
        self.hard.configure(command=self.harddif)
        self.easy.pack(pady=10)
        self.normal.pack(pady=10)
        self.hard.pack(pady=10)
    def easydif(self):
        self.rollingLabel.pack()
        self.rolling()
        self.blind = 300
        self.difficulties_frame.pack_forget()
        self.blindtxt.configure(text=f"the score you gotta beat: {self.blind}")
    def normaldif(self):
        self.rollingLabel.pack()
        self.rolling()
        self.blind = 450
        self.difficulties_frame.pack_forget()
        self.blindtxt.configure(text=f"the score you HAVE to beat: {self.blind}")
    def harddif(self):
        self.rollingLabel.pack()
        self.rolling()
        self.blind = 650
        self.difficulties_frame.pack_forget()
        self.blindtxt.configure(text=f"the score were forcing you to beat: {self.blind}")
if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()