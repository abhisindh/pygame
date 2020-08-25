import pygame
r=True
q=True
k=0
m=0
X=[]
O=[]
entered=[]
pygame.init()
backc=(250,150,10)
rectc=(0,100,100)
circ=(100,200,0)
croc=(200,0,100)

#functions
def cir():
	pygame.draw.circle(screen,(0,0,0),(mx+20,my+20),100,50)
	pygame.draw.circle(screen,circ,(mx,my),100,50)
	
def cross():
	pygame.draw.line(screen,(0,0,0),(mx-30,my-30),(mx+70,my+70),50)
	pygame.draw.line(screen,(0,0,0),(mx-30,my+70),(mx+70,my-30),50)
	pygame.draw.line(screen,croc,(mx-50,my-50),(mx+50,my+50),50)
	pygame.draw.line(screen,croc,(mx-50,my+50),(mx+50,my-50),50)
	
def posx(x):
	if 100<x<400:
		return(250)
	if 400<x<700:
		return(550)
	if 700<x<1000:
		return(850)
def posy(y):
	if 600<y<900:
		return(750)
	if 900<y<1200:
		return(1050)
	if 1200<y<1500:
		return(1350)

def rect(k):
	global n
	global o
	n=100+300*k
	o=600+300*m
	pygame.draw.rect(screen,rectc,(n,o,290,290))
def rects(k):
	global n
	global o
	n=130+300*k
	o=630+300*m
	pygame.draw.rect(screen,(0,0,0),(n,o,290,290))

def num(x,y):
	list1=[(250,750),(250,1050),(250,1350),(550,750),(550,1050),(550,1350),(850,750),(850,1050),(850,1350)]
	list2=['1','2','3','4','5','6','7','8','9']
	if (x,y) in list1:
		return(list2[list1.index((x,y))])
	else:
		return(10)
	
def win():
	if ('1' in O and '2' in O and '3' in O) or ('4' in O and '5' in O and '6' in O) or ('7' in O and '8' in O and '9' in O) or ('2' in O and '5' in O and '8' in O) or ('3' in O and '6' in O and '9' in O) or ('1' in O and '4' in O and '7' in O) or ('1' in O and '5' in O and '9' in O) or ('3' in O and '5' in O and '7' in O):
		return(2)
	elif ('1' in X and '2' in X and '3' in X) or ('4' in X and '5' in X and '6' in X) or ('7' in X and '8' in X and '9' in X) or ('2' in X and '5' in X and '8' in X) or ('3' in X and '6' in X and '9' in X) or ('1' in X and '4' in X and '7' in X) or ('1' in X and '5' in X and '9' in X) or ('3' in X and '5' in X and '7' in X):
		return(1)
	
#edit screen
screen=pygame.display.set_mode((300,100))
screen.fill(backc)
font=pygame.font.SysFont(None,200)
img=font.render('TIC-TAC-TOE',True,(0,0,0))
screen.blit(img,(110,210))
img=font.render('TIC-TAC-TOE',True,(100,200,30))
screen.blit(img,(100,200))
while q:
	rects(k)
	rect(k)
	pygame.display.flip()
	k=k+1
	if k==3 and m==2:
		q=False
	elif k==3:
		k=0
		m=m+1
k=0
m=0
q=True


#edit input
while r:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			r=False
		elif ev.type==pygame.MOUSEBUTTONDOWN:
			(mx,my)=pygame.mouse.get_pos()
			mx=posx(mx)
			my=posy(my)
			
		
			if k>7:
				screen.fill(backc)
				font=pygame.font.SysFont(None,500)
				img=font.render('TIE',True,rectc)
				screen.blit(img,(200,850))	
			
			elif k%2==1 and num(mx,my) not in entered and num(mx,my)!=10:
				X.insert(1,num(mx,my))
				cir()
				k=k+1
			elif k%2==0 and num(mx,my) not in entered and num(mx,my)!=10:
				O.insert(1,num(mx,my))
				cross()
				k=k+1
			entered.insert(1,num(mx,my))
			#if O won
			if win()==1:
				screen.fill(backc)
				font = pygame.font.SysFont(None, 500)
				img = font.render('O won', True,(0,0,0))
				screen.blit(img, (30, 870))
				img = font.render('O won', True,circ)
				screen.blit(img, (10, 850))
			#if X won
			elif win()==2:
				screen.fill(backc)
				font = pygame.font.SysFont(None,500)
				img = font.render('X won', True,(0,0,0))
				screen.blit(img, (80, 870))
				img = font.render('X won', True,croc)
				screen.blit(img, (50, 850))
				
					
			pygame.display.flip()
		
				

			


			