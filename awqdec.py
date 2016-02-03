#!/usr/bin/python
#With help of Colorama for the colors on Windows cmd.exe
# print grid of all colors and brightnesses
# uses stdout.write to write chars with no newline nor spaces between them
# This should run more-or-less identically on Windows and Unix.
from __future__ import print_function
import sys #for sys.stdout.write
import time
from colorama import init, Fore, Back, Style

init() #initialize colorama

# Fore, Back and Style are convenience classes for the constant ANSI strings that set
#     the foreground, background and style. The don't have any magic of their own.
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
#BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
#STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]
write = sys.stdout.write
import unicodedata
import codecs

def init_map():
	global coordinates_lookup
	global shifter,colorer,mover,speeder
	
	"""with codecs.open("config.txt",'r',encoding='utf8') as f:
		text = f.read()
	write(text)"""
	"""
	file=open("config.txt");
	s = file.read();
	print(sys.stdout.encoding)
	s=unicodedata.normalize('NFKD', s).encode(sys.stdout.encoding, 'replace').decode(sys.stdout.encoding)
	#sutf8 = s.encode(sys.stdout.encoding)
	print("*"*80+"&é'(§è!çà)\n\n")
	print(s)
	write(s)
	file.close()"""
	
	"""
	file=open('utf-8.out.txt', 'w')
	file.write(s)
	file.close()
	
	file=open("config.txt");"""
	file = codecs.open("config.txt",'r',encoding='utf8');
	data=file.readlines();
	data=[line.strip() for line in data];
	#print(data)
	file.close();
	default = data[data.index("default")+1]
	print("Using default keyboard map : ",default)
	print("4 lines mapping : ")
	key_index = data.index(default) +1;
	keylines = data[key_index:key_index+4]
	for line in keylines:
		print(line)
	
	shifter = data[data.index("shifter")+1]
	print("\nShift origin with : ",shifter)
	mover = data[data.index("mover")+1]
	#print("Start moving with : ",mover)
	colorer = data[data.index("color")+1]
	print("Change color with : ",colorer)
	speeder = data[data.index("speed")+1]
	print("Change speed with : ",speeder)
	#enter = data[data.index("enter")+1]
	#print("Shift with : ",shifter)
	#leave = data[data.index("leave")+1]
	#print("Shift with : ",shifter)
	
	coordinates_lookup = dict()
	for j in range(len(keylines)):
		for i in range(len(keylines[j])):
			#coordinates_lookup[(i,j)]=keylines[j][i];#
			#write(keylines[j][i])
			coordinates_lookup[keylines[j][i]]=(i,j);
			
	#print(coordinates_lookup)
	#return coordinates_lookup
	
def isInView(line,decal):
	point1=line[0]
	point2=line[1]
	return (0<=point1[0]-decal[0]<80 and 0<=point1[1]-decal[0]<25)\
	and (0<=point2[0]-decal[0]<80 and 0<=point2[1]-decal[0]<25)

def COORD(character):
	return coordinates_lookup[character];
	

def CGET(colorstring=""):
	lightness=Style.NORMAL;
	if(len(colorstring)<4):
		return Style.RESET_ALL;
	elif(" " in colorstring[:3]):
		return Style.RESET_ALL;
	elif(colorstring[-1] == " "):
		#lightness=Style.NORMAL;
		lightness = Style.BRIGHT;
	elif(COORD(colorstring[-1]) == (3,0)):
		lightness = Style.BRIGHT;
	elif(COORD(colorstring[-1]) == (3,1)):
		lightness = Style.DIM;
	
	color = (COORD(colorstring[0])== (0,0))+\
	(COORD(colorstring[1])== (1,0))*2+\
	(COORD(colorstring[2])== (2,0))*4;
	color=FORES[color]
	
	return lightness + color;

def sign(x):
	return (x > 0) - (x < 0)

def pos(x,y):
	return "\x1b["+str(y+1)+";"+str(x+1)+"H"
	
def printscreen(screen):
	write(pos(0,0));
	for j in range(len(screen[0])):
		for i in range(len(screen)):
			write(screen[i][j])
			#if(screen[i][j]):
		#		write(pos(i,j)+screen[i][j])
	write(pos(80,20))
		
