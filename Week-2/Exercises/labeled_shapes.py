# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()
from expyriment.misc import geometry

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "two_Square")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)


# Create the left 50px red square
purple_triangle = stimuli.Shape(position=(-50,0), colour = (148,87,235))
purple_triangle.add_vertices(geometry.vertices_regular_polygon(3, 50))

yellow_hexagon = stimuli.Shape(position=(50,0), colour= (255,216,0))
yellow_hexagon.add_vertices(geometry.vertices_regular_polygon(6, 25))

white_line_triangle = stimuli.Line(start_point = (-50, 21), end_point = (-50, 71), line_width= 3)
white_line_hexagon = stimuli.Line(start_point = (50, 21), end_point = (50, 71), line_width= 3)

triangle_text = stimuli.TextBox(text = "triangle", size= (100,30), position= (-50, 91))
hexagon_text = stimuli.TextBox(text = "hexagon",  size= (100,30), position= (50, 91))

# Start running the experiment
control.start(subject_id=1)

purple_triangle.present(clear = True, update = False)
yellow_hexagon.present(clear= False, update= False)
white_line_triangle.present(clear= False, update= False)
white_line_hexagon.present(clear= False, update= False)
triangle_text.present(clear= False, update= False)
hexagon_text.present(clear= False, update= True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()