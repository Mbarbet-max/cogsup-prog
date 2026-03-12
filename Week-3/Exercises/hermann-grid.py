# Import the main modules of expyriment
import expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "hermann_grid", background_colour=(255,255,255))

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)
control.start()

# Retrieves height and length of screen
width, height = exp.screen.size

def hermann(sq_size, space_btwn_sq, nbr_row, nbr_col, sq_colour, background_clr) :
    # Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
    exp = design.Experiment(name = "hermann_grid", background_colour=(background_clr))

    # Initialize the experiment: Must be done before presenting any stimulus
    control.initialize(exp)
    control.start()

    # Retrieves height and length of screen
    width, height = exp.screen.size
    positions = []

    for i in range(nbr_col*nbr_row) :
        positions.append((sq_size * ))

    for i in range(nbr_col*nbr_row) :
        square = stimuli.Rectangle(size = (sq_size, sq_size), colour = sq_colour)
        
    

   
    



    # Wait for a ket to be pressed before presenting shapes
    exp.keyboard.wait()



    # Displays until a key is pressed
    exp.keyboard.wait()

    # End experiment
    control.end()

kanisza(1.5, 0.20, 0.05)