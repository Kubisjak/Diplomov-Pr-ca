# Imports --------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
import time
import numpy as np
import matplotlib
from scipy.stats import norm

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # NavigationToolbar2TkAgg

# from matplotlib.figure import Figure
plt.rcParams["toolbar"] = "None"  # Do not display toolbar when calling plot


# ----------------------------------------------------------------------------------------------------------------------
def _quit():
    GUI.quit()
    GUI.destroy()

master = tk.Tk()
master.title("Asian Option Pricing Model")

GUI = tk.Frame(master, borderwidth=1, padx=10, pady=10)
GUI.pack()

# Configure grid -------------------------------------------------------------------------------------------------------

GUI.grid_columnconfigure(0, weight=1)
GUI.grid_columnconfigure(1, weight=1)

# Create two frames that will host on the left side the parameters frame and on the right side the canvas frame

frame_left = tk.Frame(GUI, borderwidth=1, padx=10, pady=10, relief=tk.GROOVE, height=500)
frame_left.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
frame_right = tk.Frame(GUI, borderwidth=1, padx=10, pady=10, relief=tk.GROOVE, height=500)
frame_right.grid(row=0, column=1, sticky=tk.W + tk.E + tk.N + tk.S)

frame_left_position_row = 0
parameter_frame_position_row = 0

# Left frame -----------------------------------------------------------------------------------------------------------
label_parameter_frame = tk.Label(frame_left, text="Parameters: ", bg="red", justify=tk.LEFT)  # Create label for parameter
label_parameter_frame.grid(row=frame_left_position_row, column=0, columnspan=1, sticky=tk.W)  # Place label on gridR
frame_left_position_row += 1

