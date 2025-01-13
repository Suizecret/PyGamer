from random import randint
from tkinter import *
from tkinter import ttk, messagebox
from numberGuess import *
from rps import *


class GUI:
    root: Tk
    mainframe: ttk.Frame

    # NG VALUES #
    ng_user_value: int
    ng_score = int
    ng_random_value = int
    ng_hint = "Take a Guess First"

    # RPS VALUES #
    rps_selected: list

    # Draw the Frame for the Number guesser Game #
    def ng_draw_guessing_frame(self):
        self.reset_mainframe()

        # Create new UI Elements #
        # LABEL #
        Label(
            self.mainframe,
            text="Possible Score: " + str(self.ng_score),
        ).grid(column=0, row=0, sticky=W)
        Label(
            self.mainframe,
            text="last Guess: %s" % ("" if self.ng_user_value is int else self.ng_user_value)
        ).grid(column=0, row=1, sticky=N)
        Label(
            self.mainframe,
            text="hint: " + self.ng_hint
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
            command=lambda: self.ng_check_guess(user_text, self.ng_random_value, self.ng_score)


        ).grid(column=1, row=3, sticky=N)

    # Re/Set Needed Variable generate Random Value #
    def ng_setup_guessing(self, high, low):

        # init and reset the values #

        self.ng_user_value: int = int()
        self.ng_hint = "Take a Guess First"
        self.ng_score: int = int()
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
        self.ng_score = 10 * num_range
        self.ng_random_value = randint(num_min, num_max)

        # Check if there is any Range to guess
        if num_range == 0:
            messagebox.showerror("Wrong Input", "The Range between these Numbers is to Low")
            raise ValueError("The Range between these Numbers is to Low")

        # Prepare new Frame to Guess #
        self.ng_draw_guessing_frame()

    # prepare and Check the Guess, receive and handel Answer #
    def ng_check_guess(self, user_text, random_value, score):
        try:
            user_value = user_text.get()
        except TclError as e:
            messagebox.showerror("Wrong Input", "Please Only use Integer numbers")
            logging.exception(e)
            return
        self.ng_user_value = user_value
        value = check_guess(user_value, random_value, score)
        win = value[0]
        self.ng_score = value[1]
        self.ng_hint = value[2]
        self.ng_game_round(win)

    # Build First NG window to Receive initial game Information's #
    def ng_number_guesser_game(self):
        # Refactor the Window #
        self.root.title("Number Guesser")
        self.root.geometry("300x200")
        self.reset_mainframe()

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
            command=lambda: self.ng_setup_guessing(high, low)
        ).grid(column=1, row=3, sticky=S)
        ttk.Button(
            self.mainframe,
            text="Back",
            width=15,
            command=lambda: self.start()
        ).grid(column=1, row=3, sticky=S)

    def ng_game_round(self, win):
            if win:
                self.reset_mainframe()
                Label(
                    self.mainframe,
                    text=self.ng_hint
                ).grid(column=1, row=0, sticky=N)
                Label(
                    self.mainframe,
                    text="Your Score is: " + str(self.ng_score)
                ).grid(column=1, row=1, sticky=N)
                ttk.Button(
                    self.mainframe,
                    text="New Round",
                    command=lambda: (
                        self.ng_number_guesser_game()
                    )
                ).grid(column=1, row=2, sticky=N)
                return
            else:
                self.ng_draw_guessing_frame()

    # Add the Value to list #
    def rps_returner(self,selected,amount_of_player):
        self.rps_selected.append(selected)
        self.rps_game_round(amount_of_player)

    # Draw the Frame for the Number guesser Game #
    def rps_select(self,amount_of_player):
        self.reset_mainframe()

        player_text = ""

        if amount_of_player > 1:
            if len(self.rps_selected) == 0:
                player_text = "Player One "
            else:
                player_text = "Player Two "

        Label(
            self.mainframe,
            text=player_text + "Pic your Weapon: ",
        ).grid(column=0, row=0, sticky=W)
        ttk.Button(
            self.mainframe,
            text="Rock",
            width=15,
            command=lambda: self.rps_returner(0,amount_of_player)
        ).grid(column=1, row=0, sticky=S)
        ttk.Button(
            self.mainframe,
            text="Paper",
            width=15,
            command=lambda: self.rps_returner(1,amount_of_player)
        ).grid(column=1, row=1, sticky=S)
        ttk.Button(
            self.mainframe,
            text="Scissors",
            width=15,
            command=lambda: self.rps_returner(2,amount_of_player)
        ).grid(column=1, row=2, sticky=S)
        ttk.Button(
            self.mainframe,
            text="Back",
            width=15,
            command=lambda: self.rps_game_setup()
        ).grid(column=1, row=3, sticky=S)

    # Progress received Data #
    def rps_game_round(self, amount_of_players):
        win_msg = ""

        match amount_of_players:
            case 1:
                if len(self.rps_selected) == 1:
                    cpu = randint(0,2)
                    winner = rps_check_win(self.rps_selected[0], cpu)
                    self.reset_mainframe()
                    match winner:
                        case 0:
                            win_msg ="draw You Picked " + str(self.rps_selected[0]) + " and the CPU Picked also " + str(cpu)
                        case 1:
                            win_msg = "YOU WON"
                        case 2:
                            win_msg ="Sad news, you were Unlucky"
                    Label(
                        self.mainframe,
                        text=win_msg,
                    ).grid(column=0, row=0, sticky=W)
                    ttk.Button(
                        self.mainframe,
                        text="Back",
                        command=lambda: self.rps_game_setup()
                    ).grid(column=0, row=1,sticky=N)
                else:
                    self.rps_select(amount_of_players)
            case 2:
                if len(self.rps_selected) == 2:
                    winner = rps_check_win(self.rps_selected[0],self.rps_selected[1])
                    self.reset_mainframe()
                    match winner:
                        case 0:
                            win_msg ="draw P1 Picked " + str(self.rps_selected[0]) + " and P2 Picked also " + str(self.rps_selected[1])
                        case 1:
                            win_msg ="P1 Won"
                        case 2:
                            win_msg ="P2 Won"
                    Label(
                        self.mainframe,
                        text=win_msg,
                    ).grid(column=0, row=0, sticky=W)
                    ttk.Button(
                        self.mainframe,
                        text="Back",
                        command=lambda: self.rps_game_setup()
                    ).grid(column=0, row=1,sticky=N)
                else:
                    self.rps_select(amount_of_players)

    def rps_game_setup(self):
        # Refactor the Window #
        self.root.title("Rock Paper Scissors")
        self.root.geometry("300x200")
        self.rps_selected = list()

        self.reset_mainframe()
        Label(
            self.mainframe,
            text="PVE or PVP: ",
        ).grid(column=0, row=0, sticky=W)
        ttk.Button(
            self.mainframe,
            text="PVP",
            width=15,
            command=lambda: self.rps_game_round(2)
        ).grid(column=1, row=0, sticky=S)
        ttk.Button(
            self.mainframe,
            text="PVE",
            width=15,
            command=lambda: self.rps_game_round(1)
        ).grid(column=1, row=1, sticky=S)
        ttk.Button(
            self.mainframe,
            text="Back",
            width=15,
            command=lambda: self.start()
        ).grid(column=1, row=3, sticky=S)

    def start(self):
        # Create The Window #
        if not hasattr(self,'root'):
            self.root = Tk()
        self.root.title("Python Gamer")
        self.root.geometry("300x200")

        # Create the Mainframe #
        if not hasattr(self,'mainframe'):
            self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
            self.mainframe.grid(column=0, row=0, )
        else:
            self.reset_mainframe()

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
            command=self.ng_number_guesser_game
        ).grid(column=1, row=0, sticky=W)

        ttk.Button(
            self.mainframe,
            width=15,
            text="Start",
            command=lambda: self.rps_game_setup()
        ).grid(column=1, row=1, sticky=W)

        # Starting the Main Loop #
        self.root.mainloop()

    def reset_mainframe(self):
        self.mainframe.destroy()
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, )


if __name__ == "__main__":
    gameGui = GUI()
    gameGui.start()
