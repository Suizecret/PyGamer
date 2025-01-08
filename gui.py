import logging
import random
from tkinter import ttk, messagebox
from tkinter import *
import numberGuess


class GUI:
    root: Tk
    mainframe: ttk.Frame
    user_value: int
    score: int = int
    random_value: int = int
    hint = "Take a Guess First"

    def draw_guessing_frame(self):
        self.mainframe.destroy()
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0)

        # Create new UI Elements #
        # LABEL #
        Label(
            self.mainframe,
            text="Possible Score: " + str(self.score),
        ).grid(column=0, row=0, sticky=W)
        Label(
            self.mainframe,
            text="last Guess: %s" % ("" if self.user_value is int else self.user_value)
        ).grid(column=0, row=1, sticky=N)
        Label(
            self.mainframe,
            text="hint: " + self.hint
        ).grid(column=0, row=2, sticky=N)

        # ENTRY #
        user_text = IntVar()
        ttk.Entry(
            self.mainframe,
            width=20,
            textvariable=user_text,
        ).grid(column=0, row=3, sticky=N)

        # BUTTON #
        ttk.Button(
            self.mainframe,
            text="Take a Guess",
            width=15,
            command=lambda: self.check_guess(user_text, self.random_value, self.score)


        ).grid(column=1, row=3, sticky=N)

    def setup_guessing(self, high, low):

        # init and reset the values #

        self.user_value: int = int()
        self.hint = "Take a Guess First"
        self.score: int = int()
        # Parsing int #
        try:
            num_min = int(low.get())
            num_max = int(high.get())
        except TclError as e:
            logging.exception(e)
            messagebox.showerror("Wrong Input", "Please Only use Integer numbers")
            return

        # Check input #
        if num_min > num_max:
            num_min += num_max
            num_max = num_min - num_max
            num_min -= num_max
            messagebox.showinfo("Number Switch", "Your Numbers where switched")

        # Round Setup #
        num_range = num_max - num_min
        self.score = 10 * num_range
        self.random_value = random.randint(num_min, num_max)

        # Check if there is any Range to guess
        if num_range == 0:
            messagebox.showerror("Wrong Input", "The Range between these Numbers is to Low")
            raise ValueError("The Range between these Numbers is to Low")

        # Prepare new Frame to Guess #
        self.draw_guessing_frame()

    def check_guess(self, user_text, random_value, score):
        try:
            user_value = user_text.get()
        except TclError as e:
            messagebox.showerror("Wrong Input", "Please Only use Integer numbers")
            logging.exception(e)
            return
        self.user_value = user_value
        value = numberGuess.check_guess(user_value, random_value, score)
        win = value[0]
        self.score = value[1]
        self.hint = value[2]
        self.game_round(win)

    def number_guesser_game(self):
        # Refactor the Window #
        self.root.title("Number Guesser")
        self.root.geometry("500x500")
        self.mainframe.destroy()

        # Create and Add new UI Elements #
        # FRAME #
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0)

        # LABEL #
        Label(
            self.mainframe,
            text="Please enter the Range you want to play in."
        ).grid(column=1, row=0, sticky=N)
        Label(
            self.mainframe,
            text="Min: "
        ).grid(column=0, row=1, sticky=W)
        Label(
            self.mainframe,
            text="Max: "
        ).grid(column=0, row=2, sticky=W)

        # ENTRY #
        low = IntVar()
        ttk.Entry(
            self.mainframe,
            width=20,
            textvariable=low
        ).grid(column=1, row=1, sticky=W)
        high = IntVar()
        ttk.Entry(
            self.mainframe,
            width=20,
            textvariable=high
        ).grid(column=1, row=2, sticky=W)

        # BUTTONS #
        ttk.Button(
            self.mainframe,
            text="Start",
            width=15,
            command=lambda: self.setup_guessing(high, low)
        ).grid(column=1, row=3, sticky=S)

    def game_round(self, win):
        if win:
            self.mainframe.destroy()
            self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
            self.mainframe.grid(column=0, row=0, )
            Label(
                self.mainframe,
                text=self.hint
            ).grid(column=1, row=0, sticky=N)
            Label(
                self.mainframe,
                text="Your Score is: " + str(self.score)
            ).grid(column=1, row=1, sticky=N)
            ttk.Button(
                self.mainframe,
                text="New Round",
                command=lambda: (
                    self.number_guesser_game()
                )
            ).grid(column=1, row=2, sticky=N)
            return
        else:
            self.draw_guessing_frame()

    def start(self):
        # Create The Window #
        self.root = Tk()
        self.root.title("Python Gamer")
        self.root.geometry("550x550")

        # Create the Mainframe #
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, )

        # Configure the Grid #
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Adding Ui Elements and sort them into the Grid #
        # LABELS #
        Label(
            self.mainframe,
            text="Number Guesser: ",
            padx=20,
            pady=20,
        ).grid(column=0, row=0, sticky=W)

        Label(
            self.mainframe,
            text="Rock Paper Scissors: ",
            padx=20,
            pady=20,
        ).grid(column=0, row=1, sticky=W)

        # BUTTONS #
        ttk.Button(
            self.mainframe,
            width=15,
            text="Start",
            command=self.number_guesser_game
        ).grid(column=1, row=0, sticky=W)

        ttk.Button(
            self.mainframe,
            width=15,
            text="Start",
            command=lambda: messagebox.showinfo("Under Construction", "This is the Teaser for the upcoming Game, "
                                                                      "Please be patient.")
        ).grid(column=1, row=1, sticky=W)

        # Starting the Main Loop #
        self.root.mainloop()
if __name__ == "__main__":
    gameGui = GUI()
    gameGui.start()
