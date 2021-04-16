import turtle
import pandas
from print_state import PrintState

print_state = PrintState()
screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
data = pandas.read_csv("50_states.csv")

guessed_states = []
states = data.state.to_list()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state's name").title()
    if answer_state == "Exit":
        break
    for i in range(50):
        if data.state[i] == answer_state:
            x_cor = data.x[i]
            y_cor = data.y[i]
            print_state.print_state_name(x_cor, y_cor, data.state[i])
            guessed_states.append(data.state[i])

states_to_learn = []
for state in states:
    if state not in guessed_states:
        states_to_learn.append(state)
data = pandas.DataFrame(states_to_learn)
data.to_csv("states_to_learn.csv")


