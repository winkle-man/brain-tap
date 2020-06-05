from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Editor")

def resize(something):
    global user_width, user_height, pic_width, pic_height, pic_src, pic_opened, pic_resized, pic_conv
    pic_opened.close()
    pic_opened = Image.open("fish.jpg")

    if user_width.get() == '':
        pic_width = 1
    elif user_height.get() == '':
        pic_height = 1
    else:
        pic_width = int(user_width.get())
        pic_height = int(user_height.get())
    
    pic_resized = pic_opened.resize((pic_width, pic_height))
    pic_conv = ImageTk.PhotoImage(pic_resized)
    pic = Label(image = pic_conv)
    pic.grid(row = 0, column = 1)



# Contents
pic_src = "fish.jpg"
pic_width = 200
pic_height = 200
pic_opened = Image.open(pic_src)
pic_resized = pic_opened.resize((pic_width, pic_height))
pic_conv = ImageTk.PhotoImage(pic_resized)

pic = Label(image = pic_conv)
frame = Frame(root)
label_width = Label(frame, text = "Width:", width = 7)
user_width = Entry(frame, width = 10)
user_width.bind("<Return>", resize)
label_height = Label(frame, text = "Height:", width = 7)
user_height = Entry(frame, width = 10)
user_height.bind("<Return>", resize)
preserve_ratio = Checkbutton(frame, text = "Preserve ratio")
btn = Button(frame, text = "Resize", command = lambda: resize(user_width, user_height))

# Framed objects
frame.grid(sticky = N, pady = 20)
label_width.grid(row = 0, column = 0, sticky = E)
user_width.grid(row = 0, column = 1, sticky = W)
label_height.grid(row = 1, column = 0, sticky = E)
user_height.grid(row = 1, column = 1, sticky = W)
btn.grid(row = 2, column = 1, columnspan = 2, sticky = N, pady = 10)
preserve_ratio.grid(row = 2, column = 0, sticky = E)

# Picture Grid
pic.grid(row = 0, column = 1, padx = 10)


# Main Loop
root.mainloop()