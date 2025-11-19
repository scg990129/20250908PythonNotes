# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251118
# @version Lab13 - Ex 1 - Name and Address

# Write a GUI program that displays your name and address when a button is clicked. The program’s window should appear as the sketch below when it runs. When the user clicks the Show Info button, the program should display your name and address, as shown in the sketch on the right of the figure.  (12 points)
#
# Upload an image that displays the data when the Show Info button is clicked. (3 points)

import tkinter as tk

MyName = "Jacob Yeung"
MyAddress = "1527 Palm Ave, APT E\nSan Gabriel, CA 91776"

class CustomApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ex 1 - Name and Address")
        self.geometry("300x150")

        self.topFrame = tk.Frame(self, borderwidth=5)
        self.bottomFrame = tk.Frame(self, borderwidth=5)
        self.labelName = tk.Label(self.topFrame)
        self.msgAddress = tk.Message(self.topFrame, width=300)
        txt = "Show Info"
        self.buttonShowInfo = tk.Button(self.bottomFrame, text=txt ,command=self.showInfo, width=len(txt))
        self.buttonShowInfo.pack(side=tk.LEFT, padx=(5, 5))
        self.buttonExit = tk.Button(self.bottomFrame, text="Quit", command=self.destroy, width=len(txt))
        self.buttonExit.pack(side=tk.RIGHT, padx=(5, 5))
        self.labelName.pack(side=tk.TOP, pady=(5, 5)) # #fill=tk.X)
        self.msgAddress.pack(side=tk.BOTTOM,pady=(5, 5)) #fill=tk.X)

        self.topFrame.pack()
        self.bottomFrame.pack(side=tk.BOTTOM)

    def showInfo(self):
        self.labelName.config(text=MyName)
        self.msgAddress.config(text=MyAddress)

if __name__ == '__main__':
    app = CustomApp()
    app.mainloop()

# https://onlinegdb.com/dJ_XCEaBcM
# Case A:
"""
==================================================
             Ex A. Largest List Item              
==================================================

The largest item in the list is: 90
==================================================
          End of Ex A. Largest List Item          
==================================================

Process finished with exit code 0
"""
