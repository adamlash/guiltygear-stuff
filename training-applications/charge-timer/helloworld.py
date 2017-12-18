from tkinter import *

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    """
    tkinter hello world class
    """
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        # reference to the master widget, which is the tk window
        self.master = master
        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):
      """
      Window Settings
      """
      # Changing title of Master Widget
      self.master.title("GUI")

      # allowing the widget to take the full space of the root
      # window
      self.pack(fill=BOTH, expand=1)

      # Create Menu Instance
      menu = Menu(self.master)
      self.master.config(menu=menu)

      # Create the file Object
      file = Menu(menu)

      # add a command to the menu option, calling it exit, and the command
      # it runs on event is client_exit
      file.add_command(label="Exit", command=self.client_exit)

      # Added 'File' to our menu
      menu.add_cascade(label="File", menu=file)
      """
      # Create the file object
      edit = Menu(menu)

      # adds a command to the menu option, calling it exit and the command it
      # runs on evnet is client_exit
      edit.add_command(Label="Undo")

      # added "File to our menu"
      menu.add_cascade(label="Edit", menu=edit)
      """
      # Creating a button
      QuitButton = Button(self, text="Quit", command=self.client_exit)

      # Placing the button
      QuitButton.place(x=0, y=0)

    def client_exit(self):
      exit()

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

# Size of the Window
root.geometry("400x300")


app = Window(root)
root.mainloop()
