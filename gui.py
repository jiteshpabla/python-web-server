# Made by Jitesh, Vaibhav and Priyam for - OSSP Lab, JIIT; April-May 2017

import Tkinter, Tkconstants, tkFileDialog
from Tkinter import *

filename =''

from wsgi_multi import *


class TkFileDialogExample(Tkinter.Frame):

    def __init__(self, root):

        Tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 50, 'pady': 10}
        button_opt2 = {'padx': 50, 'pady': 10}

        # define buttons
        Tkinter.Button(self, text='choose web app', command=self.choose_file).grid(row = 1, column = 0, padx = 50, pady = 5)
        Tkinter.Button(self, text='start server', command=self.server_fn).grid(row = 4, column = 0, padx = 20, pady = 10)
        Tkinter.Button(self, text='stop server', command=self.decompress_fn).grid(row = 5, column = 0, padx = 20, pady = 10)
        label_var = StringVar()
        label = Label(self, textvariable=label_var).grid(row = 2, column = 0, padx = 10, pady = 5)

        label_var.set("Port:")

        global e1
        e1 = Tkinter.Entry(self)

        e1.grid(row=3, column=0)
        #label1 = Label(self, textvariable="henlo!!!!!!!!!!!!", height=4).grid(row = 3, column = 0, padx = 20, pady = 10)
        #Tkinter.Button(self, text='asksaveasfilename', command=self.asksaveasfilename).pack(**button_opt)

        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = root

        options['title'] = 'Choose the web app'


        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'Choose the web app file'


    def choose_file(self):

        # get filename
        global filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)

        return filename

        # open file on your own
        #if filename:
        #  return open(filename, 'r')


    def server_fn(self):

        port_num = int(e1.get())

        main_fn(filename, port_num)

        return 0

    def decompress_fn(self):

        stop_server_fn()
        return 0



if __name__=='__main__':
    root = Tkinter.Tk()
    #TkFileDialogExample(root).pack()
    TkFileDialogExample(root).grid(row = 0, column = 0)
    root.mainloop()
