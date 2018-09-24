import simplegui
import random

# helper function to initialize globals
def new_game():
    global fulldeck, exposed, state, cardindex1, cardindex2, turns
    state, turns, cardindex1, cardindex2 = 0, 0, None, None
    lst1 = [i for i in range(8)]
    lst2 = [i for i in range(8)]
    fulldeck = lst1 + lst2
    random.shuffle(fulldeck)
    exposed = [False for i in range(16)]
    indicator.set_text("Turns: " + str(turns))

     
# define event handlers
def mouseclick(pos):
    global fulldeck, exposed, state, cardindex1, cardindex2, turns
    position = pos[0]/50
    
    if not exposed[position]:
        if state == 0:
            cardindex1 = position
            exposed[cardindex1] = True
            state = 1
        elif state == 1:
            cardindex2 = position
            exposed[cardindex2] = True
            state = 2
            turns += 1
            indicator.set_text("Turns: " + str(turns))
        elif state == 2:
            if fulldeck[cardindex1] != fulldeck[cardindex2]:
                exposed[cardindex1], exposed[cardindex2] = False, False
                cardindex2, cardindex2 = None, None
            cardindex1 = position
            exposed[position] = True
            state = 1  

                            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for num in range(16):
        if exposed[num] is True:
            canvas.draw_polygon([[num*50, 0],
                                [(num+1)*50, 0],
                                [(num+1)*50, 100],
                                [num*50, 100]], 1,
                                "White", "White")
            canvas.draw_text(str(fulldeck[num]),
                             (num*50+10, 60),
                             50, "Black")
            
        else:
            canvas.draw_polygon([[num*50, 0],
                                [(num+1)*50, 0],
                                [(num+1)*50, 100],
                                [num*50, 100]], 1,
                                "White", "Black")


# create frame and add a button and labels

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
indicator = frame.add_label("Turns: 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()