import pygame
from pygame.locals import *
import sys

####Color Setup####
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
ORANGE = (250,125,0)
PURPLE = (250,0,250)
BLACK = (0,0,0)

####SCREEN SETUP####
hieght = 350
width = 210
screen = pygame.display.set_mode((width, hieght))
screen.fill((WHITE))

####GENERAL VAR SETUP####
mx = 0
my = 0
click_val = 0
clr_val = 0
n = 1


####BUTTON CLASS####

class Button(pygame.sprite.Sprite):
    def __init__(self, sprite, coord):
        super().__init__()
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
        self.rect.x, self.rect.y = coord
        self.button_val = 0
        self.collision_val = 0

    def buttonclick(self, click_stat):
        self.click_stat = click_stat
        if self.click_stat == 1 and self.collision_val == 1:
            self.button_val = 1
            print ('button clicked')
        else:
            self.button_val = 0

    def draw(self):
        screen.blit(self.sprite, (self.rect.x, self.rect.y))

    def collide_check(self):
        collision_val = pygame.sprite.collide_rect(mouse1, self)
        if collision_val == True:
            self.collision_val = 1
        else:
            self.collision_val = 0
            
####CURSOR CLASS####
            
class Cursor(pygame.sprite.Sprite):
    def __init__(self, sprite, coord):
        super().__init__()
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
        self.rect.x, self.rect.y = coord
    def draw(self):
        screen.blit(self.sprite, (self.rect.x, self.rect.y))


####CALCULATOR / SCREEN CLASS####
        
class Screen():
    def __init__(self, coord):
        self.x, self.y = coord
        self.x1, self.y1 = coord
        self.key = ' '
        self.disp_list = []
        self.dispval = 0
        self.key = ' '
        self.num = ' '
        self.int1 = 0
        self.dumpval = ''
        self.dump1 = 0
        self.op = ''
        self.calc_list = []
    
        
    def send(self, key):
        self.key = str(key)
        
        if self.key == '1'  or self.key == '2' or self.key == '3' or self.key == '4' or self.key == '5' or self.key == '6' or self.key == '7' or self.key == '8' or self.key == '9' or self.key == '0' or self.key == '.' or self.key == '-':
            self.dispval = 0
            self.disp_list.append(self.key)

        else:
            for digit in self.disp_list:
                self.num = self.num + digit
            try:
                self.calc_list.append(float(self.num))
            except ValueError:
                self.disp_list = ["Err"]
                
            print (self.disp_list, self.num)
            print (self.calc_list)

            self.disp_list = []
            self.num = ' '

            if len(self.calc_list) >= 2 and self.op == 'add':
                self.disp_list = []
                self.int1 = float(self.calc_list[0]) + float(self.calc_list[1])

                self.calc_list = [self.int1]
                
                self.dispval = 1

            if len(self.calc_list) >= 2 and self.op == 'subtract':
                self.disp_list = []
                self.int1 = float(self.calc_list[0]) - float(self.calc_list[1])

                self.calc_list = [self.int1]
                
                self.dispval = 1

            if len(self.calc_list) >= 2 and self.op == 'multiply':
                self.disp_list = []
                self.int1 = float(self.calc_list[0]) * float(self.calc_list[1])

                self.calc_list = [self.int1]
                
                self.dispval = 1

            if len(self.calc_list) >= 2 and self.op == 'divide':
                self.disp_list = []
                self.int1 = float(self.calc_list[0])/float(self.calc_list[1])

                self.calc_list = [self.int1]
                
                self.dispval = 1

            if self.key == 'plus':
                self.op = 'add'

            if self.key == 'minus':
                self.op = 'subtract'

            if self.key == 'mult':
                self.op = 'multiply'

            if self.key == 'div':
                self.op = 'divide'

        if self.key == 'eq':
            self.disp_list = []
            self.calc_list = []
            for digit in str(self.int1):
                self.disp_list.append(digit)
                self.dispval = 0
    
        

    def draw(self):
        if self.dispval == 0:
            for i in range(0,15):
                self.x = i*10
                label = font.render(str(self.disp_list[i]), 1, BLACK)
                screen.blit(label, (self.x + 10, self.y))
                
        elif self.dispval == 1:
            label = font.render(str(self.calc_list[0]), 1, BLACK)
            screen.blit(label, (self.x1 + 10, self.y1))


            
        
pygame.init()


####LABEL SETUP####
font = pygame.font.SysFont("monospace", 15)

ONE = font.render("1", 1, BLACK)
TWO = font.render("2", 1, BLACK)
THREE = font.render("3", 1, BLACK)
FOUR = font.render("4", 1, BLACK)
FIVE = font.render("5", 1, BLACK)
SIX = font.render("6", 1, BLACK)
SEVEN = font.render("7", 1, BLACK)
EIGHT = font.render("8", 1, BLACK)
NINE =  font.render("9", 1, BLACK)
ZERO = font.render("0", 1, BLACK)

PLUS = font.render("+", 1, BLACK)
MINUS = font.render("-", 1, BLACK)
DIVIDE = font.render("/", 1, BLACK)
MULTIPLY = font.render("*", 1, BLACK)
EQUAL = font.render("=", 1, BLACK)
DECIMAL = font.render(".", 1, BLACK)

NEG = font.render("(-)", 1, BLACK)
CLEAR = font.render("CE", 1, BLACK)

