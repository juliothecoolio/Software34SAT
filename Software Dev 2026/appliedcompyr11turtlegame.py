# Import the turtle graphics module
import turtle
import pygame
import math


# Constants for screen width and height
WIDTH = 1024
HEIGHT = 768




# ////////  F U N C T I O N S  /////////




# curb: dotted white lines going from left to right and from down to up only
def dotted_line(pen, offset, offsetgap, startx, starty, endx, endy):
    if startx == endx and starty < endy:  # Vertical line (down to up)
        pen.penup()
        current = starty
        pen.goto(startx, current)
        line_is_blank = False  # start by drawing


        while current < endy:
            if not line_is_blank:
                pen.pendown()
                next_pos = min(current + offset, endy)
                pen.goto(startx, next_pos)
            else:
                pen.penup()
                next_pos = min(current + offset + offsetgap, endy)
                pen.goto(startx, next_pos)
            current += offset + offsetgap
            line_is_blank = not line_is_blank


    elif starty == endy and startx < endx:  # Horizontal line (left to right)
        pen.penup()
        current = startx
        pen.goto(current, starty)
        line_is_blank = False  # start by drawing


        while current < endx:
            if not line_is_blank:
                pen.pendown()
                next_pos = min(current + offset, endx)
                pen.goto(next_pos, starty)
            else:
                pen.penup()
                next_pos = min(current + offset + offsetgap, endx)
                pen.goto(next_pos, starty)
            current += offset + offsetgap
            line_is_blank = not line_is_blank


    else:
        print("Invalid parameters: only horizontal (left to right) or vertical (down to up) lines supported.")
        return 1


    pen.penup()
    return 0


# Set up the Turtle for the graphics window
wn = turtle.Screen()                                   # Create the screen object
wn.title(("Julian JURISTA - Basic Game Screen"))       # Set the title of the window
wn.bgcolor("#3f9b0b")                                  # Set the background color to grass green
wn.setup(WIDTH, HEIGHT)                                # Set the window size using constants
wn.tracer(0)                                           # Turn off automatic screen updates for manual control




# ////////  S P R I T E   C O D E  /////////


class Sprite():
    def __init__(self):
        # Set up the shape for the ship
        s = turtle.Shape("compound") #note that the other parameters can be "polygon" or "image"
        #wheels
        s.addcomponent(([4.5,-4], [4.5,-2], [3.7,-2], [3.7,-0.6], [3.3,-0.6], [3.3,-2], [2.5,-2], [2.5,-4], [4.5,-4]), "black", "black")
        s.addcomponent(([4.5,4], [4.5,2], [3.7,2], [3.7,0.6], [3.3,0.6], [3.3,2], [2.5,2], [2.5,4], [4.5,4]), "black", "black")
        s.addcomponent(([-5,4.5], [-3,4.5], [-3,3], [-5,3], [-5,4.5]), "black", "black")
        s.addcomponent(([-5,-4.5], [-3,-4.5], [-3,-3], [-5,-3], [-5,-4.5]), "black", "black")
        #frame
        s.addcomponent(([-5,4], [-7,4], [-7,-4], [-5,-4], [-5,-1], [-2,-3], [-1,-3], [-1,-1], [5,-0.5], [5,-3.5], [6.5,-3.5], [6.5,-0.5], [7,-0.5], [7,0.5], [6.5,0.5], [6.5,3.5], [5,3.5], [5,0.5], [-1,1], [-1,3], [-2,3], [-5,1], [-5,4]), "orange", "")
        s.addcomponent(([-5,1], [-5,3], [-2,3], [-5,1]), "grey", "")
        s.addcomponent(([-5,-1], [-5,-3], [-2,-3], [-5,-1]), "grey", "")
        s.addcomponent(([-2,0.5], [-2,-0.5], [-2.5,-0.5], [-2.5,0.5], [-2,0.5]), "black", "")
        s.addcomponent(([-1.5,0.5], [-1.5,-0.5], [0,-0.5], [0,0.5], [-1.5,0.5]), "black", "black")
        turtle.register_shape("racecar_orange",s)


        s = turtle.Shape("compound") #note that the other parameters can be "polygon" or "image"
        #wheels
        s.addcomponent([[4.5,-4], [4.5,-2], [3.7,-2], [3.7,-0.6], [3.3,-0.6], [3.3,-2], [2.5,-2], [2.5,-4], [4.5,-4]], "black", "black")
        s.addcomponent([[4.5,4], [4.5,2], [3.7,2], [3.7,0.6], [3.3,0.6], [3.3,2], [2.5,2], [2.5,4], [4.5,4]], "black", "black")
        s.addcomponent([[-5,4.5], [-3,4.5], [-3,3], [-5,3], [-5,4.5]], "black", "black")
        s.addcomponent([[-5,-4.5], [-3,-4.5], [-3,-3], [-5,-3], [-5,-4.5]], "black", "black")
        #frame
        s.addcomponent([[-5,4], [-7,4], [-7,-4], [-5,-4], [-5,-1], [-2,-3], [-1,-3], [-1,-1], [5,-0.5], [5,-3.5], [6.5,-3.5], [6.5,-0.5], [7,-0.5], [7,0.5], [6.5,0.5], [6.5,3.5], [5,3.5], [5,0.5], [-1,1], [-1,3], [-2,3], [-5,1], [-5,4]], "red", "")
        s.addcomponent([[-5,1], [-5,3], [-2,3], [-5,1]], "white", "")
        s.addcomponent([[-5,-1], [-5,-3], [-2,-3], [-5,-1]], "white", "")
        s.addcomponent([[-2,0.5], [-2,-0.5], [-2.5,-0.5], [-2.5,0.5], [-2,0.5]], "black", "")
        s.addcomponent([[-1.5,0.5], [-1.5,-0.5], [0,-0.5], [0,0.5], [-1.5,0.5]], "black", "black")
        turtle.register_shape("racecar_red",s)


