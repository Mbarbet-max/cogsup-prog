# Import the main modules of expyriment
import expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import *

# Allows to use window not in full screen
expyriment.control.set_develop_mode(True)

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "pre_ex1")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Define all stimuli
circle = stimuli.Circle(radius = 50, position=(-200, 0))
square = stimuli.Rectangle(size = (100,100), position=(200,0))

# Preload stimuli
circle.preload()
square.preload()

# Present cue for 3 seconds
cue = stimuli.TextLine("Press the arrow corresponding to the circle's side")
cue.present()
exp.clock.wait(3000)

# Present the sqaure and the circle
circle.present(clear = True, update= False)
square.present(clear = False, update= True)

key, rt = exp.keyboard.wait()

if key == K_LEFT :
    feedback = stimuli.TextLine("Congrats!")
    time_feedback = stimuli.TextLine("It took you " + str(rt/1000) + " seconds", position=(0,-50))

    feedback.present(clear = True, update= False)
    time_feedback.present(clear = False, update= True)
else :
    feedback = stimuli.TextLine("Wroooong")
    feedback.present()


exp.keyboard.wait()


# End experiment
expyriment.control.end()