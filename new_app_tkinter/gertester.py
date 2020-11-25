import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("GerTester")
        self.configure(bg="blue")
        self.geometry("600x600")
        MainWindown(self)


class MainWindown(tk.Canvas):
    list_card_frame = []
    button_width = 0.2
    button_height = 0.1
    canvas_width = 1
    canvas_height = 0.8
    relx = 0
    rely = 0

    def correct_positioning(
        self, width: float, height: float, place_right: bool
    ) -> None:
        if place_right == True:
            self.rely = self.canvas_height
            self.relx += width
        else:
            self.rely += height

    def __init__(self, application):
        super().__init__(master=application)
        self.pack(fill="both", expand=True)
        self.config(bg="black")
        self.create_widgets()

    def create_widgets(self):
        self.canvas_for_frames = tk.Canvas(master=self)
        self.BT_add = tk.Button(
            master=self,
            text="Add Card Frame",
            command=self.create_card,
        )
        self.BT_del = tk.Button(
            master=self,
            text="Delete Card Frame",
            command=self.delete_card,
        )
        self.BT_1 = tk.Button(
            master=self,
            text="BT1",
        )
        self.BT_2 = tk.Button(
            master=self,
            text="BT2",
        )
        self.place_widgets()

    def place_widgets(self):
        self.canvas_for_frames.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.canvas_width,
            relheight=self.canvas_height,
        )
        self.correct_positioning(
            width=self.canvas_width, height=self.canvas_height, place_right=False
        )
        self.BT_add.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.button_width,
            relheight=self.button_height,
        )
        self.correct_positioning(
            width=self.button_width, height=self.button_height, place_right=False
        )
        self.BT_del.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.button_width,
            relheight=self.button_height,
        )
        self.correct_positioning(
            width=self.button_width, height=self.button_height, place_right=True
        )
        self.BT_1.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.button_width,
            relheight=self.button_height,
        )
        self.correct_positioning(
            width=self.button_width, height=self.button_height, place_right=False
        )
        self.BT_2.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.button_width,
            relheight=self.button_height,
        )

    def create_card(self):
        frame = CardFrame(main_windown=self.canvas_for_frames)
        self.list_card_frame.append(frame)

    def delete_card(self):
        last_card = int(len(self.list_card_frame)) - 1
        if last_card > 0:
            self.list_card_frame[last_card].destroy()
            self.list_card_frame.pop(last_card)
            print(self.list_card_frame)
        elif last_card == 0:
            print("Can't delete all cards")
        else:
            print("CardFrame was not initiated, add card frame")


class CardFrame(tk.Frame):
    resources = ["AGI", "KUNI"]
    list_widgets = []
    button_width = 1
    button_height = 0.2
    option_menu_width = 1
    option_menu_height = 0.2
    relx = 0.0
    rely = 0.0

    def correct_positioning(
        self, width: float, height: float, place_right: bool
    ) -> None:
        if place_right == True:
            self.rely = 0
            self.relx += width
        else:
            self.rely += height

    def __init__(self, main_windown):
        super().__init__(master=main_windown)
        self.pack(fill="both", expand=True, side="left")
        self.config(bg="green")
        self.create_widgets()

    def create_widgets(self):
        self.selected_resource = tk.StringVar()
        self.resource_menu = tk.OptionMenu(
            self, self.selected_resource, *self.resources
        )
        self.place_widgets()
        self.trace_variables()

    def place_widgets(self):
        self.resource_menu.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.option_menu_width,
            relheight=self.option_menu_height,
        )
        self.correct_positioning(
            width=self.option_menu_width,
            height=self.option_menu_height,
            place_right=False,
        )

    def trace_variables(self):
        self.selected_resource.trace_add(
            mode="write",
            callback=lambda *args, selected_resource=self.selected_resource: self.validate(
                selected_resource
            ),
        )

    def validate(self, selected_resource):
        selected_resource = selected_resource.get()
        print(selected_resource)
        self.on_change_selected_resource()

    def on_change_selected_resource(self):
        tinta = self.selected_resource.get()
        if tinta == self.resources[0]:
            self.create_agi()
        elif tinta == self.resources[1]:
            self.create_kuni()

    def create_agi(self):
        Bt_agi = tk.Button(self, text="BT agi", command=self.print_it)
        Bt_agi.place(
            relx=self.relx,
            rely=self.rely + 0.2,
            relwidth=self.button_width,
            relheight=self.button_height,
        )

    def create_kuni(self):
        Bt_agi = tk.Button(self, text="BT Kuni", command=self.print_it)
        Bt_agi.place(
            relx=self.relx,
            rely=self.rely + 0.2,
            relwidth=self.button_width,
            relheight=self.button_height,
        )

    def print_it(self):
        print(self.winfo_children()[0])


def main():
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()
