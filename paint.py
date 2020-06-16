from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
import PIL
from PIL import Image,ImageDraw,ImageGrab,ImageTk
from tkinter import messagebox

root=Tk()
root.title("Python Program!!")
root.geometry('800x800')

brush_color="black"
def paint(e):
	#brush parameter
	brush_width=int(my_slider.get())
	#brush_color='green'
	#brush type=BUTT,ROUND,PROJECTING
	brush_type2=brush_type.get()

	#satrting pos
	x1=e.x-1
	y1=e.y-1
	#end pos
	x2=e.x+1
	y2=e.y+1

	my_canvas.create_line(x1,y1,x2,y2,fill=brush_color,width=brush_width,capstyle=brush_type2,smooth=True)

def change_brush_size(things):
	slider_label.config(text=int(my_slider.get()))

#change brush color
def change_brush_color():
	global brush_color
	brush_color='black'
	brush_color=colorchooser.askcolor(color=brush_color)[1]

#change canvas color
def change_canvas_color():
	global bg_color
	bg_color='white'
	bg_color=colorchooser.askcolor(color=bg_color)[1]
	my_canvas.config(bg=bg_color)

# clear screen
def clear_screen():
	my_canvas.delete(ALL)
	my_canvas.config(bg='white')


# save to png
def save_as_png():
	result=filedialog.asksaveasfilename(initialdir='C:/Users/MUKUL KUMAR/Desktop/paint/images',filetypes=(("png files","*.png"),("all files","*.*")))
	if result.endswith('.png'):
		pass
	else:
		result+='.png'

	if result:
		x=root.winfo_rootx()+my_canvas.winfo_x()
		y=root.winfo_rooty()+my_canvas.winfo_y()
		x1=x+my_canvas.winfo_width()
		y1=y+my_canvas.winfo_height()
		ImageGrab.grab().crop((x,y,x1,y1)).save(result)

		#pop up success message box
		messagebox.showinfo('Image Saves',"Youe image has been Saved!")






# create our convas
w=600
h=400
my_canvas=Canvas(root,width=w,height=h,bg='white')
my_canvas.pack(pady=20)

my_canvas.bind('<B1-Motion>',paint)

#Brush Option Frame
brush_options_frame=Frame(root)
brush_options_frame.pack(pady=20)

#Brush size
brush_size_frame=LabelFrame(brush_options_frame,text="Brush Size")
brush_size_frame.grid(row=0,column=0,padx=50)

#Brush Slider
my_slider=ttk.Scale(brush_size_frame,from_=1,to=100,command=change_brush_size,orient=VERTICAL,value=10)
my_slider.pack(padx=10,pady=10)

slider_label=Label(brush_size_frame,text=my_slider.get())
slider_label.pack(pady=5)

#brush type 
brush_type_frame=LabelFrame(brush_options_frame,text="Brush type",height=400)
brush_type_frame.grid(row=0,column=1,padx=50)

#create radio button for brush_type
brush_type=StringVar()
brush_type.set("round")

brush_type_radio1=Radiobutton(brush_type_frame,text="Round",variable=brush_type,value="round")
brush_type_radio2=Radiobutton(brush_type_frame,text="Slash",variable=brush_type,value="butt")
brush_type_radio3=Radiobutton(brush_type_frame,text="Diamond",variable=brush_type,value="projecting")

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

#change color
change_color_frame=LabelFrame(brush_options_frame,text="Change Color")
change_color_frame.grid(row=0,column=2)

#Change brush color button
brush_color_button=Button(change_color_frame,text="Brush Color",command=change_brush_color)
brush_color_button.pack(pady=10,padx=10)

#Change canvas color button
canvas_color_button=Button(change_color_frame,text="Canvas Color",command=change_canvas_color)
canvas_color_button.pack(pady=10,padx=10)

#Program option frame
options_frame=LabelFrame(brush_options_frame,text="Program Option")
options_frame.grid(row=0,column=3,padx=50)

#clear screen button
clear_screen=Button(options_frame,text='clear screen',command=clear_screen)
clear_screen.pack(padx=10,pady=10)

#save image button
save_image_button=Button(options_frame,text="Save to PNG",command=save_as_png)
save_image_button.pack(padx=10,pady=10)

root.mainloop()