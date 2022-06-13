from vpython import *

simulation = canvas(align = 'left')
    
# global variables
g=9.81 # acceleration due to gravity
l = 6

ω=0.0 # angular velocity
x = 2.0 # make this variable with a slider
v = 0.0
a = 0.0
α = 0.0
θ = pi/2

onoff = False

pivot=vector(0,4,0)

ball=sphere(pos=vector(pivot.x+(l+x)*sin(θ),pivot.y-(l+x)*cos(θ),0),radius=0.2,color=color.blue, mass = 1, make_trail=True) #creates ball and spring objects

phgraph = graph(width = 400, height = 400, xtitle = 'θ', ytitle = 'ω', align = 'left') #creates phase graph
phcurve = gcurve(graph = phgraph, color = color.red) # curve on phase graph
phgraph2 = graph(width = 400, height = 400, xtitle = 'displacement', ytitle = 'v', align = 'left') #creates phase graph
phcurve2 = gcurve(graph = phgraph2, color = color.blue) # curve on phase graph

spring = helix(pos = pivot,axis=ball.pos-pivot,radius=0.2,color=color.red,size=vector(1,0.3,0.3), coils=5, thickness=0.1, stiffness = 2 * ball.mass * g /l )


dt=0.01 # time interval 
#cosine=(pivot.y-ball.pos.y)/l # calculation of cos(theta) 
#theta=acos(cosine) # angle with vertical direction

#print(theta)


#functions for sliders and buttons
def gravityshift(s):
    global g
    g = s.value
    gs_caption.text = '<b>gravity</b> = '+'{:1.2f}'.format(gs.value)+' m/s<sup>2</sup>\n\n'
    
#creates gravity slider
gs = slider(bind = gravityshift, min = 0.0, max = 39.4, value = g)
gs_caption = wtext(text = '<b>gravity</b> = '+'{:1.2f}'.format(gs.value)+' m/s<sup>2</sup>\n\n')

#creates mass slider
def massshift(s):
    ball.mass = s.value
    ball.radius = s.value **(1/3) * 0.2 #visually increase radius proportionally to mass
    ms_caption.text = '<b>mass</b> = '+'{:1.2f}'.format(ball.mass)+' g\n\n'
    
    
ms = slider(bind = massshift, min = 0.0, max = 10.0, value = 1.0)
ms_caption = wtext(text = '<b>mass</b> = '+'{:1.2f}'.format(ball.mass)+' g\n\n')

#creates initial angle slider
def thetashift(s):
    global θ
    θ = s.value
    ts_caption.text = '<b>initial angle</b> = '+'{:1.3f}'.format(ts.value/pi)+'π rad\n\n'
    
ts = slider(bind = thetashift, min = -pi, max = pi, value = pi/4, step = pi/8)
ts_caption = wtext(text = '<b>initial angle</b> = '+'{:1.3f}'.format(ts.value / pi)+'π rad\n\n')

#creates spring length slider


#creates initial displacement slider 
def xshift(s):
    global x
    x = s.value
    xs_caption.text = '<b>initial displacement</b> = '+'{:1.2f}'.format(xs.value)+' m\n\n'
    
xs = slider(bind = xshift, min = 0.0, max = 5, value = 2.0)
xs_caption = wtext(text = '<b>initial displacement</b> = '+'{:1.2f}'.format(xs.value)+' m\n\n')

#creates spring constant slider
def kshift(s):
    global k 
    k = s.value
    ks_caption.text = '<b>spring constant</b> = '+'{:1.2f}'.format(spring.stiffness)+' N/m\n\n'
    
ks = slider(bind = kshift, min = 1, max = 100, value = 10.0)
ks_caption = wtext(text = '<b>spring constant</b> = '+'{:1.2f}'.format(spring.stiffness)+' N/m\n\n')

#creates pause unpause button
def pause():
    global onoff
    onoff = not onoff
    if onoff: 
        rs.text = "Pause"
        ball.clear_trail()
    else: rs.text = "Resume"

rs = button(bind = pause, text = "Run")


# while loop constantly checks if run button is clicked. If so, simulation plays. Calculates movement based on Lagrange Equations.        
while(True):
    rate(1/dt)
    if (onoff): # maximum 100 calculations per second
        a = (l + x) * ω**2 - spring.stiffness/ball.mass * x + g * cos(θ)
        α = -2/(l + x) * v * ω - g/(l + x) * sin(θ)
        v = v + a * dt
        x = x + v * dt
        ω = ω + α *dt
        θ = θ + ω * dt
        
        ball.pos=vector((l+x)*sin(θ),pivot.y-(l+x)*cos(θ),0) # cal. position
        spring.axis=ball.pos-spring.pos # updating other end of rod of pendulum

        phcurve.plot((θ, ω))
        phcurve2.plot((x, v))

#spring = helix( pos=vector(0,2,0), axis=vector(0,-3,0), size=vector(1,0.3,0.3), coils=5, thickness=0.03, stiffness=0.05)

#eq_pos = spring.pos+spring.axis

#ball = sphere( pos=spring.pos+spring.axis, color=color.red, radius=0.2,mass=1.0, velocity=vector(0,0.1,0), force=vector(0,0,0), make_trail=True )

#dt = 0.01

#while(True):
#    rate(1000)
#    ball.force = -spring.stiffness*(ball.pos-eq_pos) #spring force equation F = -kx
#    ball.velocity = ball.velocity + ball.force/ball.mass*dt # vf = vi + at
#    ball.pos = ball.pos + ball.velocity*dt # xf = xi + vt
#    spring.axis = ball.pos - spring.pos