#player movement distance
step_size = 10


#create player
class Player(Sprite):


    # Variables to handle acceleration and movement
    current_speed = 0
    max_speed = 10
    acceleration = 0.2
    accelerating = False
    turn_left = False
    turn_right = False
    is_forward = False
    is_reverse = False


    def __init__(self, sprite, x, y):
        Sprite().__init__()
        self.player = turtle.Turtle()
        self.player.tilt(90)
        self.player.shape(sprite)
        self.player.shapesize(4,4)
        self.player.pu()
        self.x = x
        self.y = y
        self.player.setpos(x, y)
        print(self.player.xcor())




    # ////////  M O V E M E N T   C O D E  /////////




    def player_left_start(self):
        self.turn_left = True
       
    def player_left_end(self):
        self.turn_left = False


    def player_right_start(self):
        self.turn_right = True
       
    def player_right_end(self):
        self.turn_right = False


    def player_forward_start(self):
        self.is_forward = True
        # pygame.init()
        # pygame.mixer.init()
        # accelerationsound = pygame.mixer.Sound("sound_files/accelerationmotor.wav")
        # accelerationsound.play()
        # pygame was not able to run on my computer and therefore there won't be any audio to my game :(
       
    def player_forward_end(self):
        self.is_forward = False
        # self.accelerationsound.stop()


    def player_reverse_start(self):
        self.is_reverse = True
       
    def player_reverse_end(self):
        self.is_reverse = False
       


    #MOVE UP
    def drive_forward(self, speed):
        if self.is_forward:
            self.player.forward(speed)


    #MOVE DOWN
    def drive_reverse(self, speed):
        if self.is_reverse:
            self.player.back(speed)


    #turn left
    def drive_turn_left(self, turn_speed):
        if self.turn_left and self.is_forward:
            self.player.left(turn_speed)


    #turn right
    def drive_turn_right(self, turn_speed):
        if self.turn_right and self.is_forward:
            self.player.right(turn_speed)


    #turn left
    def drive_reverse_turn_left(self, turn_speed):
        if self.turn_left and self.is_reverse:
            self.player.left(turn_speed)


    #turn right
    def drive_reverse_turn_right(self, turn_speed):
        if self.turn_right and self.is_reverse:
            self.player.right(turn_speed)




        # Check for collisions with edge of screen
        if (self.x >= WIDTH) or (self.x <= -WIDTH):
            self.x *= 0
            print("outer edge collision")


        elif (self.y >= HEIGHT) or (self.y <= -HEIGHT):
            self.y *= 0
            print("outer edge collision")


        # Check for collisions with inner walls
        elif (self.x < 250 and self.x > -250) and (self.y > 140 and self.y < 150):
            self.y = 150
            self.dy *= 0


        elif (self.x < 250 and self.x > -250) and (self.y > -150 and self.y < -140):
            self.y = -150
            self.dy *= 0


        elif (self.y < 150 and self.y > -150) and (self.x > -250 and self.x < -240):
            self.x = -250
            self.dx *= 0


        elif (self.y < 150 and self.y > -150) and (self.x > 240 and self.x < 250):
            self.x = 250
            self.dx *= 0




player_one = Player("racecar_orange", -100, -200)
player_two = Player("racecar_red", -180, -250)


