from Tkinter import *
import tkFileDialog

class DialogManager():
    """
    Controls the display of a file dialogue
    to the user.

    Author:     M. Gill
    Copyright:  M. Gill
    """
    
    def __init__ (self):
        """
        Constructor
        """
        pass    

    def choosefile(self, diagtitle):
        """
        Allows user to choose a file through the
        display of a file dialogue

        diagtitle - the title shown on the dialogue
        returns   - String representing the full path
                    and name of the file
        """
        root = Tk()
        root.withdraw()
        sfile = tkFileDialog.askopenfilename(
            parent=root,
            filetypes = [('.TXT files', '.txt')],
            title=diagtitle )
        return sfile
