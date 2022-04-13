from ursina import *
import math
import numpy as np

'''a hypothetical solar system constructed as per the real solar system
which contains arbitrary values for masses of celestial bodies and the value of G.
but the laws of physics and gravitation hold'''

app=Ursina()
Sky(texture='back')

def update():
    global velocity_mercury,velocity_venus,velocity_earth,velocity_mars,velocity_jupiter,velocity_saturn,velocity_uranus,velocity_neptune,velocity_pluto
    global mass_sun,mass_mercury,mass_venus,mass_earth,mass_mars,mass_jupiter,mass_saturn,mass_uranus,mass_neptune,mass_pluto
    global sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune
    global moon
    global r,angle_phi,angle_theta
    global asteroids,dist,angle,rot_angle,moon_angle
    global rot_angle,rot_inc
    if held_keys['+']: 
	    rot_inc=rot_inc*1.05
    if held_keys['-']: 
	    rot_inc=rot_inc*0.95
    if not held_keys['space']:
        move(mercury,mass_mercury,velocity_mercury,time.dt)
        move(venus,mass_venus,velocity_venus,time.dt)
        move(earth,mass_earth,velocity_earth,time.dt)
        moon_angle+=3*time.dt
        moon.position=(earth.x+.5*np.cos(moon_angle),earth.y,earth.z+.5*np.sin(moon_angle))
        move(mars,mass_mars,velocity_mars,time.dt)
        move(jupiter,mass_jupiter,velocity_jupiter,time.dt)
        move(saturn,mass_saturn,velocity_saturn,time.dt)
        ring_saturn.position=saturn.position
        move(uranus,mass_uranus,velocity_uranus,time.dt)
        move(neptune,mass_neptune,velocity_neptune,time.dt)
        move(pluto,mass_pluto,velocity_pluto,time.dt)
        sun.rotation_y=(rot_angle/30)
        mercury.rotation_y=rot_angle*0.41
        venus.rotation_y=rot_angle/116
        earth.rotation=(0,rot_angle*0.917,0)
        mars.rotation_y=rot_angle
        jupiter.rotation_y=2.667*rot_angle
        saturn.rotation_y=rot_angle*2.4
        uranus.rotation_z=1.41*rot_angle
        neptune.rotation_y=rot_angle*1.5
        pluto.rotation_y=rot_angle/6.4
        for i in range(0,511,1):
            angle[i]+=random.random()*0.001
            if angle[i]>2*np.pi: angle[i]-=2*np.pi
            asteroids[i].position=(dist[i]*np.cos(angle[i]),1-2*random.random(),dist[i]*np.sin(angle[i]))

    if held_keys['w']:r-=(r/100)
    if held_keys['s']:r+=(r/100)
    if r<=0.5: r=0.5
    if held_keys['d']:angle_phi+=0.01
    if held_keys['a']:angle_phi-=0.01

    x,y,z=mouse.position;angle_theta=y*np.pi+(np.pi/2.0)
    camera.position=(r*np.sin(angle_theta)*np.sin(angle_phi),r*np.cos(angle_theta),-r*np.sin(angle_theta)*np.cos(angle_phi));camera.look_at(sun,axis='forward')

    if held_keys['1']:camera.x+=mercury.x;camera.y+=mercury.y;camera.z+=mercury.z
    if held_keys['2']:camera.x+=venus.x;camera.y+=venus.y;camera.z+=venus.z
    if held_keys['3']:camera.x+=earth.x;camera.y+=earth.y;camera.z+=earth.z
    if held_keys['4']:camera.x+=mars.x;camera.y+=mars.y;camera.z+=mars.z
    if held_keys['5']:camera.x+=jupiter.x;camera.y+=jupiter.y;camera.z+=jupiter.z
    if held_keys['6']:camera.x+=saturn.x;camera.y+=saturn.y;camera.z+=saturn.z
    if held_keys['7']:camera.x+=uranus.x;camera.y+=uranus.y;camera.z+=uranus.z
    if held_keys['8']:camera.x+=neptune.x;camera.y+=neptune.y;camera.z+=neptune.z
    if held_keys['9']:camera.x+=pluto.x;camera.y+=pluto.y;camera.z+=pluto.z
    rot_angle+=rot_inc
sun=Entity(model='sphere',color=color.white,texture='sun',position=(0,0,0),scale=50)
mass_sun=10000

mercury=Entity(model='sphere',color=color.white,texture='mercury',position=(28,0,0),rotation=(0,0,2),scale=0.2)
orbit_mercury=Entity(model=Circle(resolution=63,radius=27,mode='line'),color=color.dark_gray,rotation=(90,0,0))
mass_mercury=4.5

venus=Entity(model='sphere',color=color.white,texture='venus',position=(36.5,0,0),rotation=(0,0,177.5),scale=0.48)
orbit_venus=Entity(model=Circle(resolution=63,radius=36.5,mode='line'),color=color.dark_gray,rotation=(90,0,0))
mass_venus=8.15

