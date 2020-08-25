import pygame
pygame.init()
run=True
equip=[]
font=pygame.font.SysFont(None,100)
S=[]
O=[]
add=0


#functions
def bg():
	global screen
	screen=pygame.display.set_mode((1,2))
	screen.fill((255,255,255))
def grid():
	for i in range(9):
		for j in range(12):
			w=100+100*i
			h=600+100*j
			pygame.draw.rect(screen,(0,0,0),(w,h,90,90))
def posx(x):
	for i in range(9):
		if 100+100*i<x<100+100*(i+1):
			return(100+100*i)
	else:
		return(1)
def posy(y):
	for i in range(17):
		if 600+100*i<y<600+100*(i+1):
			return(600+100*i)
	else:
		return(1)
def ponx(x):
		for i in range(1,4):
			if (160*i)-20<x<(160*(i+1)-20):
			
				return((160*i)-10)
		else:
				return(10)
def pony(y):
				if 190<y<330:
					return(190)
				else:
					return(10)
def gin(q,r):
	if (q,r) in O:
		if ((q+100,r-100) in S and (q-100,r+100) in S) or ((q+100,r+100) in S and (q-100,r-100) in S) or ((q,r-100) in S and (q,r+100) in S) or ((q-100,r) in S and (q+100,r) in S):
			return(1)
		else:
			return(0)
	elif (q,r) in S:
		 if ((q+100,r+100) in O and (q+200,r+200) in S) or ((q-100,r-100) in O and (q-200,r-200) in S) or ((q+100,r) in O and (q+200,r) in S) or ((q-100,r) in O and (q-200,r) in S) or ((q,r+100) in O and (q,r+200) in S) or ((q,r-100) in O and (q,r-200) in S) or ((q+100,r-100) in O and (q+200,r-200) in S) or ((q-100,r+100) in O and (q-200,r+200) in S):
		 	return(1)
		 else:
		 	return(0)

		




def win():
	global add
	if (q,r) in O:
		if (q+100,r-100) in S and (q-100,r+100) in S:
			pygame.draw.line(screen,(250,0,0),(q+200,r-100),(q-90,r+190),10)
			add+=1
		if (q+100,r+100) in S and (q-100,r-100) in S:
			pygame.draw.line(screen,(250,0,0),(q-100,r-100),(q+190,r+190),10)
			add+=1
		if (q,r-100) in S and (q,r+100) in S:
			pygame.draw.line(screen,(250,0,0),(q+50,r-100),(q+50,r+190),10)
			add+=1
		if (q-100,r) in S and (q+100,r) in S:
			pygame.draw.line(screen,(250,0,0),(q-100,r+50),(q+190,r+50),10)
			add+=1
	if (q,r) in S:
			if (q+100,r+100) in O and (q+200,r+200) in S:
				pygame.draw.line(screen,(250,0,0),(q,r),(q+290,r+290),10)
				add+=1
			if (q-100,r-100) in O and (q-200,r-200) in S:
				pygame.draw.line(screen,(250,0,0),(q+90,r+90),(q-200,r-200),10)
				add+=1
			if (q+100,r) in O and (q+200,r) in S:
				pygame.draw.line(screen,(250,0,0),(q,r+50),(q+290,r+50),10)
				add+=1
			if (q-100,r) in O and (q-200,r) in S:
				pygame.draw.line(screen,(250,0,0),(q-200,r+50),(q+100,r+50),10)
				add+=1
			if (q,r+100) in O and (q,r+200) in S:
				pygame.draw.line(screen,(250,0,0),(q+50,r),(q+50,r+300),10)
				add+=1
			if (q,r-100) in O and (q,r-200) in S:
				pygame.draw.line(screen,(250,0,0),(q+50,r+100),(q+50,r-200),10)
				add+=1
			if (q+100,r-100) in O and (q+200,r-200) in S:
				pygame.draw.line(screen,(250,0,0),(q,r+100),(q+290,r-200),10)
				add+=1
			if (q-100,r+100) in O and (q-200,r+200) in S:
				pygame.draw.line(screen,(250,0,0),(q+100,r),(q-200,r+300),10)
				add+=1
			else:
				return(0)
			
def score():
				pygame.draw.rect(screen,(0,0,0),(0,1800,2000,1000))
				score=font.render('player 1                player 2',True,(250,250,250))
				screen.blit(score,(100,1900))
				pla=font.render(str(plya),True,(250,250,250))
				screen.blit(pla,(200,2000))
				plb=font.render(str(plyb),True,(250,250,250))
				screen.blit(plb,(800,2000))
				
		
	
	
def select():
	pygame.draw.rect(screen,(250,0,0),			(ponx(mx),pony(my),140,140))
def play():
	pygame.draw.rect(screen,color,(q,r,90,90))
	img=font.render(a,True,(100,100,100))
	screen.blit(img,(q+20,r+10))

def sos():
	font=pygame.font.SysFont(None,200)
	img=font.render('S O S',True,(0,0,0))
	for i in range(1,4):
		pygame.draw.rect(screen,(250,0,250),((160*i)-10,190,140,140))
	screen.blit(img,(200,200))




#screen
bg()
grid()
sos()
pygame.display.flip()

k=0
plya=0
plyb=0
#input
while run:
	for e in pygame.event.get():
		if e.type==pygame.QUIT:
			run=False
		elif e.type==pygame.MOUSEBUTTONDOWN:
			(mx,my)=pygame.mouse.get_pos()
			q=int(posx(mx))
			r=int(posy(my))
			
			if k%2==0 and ponx(mx)!=10 and pony(my)!=10:
				select()
				k+=1
				m=ponx(mx)
				n=pony(mx)
				if ponx(mx)==310:
					color=(0,250,0)
					a='O'
				else:
					color=(0,0,250)
					a='S'
			elif k%4==1 and (q,r) not in equip and q!=1 and r!=1:
				play()
				equip.insert(1,(q,r))
				k+=1
				if m==310:
					O.insert(1,(q,r))
				else:
					S.insert(1,(q,r))
				win()
				if gin(q,r)==1:
					plya+=add
					k+=2
				score()
				pygame.display.update()
				sos()
			elif k%4==3 and (q,r) not in equip and q!=1 and r!=1:
				play()
				k+=1
				equip.insert(1,(q,r))
				if m==310:
					O.insert(1,(q,r))
				else:
					S.insert(1,(q,r))
				win()
				if gin(q,r)==1:
					plyb+=add
					k+=2
				score()
				pygame.display.update()
				sos()
			if len(equip)==108:
				screen.fill((0,0,0))
				font=pygame.font.SysFont(None,150)
				if plya>plyb:
					img=font.render('PLAYER 1 WON',True,(250,250,250))
					screen.blit(img,(100,200))
				elif plya<plyb:
					img=font.render('PLAYER 2 WON',True,(250,250,250))
					screen.blit(img,(100,200))
				elif plya==plyb:
					img=font.render('TIE',True,(250,250,250))
					screen.blit(img,(100,200))
					
	
			pygame.display.flip()
			add=0