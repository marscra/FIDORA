import tkinter as tk
from tkinter import ttk, StringVar

global form 
form = tk.Tk()

global tab_parent
tab_parent = ttk.Notebook(form)

global tab1
tab1 = ttk.Frame(tab_parent)
global tab2
tab2 = ttk.Frame(tab_parent)

global CoMet_dpi
CoMet_dpi = StringVar(tab1)
CoMet_dpi.set("127")

global CoMet_uploaded_filename 
CoMet_uploaded_filename=StringVar(tab1)
CoMet_uploaded_filename.set("Error!")

global CoMet_export_folder
CoMet_export_folder=StringVar(tab1)
CoMet_export_folder.set("Error!")