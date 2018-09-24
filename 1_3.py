import simplegui

# define global variables
time = 0
count = 0
win = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global message
    min = t // 600
    tensec = (t - min*600) // 100
    sec = (t - min*600 - tensec*100) // 10
    milisec = t%10
    return str(min)+":"+str(tensec)+str(sec)+":"+str(milisec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    running = True
    timer.start()

def stop():
    global running, win, count
    timer.stop()
    if running == True:
        count += 1
        if time%10 == 0:
            win += 1
            
def reset():
    global running, win, count, time
    timer.stop()
    running = False
    time = 0
    win = 0
    count = 0
    
# define event handler for timer with 0.1 sec interval
def timer():
    global time
    time += 1

# define draw handler
def drawing(canvas):
    canvas.draw_text(format(time), (100,100), 30, "Red")  
    result = str(win)+" / "+str(count)
    canvas.draw_text(result, (150, 20), 20, "Green")

    
# create frame
frame = simplegui.create_frame("GAME", 200, 200)
timer = simplegui.create_timer(100, timer)

# register event handlers
frame.set_draw_handler(drawing)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("reset", reset, 100)

frame.start()
