# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()
from expyriment.misc import geometry
import math

def shape_fct(nbr_sides, colour_code, x_pos, y_pos) :

    # Create an object of class Experiment
    exp = design.Experiment(name = "labeled shapes function")

    # Initialize the experiment
    control.initialize(exp)

    # Creating the polygon
    coloured_shape = stimuli.Shape(position = (x_pos, y_pos), colour = colour_code)
    coloured_shape.add_vertices(geometry.vertices_regular_polygon(nbr_sides, 50))

    # Creating the line that points to the polygon
    white_line_shape = stimuli.Line(start_point = (x_pos, y_pos + (1/2 * 50 * 1/math.tan(math.pi/nbr_sides))), 
                                    end_point = (x_pos, y_pos + (1/2 * 50 * 1/math.tan(math.pi/nbr_sides)) + 50), 
                                    line_width= 3)

    # Dictionary with the number of sides and the corresponding name of the polygon
    dict_polygon = {3 : "triangle", 4 : "square", 5 : "pentagon", 6 : "hexagon", 7 : "heptagon", 8 : "octogon"}

    # if the number of sides exceeds 9, print "fick dich", otherwise, print the corresponding name
    if nbr_sides > 9:
        shape_text = stimuli.TextBox(
        text="fick dich",
        size=(200, 40),
        position=(x_pos,
                  y_pos + (1/2 * 50 * 1/math.tan(math.pi/nbr_sides)) + 70))
        
    else:
        shape_text = stimuli.TextBox(
        text=dict_polygon[nbr_sides],
        size=(200, 40),
        position=(x_pos,
                  y_pos + (1/2 * 50 * 1/math.tan(math.pi/nbr_sides)) + 70)
    )

    # Start running the experiment
    control.start(subject_id=1)

    # Presenting shapes
    coloured_shape.present(clear= True, update= False)
    white_line_shape.present(clear= False, update= False)
    shape_text.present(clear= False, update= True)

    # Leave it on-screen until a key is pressed
    exp.keyboard.wait()

    # End the current session and quit expyriment
    control.end()

shape_fct()