# Import the main modules of expyriment
import expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "kanisza_square", background_colour=(100,100,100))

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)
control.start()

# Retrieves height and length of screen
width, height = exp.screen.size

# Set the constants :

sq_len = 0.25 * width       # length of the square's sides (25% of width of screen)
circ_rad = 0.05 * width     # radius of the circle (5% of width of screen)

# Wait for a ket to be pressed before presenting shapes
exp.keyboard.wait()

# Create all objects :
# The circles in the 4 corners of the screen
circ_top_right = stimuli.Circle(radius = circ_rad, colour = (0,0,0), position= (sq_len//2, sq_len//2))
circ_top_left = stimuli.Circle(radius = circ_rad, colour = (0,0,0), position= (sq_len//2, -sq_len//2))
circ_bottom_right = stimuli.Circle(radius = circ_rad, colour = (255,255,255), position= (-sq_len//2, sq_len//2))
circ_bottom_left = stimuli.Circle(radius = circ_rad, colour = (255,255,255), position= (-sq_len//2, -sq_len//2))

# The grey square in the middle
rect = stimuli.Rectangle(size= (sq_len, sq_len), colour = (100,100,100))


# Presents all previously created objects
circ_top_right.present(clear = True, update=False)
circ_top_left.present(clear = False, update=False)
circ_bottom_right.present(clear = False, update=False)
circ_bottom_left.present(clear = False, update=False)
rect.present(clear = False, update=True)

# Displays until a key is pressed
exp.keyboard.wait()

# End experiment
control.end()