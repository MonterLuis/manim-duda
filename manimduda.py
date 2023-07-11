from manim import *
from manim.utils.color import Colors
import math 
config.disable_caching = True

def dgr2rad(grados):
    return ((2*math.pi)/360)*grados
def rad2dgr(rad):
    return (360/(2*math.pi))*rad
class TikZToManim(MovingCameraScene):

    def construct(self):
        
        # Define colors
        light_blue = "#1566C2"
        pure_blue = Colors.pure_blue.value
        orange= Colors.orange.value
        pink = Colors.pink.value
        white= Colors.white.value
        a=20*DEGREES
        b=20*DEGREES
        VTalfa= ValueTracker(a)
        VTbeta= ValueTracker(b)
        VTradio= ValueTracker(5)

        ax = Axes(x_length =10, y_length =10, tips= False, axis_config={'include_ticks': False})
        circle = Circle(radius=5, color= white)
        self.add(ax, circle)
        center = always_redraw( lambda: Dot(np.array([0, 0, 0]), color=pink))
        
        p_orange = always_redraw(lambda: Dot(np.array([VTradio.get_value()*math.cos((VTalfa.get_value()+VTbeta.get_value())), VTradio.get_value()*math.sin((VTalfa.get_value()+VTbeta.get_value())), 0]), color=orange))
     
       
        p_blue = always_redraw( lambda: Dot(np.array([VTradio.get_value()*math.cos(VTbeta.get_value())*math.cos(VTalfa.get_value()), VTradio.get_value()*math.cos(VTbeta.get_value())*math.sin(VTalfa.get_value()), 0]), color=light_blue))
        p_blue2 = always_redraw( lambda: Dot(np.array([VTradio.get_value()*math.cos(VTalfa.get_value()), VTradio.get_value()*math.sin(VTalfa.get_value()), 0]), color=light_blue))
        p_blue3 = always_redraw( lambda: Dot(np.array([-VTradio.get_value()*math.cos(VTalfa.get_value()), -VTradio.get_value()*math.sin(VTalfa.get_value()), 0]), color=light_blue))

        self.add(p_blue, p_orange)

        control_line = always_redraw( lambda: DashedLine(center,p_blue2))
        control_line2 = always_redraw( lambda: DashedLine(center, p_blue3))
        
        self.add(control_line, control_line2)

        l_beta_adjacent = always_redraw( lambda: Line(
            start=center.get_center(),
            end=p_blue.get_center(),
            stroke_width=4,
            color=pink
        ))

        l_pink = always_redraw( lambda: Line(
            start=center.get_center(),
            end=p_orange.get_center(),
            stroke_width=4,
            color=pink
        ))
        l_beta_opposite =always_redraw( lambda:  Line(
            start=p_blue.get_center(),
            end=p_orange.get_center(),
            stroke_width=4,
            color=pink
        ))
       
        
        self.add(   l_pink,
            
            l_beta_opposite,
            
            l_beta_adjacent,)

        anglebeta = always_redraw( lambda: Angle(control_line, l_pink, radius=0.6, color= pink))
        anglealfacontrol = always_redraw( lambda: Angle(ax.get_x_axis(), control_line, radius=0.6, color= pure_blue))
        self.add(anglealfacontrol, anglebeta)

        self.play(
        self.camera.frame.animate.scale(1.5) #.move_to(p_blue),
        )
        self.wait(2)
        self.play(
         VTbeta.animate.set_value(360*DEGREES), run_time=14, rate_func= linear
        )
        self.wait()