def setscreen(lines,screen,origin,position):
	x0,y0=origin
	W = len(screen)
	H = len(screen[0])
	
	for i in range(len(screen)):
		screen[i]=[Fore.BLACK+Style.BRIGHT+"_"]*20
	for p1,p2,color in lines:
		x,y=p1
		xx,yy=p2
		if((x>=x0 and x<x0+W and y>=y0 and y<y0+H) or (xx>=x0 and xx<x0+W and yy>=y0 and yy<y0+H)):
			cx,cy = x,y
			if((cx>=x0 and cx<x0+W and cy>=y0 and cy<y0+H)):
				screen[cx-x0][cy-y0]= color + "X";
				
			if(abs(x-xx)>abs(y-yy)):
				mov=[sign(xx-x),0]
			else:
				mov=[0,sign(yy-y)]

			while (mov[0]!=0 and (cx!=xx)) or (mov[1]!=0 and (cy!=yy)):
				if(mov[0]!=0): #not 0 distance x
					cx+=mov[0]
					cy=y+int(round(  (cx-x)/(xx-x)*(yy-y) )) #can divide by difference
				if(mov[1]!=0): #not 0 distance y
					cy+=mov[1]
					cx=x+int(round(  (cy-y)/(yy-y)*(xx-x) )) #can divide by difference
					
				if((cx>=x0 and cx<x0+W and cy>=y0 and cy<y0+H)):
					screen[cx-x0][cy-y0] = color + "X";
	x,y=position
	if(x>=0 and x<0+W and y>=0 and y<0+H):
		screen[x][y]=Fore.GREEN+"0"
			
def add_up(p1,p2):
	return (p1[0]+p2[0],p1[1]+p2[1])
if(__name__=="__main__"):
	init_map();
	color = CGET("")
	space = True;
	delay = 0;
	lines = [];
	position = [0,0];
	origin = [0,0]
	screen = [[Fore.BLACK+Style.BRIGHT+"_"]*20 for i in range(80)];
	input_msg=input("Enter commands :")
	move=False;
	i=0;
	print(("\n"+" "*80)*25)
	printscreen(screen)
	while(i<len(input_msg)):
		print(Fore.GREEN+input_msg[:i]+Fore.RED+input_msg[i]+Fore.WHITE+input_msg[i+1:]+Style.RESET_ALL)
		l=input_msg[i];
		if(l is colorer): #\
			c=input_msg[i+1:i+5] #azer (\azer)
			color=CGET(c)
			print("Set color to ",color,"this")
			while(i+1<len(input_msg) and input_msg[i+1]!=" "):
				i+=1
		elif(l is speeder): #+
			c=input_msg[i+1]
			delay = 9-COORD(c)[0]
			i+=1
			print("Set delay to ",delay)
		elif(l is shifter): #>
			space=False;
			c=input_msg[i+1]
			decal = COORD(c)
			#print(position,"recentered on",c,decal)
			origin[0]=origin[0]+position[0]-decal[0]
			origin[1]=origin[1]+position[1]-decal[1]
			position[0]=decal[0]
			position[1]=decal[1]
			print("Changed origin :",origin," - Current position:",add_up(position,origin))
			i+=1
		elif(l is mover): #<
			move=True
			space=True
		elif(l in coordinates_lookup): #azerrty
			if space:
				space = False;
				position=list(COORD(l))
				print("Moved to ",add_up(position,origin))
			elif not move:
				p1 = list(position)
				p1[0]+=origin[0]
				p1[1]+=origin[1]
				position=list(COORD(l))
				p2 = list(position)
				p2[0]+=origin[0]
				p2[1]+=origin[1]
				lines.append([p1,p2,color])
				print("Drawed to ",p1,p2)
			else:
				decal = COORD(l)
				origin[0]+=decal[0]-position[0]
				origin[1]+=decal[1]-position[1]
				position[0]=decal[0]
				position[1]=decal[1]
				print("Origin moved to ",origin)
		elif(l is " "): #spacer
			space=True
		#print(origin)
		time.sleep(0.1*delay)
		#print("\n"*2)
		setscreen(lines,screen,origin,position)
		printscreen(screen)
		i+=1;
	
	print(pos(0,22)+"Finished")
	

		