parameter_frame = tk.Frame(frame_left, relief=tk.GROOVE, borderwidth=1, padx=10, pady=10)
parameter_frame.grid(row=frame_left_position_row, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

S0 = tk.DoubleVar(GUI)  # Create IntVariable called
label_S0 = tk.Label(parameter_frame, text="S0: ")  # Create label for parameter
label_S0.grid(row=parameter_frame_position_row, column=0, sticky=tk.E)  # Place label on grid
entry_S0 = tk.Entry(parameter_frame, textvariable=S0)  # Create entry widget
entry_S0.grid(row=parameter_frame_position_row, column=1, sticky=tk.W + tk.E + tk.S + tk.N)  # Place entry widget on grid
parameter_frame_position_row += 1

K = tk.DoubleVar(GUI)  # Create IntVariable
label_K = tk.Label(parameter_frame, text="K: ")  # Create label for parameter
label_K.grid(row=parameter_frame_position_row, column=0, sticky=tk.E)  # Place label on grid
entry_K = tk.Entry(parameter_frame, textvariable=K)  # Create entry widget
entry_K.grid(row=parameter_frame_position_row, column=1, sticky=tk.W + tk.E + tk.S + tk.N)  # Place entry widget on grid
parameter_frame_position_row += 1

sigmaS = tk.DoubleVar(GUI)  # Create IntVariable
label_sigmaS = tk.Label(parameter_frame, text="SigmaS: ")  # Create label for parameter
label_sigmaS.grid(row=parameter_frame_position_row, column=0, sticky=tk.E)  # Place label on grid
entry_sigmaS = tk.Entry(parameter_frame, textvariable=sigmaS)  # Create entry widget
entry_sigmaS.grid(row=parameter_frame_position_row, column=1, sticky=tk.W + tk.E + tk.S + tk.N)  # Place entry widget on grid
parameter_frame_position_row += 1

nsteps = tk.IntVar(GUI)  # Create IntVariable
label_nsteps = tk.Label(parameter_frame, text="nsteps: ")  # Create label for parameter
label_nsteps.grid(row=parameter_frame_position_row, column=0, sticky=tk.E)  # Place label on grid
entry_nsteps = tk.Entry(parameter_frame, textvariable=nsteps)  # Create entry widget
entry_nsteps.grid(row=parameter_frame_position_row, column=1, sticky=tk.W + tk.E + tk.S + tk.N)  # Place entry widget on grid
parameter_frame_position_row += 1

nsims = tk.IntVar(GUI)  # Create IntVariable
label_nsims = tk.Label(parameter_frame, text="nsims: ")  # Create label for parameter
label_nsims.grid(row=parameter_frame_position_row, column=0, sticky=tk.E)  # Place label on grid
entry_nsims = tk.Entry(parameter_frame, textvariable=nsims)  # Create entry widget
entry_nsims.grid(row=parameter_frame_position_row, column=1, sticky=tk.W + tk.E + tk.S + tk.N)  # Place entry widget on grid
parameter_frame_position_row += 1

R0 = tk.DoubleVar(GUI)  # Create IntVariable
label_R0 = tk.Label(parameter_frame, text="R0: ", width=20)  # Create label for parameter
label_R0.grid(row=parameter_frame_position_row, column=0, sticky=tk.E)  # Place label on grid
entry_R0 = tk.Entry(parameter_frame, textvariable=R0)  # Create entry widget
entry_R0.grid(row=parameter_frame_position_row, column=1, sticky=tk.W + tk.E + tk.S + tk.N)  # Place entry widget on grid
parameter_frame_position_row += 1

sigmaR = tk.DoubleVar(GUI)  # Create IntVariable
label_sigmaR = tk.Label(parameter_frame, text="SigmaR: ")  # Create label for parameter
label_sigmaR.grid(row=parameter_frame_position_row, column=0, sticky=tk.E)  # Place label on grid
entry_sigmaR = tk.Entry(parameter_frame, textvariable=sigmaR)  # Create entry widget
entry_sigmaR.grid(row=parameter_frame_position_row, column=1, sticky=tk.W + tk.E + tk.S + tk.N)  # Place entry widget on grid
parameter_frame_position_row += 1

gamma = tk.DoubleVar(GUI)  # Create IntVariable
label_gamma = tk.Label(parameter_frame, text="Gamma: ")  # Create label for parameter
label_gamma.grid(row=parameter_frame_position_row, column=0, sticky=tk.E)  # Place label on grid
entry_gamma = tk.Entry(parameter_frame, textvariable=gamma)  # Create entry widget
entry_gamma.grid(row=parameter_frame_position_row, column=1, sticky=tk.W + tk.E + tk.S + tk.N)  # Place entry widget on grid
parameter_frame_position_row += 1

rho = tk.DoubleVar(GUI)  # Create IntVariable
label_rho = tk.Label(parameter_frame, text="Rho: ")  # Create label for parameter
label_rho.grid(row=parameter_frame_position_row, column=0, sticky=tk.E)  # Place label on grid
entry_rho = tk.Entry(parameter_frame, textvariable=rho)  # Create entry widget
entry_rho.grid(row=parameter_frame_position_row, column=1, sticky=tk.W + tk.E + tk.S + tk.N)  # Place entry widget on grid
parameter_frame_position_row += 1

alpha = tk.DoubleVar(GUI)  # Create IntVariable
label_alpha = tk.Label(parameter_frame, text="Alpha: ")  # Create label for parameter
label_alpha.grid(row=parameter_frame_position_row, column=0, sticky=tk.E)  # Place label on grid
entry_alpha = tk.Entry(parameter_frame, textvariable=alpha)  # Create entry widget
entry_alpha.grid(row=parameter_frame_position_row, column=1, sticky=tk.W + tk.E + tk.S + tk.N)  # Place entry widget on grid
parameter_frame_position_row += 1

current_frame = parameter_frame

total_rows_left = parameter_frame_position_row + frame_left_position_row


# Right Frame ----------------------------------------------------------------------------------------------------------
# Animation canvas frame
canvas_rowspan = parameter_frame_position_row

canvas_frame = tk.Frame(frame_right)
canvas_frame.grid(row=0, rowspan=canvas_rowspan, column=0, columnspan=2)
f = plt.figure(figsize=(2, 2), dpi=150)
canvas = FigureCanvasTkAgg(f, master=canvas_frame)
canvas.show()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH)

button_quit = ttk.Button(frame_right, text="Quit", command=_quit)
button_quit.grid(row=canvas_rowspan+1, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

button_calculate = ttk.Button(frame_right, text="Calculate", command=_quit)
button_calculate.grid(row=canvas_rowspan+1, column=1, sticky=tk.W + tk.E + tk.N + tk.S)

# Output Frame ---------------------------------------------------------------------------------------------------------
frame_bottom_position_row = 0

frame_bottom = tk.Frame(GUI, borderwidth=1, padx=10, pady=10, relief=tk.GROOVE, height=100)
frame_bottom.grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E + tk.N + tk.S)

label_bottom_frame = tk.Label(frame_bottom, text="Output: ", bg="red", justify=tk.LEFT)  # Create label for parameter
label_bottom_frame.grid(row=frame_bottom_position_row, column=0, columnspan=1, sticky=tk.W)  # Place label on gridR

GUI.mainloop()
