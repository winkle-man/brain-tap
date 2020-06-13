from tkinter import *

def button_click(input):
    user_input_container.insert(END, input)

def answer_button():
    user_input_equation = user_input_container.get()
    user_input_container.delete(0,END)
    try:
        user_input_container.insert(0, eval(user_input_equation))
    except:
        user_input_container.delete(0,END)

def answer_keyboard_return(come):
    user_input_equation = user_input_container.get()
    user_input_container.delete(0,END)
    user_input_container.insert(0, eval(user_input_equation))

def delete_user_input():
    user_input_container.delete(0,END)

root = Tk()
root.resizable(0,0)
root.title('Simple Calculator')
frame = Frame(root)
frame.grid(row = 1)
user_input_container = Entry(root, borderwidth = 10, justify = RIGHT, insertborderwidth=30, font= ('calculator', 20))
user_input_container.grid(row = 0, ipady = 20, sticky = 'ew')
user_input_container.focus()
user_input_container.bind("<Return>", answer_keyboard_return)



btn_7 = Button(frame, text = '7', width = 8, height = 3, command = lambda: button_click(7)).grid(row = 0, column = 0, padx = 3, pady = 3, sticky = 'w')
btn_8 = Button(frame, text = '8', width = 8, height = 3, command = lambda: button_click(8)).grid(row = 0, column = 1, padx = 3)
btn_9 = Button(frame, text = '9', width = 8, height = 3, command = lambda: button_click(9)).grid(row = 0, column = 2, padx = 3)
btn_divide = Button(frame, text = '/', width = 8, height = 3, command = lambda: button_click('/')).grid(row = 0, column = 3, padx = 3, sticky = 'e')

btn_4 = Button(frame, text = '4', width = 8, height = 3, command = lambda: button_click(4)).grid(row = 1, column = 0, pady = 3, sticky = 'w')
btn_5 = Button(frame, text = '5', width = 8, height = 3, command = lambda: button_click(5)).grid(row = 1, column = 1, pady = 3)
btn_6 = Button(frame, text = '6', width = 8, height = 3, command = lambda: button_click(6)).grid(row = 1, column = 2, pady = 3)
btn_multiply = Button(frame, text = '*', width = 8, height = 3, command = lambda: button_click('*')).grid(row = 1, column = 3, pady = 3, sticky = 'e')

btn_1 = Button(frame, text = '1', width = 8, height = 3, command = lambda: button_click(1)).grid(row = 2, column = 0, pady = 3, sticky = 'w')
btn_2 = Button(frame, text = '2', width = 8, height = 3, command = lambda: button_click(2)).grid(row = 2, column = 1, pady = 3)
btn_3 = Button(frame, text = '3', width = 8, height = 3, command = lambda: button_click(3)).grid(row = 2, column = 2, pady = 3)
btn_minus = Button(frame, text = '-', width = 8, height = 3, command = lambda: button_click('-')).grid(row = 2, column = 3, pady = 3, sticky = 'e')

btn_equalsign = Button(frame, text = '=', width = 8, height = 3, command = lambda: answer_button()).grid(row = 3, column = 0, pady = 3, sticky = 'w')
btn_0 = Button(frame, text = '0', width = 8, height = 3, command = lambda: button_click('0')).grid(row = 3, column = 1, pady = 3)
btn_C = Button(frame, text = 'C', width = 8, height = 3, command = lambda: delete_user_input()).grid(row = 3, column = 2, pady = 3)
btn_plus = Button(frame, text = '+', width = 8, height = 3, command = lambda: button_click('+')).grid(row = 3, column = 3, pady = 3, sticky = 'e')

root.mainloop()