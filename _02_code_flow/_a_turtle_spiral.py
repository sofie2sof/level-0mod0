import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================
intcount = 0

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    turtlebob= turtle.Turtle()
    # This code sets our shape to a turtle
    turtlebob.turtlesize(stretch_wid=10, stretch_len=10, outline=4)
    turtlebob.shape('turtle')
    turtlebob.width(10)
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    turtlebob.speed(0)
    # Set your turtle's color using .color('green')
    turtlebob.color('green')
    # Use a loop to repeat a the code below 50 times
    for i in range(50):
     turtlebob.color(get_random_color())
     turtlebob.forward(5*i)
     turtlebob.right(360/7)
     intcount+=1


    turtlebob.hideturtle()

        # Set the turtle color to a random color

        # Move the turtle (5*i) pixels. 'i' is the loop variable
        
        # Turn the turtle (360/7) degrees to the right
         
        # Change the turtle width to 'i' (the loop variable)
        
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
