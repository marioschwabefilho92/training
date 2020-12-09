import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("GerTester")
        self.configure(bg="blue")
        self.geometry("1200x700")
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
        frame_list = []
        parameters_list = []
        frame_list = self.get_frame_list()
        print(frame_list)
        if self.all_resources_selected(frame_list) == True:
            parameter_dict = self.get_parameter_dict(frame_list)
            print(parameter_dict)
            if self.all_parameters_selected() == True:
                print("all parameters selected")
            else:
                print("select all parameters in the frames")
            print("all seleceted")
        else:
            print("Not selected")

    def get_frame_list(self) -> list:
        frame_list = []
        """Get all selected_resource inside the frames in self.canvas_for_frames
        To get a better understading use:
        self.winfo_children()
        self.winfo_children()[0]
        self.winfo_children()[0].winfo_children()
        self.winfo_children()[0].winfo_children()[0].selected_resource.get()
        """
        for frame in self.winfo_children()[0].winfo_children():
            resource_name = frame.selected_resource.get()
            frame_list.append(resource_name)
        return frame_list

    def all_resources_selected(self, frame_list) -> bool:
        for frame in frame_list:
            if frame == "":
                return False
            else:
                return True

    def get_parameter_dict(self, frame_list) -> dict:
        """Get all values inside the Optionsmenu/Entry/etc... inside the frames in self.canvas_for_frames
        To get a better understading read self.get_frame_list or use the command bellow with class Agilent34410A(tk.Frame)::
        print(self.winfo_children()[0].winfo_children()[0].winfo_children()[0].winfo_children()[0].selected_visa.get())
        """
        # STOPED HERE ON parameter_dict
        card_frame_number = 0
        numb = 0
        parameter_dict = {}
        for resource in frame_list:
            if resource == CardFrame.list_resources[0]:
                one = (
                    self.winfo_children()[0]
                    .winfo_children()[card_frame_number]
                    .winfo_children()[0]
                    .winfo_children()[0]
                    .selected_visa.get()
                )
                two = (
                    self.winfo_children()[0]
                    .winfo_children()[card_frame_number]
                    .winfo_children()[0]
                    .winfo_children()[0]
                    .selected_range.get()
                )
                three = (
                    self.winfo_children()[0]
                    .winfo_children()[card_frame_number]
                    .winfo_children()[0]
                    .winfo_children()[0]
                    .selected_configuration.get()
                )
                four = (
                    self.winfo_children()[0]
                    .winfo_children()[card_frame_number]
                    .winfo_children()[0]
                    .winfo_children()[0]
                    .selected_resolution.get()
                )
                print(one, two, three, four)
            elif resource == CardFrame.list_resources[1]:
                pass
            else:
                print("Unkown Resource")
            card_frame_number += 1

    def all_parameters_selected(self) -> bool:
        pass

    def stop_measure(self):
        print("Implement stop_measure")
        pass


class CardFrame(tk.Frame):
    list_resources = ["Agilent 34410A", "ClimaEvent 340C"]
    resource = ""
    button_width = 1
    button_height = 0.2
    option_menu_width = 1
    option_menu_height = 0.2
    frame_width = 1
    frame_height = 0.8
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
        self.frame_for_resource = tk.Frame(master=self)
        self.selected_resource = tk.StringVar()
        self.resource_menu = tk.OptionMenu(
            self, self.selected_resource, *self.list_resources
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
        self.frame_for_resource.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.frame_width,
            relheight=self.frame_height,
        )
        self.correct_positioning(
            width=self.frame_width,
            height=self.frame_height,
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
        resource_name = selected_resource.get()
        if self.resource == "":
            self.on_change_selected_resource(resource_name)
        elif self.resource != resource_name:
            self.delete_resource(resource_name)
        else:
            print("Resource was not changed")

    def delete_resource(self, resource_name):
        for widget in self.frame_for_resource.winfo_children():
            widget.destroy()
        self.on_change_selected_resource(resource_name)

    def on_change_selected_resource(self, resource_name):
        if resource_name == self.list_resources[0]:
            self.resource = resource_name
            Agilent34410A(card_frame=self.frame_for_resource)
        elif resource_name == self.list_resources[1]:
            self.resource = resource_name
            ClimaEvent340C(card_frame=self.frame_for_resource)

    def print_it(self):
        print(self.winfo_children())


class Agilent34410A(tk.Frame):
    agi_visa = ["a", "b", "c"]
    agi_range = ["1", "2", "3"]
    agi_config = ["DC", "AC"]
    agi_res = ["Big", "Small"]
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

    def __init__(self, card_frame):
        super().__init__(master=card_frame)
        self.pack(fill="both", expand=True)
        self.config(bg="green")
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.selected_visa = tk.StringVar()
        self.selected_range = tk.StringVar()
        self.selected_configuration = tk.StringVar()
        self.selected_resolution = tk.StringVar()
        self.visa_menu = tk.OptionMenu(self, self.selected_visa, *self.agi_visa)
        self.range_menu = tk.OptionMenu(self, self.selected_range, *self.agi_range)
        self.config_menu = tk.OptionMenu(
            self, self.selected_configuration, *self.agi_config
        )
        self.res_menu = tk.OptionMenu(self, self.selected_resolution, *self.agi_res)

    def place_widgets(self):
        self.visa_menu.place(
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
        self.range_menu.place(
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
        self.config_menu.place(
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
        self.res_menu.place(
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


class ClimaEvent340C(tk.Frame):
    def __init__(self, card_frame):
        super().__init__(master=card_frame)
        self.pack(fill="both", expand=True)
        self.config(bg="red")


def main():
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()
