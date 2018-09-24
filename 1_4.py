import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = 0
paddle1_vel = 0
paddle2_pos = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    horizon = random.randrange(120, 240) / 60.0    
    if direction == LEFT: #leftwards
        horizon = - horizon
    vertical = - random.randrange(60, 180) / 60.0 #upwards
    ball_vel = [horizon, vertical]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = [[0,HEIGHT/2 - HALF_PAD_HEIGHT], [PAD_WIDTH,HEIGHT/2 - HALF_PAD_HEIGHT],
                   [PAD_WIDTH,HEIGHT/2 + HALF_PAD_HEIGHT],[0,HEIGHT/2 + HALF_PAD_HEIGHT]]

    paddle2_pos = [[WIDTH-PAD_WIDTH,HEIGHT/2-HALF_PAD_HEIGHT], [WIDTH,HEIGHT/2-HALF_PAD_HEIGHT],
                   [WIDTH,HEIGHT/2+HALF_PAD_HEIGHT],[WIDTH-PAD_WIDTH,HEIGHT/2+HALF_PAD_HEIGHT]]
    spawn_ball(random.choice([RIGHT, LEFT]))

    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
         
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0][1] += paddle1_vel
    paddle1_pos[1][1] += paddle1_vel
    paddle1_pos[2][1] += paddle1_vel
    paddle1_pos[3][1] += paddle1_vel

    paddle2_pos[0][1] += paddle2_vel
    paddle2_pos[1][1] += paddle2_vel
    paddle2_pos[2][1] += paddle2_vel
    paddle2_pos[3][1] += paddle2_vel

    if paddle1_pos[0][1] < 0 or paddle1_pos[0][1] >= (HEIGHT - PAD_HEIGHT):
        paddle1_pos[0][1] -= paddle1_vel
        paddle1_pos[1][1] -= paddle1_vel
        paddle1_pos[2][1] -= paddle1_vel
        paddle1_pos[3][1] -= paddle1_vel

    if paddle2_pos[0][1] < 0 or paddle2_pos[0][1] >= (HEIGHT - PAD_HEIGHT):
        paddle2_pos[0][1] -= paddle2_vel
        paddle2_pos[1][1] -= paddle2_vel
        paddle2_pos[2][1] -= paddle2_vel
        paddle2_pos[3][1] -= paddle2_vel

    
    # draw paddles
    canvas.draw_polygon(paddle1_pos, 1, "Yellow", "Yellow")
    canvas.draw_polygon(paddle2_pos, 1, "Yellow", "Yellow")    
    
    #collision with the top or bottom wall
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    
    # determine whether paddle and ball collide    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos[0][1] <= ball_pos[1] and paddle1_pos[3][1] >= ball_pos[1]:
            ball_vel[0] += 0.1*(ball_vel[0])
            ball_vel[1] += 0.1*(ball_vel[1])
            ball_vel[0] = - ball_vel[0]
        else:
            spawn_ball(RIGHT)
            score2 += 1

    if ball_pos[0] >= WIDTH - (BALL_RADIUS + PAD_WIDTH):
        if paddle2_pos[0][1] <= ball_pos[1] and paddle2_pos[3][1] >= ball_pos[1]:
            ball_vel[0] += 0.1*(ball_vel[0])
            ball_vel[1] += 0.1*(ball_vel[1])
            ball_vel[0] = - ball_vel[0]
        else:
            spawn_ball(LEFT)
            score1 += 1
            
    # draw scores
    canvas.draw_text(str(score1), (240, 60), 50, "White")
    canvas.draw_text(str(score2), (330, 60), 50, "White")

    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["W"]:
        paddle1_vel -= 5
    elif key==simplegui.KEY_MAP["S"]:
        paddle1_vel += 5
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= 5
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += 5

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["W"]:
        paddle1_vel += 5
    elif key==simplegui.KEY_MAP["S"]:
        paddle1_vel -= 5
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel += 5
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel -= 5


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("New Game", new_game, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
