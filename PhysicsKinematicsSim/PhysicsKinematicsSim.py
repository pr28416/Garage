import pygame, math
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.toggle import Toggle
from datetime import datetime
w, h = 0, 1

class Entry:
    def __init__(self, time=0, heading_ang=0, pos_x=0, pos_y=0, vel_x=0, vel_y=0, accel_x=0, accel_y=0):
        self.time = time
        self.heading_ang=heading_ang
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.accel_x = accel_x
        self.accel_y = accel_y
    
    def __str__(self):
        return f"{self.time},{self.heading_ang},{self.pos_x},{self.pos_y},{self.vel_x},{self.vel_y},{self.accel_x},{self.accel_y}"

class DataEntries:
    def __init__(self, time=0, heading_ang=0, pos_x=0, pos_y=0, vel_x=0, vel_y=0, accel_x=0, accel_y=0):
        self.entries = [Entry(time,heading_ang,pos_x,pos_y,vel_x,vel_y,accel_x,accel_y)]
    
    def add(self, time=0, heading_ang=0, pos_x=0, pos_y=0, vel_x=0, vel_y=0, accel_x=0, accel_y=0):
        e = Entry(time,heading_ang,pos_x,pos_y,vel_x,vel_y,accel_x,accel_y)
        # print("Added", e)
        self.entries.append(e)

    def logToFile(self, filename=None):
        if filename is None:
            filename = f"{datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.csv"
        with open(f"data/{filename}", "w") as f:
            f.write("time,heading_ang,pos_x,pos_y,vel_x,vel_y,accel_x,accel_y\n")
            for entry in self.entries:
                f.write(f"{str(entry)}\n")

