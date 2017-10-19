import ui
import random

rps = random.randint(1,3)

def check_touch_up_inside(sender):
    
    number_entered = int(view['guess_textfield'].text)
    
    global number_to_guess
    if number_entered == rps:
        view['answer_label'].text = "tie"
    else:
        view['answer_label'].text = "sorry, you loose."

view = ui.load_view()
view.present('full_screen')
