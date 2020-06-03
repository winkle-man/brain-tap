from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Resizer")

# Content
pic_src = Image.open("fish.jpg").resize((100, 100))
pic_conv = ImageTk.PhotoImage(pic_src)
frame = Frame(root)

height = Label(frame, text = "Height:", width = 7)
height_inp = Entry(frame, width = 10)
pic = Label(root, image = pic_conv)

width = Label(frame, text = "Width:", width = 7)
width_inp = Entry(frame, width = 10)

preserve_ratio = Checkbutton(frame, text = "Preserve ratio")
save_as = Button(frame, text = "Save as")

# Grid
frame.grid(sticky = N, pady = 20)

height.grid(row = 0, column = 0, sticky = E)
width.grid(row = 1, column = 0, sticky = E)

height_inp.grid(row = 0, column = 1, sticky = W)
width_inp.grid(row = 1, column = 1, sticky = W)

preserve_ratio.grid(row = 2, column = 0, sticky = E)
save_as.grid(row = 2, column = 1, columnspan = 2, sticky = N, pady = 10)

pic.grid(row = 0, column = 2, rowspan = 2, columnspan = 2, padx = 10, pady = 10)

# Main Loop
root.mainloop()