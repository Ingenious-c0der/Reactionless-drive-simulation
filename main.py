import pygame
import math
import sys
import numpy as np
from scipy.integrate import quad
import scipy.special as special
vel = 0
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1500,800))
green = (0, 255, 0)
blue = (29, 10, 46)
angle = 0
bangle= 0
mass_angle = 0
d=1155
y_mass = 400
z=0
y2_mass= 680
v=0
V=0
#image loading
#axes
#axis length 410
axis = pygame.image.load("oriaxis.png")
axis_rect = axis.get_rect(center = [400,400])
axis_centre = (310,400)

axis2 = pygame.image.load("oriaxis.png")
axis_rect2 = axis2.get_rect(center = [800,800])
axis2_centre = (930,400)
print(axis2.get_width(),axis2.get_height())
#masses
mass = pygame.image.load("mass_smol.png")
mass_rect = mass.get_rect(center=[45,400])
mass2 = pygame.image.load("mass_smol.png")
mass_rect2 = mass.get_rect(center=[1155,500])
weight = 10

#sqaures
sqaure = pygame.image.load("appeareance sqaure.png")
sqaure_rect = sqaure.get_rect(center=[515,400])
sqaure2 = pygame.image.load("appeareance sqaure.png")
sqaure_rect2 = sqaure.get_rect(center=[105,400])
sqaure3 = pygame.image.load("appeareance sqaure.png")
sqaure_rect3 = sqaure.get_rect(center=[740,400])
sqaure4 = pygame.image.load("appeareance sqaure.png")
sqaure_rect4 = sqaure.get_rect(center=[1125,400])

transit_sqaure = pygame.image.load("appeareance sqaure_transit.png")
transit_sqaure_rect = transit_sqaure.get_rect(center = [515,400])
transit_sqaure2 = pygame.image.load("appeareance sqaure_transit.png")
transit_sqaure_rect2 = transit_sqaure.get_rect(center = [105,400])
transit_sqaure3 = pygame.image.load("appeareance sqaure_transit.png")
transit_sqaure_rect3 = transit_sqaure.get_rect(center = [740,400])
transit_sqaure4 = pygame.image.load("appeareance sqaure_transit.png")
transit_sqaure_rect4 = transit_sqaure.get_rect(center = [1125,400])

#background
background = pygame.image.load("background_space.png").convert_alpha()
background_rect = background.get_rect(center=[750,400])
#Textbox
font = pygame.font.Font('freesansbold.ttf', 25)
c=0
t=0
font2 = pygame.font.Font('freesansbold.ttf',60)

#Stopper
Stopper = pygame.image.load("stopper.png")
Stopper_rect = Stopper.get_rect(center=[1235,380])
stopperi = pygame.image.load("stopper_inverted.png")
stopperi_rect = stopperi.get_rect(center=[23,380])
#pipeline
pipeline = pygame.image.load("pipeline.png")
pipeline_rect = pipeline.get_rect(center=[990,575])
pipelinei = pygame.image.load("pipeline_inverted.png")
pipelinei_rect = pipelinei.get_rect(center=[285,575])
class pipelinemass:
    def __init__(self,surface,rect):
        self.surface = surface
        self.rect = rect



def rotate(surface,angle,center_new):
    """Axis rotatons"""

    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=[center_new[0],center_new[1]])

    return rotated_surface,rotated_rect