class Game:
    # Game constants
    SCREEN_DIMENSIONS = (1080,720) # width x height
    BOTTOM_PALETTE_HEIGHT = 120
    SIDE_PALETTE_WIDTH = 0
    MAX_FRAMERATE = 60 # fps

    def __init__(self):
        # Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((Game.SCREEN_DIMENSIONS[w]+Game.SIDE_PALETTE_WIDTH, Game.SCREEN_DIMENSIONS[h]+Game.BOTTOM_PALETTE_HEIGHT))
        pygame.display.set_caption("Physics Kinematics Simulator")
        # Load images
        self.backdrop = pygame.image.load("backdrop.jpeg")
        bgscale = Game.SCREEN_DIMENSIONS[h] if Game.SCREEN_DIMENSIONS[h] > Game.SCREEN_DIMENSIONS[w] else Game.SCREEN_DIMENSIONS[w]
        self.backdrop = pygame.transform.scale(self.backdrop, (self.backdrop.get_width()*bgscale/Game.SCREEN_DIMENSIONS[h], self.backdrop.get_height()*bgscale/Game.SCREEN_DIMENSIONS[w]))
        self.personImg = pygame.image.load("person.png")
        self.personImg = pygame.transform.scale(self.personImg, (self.personImg.get_width()//8, self.personImg.get_height()//8))
        self.cannonImg = pygame.image.load("cannon1.png")
        self.cannonImg = pygame.transform.scale(self.cannonImg, (self.cannonImg.get_width()//8, self.cannonImg.get_height()//8))
        self.explosionImgs = [pygame.image.load(f"explosion/explosion{i}.png") for i in range(1, 18)]
        # Set game parameters
        self.gameParameters = {
            "PROGRAM_RUNNING": True,
            "cliff_dimensions": (200,360),
            "current_launch_velocity": 600,
            "current_launch_angle": 60,
            "starting_launch_velocity": 450,
            "starting_launch_angle": 45,
            "starting_gravity": (0,400),
            "run_sim": False,
            "projectile_has_reset": False,
            "projectile_start_tick": 0,
            "is_playing_explosion": False,
            "explosion_current_idx": 0,
            "didAccountForCeilingHit": False,
            "dataEntries": [],
            "enableVelocityArrows": False
        }
        self.setGameParam("cannon_pos", (100, self.getGameParam("cliff_dimensions")[h]+self.cannonImg.get_height()-10))
        self.setGameParam("projectile_default_starting_pos", (100, self.getGameParam("cliff_dimensions")[h]+self.cannonImg.get_height()-10))

    def rotateImgAboutCenter(self, image, topleft, new_angle):
        rotated_image = pygame.transform.rotate(image, new_angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
        return rotated_image, new_rect

    def setGameParam(self, key, value):
        self.gameParameters[key] = value

    def getGameParam(self, key):
        return self.gameParameters[key]

    def updateProjectilePos(self, tick):
        # Starting simulation
        if not self.getGameParam("projectile_has_reset"):
            # Reset projectile at the start
            self.setGameParam("projectile_default_starting_pos", (self.getGameParam("cliff_dimensions")[w]-self.cannonImg.get_width(), self.getGameParam("cliff_dimensions")[h]))
            self.setGameParam("projectile_starting_pos", self.getGameParam("projectile_default_starting_pos"))
            self.setGameParam("projectile_current_pos", self.getGameParam("projectile_starting_pos"))
            self.setGameParam("current_launch_angle", self.getGameParam("starting_launch_angle"))
            self.setGameParam("current_launch_velocity", self.getGameParam("starting_launch_velocity"))
            self.setGameParam("current_gravity", self.getGameParam("starting_gravity"))
            self.getGameParam("dataEntries").append(DataEntries(
                time=0,
                heading_ang=self.getGameParam("starting_launch_angle"),
                pos_x=self.getGameParam("projectile_default_starting_pos")[w],
                pos_y=self.getGameParam("projectile_default_starting_pos")[h],
                vel_x=self.getGameParam("starting_launch_velocity")*math.cos(self.getGameParam("starting_launch_angle")*math.pi/180),
                vel_y=self.getGameParam("starting_launch_velocity")*math.sin(self.getGameParam("starting_launch_angle")*math.pi/180),
                accel_x=self.getGameParam("current_gravity")[w],
                accel_y=self.getGameParam("current_gravity")[h],
            ))
            self.setGameParam("didAccountForCeilingHit", False)
            self.setGameParam("projectile_start_tick", tick)
            self.setGameParam("projectile_has_reset", True)

        # Play explosion at end of simulation
        elif self.getGameParam("is_playing_explosion"):
            # Loop through all frames of explosion
            if (self.getGameParam("explosion_current_idx") >= len(self.explosionImgs)*10):
                # Explosion is done
                print("explosion done")
                # Log to file
                self.getGameParam("dataEntries")[-1].logToFile()
                # Reset elements
                self.setGameParam("is_playing_explosion", False)
                self.setGameParam("run_sim", False)
                self.setGameParam("projectile_has_reset", False)
            else:
                i = self.getGameParam("explosion_current_idx")
                pos = self.getGameParam("projectile_current_pos")
                self.screen.blit(self.explosionImgs[i//10], (pos[w]-self.personImg.get_width()//2, pos[h]-2*self.personImg.get_height()))
                self.setGameParam("explosion_current_idx", i+1)

        # Move projectile along trajectory
        else:
            dt = (tick - self.getGameParam("projectile_start_tick"))/1000
            current_pos = self.getGameParam("projectile_current_pos")

            # Projectile has hit the ground
            if current_pos[h]+self.personImg.get_height() >= Game.SCREEN_DIMENSIONS[h]:
                self.setGameParam("is_playing_explosion", True)
                self.setGameParam("explosion_current_idx", 0)

            # Projectile has hit the ceiling or side; remove vel_x
            elif (current_pos[h] <= 0 or current_pos[w] + self.personImg.get_width() >= Game.SCREEN_DIMENSIONS[w] or current_pos[w] <= 0) and not self.getGameParam("didAccountForCeilingHit"):
                self.setGameParam("projectile_starting_pos", (current_pos[w], 720-current_pos[h]))
                self.setGameParam("current_launch_velocity", 0)
                self.setGameParam("projectile_start_tick", tick)
                self.setGameParam("didAccountForCeilingHit", True)

            # Set position of projectile
            else:
                # Set position of projectile
                x0, v0, theta0, g = self.getGameParam("projectile_starting_pos"), self.getGameParam("current_launch_velocity"), self.getGameParam("starting_launch_angle"), self.getGameParam("current_gravity")
                self.setGameParam("projectile_current_pos", (
                    x0[w] + v0*math.cos(theta0*math.pi/180)*dt - g[w]/2*dt**2,
                    Game.SCREEN_DIMENSIONS[h]-(x0[h] + v0*math.sin(theta0*math.pi/180)*dt - g[h]/2*dt**2)
                ))

                # Set heading of projectile
                vx, vy = v0*math.cos(theta0*math.pi/180)-g[w]*dt, v0*math.sin(theta0*math.pi/180)-g[h]*dt
                rot_angle = 180/math.pi*math.atan(vy/(0.00001 if vx == 0 else vx))-90
                rotPersonImg, rotPersonPos = self.rotateImgAboutCenter(self.personImg, self.getGameParam("projectile_current_pos"), rot_angle)

                # Write data to entries
                self.getGameParam("dataEntries")[-1].add(
                    time=dt,
                    heading_ang=rot_angle+90,
                    pos_x=rotPersonPos.topleft[w],
                    pos_y=Game.SCREEN_DIMENSIONS[h]-rotPersonPos.topleft[h],
                    vel_x=vx,
                    vel_y=vy,
                    accel_x=self.getGameParam("current_gravity")[w],
                    accel_y=self.getGameParam("current_gravity")[h]
                )

                # Render projectile image
                self.screen.blit(rotPersonImg, rotPersonPos)

                # Render velocity arrows
                if self.getGameParam("enableVelocityArrows"):
                    signum = lambda x: 1 if x > 0 else -1 if x < 0 else 0
                    pygame.draw.polygon( # vel_x
                        self.screen,
                        (0,0,255),
                        tuple(map(
                            lambda t: (t[0]+rotPersonPos.centerx, t[1]+rotPersonPos.centery),
                            (
                                (0,0),
                                (vx//5,0),
                                (vx//5,5),
                                (vx//5+signum(vx)*5*2/3**0.5,0),
                                (vx//5,-5),
                                (vx//5,0)
                            )
                        )),
                        width=4
                    )
                    pygame.draw.polygon( # vel_y
                        self.screen,
                        (255,0,0),
                        tuple(map(
                            lambda t: (t[0]+rotPersonPos.centerx, t[1]+rotPersonPos.centery),
                            (
                                (0,0),
                                (0,-vy//5),
                                (5,-vy//5),
                                (0,-(vy//5+signum(vy)*5*2/3**0.5)),
                                (-5,-vy//5),
                                (0,-vy//5),
                            )
                        )),
                        width=4
                    )

    def drawEnvironment(self):
        # Background
        # self.screen.fill((255,255,255))
        self.screen.blit(self.backdrop, (0,0))

        # Cliff
        cliff = pygame.Rect(0, Game.SCREEN_DIMENSIONS[h]-(self.getGameParam("cliff_dimensions")[h]-self.cannonImg.get_height()+10), *self.getGameParam("cliff_dimensions"))
        pygame.draw.rect(
            surface=self.screen,
            color=(0,0,255),
            rect=cliff
        )

        # Ground
        pygame.draw.rect(
            surface=self.screen,
            color=(40,40,40),
            rect=pygame.Rect(0, Game.SCREEN_DIMENSIONS[h], Game.SCREEN_DIMENSIONS[w], Game.BOTTOM_PALETTE_HEIGHT)
        )
        
        # Right palette
        pygame.draw.rect(
            surface=self.screen,
            color=(40,60,80),
            rect=pygame.Rect(Game.SCREEN_DIMENSIONS[w], 0, Game.SIDE_PALETTE_WIDTH, Game.SCREEN_DIMENSIONS[h]+Game.BOTTOM_PALETTE_HEIGHT)
        )
        
        # Cannon
        rotCannonImg, rotCannonPos = self.rotateImgAboutCenter(
            image=self.cannonImg,
            # topleft=(self.getGameParam("cannon_pos")[w], Game.SCREEN_DIMENSIONS[h]-self.getGameParam("cannon_pos")[h]),
            topleft=(self.getGameParam("cliff_dimensions")[w]-self.cannonImg.get_width(), Game.SCREEN_DIMENSIONS[h]-self.getGameParam("cliff_dimensions")[h]),
            new_angle=self.getGameParam("starting_launch_angle")
        )

        # Render elements
        self.screen.blit(rotCannonImg, rotCannonPos)

    def run(self):
        clock = pygame.time.Clock()

        # GUI controls
        # Run button
        runSimButton = Button(self.screen, 12, 12, 144, 36,
                            text="Run simulation", fontSize=24, textColour=(255,255,255),
                            inactiveColour=(40,80,120),
                            onClick=lambda: self.setGameParam("run_sim", True))
        
        # Launch velocity
        launchVelocitySlider = Slider(self.screen, 24, Game.SCREEN_DIMENSIONS[h]+24, 144, 28,
                            min=0, max=1000, step=10, initial=400)
        launchVelocityText = TextBox(self.screen, 16, Game.SCREEN_DIMENSIONS[h]+68, 160, 36, fontSize=24, borderThickness=1)
        launchVelocityText.disable()

        # Launch angle
        launchAngleSlider = Slider(self.screen, 24+180, Game.SCREEN_DIMENSIONS[h]+24, 144, 28,
                            min=0, max=90, step=1, initial=45)
        launchAngleText = TextBox(self.screen, 16+180, Game.SCREEN_DIMENSIONS[h]+68, 160, 36, fontSize=24, borderThickness=1)
        launchAngleText.disable()

        # Gravity
        gravitySlider = Slider(self.screen, 24+360, Game.SCREEN_DIMENSIONS[h]+24, 144, 28,
                            min=10, max=1000, step=10, initial=500)
        gravityText = TextBox(self.screen, 16+360, Game.SCREEN_DIMENSIONS[h]+68, 160, 36, fontSize=24, borderThickness=1)
        gravityText.disable()

        # Cliff width
        cliffWidthSlider = Slider(self.screen, 24+540, Game.SCREEN_DIMENSIONS[h]+24, 144, 28,
                            min=self.cannonImg.get_width(), max=Game.SCREEN_DIMENSIONS[w]//2, step=10, initial=self.getGameParam("cliff_dimensions")[w])
        cliffWidthText = TextBox(self.screen, 16+540, Game.SCREEN_DIMENSIONS[h]+68, 160, 36, fontSize=24, borderThickness=1)
        cliffWidthText.disable()

        # Cliff height
        cliffHeightSlider = Slider(self.screen, 24+720, Game.SCREEN_DIMENSIONS[h]+24, 144, 28,
                            min=self.cannonImg.get_height(), max=Game.SCREEN_DIMENSIONS[w]//2, step=10, initial=self.getGameParam("cliff_dimensions")[h])
        cliffHeightText = TextBox(self.screen, 16+720, Game.SCREEN_DIMENSIONS[h]+68, 160, 36, fontSize=24, borderThickness=1)
        cliffHeightText.disable()

        # Velocity arrows toggle
        velocityArrowsToggle = Toggle(self.screen, 24+900, Game.SCREEN_DIMENSIONS[h]+24, 40, 28)
        velocityArrowsText = TextBox(self.screen, 16+900, Game.SCREEN_DIMENSIONS[h]+68, 160, 36, fontSize=18, borderThickness=1)
        velocityArrowsText.disable()

        while self.getGameParam("PROGRAM_RUNNING"):
            tick = pygame.time.get_ticks()
            events = pygame.event.get()
            for event in events:
                # Quit event
                if event.type == pygame.QUIT:
                    self.setGameParam("PROGRAM_RUNNING", False)
            
            # Draw environment
            self.drawEnvironment()

            # Update game parameters
            self.setGameParam("starting_launch_velocity", launchVelocitySlider.getValue())
            launchVelocityText.setText(f"{launchVelocitySlider.getValue()} vel px/s")
            self.setGameParam("starting_launch_angle", launchAngleSlider.getValue())
            launchAngleText.setText(f"{launchAngleSlider.getValue()}° angle")
            self.setGameParam("starting_gravity", (self.getGameParam("starting_gravity")[w], gravitySlider.getValue()))
            gravityText.setText(f"{gravitySlider.getValue()} px/s^2 gravity")
            self.setGameParam("cliff_dimensions", (cliffWidthSlider.getValue(), cliffHeightSlider.getValue()))
            cliffWidthText.setText(f"{cliffWidthSlider.getValue()} px cliff width")
            cliffHeightText.setText(f"{cliffHeightSlider.getValue()} px cliff height")
            self.setGameParam("enableVelocityArrows", velocityArrowsToggle.getValue())
            velocityArrowsText.setText(f"Show vel arrows: {velocityArrowsToggle.getValue()}")

            # Update projectile position
            if self.getGameParam("run_sim"):
                self.updateProjectilePos(tick)

            # Refresh window
            pygame_widgets.update(events)
            pygame.display.flip()
            clock.tick()

        pygame.quit()

if __name__ == "__main__":
    Game().run()