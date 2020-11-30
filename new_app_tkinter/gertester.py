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
    label_width = 0.3
    label_height = 0.1
    entry_width = 0.3
    entry_height = 0.1
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
        self.create_card()

    def create_widgets(self):
        self.canvas_for_frames = tk.Canvas(master=self)
        self.bt_add = tk.Button(
            master=self,
            text="Add Card Frame",
            command=self.create_card,
        )
        self.bt_del = tk.Button(
            master=self,
            text="Delete Card Frame",
            command=self.delete_card,
        )
        self.bt_mes = tk.Button(
            master=self,
            text="Measure",
            command=self.validate_data,
        )
        self.bt_stop = tk.Button(
            master=self,
            text="Stop Measure",
            command=self.stop_measure,
        )
        self.lb_smp = tk.Label(master=self, text="Samples")
        self.ent_smp = tk.Entry(master=self)
        self.lb_f_name = tk.Label(master=self, text="File Name")
        self.ent_f_name = tk.Entry(master=self)
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
        self.bt_add.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.button_width,
            relheight=self.button_height,
        )
        self.correct_positioning(
            width=self.button_width, height=self.button_height, place_right=False
        )
        self.bt_del.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.button_width,
            relheight=self.button_height,
        )
        self.correct_positioning(
            width=self.button_width, height=self.button_height, place_right=True
        )
        self.bt_mes.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.button_width,
            relheight=self.button_height,
        )
        self.correct_positioning(
            width=self.button_width, height=self.button_height, place_right=False
        )
        self.bt_stop.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.button_width,
            relheight=self.button_height,
        )
        self.correct_positioning(
            width=self.button_width, height=self.button_height, place_right=True
        )
        self.lb_smp.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.label_width,
            relheight=self.label_height,
        )
        self.correct_positioning(
            width=self.label_width, height=self.label_height, place_right=False
        )
        self.ent_smp.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.entry_width,
            relheight=self.entry_height,
        )
        self.correct_positioning(
            width=self.entry_width, height=self.entry_height, place_right=True
        )
        self.lb_f_name.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.label_width,
            relheight=self.label_height,
        )
        self.correct_positioning(
            width=self.label_width, height=self.label_height, place_right=False
        )
        self.ent_f_name.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.entry_width,
            relheight=self.entry_height,
        )
        self.correct_positioning(
            width=self.entry_width, height=self.entry_height, place_right=False
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

    def validate_data(self):
        print("Implement validate_data")
        pass

    def stop_measure(self):
        print("Implement stop_measure")
        pass


class CardFrame(tk.Frame):
    resources = ["Agilent 34410A", "ClimaEvent 340C"]
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
            self.create_agilent()
        elif tinta == self.resources[1]:
            self.create_kuni()

    def create_agilent(self):
        self.BT_agi = tk.Button(self, text="BT agi", command=self.print_it)
        SEL_1 = tk.StringVar(master=self)
        SEL_2 = tk.StringVar(master=self)
        SEL_3 = tk.StringVar(master=self)
        SEL_4 = tk.StringVar(master=self)
        # Stopped here!
        # Stopped here!
        # Stopped here!
        # Stopped here!
        # Stopped here!

    def place_agilent(self):
        self.BT_agi.place(
            relx=self.relx,
            rely=self.rely,
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
        print(self.winfo_children())


def main():
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()