def massrotate(surface,origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """

    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=(qx, qy))
    return rotated_surface, rotated_rect


def getforceY(angle:float,omega)-> float:
    """ throws out net y force at the instant"""

    if 180<=angle<=270:
        F_y =  ((weight*(omega)**2)*2.05)*math.sin(math.radians(angle-180))


        return F_y

    else :
        F_y = ((weight*(omega)**2)*2.05)*math.cos(math.radians(angle-270))

        return  F_y



def equation(t):
    global x
    x = (abs(f_max*(math.sin(omega*t-math.pi))) - f_max*(math.sin(omega*t)))/2

    return x





def velocity(weight,omega,weight_system,time)->float:

    """"Fucntion for calculating the velocity at the given instant from the force equation in the equation function"""
    V = ((quad(equation,0,t)[0]))/weight_system


    return V


def constant_velocity(weight,fixed_omega,weight_system,time)->float:
    """Since pygame is a ... and omega keeps varying , the velocity is erroneous wrt processing power.So velocity needs to be corrected and averaged out for max trials"""
    V = ((quad(equation,0,t)[0]))/weight_system

    return V


start_ticks=pygame.time.get_ticks() #starter tick


#sub_v =quad()


#main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    angle_store = angle

    t=(pygame.time.get_ticks()-start_ticks)/1000

    angle+=7



    delta_angle = angle - angle_store
    bangle += delta_angle
    text = font.render(f"Net force upwards :   0 N", True, green, blue)
    textRect = text.get_rect(center=[650, 200])
    text2 = font.render(f"Instantaneous velocity : {int(vel)} m/s ",True,green,blue)

    text2Rect = text2.get_rect(center = [900,150])
    omega = ((bangle/360)*(2*math.pi))/t
    f_max = 2*weight*(omega**2)*2.05



#v_initial not getting updated
    text3 = font.render(f" Seconds passed from start : {int(t)}  RPM : {int((omega)*9.5493)} ",True,green,blue)

    text3Rect = text3.get_rect(center = [300,150])
    if 356<=angle<=362:
        angle = 0


    axis_rotated, axis_rotated_rect = rotate(axis, angle,axis_centre)
    axis_rotated2,axis_rotated_rect2 = rotate(axis2,-angle,axis2_centre)
    mass_rotated,mass_rotated_rect = massrotate(mass,(310,400),(105,400),math.radians(-angle))
    mass_rotated2,mass_rotated_rect2 = massrotate(mass2,(930,400),(1125,400),math.radians(angle))


    mass_pipeline_pos_rect = mass2.get_rect(center=[angle,angle])


    #force summation calculation
    if 180<=angle<=360:
        fy_net = 2*getforceY(angle,omega)

        vel = velocity(weight, omega, 200, t)
        print(f_max,omega)





        text = font.render(f"Net force upwards : {math.trunc(fy_net)} N",True, green, blue)
        textRect = text.get_rect(center=[650,200])
















    #bliting
    screen.fill((0, 0, 0))
    rel_z =z % background.get_rect().height
    screen.blit(background,(0,rel_z- background.get_rect().height))
    if rel_z  < 1200 :
        screen.blit(background,(0,rel_z))
    z+=vel/10



    pygame.draw.rect(screen, (29, 10, 46), (5, 80, 1250, 630))


    pygame.draw.rect(screen, (0, 100, 255), (5, 80, 1250, 630),3)
    screen.blit(pipeline,pipeline_rect)
    screen.blit(pipelinei,pipelinei_rect)
    screen.blit(axis_rotated,axis_rotated_rect)

    screen.blit(axis_rotated2,axis_rotated_rect2)
    if 180 <=angle <= 360:
        screen.blit(mass_rotated2, mass_rotated_rect2)

        screen.blit(mass_rotated, mass_rotated_rect)


    screen.blit(sqaure,sqaure_rect)
    screen.blit(sqaure2, sqaure_rect2)
    screen.blit(sqaure3, sqaure_rect3)
    screen.blit(sqaure4, sqaure_rect4)
    if 160<= angle <=190:
        screen.blit(transit_sqaure,transit_sqaure_rect)
        screen.blit(transit_sqaure3,transit_sqaure_rect3)



    if 340<= angle <=380:
        screen.blit(transit_sqaure2,transit_sqaure_rect2)
        screen.blit(transit_sqaure4,transit_sqaure_rect4)

    screen.blit(text,textRect)
    screen.blit(text2,text2Rect)
    screen.blit(text3, text3Rect)
    screen.blit(Stopper,Stopper_rect)
    screen.blit(stopperi,stopperi_rect)
    clock.tick(100)
    pygame.display.flip()
