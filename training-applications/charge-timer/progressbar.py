try:
    import Tkinter              # Python 2
    import ttk
except ImportError:
    import tkinter as Tkinter   # Python 3
    import tkinter.ttk as ttk
import time

root = Tkinter.Tk()
ft = ttk.Frame()

def progressbar(event):

    ft.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
    pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='determinate')
    pb_hd.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
    pb_hd.start(3)
    time.sleep(0.3)

root.bind_all('<Control-Key-o>', progressbar)
root.mainloop()
