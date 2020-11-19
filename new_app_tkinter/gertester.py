import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("GerTester")
        self.configure(bg="blue")
        self.geometry("600x600")
        MainWindown(self)


class MainWindown(tk.Canvas):
    list_card_frame = []
    BT_x = 0.2
    BT_y = 0.050
    pos_x = 0.0
    pos_y = 0.4

    @staticmethod
    def correct_widget_y_positioning(self) -> None:
        self.pos_y = self.pos_y + self.BT_y


    def __init__(self, application):
        tk.Canvas.__init__(self, master=application)
        self.pack(side="top", fill="both", expand=True)
        self.config(bg="black")
        self.create_widgets()

    def create_widgets(self):
        self.BT_add = tk.Button(
            self,
            text="Add Card Frame",
            command=self.create_card,
        )
        self.BT_del = tk.Button(
            self,
            text="Delete Card Frame",
            command=self.delete_card,
        )
        self.place_widgets()

    def place_widgets(self):
        self.BT_add.place(relx=self.pos_x, rely=self.pos_y, relwidth=self.BT_x, relheight=self.BT_y)
        self.correct_widget_y_positioning(self)
        self.BT_del.place(relx=self.pos_x, rely=self.pos_y, relwidth=self.BT_x, relheight=self.BT_y)
        self.correct_widget_y_positioning(self)

    def create_card(self):
        frame = CardFrame(self)
        self.list_card_frame.append(frame)

    def delete_card(self):
        list_size = len(self.list_card_frame)
        print(list_size)


class CardFrame(tk.Frame):
    def __init__(self, main_windown):
        tk.Frame.__init__(self, master=main_windown)
        self.pack(padx=0, pady=0)
        self.config(bg="green", height=150, width=150)
        button_1 = tk.Button(self, text="Click Me")
        button_1.place(x=0, y=0)


def main():
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()
