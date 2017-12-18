from tkinter import Tk, HORIZONTAL, BOTH, TOP

from tkinter.ttk import Progressbar, Frame
import time
import threading


class ChargeProgress(Tk):
    def __init__(self):
        super().__init__()

        self.progress = Progressbar(self, orient=HORIZONTAL, mode='determinate')

    def runbar(self, event=None):
        def real_runbar():
            self.progress.pack(expand=True, fill=BOTH, side=TOP)
            self.progress.start(3)
            time.sleep(0.3)
            self.progress.stop()
            self.progress.grid_forget()

        threading.Thread(target=real_runbar).start()

if __name__ == '__main__':

    app = ChargeProgress()
    app.bind_all('<Control-Key-o>', app.runbar)
    app.mainloop()
