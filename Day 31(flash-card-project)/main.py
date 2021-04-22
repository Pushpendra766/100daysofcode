from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# reading data from datafile
try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_file = pandas.read_csv("data/french_words.csv")
finally:
    data_dict = data_file.to_dict(orient="records")




# change the word on click
def next_word():
    global current_card, flip_timer
    windows.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(canvas_background, image=card_image_front)
    flip_timer = windows.after(3000, func=flip_card)


# flips the card to show its meaning in English
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(canvas_background, image=card_image_back)

def words_to_learn():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()
# Setup windows
windows = Tk()
windows.title("Flash Cards")
windows.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = windows.after(3000, func=flip_card)


# Setting up Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_image_front = PhotoImage(file="images/card_front.png")
card_image_back = PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=card_image_front)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text='text', font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Creating right(✅) button
right_image = PhotoImage(file="images/already_know.PNG")
right_button = Button(image=right_image, highlightthickness=0, command=words_to_learn)
right_button.grid(row=1, column=1)


# Creating cross(❌) button
left_image = PhotoImage(file="images/dont_know.PNG")
left_button = Button(image=left_image, highlightthickness=0, command=next_word)
left_button.grid(row=1, column=0)
next_word()  # calling next_word() as to set a word at starting


# loop ends here 👇
windows.mainloop()
