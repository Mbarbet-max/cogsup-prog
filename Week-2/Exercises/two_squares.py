# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "two_Square")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)


# Create the left 50px red square
left_square = stimuli.Rectangle(size = (50,50), colour = (168,28,7), position=(-125, 0))

# Create the right 50px green square
right_square = stimuli.Rectangle(size = (50,50), colour = (46,139,87), position=(125, 0))

# Start running the experiment
control.start(subject_id=1)

#Present the square
left_square.present(clear = True, update=False)

# Present the fixation cross
right_square.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()