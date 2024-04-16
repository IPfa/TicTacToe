import tkinter as tk
from tkinter import messagebox
from random import randrange


FIELD = {
    1: (0, 0, 1),
    2: (0, 1, 2),
    3: (0, 2, 3),
    4: (1, 0, 4),
    5: (1, 1, 5),
    6: (1, 2, 6),
    7: (2, 0, 7),
    8: (2, 1, 8),
    9: (2, 2, 9),
}
LEFT_MOUSE_BUTTON = '"<Button-1>"'
MOVE_COUNTER = 0


def move(event=None):
    global MOVE_COUNTER
    button_pressed = event.widget._name.replace("!", "")
    if button_pressed == "button":
        button_pressed = "button1"
    exec(f'{button_pressed}.unbind({LEFT_MOUSE_BUTTON})')
    exec(f'{button_pressed}.config(state=tk.DISABLED)')
    player_move = int(button_pressed.replace("button", ""))
    FIELD["O"] = FIELD[player_move]
    del FIELD[player_move]
    update_field()
    window.update()
    MOVE_COUNTER += 1
    if victory_check():
        messagebox.showinfo(
            title="End of the Game",
            message="You won!"
        )
        window.destroy()
    else:
        computer_move()
        update_field()
        window.update()
        MOVE_COUNTER += 1
        if victory_check():
            messagebox.showinfo(
                title="End of the Game",
                message="Computer won!"
            )
            window.destroy()
        elif MOVE_COUNTER == 9:
            messagebox.showinfo(
                title="End of the Game",
                message="It's a tie!"
            )
            window.destroy()


window = tk.Tk()
window.title("TicTacToe")

for i in range(1, 10):
    name = str("button" + str(i))
    globals()[name] = tk.Button(window, height=5, width=10)
    exec(f'{name}.bind({LEFT_MOUSE_BUTTON}, move)')
for i in FIELD.keys():
    globals()["button" + str(i)].grid(row=FIELD[i][0], column=FIELD[i][1])


def victory_check():
    field = {}
    for key in FIELD.keys():
        if type(key) is int:
            field[key] = FIELD[key]
        else:
            new_key = int(key.replace("U", ""))
            field[new_key] = FIELD[key]
    pos_1 = field[1][2]
    pos_2 = field[2][2]
    pos_3 = field[3][2]
    pos_4 = field[4][2]
    pos_5 = field[5][2]
    pos_6 = field[6][2]
    pos_7 = field[7][2]
    pos_8 = field[8][2]
    pos_9 = field[9][2]
    if pos_1 == pos_2 == pos_3:
        return True
    elif pos_4 == pos_5 == pos_6:
        return True
    elif pos_7 == pos_8 == pos_9:
        return True
    elif pos_1 == pos_4 == pos_7:
        return True
    elif pos_2 == pos_5 == pos_8:
        return True
    elif pos_3 == pos_6 == pos_9:
        return True
    elif pos_1 == pos_5 == pos_9:
        return True
    elif pos_3 == pos_5 == pos_7:
        return True
    else:
        return False


def computer_move(position=None):
    correct_move = True
    while correct_move:
        if position:
            computer_move = position
        else:
            computer_move = randrange(1, 10)
        if computer_move in FIELD.keys():
            FIELD["X"] = FIELD[computer_move]
            del FIELD[computer_move]
            button_pressed = "button" + str(computer_move)
            exec(f'{button_pressed}.unbind({LEFT_MOUSE_BUTTON})')
            exec(f'{button_pressed}.config(state=tk.DISABLED)')
            correct_move = False
        else:
            continue


def create_canvas(sign, row, column):
    if sign == "X":
        color = "red"
    else:
        color = "green"
    canvas = tk.Canvas(window, height=78, width=112)
    canvas.create_text(
        57,
        43,
        text=sign,
        font=("Arial", "55", "bold"),
        fill=color
    )
    canvas.grid(row=row, column=column)


def update_field():
    for i in FIELD.keys():
        if i == "X" or i == "O":
            sign = i
            row = FIELD[i][0]
            column = FIELD[i][1]
            update_key = "U" + str(FIELD[i][2])
            update_value = (row, column, sign)
    FIELD[update_key] = update_value
    del FIELD[sign]
    create_canvas(sign, row, column)


computer_move(5)
update_field()
MOVE_COUNTER += 1
window.mainloop()
