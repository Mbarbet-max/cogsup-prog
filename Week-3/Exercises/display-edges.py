# Import the main modules of expyriment
import expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "display_edges")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)
control.start()

width, height = exp.screen.size
len_sq = 0.05*width

# Create corner rectangles
square_top_right = stimuli.Rectangle(size= (len_sq, len_sq), colour= (255,0,0), line_width= 1, position= (width//2 - len_sq/2, height//2 - len_sq/2))
square_top_left = stimuli.Rectangle(size= (len_sq, len_sq), colour= (255,0,0), line_width= 1, position= (-width//2 + len_sq/2, height//2 - len_sq/2))
square_bottom_right = stimuli.Rectangle(size= (len_sq, len_sq), colour= (255,0,0), line_width= 1, position= (width//2 - len_sq/2, -height//2 + len_sq/2))
square_bottom_left = stimuli.Rectangle(size= (len_sq, len_sq), colour= (255,0,0), line_width= 1, position= (-width//2 + len_sq/2, -height//2 + len_sq/2))

# Wait for a ket to be pressed before presenting shapes
exp.keyboard.wait()

# Presents all previously created rectangles
square_top_right.present(clear = True, update=False)
square_top_left.present(clear = False, update=False)
square_bottom_right.present(clear = False, update=False)
square_bottom_left.present(clear = False, update=True)

# Displays until a key is pressed
exp.keyboard.wait()

# End experiment
control.end()