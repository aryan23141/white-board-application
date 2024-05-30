import tkinter as tk
from tkinter.colorchooser import askcolor
#creating functionalties
def start_drawing(event):#event-mouse clicks etc
    global is_drawing,prev_x,prev_y
    is_drawing=True
    prev_x,prev_y=event.x,event.y#coordinates of the cursors when function as called
def draw(event):
    global is_drawing,prev_x,prev_y
    if is_drawing:
        current_x,current_y=event.x,event.y
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill=drawing_color, width=line_width, capstyle=tk.ROUND, smooth=True)
        prev_x,prev_y=current_x,current_y
def stop_drawing(event):
    global is_drawing
    is_drawing=False
def change_pen_color():
    
    global drawing_color
    color=askcolor()[1]
    if color:
        drawing_color=color
#creating window
window=tk.Tk()#This creates a window
window.title('Aryans Whiteboard application')
canvas=tk.Canvas(window,bg="white")
canvas.pack(fill="both", expand=True)
window.geometry("800x600")
is_drawing=False 
drawing_color="black"
line_width=2
#creating navbar and buttons
controls_frame=tk.Frame(window)#builds the frame to hold buttons
controls_frame.pack(side="top",fill="x")#position of frame
#creating buttons
color_button=tk.Button(controls_frame,text="change color",command=change_pen_color)
color_button.pack(side="left",padx=5,pady=5)
clear_button=tk.Button(controls_frame,text="clear",command=lambda:canvas.delete("all"))
clear_button.pack(side="right",padx=5,pady=5)
#connecting features with GUI
canvas.bind("<Button-1>",start_drawing)
canvas.bind("<B1-Motion>",draw)
canvas.bind("<ButtonRelease-1>",stop_drawing)
window.mainloop()





        
    

