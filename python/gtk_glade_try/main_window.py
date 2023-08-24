import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
builder = Gtk.Builder()
builder.add_from_file('user_interface.glade')
class Handler(object):

    def __init__(self, **kwargs):
        super(Handler, self).__init__(**kwargs)
        self.entry_num = builder.get_object('entry_num')
        self.lb_result = builder.get_object('lb_result')

    def on_main_window_destroy(self, window):
        Gtk.main_quit()

    def on_click_button_clicked(self, button):
        text = self.entry_num.get_text()
        self.lb_result.set_text(f'O numero informado foi {text}')

builder.connect_signals(Handler())
window = builder.get_object('main_window')
window.show_all()
if __name__ == '__main__':
    Gtk.main()