####BUTTON SETUP####
button1 = Button('Button.png', (10, 50))
button2 = Button('Button.png', (60, 50))
button3 = Button('Button.png', (110, 50))
button4 = Button('Button.png', (10, 110))
button5 = Button('Button.png', (60, 110))
button6 = Button('Button.png', (110, 110))
button7 = Button('Button.png', (10, 170))
button8 = Button('Button.png', (60, 170))
button9 = Button('Button.png', (110, 170))
button0 = Button('Button.png', (10, 230))

button_plus = Button('Button.png', (160, 50))
button_minus = Button('Button.png', (160, 110))
button_div = Button('Button.png', (160, 170))
button_mult = Button('Button.png', (160, 230))
button_neg = Button('Button.png', (110, 230))
button_dec = Button('Button.png', (60,230))

button_eq = Button('Big Button.png', (110,290))
button_clr = Button('Big Button.png', (10,290))

####MOUSE SETUP####

mouse1 = Cursor('curser2.png', (50,50))

####CALCULATOR AND DISPLAY INITIALIZATION####

display = Screen((0,10))

####MAIN LOOP####

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mouse1.rect.x, mouse1.rect.y= event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_val = 1

        else:
            click_val = 0


        screen.fill((WHITE))

    

        if clr_val == 1:
            display.key = ''
            display.disp_list = []
            display.dispval = 0
            display.key = ''
            display.num = ''
            display.int1 = 0
            display.dumpval = ''
            display.dump1 = 0
            display.op = ''
            display.calc_list = []
            clr_val = 0
        
        button1.draw()
        button1.collide_check()
        button1.buttonclick(click_val)

        button2.draw()
        button2.collide_check()
        button2.buttonclick(click_val)

        button3.draw()
        button3.collide_check()
        button3.buttonclick(click_val)

        button4.draw()
        button4.collide_check()
        button4.buttonclick(click_val)

        button5.draw()
        button5.collide_check()
        button5.buttonclick(click_val)

        button6.draw()
        button6.collide_check()
        button6.buttonclick(click_val)

        button7.draw()
        button7.collide_check()
        button7.buttonclick(click_val)

        button8.draw()
        button8.collide_check()
        button8.buttonclick(click_val)

        button9.draw()
        button9.collide_check()
        button9.buttonclick(click_val)

        button0.draw()
        button0.collide_check()
        button0.buttonclick(click_val)

        button_plus.draw()
        button_plus.collide_check()
        button_plus.buttonclick(click_val)

        button_minus.draw()
        button_minus.collide_check()
        button_minus.buttonclick(click_val)

        button_div.draw()
        button_div.collide_check()
        button_div.buttonclick(click_val)

        button_mult.draw()
        button_mult.collide_check()
        button_mult.buttonclick(click_val)

        button_eq.draw()
        button_eq.collide_check()
        button_eq.buttonclick(click_val)

        button_dec.draw()
        button_dec.collide_check()
        button_dec.buttonclick(click_val)

        button_neg.draw()
        button_neg.collide_check()
        button_neg.buttonclick(click_val)

        button_clr.draw()
        button_clr.collide_check()
        button_clr.buttonclick(click_val)

        

        if button1.button_val == 1:
            display.send(1)
            
        elif button2.button_val == 1:
            display.send(2)
            
        elif button3.button_val == 1:
            display.send(3)

        elif button4.button_val == 1:
            display.send(4)

        elif button5.button_val == 1:
            display.send(5)

        elif button6.button_val == 1:
            display.send(6)
            
        elif button7.button_val == 1:
            display.send(7)

        elif button8.button_val == 1:
            display.send(8)

        elif button9.button_val == 1:
            display.send(9)

        elif button0.button_val == 1:
            display.send(0)

        elif button_plus.button_val == 1:
            display.send('plus')
            
        elif button_minus.button_val == 1:
            display.send('minus')
      
        elif button_div.button_val == 1:
            display.send('div')
    
        elif button_mult.button_val == 1:
            display.send('mult')
  
        elif button_eq.button_val == 1:
            display.send('eq')

        elif button_dec.button_val == 1:
            display.send('.')

        elif button_neg.button_val == 1:
            display.send('-')

        elif button_clr.button_val == 1:
            clr_val = 1

        
    
        
        try:
            display.draw()

        except IndexError:
            n = 1
            
        mouse1.draw()
            

    screen.blit(ONE, (25, 65))
    screen.blit(TWO, (75, 65))
    screen.blit(THREE, (125, 65))
    screen.blit(FOUR, (25, 125))
    screen.blit(FIVE, (75, 125))
    screen.blit(SIX, (125, 125))
    screen.blit(SEVEN, (25, 185))
    screen.blit(EIGHT, (75, 185))
    screen.blit(NINE, (125, 185))
    screen.blit(ZERO, (25, 245))

    screen.blit(PLUS, (175, 65))
    screen.blit(MINUS, (175, 125))
    screen.blit(DIVIDE, (175, 185))
    screen.blit(MULTIPLY, (175, 245))
    screen.blit(DECIMAL, (75, 245))
    screen.blit(NEG, (116, 245))
    
    screen.blit(EQUAL, (150, 305))
    screen.blit(CLEAR, (45, 305))

        
    pygame.display.flip()