# C O M M E N T S :
# accelerate
# i want the car (player_one) to accelerate from its current speed (so far 0) to a top speed of 10 (or until released) while the Up key is being pressed and for the car to deccelerate from any speed until 0 (or if the Up key is pressed).
# simulate omega racer code, while turning, only the heading is changing not specific x and y coords


# Key bindings
wn.listen()
wn.onkeypress(player_one.player_forward_start, "Up")
wn.onkeyrelease(player_one.player_forward_end, "Up")


wn.onkeypress(player_one.player_reverse_start, "Down")
wn.onkeyrelease(player_one.player_reverse_end, "Down")


wn.onkeypress(player_one.player_left_start, "Left")
wn.onkeyrelease(player_one.player_left_end, "Left")


wn.onkeypress(player_one.player_right_start, "Right")
wn.onkeyrelease(player_one.player_right_end, "Right")




wn.onkeypress(player_two.player_forward_start, "w")
wn.onkeyrelease(player_two.player_forward_end, "w")


wn.onkeypress(player_two.player_reverse_start, "s")
wn.onkeyrelease(player_two.player_reverse_end, "s")


wn.onkeypress(player_two.player_left_start, "a")
wn.onkeyrelease(player_two.player_left_end, "a")


wn.onkeypress(player_two.player_right_start, "d")
wn.onkeyrelease(player_two.player_right_end, "d")




# ////////  C I R C U I T   D R A W I N G  /////////




# Create turtle for drawing the circuit
pen = turtle.Turtle()
pen.speed(0)
pen.color("#c20a0a") #red
pen.pensize(200)
pen.hideturtle()


# Drawing the circuit
pen.penup()
pen.goto((-WIDTH // 2) + 160, (HEIGHT // 2) - 160)
pen.pendown()
pen.goto((WIDTH // 2) - 160, (HEIGHT // 2) - 160)
pen.goto((WIDTH // 2) - 160, (-HEIGHT // 2) + 160)
pen.goto((-WIDTH // 2) + 160, (-HEIGHT // 2) + 160)
pen.goto((-WIDTH // 2) + 160, (HEIGHT // 2) - 160)


# input dotted line code here
pen.color("white")
pen.pensize(200)
dotted_line(pen, 1, 80, (-WIDTH // 2) + 160, (HEIGHT // 2) - 160, (WIDTH // 2) - 160, (HEIGHT // 2) - 160)
dotted_line(pen, 1, 80, (WIDTH // 2) - 160, (-HEIGHT // 2) + 160, (WIDTH // 2) - 160, (HEIGHT // 2) - 160)
dotted_line(pen, 1, 80, (-WIDTH // 2) + 160, (-HEIGHT // 2) + 160, (WIDTH // 2) - 160, (-HEIGHT // 2) + 160)
dotted_line(pen, 1, 80, (-WIDTH // 2) + 160, (-HEIGHT // 2) + 160, (-WIDTH // 2) + 160, (HEIGHT // 2) - 160)




pen.color("#3d3c38") #grey
pen.pensize(160)
pen.penup()
pen.goto((-WIDTH // 2) + 160, (HEIGHT // 2) - 160)
pen.pendown()
pen.goto((WIDTH // 2) - 160, (HEIGHT // 2) - 160)
pen.goto((WIDTH // 2) - 160, (-HEIGHT // 2) + 160)
pen.goto((-WIDTH // 2) + 160, (-HEIGHT // 2) + 160)
pen.goto((-WIDTH // 2) + 160, (HEIGHT // 2) - 160)




# ////////  T I T L E   L A B E L  /////////




# Create turtle for labeling
labeler = turtle.Turtle()
labeler.hideturtle()
labeler.color("#c20a0a")
labeler.penup()


# Label origin
labeler.goto(0, 0)
labeler.write("Pit Stop", font=("Formula1 Display Wide", 32, "normal"), align='center')




# ////////  F I N I S H   L I N E  /////////








# ////////  G A M E   L O O P  /////////




# Start the game loop (runs forever)
while True:
    player_one.drive_forward(0.8)
    player_one.drive_reverse(0.3)
    player_one.drive_turn_left(0.8)
    player_one.drive_turn_right(0.8)
    player_one.drive_reverse_turn_left(0.3)
    player_one.drive_reverse_turn_right(0.3)


    player_two.drive_forward(0.8)
    player_two.drive_reverse(0.3)
    player_two.drive_turn_left(0.8)
    player_two.drive_turn_right(0.8)
    player_two.drive_reverse_turn_left(0.3)
    player_two.drive_reverse_turn_right(0.3)


    wn.update()  # Manually update the screen each frame