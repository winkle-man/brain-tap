from tkinter import *
from PIL import Image, ImageTk

root = Tk()


# Content
pic_src = Image.open("fish.jpg")
pic_conv = ImageTk.PhotoImage(pic_src)

height = Label(root, text = "Height:")
height_inp = Entry(root)
pic = Label(image = pic_conv)

width = Label(root, text = "Width:")
width_inp = Entry(root)

aratio_check = Checkbutton(root, text = "Preserve Aspect")
zoom_in = Button(root, text = "Zoom in")
zoom_out = Button(root, text = "Zoom out")

# Grid
height.grid(row = 0, column = 0, sticky = E)
height_inp.grid(row = 0, column = 1)
pic.grid(row = 0, column = 2, rowspan = 2, columnspan = 2)

width.grid(row = 1, sticky = E)
width_inp.grid(row = 1, column = 1)

zoom_in.grid(row = 2, column = 0, sticky='news')
zoom_out.grid(row = 3, column = 0, sticky='news')
aratio_check.grid(row = 4, columnspan = 2, sticky = W, padx = 5)

root.columnconfigure(0, weight = 3)

# Main Loop
root.mainloop()
