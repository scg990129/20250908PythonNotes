# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251118
# @version Lab13 - Ex B - Joe’s Automotive

# Joe’s Automotive performs the following routine maintenance services:
# Oil change—$30.00
# Lube job—$20.00
# Radiator flush—$40.00
# Transmission flush—$100.00
# Inspection—$35.00
# Muffler replacement—$200.00
# Tire rotation—$20.00
#
# Write a GUI program with check buttons that allow the user to select any or all of these services.
# When the user clicks a button, the total charges should be displayed.
# Upload an image with all the services selected and the total charges calculated and displayed. (3 points)

import tkinter as tk
from datetime import datetime

ListService = [("Oil change", 30),
                     ("Lube job", 20),
                    ("Radiator flush", 40),
                     ("Transmission flush", 100),
                     ("Inspection", 35),
                     ("Muffler replacement", 200),
                     ("Tire rotation", 20)]

widthServiceName = max(len(service[0]) for service in ListService)
widthServicePrice = max(len(f"f'${service[1]:.2f}'") for service in ListService)
textNoService = "Please select the services you want to perform."
MONOSPACE_FONT = ('Courier', 10)

class CustomApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ex B - Joe’s Automotive")
        # self.geometry("600x150")

        self.topFrame = tk.Frame(self, borderwidth=5)
        self.bottomFrame = tk.Frame(self, borderwidth=5)
        FRAME_WIDTH = 400
        FRAME_HEIGHT = 200  # Needed for pack_propagate to work consistently
        self.leftFrame = tk.Frame(self.topFrame,  borderwidth=5)
        self.rightFrame = tk.Frame(self.topFrame, borderwidth=5,  width=FRAME_WIDTH, height=FRAME_HEIGHT)
        self.leftFrame.pack(side=tk.LEFT, fill=tk.Y, expand=False)
        self.rightFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.rightFrame.pack_propagate(False)

        self.boolVars = []
        # self.masterVar = tk.BooleanVar(master=self.leftFrame, value=False)
        # self.checkBtn = tk.Checkbutton(self.leftFrame, text="Select All", variable=self.masterVar, command=self.selectAll)
        # self.checkBtn.pack(anchor="w")  # side=tk.TOP, pady=(5, 5))
        for item in ListService:
            self.boolVars.append(tk.BooleanVar(master=self.leftFrame, value=False))
            checkBtn = tk.Checkbutton(self.leftFrame, text=item[0], variable=self.boolVars[-1], command=self.stateChanged)
            checkBtn.pack(anchor = "w") # side=tk.TOP, pady=(5, 5))

        txtTotal = "total charges"
        self.txtSelectAll = "Select All"
        self.txtReset = "Reset"
        txtQuit = "Quit"
        self.MAX_BUTTON_WIDTH = max(len(txtTotal), len(self.txtSelectAll), len(txtQuit))
        self.buttonShowInfo = tk.Button(self.bottomFrame, text=txtTotal, command=self.showInfo, width=self.MAX_BUTTON_WIDTH)
        self.buttonShowInfo.pack(side=tk.LEFT, padx=(5, 5))
        self.buttonReset = tk.Button(self.bottomFrame, text=self.txtSelectAll, command=self.selectAllOrReset, width=self.MAX_BUTTON_WIDTH)
        self.buttonReset.pack(side=tk.LEFT, padx=(5, 5))
        self.buttonExit = tk.Button(self.bottomFrame, text=txtQuit, command=self.destroy, width=self.MAX_BUTTON_WIDTH)
        self.buttonExit.pack(side=tk.RIGHT, padx=(5, 5))

        PIXEL_WIDTH_FOR_MESSAGE = FRAME_WIDTH - 20
        self.labelName = tk.Label(self.rightFrame, text=f"Total Charges: ${self.getSum():.2f}", justify=tk.LEFT, font=MONOSPACE_FONT)
        self.msgDetails = tk.Message(self.rightFrame, text=textNoService, justify=tk.LEFT, width=PIXEL_WIDTH_FOR_MESSAGE, font=MONOSPACE_FONT)
        self.labelName.pack(side=tk.BOTTOM, pady=(5, 5), fill=tk.X, expand=True)
        self.msgDetails.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(5, 5))

        self.topFrame.pack()
        self.bottomFrame.pack(side=tk.BOTTOM)

    # def selectAll(self):
    #     for var in self.boolVars:
    #         var.set(self.masterVar.get())
    #     self.stateChanged()

    def showInfo(self):
        print(f"Total charges: {self.getSum()}")
        self.stateChanged()

    def selectAllOrReset(self):
        selectedList = []
        isAll = True
        for var in self.boolVars:
            if not var.get():
                isAll = False
                break
        print(f"isAll: {isAll}")

        for var in self.boolVars:
            var.set(not isAll)

        self.buttonReset.config(text=self.txtSelectAll if isAll else self.txtReset)
        self.stateChanged()

    def stateChanged(self):
        selectedList = []
        messageStr = []

        isAll = True
        for var in self.boolVars:
            if var.get():
                selectedList.append(item := ListService[ self.boolVars.index(var)])
                messageStr += f"{item[0]:<{widthServiceName}}: {f'${item[1]:.2f}':>{widthServicePrice}}\n"
            else:
                isAll = False
        self.buttonReset.config(text=self.txtReset if isAll else self.txtSelectAll)

        print(f"{datetime.now()} selected services:\n{selectedList}, total: ${self.getSum():.2f}")
        self.labelName.config(text=f"Total Charges: ${self.getSum():.2f}")
        self.msgDetails.config(text=textNoService if len(messageStr) == 0 else "".join(messageStr))

    def getSum(self) -> int:
        total = 0
        for var in self.boolVars:
            total += ListService[self.boolVars.index(var)][1] if var.get() == True else 0
        return total

if __name__ == '__main__':
    app = CustomApp()
    app.mainloop()


