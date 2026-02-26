# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Launching")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create the left 50px red square
left_square = stimuli.Rectangle(size = (50,50), colour = (168,28,7), position=(-400, 0))

# Create the right 50px green square
right_square = stimuli.Rectangle(size = (50,50), colour = (46,139,87))

# Start running the experiment
control.start(subject_id=1)

# Present the squares
left_square.present(clear = True, update=False)
right_square.present(clear=False, update=True)

# Wait 1 second
exp.clock.wait(1000)

# Move the red square to the green square
for i in range(70) :
    left_square.move(offset=(5,0))
    left_square.present(clear = True, update=False)
    right_square.present(clear=False, update=True)

# Wait 2 seconds (break the time chain, 50 ms seems to be the max time not to break the causal illusion)
exp.clock.wait(2000)

# Move the green square to the right
for i in range(70) :
    right_square.move(offset=(5,0))
    left_square.present(clear = True, update=False)
    right_square.present(clear=False, update=True)

# Wait 1 second
exp.clock.wait(1000)

# End the current session and quit expyriment
control.end()