earth=Entity(model='sphere',color=color.white,texture='earth',position=(50,0,0),rotation=(0,0,23.5),scale=0.5)
orbit_earth=Entity(model=Circle(resolution=127,radius=50,mode='line'),color=color.dark_gray,rotation=(90,0,0))
mass_earth=10

moon=Entity(model='sphere',color=color.white,texture='moon',position=(55,0,0),scale=0.01)
moon_angle=0

mars=Entity(model='sphere',color=color.white,texture='mars',position=(75,0,0),rotation=(0,0,25),scale=0.47)
orbit_mars=Entity(model=Circle(resolution=127,mode='line',radius=75),color=color.dark_gray,rotation=(90,0,0))
mass_mars=10


asteroids=[];dist=[];angle=[]
for i in range(0,511,1):
	num=100+(50*random.random());dist.append(num);scl=random.random();ang=random.random()*2*np.pi;angle.append(ang)
	asteroids.append(Entity(model='sphere',texture='asteroid',scale=scl,position=(num*np.cos(ang),0,num*np.sin(ang))))

jupiter=Entity(model='sphere',color=color.white,texture='jupiter',scale=5,position=(250,0,0),rotation=(0,0,3))
orbit_jupiter=Entity(model=Circle(resolution=511,radius=250,mode='line'),color=color.dark_gray,rotation=(90,0,0))
mass_jupiter=3000

saturn=Entity(model='sphere',color=color.white,texture='saturn',position=(450,0,0),rotation=(-26.73,0,0),scale=4.25)
orbit_saturn=Entity(model=Circle(resolution=1023,radius=450,mode='line'),color=color.dark_gray,rotation=(90,0,0))
mass_saturn=930
ring_saturn=Entity(model='circle',color=color.white,texture='ring',scale=7,double_sided=True,position=saturn.position,rotation=(90-26.73,0,0))

uranus=Entity(model='sphere',color=color.white,texture='uranus',position=(950,0,0),rotation=(0,0,98),scale=2)
orbit_uranus=Entity(model=Circle(resolution=1023,radius=950,mode='line'),color=color.dark_gray,rotation=(90,0,0))
mass_uranus=145

neptune=Entity(model='sphere',color=color.white,texture='neptune',position=(1500,0,0),rotation=(0,0,28.35),scale=2)
orbit_neptune=Entity(model=Circle(resolution=2047,radius=1500,mode='line'),color=color.dark_gray,rotation=(90,0,0))
mass_neptune=170

pluto=Entity(model='sphere',color=color.white,texture='pluto',position=(1950,0,0),rotation=(0,0,57),scale=0.1)
orbit_pluto=Entity(model=Circle(resolution=2047,radius=1950,mode='line'),color=color.dark_gray,rotation=(90,0,0))
mass_pluto=0.1

r=250;angle_theta=np.pi/2.0;angle_phi=0

def vector(point1,point2):
    return Vec3((point2.x-point1.x),(point2.y-point1.y),(point2.z-point1.z))

def magnitude(vector):
    return math.sqrt(vector.x**2+vector.y**2+vector.z**2)

def normalize(vector):
    return Vec3((vector.x/magnitude(vector)),(vector.y/magnitude(vector)),(vector.z/magnitude(vector)))

def multiply(unit_vector,magnitude):
    return Vec3((unit_vector.x*magnitude),(unit_vector.y*magnitude),(unit_vector.z*magnitude))

def force_on(planet,mass):
    global sun,mass_sun
    force_dir=normalize(vector(sun,planet))
    force_mag=((mass_sun)*mass)/((magnitude(vector(sun.position,planet.position)))*(magnitude(vector(sun.position,planet.position))))
    return multiply(force_dir,-force_mag)

def move(planet,mass,velocity,time):
    global sun
    global velocity_mercury,velocity_venus,velocity_earth,velocity_mars,velocity_jupiter,velocity_saturn,velocity_uranus,velocity_neptune,velocity_pluto

    acceleration=multiply(force_on(planet,mass),(1.0/mass))
    velocity=velocity+multiply(acceleration,time)
    displacement=multiply(velocity,time)

    if planet is mercury: velocity_mercury=velocity
    elif planet is venus: velocity_venus=velocity
    elif planet is earth: velocity_earth=velocity
    elif planet is mars: velocity_mars=velocity
    elif planet is jupiter: velocity_jupiter=velocity
    elif planet is saturn: velocity_saturn=velocity
    elif planet is uranus: velocity_uranus=velocity
    elif planet is neptune: velocity_neptune=velocity
    elif planet is pluto: velocity_pluto=velocity

    planet.position+=displacement


velocity_mercury=Vec3(0,0,19.25)
velocity_venus=Vec3(0,0,16.75)
velocity_earth=Vec3(0,0,14.5)
velocity_mars=Vec3(0,0,11.6)
velocity_jupiter=Vec3(0,0,6.5)
velocity_saturn=Vec3(0,0,4.75)
velocity_uranus=Vec3(0,0,3.3)
velocity_neptune=Vec3(0,0,2.6)
velocity_pluto=Vec3(0,0,2.4)

rot_angle=0
rot_inc=8.5
app.run()