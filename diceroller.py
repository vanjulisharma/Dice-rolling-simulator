from tkinter import *
import random

# create tk instance
root = Tk()
# set window title
root.title('Dice Roller')
# set window geometry
root.geometry('400x450')


def roll_dice():
    # define list of dice unicodes
    dice_codes = ['\u2680', '\u2681',
                  '\u2682', '\u2683',
                  '\u2684', '\u2685']
    # define dictionary with key as dice
    # unicodes and value as corresponding
    # dice numbers
    numbers = {'\u2680': 1, '\u2681': 2,
               '\u2682': 3, '\u2683': 4,
               '\u2684': 5, '\u2685': 6}

    # roll dice randomly
    d1 = random.choice(dice_codes)
    d2 = random.choice(dice_codes)
    # return dice rolled number
    if d1 in numbers.keys():
        d1_number = numbers[d1]
    if d2 in numbers.keys():
        d2_number = numbers[d2]
        # configure and update dice labels
    dice1.config(text=d1)
    dice2.config(text=d2)
    # configure and update dice number labels
    dice1_number.config(text=d1_number)
    dice2_number.config(text=d2_number)
    # configure and update total rolled number
    total_numbers.config(text=f'You Rolled: {d1_number + d2_number}')


# frame to display dice
frame = Frame(root)
frame.pack(pady=5)
# dice labels
dice1 = Label(frame, font=('ariel', 150), fg='black')
dice1.grid(row=0, column=0, padx=5)
dice2 = Label(frame, font=('ariel', 150), fg='black')
dice2.grid(row=0, column=1, padx=5)
# dice number labels
dice1_number = Label(frame, font=('ariel', 18))
dice1_number.grid(row=1, column=0)
dice2_number = Label(frame, font=('ariel', 18))
dice2_number.grid(row=1, column=1)
# roll dice button
button = Button(root, text='Roll Dice', font=('ariel', 24),
                relief=GROOVE, bg='grey', command=roll_dice)
button.pack(pady=20)
# total label
total_numbers = Label(root, text='', font=('ariel', 24))
total_numbers.pack(pady=10)
roll_dice()
root.mainloop()
