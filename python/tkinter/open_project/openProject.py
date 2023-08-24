from tkinter import Tk, ttk, Frame, Canvas, Button, Label, Entry, Scrollbar
from standardData import DataTable
import os


class MainWindow(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.configure(bg="blue")
        self.grid(row=0, column=0, ipady=1, ipadx=1, sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        self.search_btt = Button(
            self, text="Search", borderwidth=1, relief="solid", command=self.initiate_search)
        self.number_lbl = Label(
            self, text="Standard Number", borderwidth=1, relief="solid")
        self.number_ent = Entry(self)
        self.sub_frame = Frame(self, bg="green")
        self.place_widgets()

    def place_widgets(self):
        self.search_btt.grid(row=0, column=0, sticky="nsew")
        self.number_lbl.grid(row=0, column=1, sticky="nsew")
        self.number_ent.grid(row=0, column=2, sticky="nsew")
        self.sub_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.configure_grid()

    def configure_grid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=10)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)

    def initiate_search(self):
        search_value = str(self.number_ent.get())
        try:
            path = find_and_create_file_path()
            table = DataTable(path)
            self.data = table.locate_string_nummer(search_value)
            self.pack_result_table()
        except:
            pop_up("normen.xls not found, stopped at: "+str(path))

    def pack_result_table(self):
        for widget in self.sub_frame.winfo_children():
            widget.destroy()
        ResultTableFrame(self.sub_frame, self.data).pack(
            fill="both", expand=True)


class ResultTableFrame(Frame):
    def __init__(self, master, data):
        super().__init__(master)
        self.master = master
        self.data = data
        self.configure(bg="black")
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self, bg="yellow")
        self.scroll_y = Scrollbar(
            self, orient="vertical", command=self.canvas.yview)
        self.scroll_x = Scrollbar(
            self, orient="horizontal", command=self.canvas.xview)
        self.black_box = Frame(self, bg="black")
        self.frame = Frame(self.canvas)
        self.create_titles_and_place_widgets()

    def create_titles_and_place_widgets(self):
        nmb_column = self.data.columns.size
        i = 0
        j = 0
        while j < nmb_column:
            element = Label(self.frame, text=(
                "%s" % (self.data.columns[j])), borderwidth=1, relief="solid")
            element.grid(row=i, column=j, sticky="nsew")
            j = j + 1
        self.create_and_place_widgets_from_data()

    def create_and_place_widgets_from_data(self):
        nmb_column = self.data.columns.size
        nmb_index = self.data.index.size
        i = 0
        j = 0
        while j < nmb_column:
            if j < 9 or j > 9:
                while i < nmb_index and i < 30:
                    element = Label(self.frame, text=(
                        "%s" % (self.data.values[i, j])), borderwidth=1, relief="solid")
                    # row+1 because of the titles create at create_titles_and_place_widgets
                    element.grid(row=i+1, column=j, sticky="nsew")
                    i = i + 1
            elif j == 9:
                while i < nmb_index and i < 30:
                    element = Button(self.frame, text=(
                        "%s" % (self.data.values[i, j])), borderwidth=2, relief="solid", bg="#c4b5f0")
                    # row+1 because of the titles create at create_titles_and_place_widgets
                    element.grid(row=i+1, column=j, sticky="nsew")
                    element.bind('<Button-1>', self.button_clicked)
                    i = i + 1
            j = j + 1
            i = 0
        self.place_widgets()

    def place_widgets(self):
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scroll_y.grid(row=0, column=1, sticky="nsew")
        self.scroll_x.grid(row=1, column=0, sticky="nsew")
        self.black_box.grid(row=1, column=1, sticky="nsew")
        self.configure_grid()

    def configure_grid(self):
        self.grid_rowconfigure(0, weight=1000)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1000)
        self.grid_columnconfigure(1, weight=1)
        self.configure_canvas()

    def configure_canvas(self):
        self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox(
            'all'), yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)

    def button_clicked(self, event):
        button = event.widget
        standard_name = str(button.config('text')[-1])
        path = find_and_create_file_path()
        path = (path.strip("normen.xls")) + standard_name
        try:
            os.startfile(path, 'open')
        except:
            pop_up("Standard "+standard_name+" not found")


def pop_up(text: str):
    root = Tk()
    root.title("Warning")
    root.geometry("600x200")
    root.minsize(300, 200)
    lbl = Label(root, text=text, bg="red")
    lbl.pack(expand=True, fill="both")


def find_and_create_file_path():
    try:
        folders_to_find = ["Box", "Eckardt Development", "Normen"]
        path = os.environ['USERPROFILE']
        folder_list = os.listdir(path)
    except:
        return "initial path could not be find"
    try:
        for folder in folder_list:
            if folder in folders_to_find:
                path = os.path.join(path, folder)
                folder_list = os.listdir(path)
                for folder in folder_list:
                    if folder in folders_to_find:
                        path = os.path.join(path, folder)
                        folder_list = os.listdir(path)
                        if "Normen" in path:
                            path = os.path.join(path, "normen.xls")
                            return path
                        for folder in folder_list:
                            if folder in folders_to_find:
                                path = os.path.join(path, folder)
                                folder_list = os.listdir(path)
                                if "Normen" in path:
                                    path = os.path.join(path, "normen.xls")
                                    return path
                            elif folder == folder_list[-1]:
                                return "Could not find normen.xls, stopped at "+path
                    elif folder == folder_list[-1]:
                        return "Could not find normen.xls, stopped at "+path
            elif folder == folder_list[-1]:
                return "Could not find normen.xls, stopped at "+path
    except:
        return "Unexpected error"


def main():
    root = Tk()
    root.title("Open Project")
    root.geometry("1200x700")
    root.minsize(300, 200)
    application = MainWindow(root)
    application.mainloop()


if __name__ == "__main__":
    main()
