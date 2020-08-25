import pygame
pygame.init()
run=True
font=pygame.font.SysFont(None,100)
q=[[],['0','3','4','5','9','1','7','6','2','8'],['0','6','1','2','8','5','4','9','7','3'],['0','9','8','7','6','2','3','1','4','5'],['0','7','5','4','1','9','6','3','8','2'],['0','8','9','3','4','7','2','5','1','6'],['0','2','6','1','5','3','8','7','9','4'],['0','5','3','8','7','4','1','2','6','9'],['0','4','7','9','2','6','5','8','3','1'],['0','1','2','6','3','8','9','4','5','7']]
ans=[[],['0','_','_','_','_','_','_','_','_','_'],['0','_','_','_','_','_','_','_','_','_'],['0','_','_','_','_','_','_','_','_','_'],['0','_','_','_','_','_','_','_','_','_'],['0','_','_','_','_','_','_','_','_','_'],['0','_','_','_','_','_','_','_','_','_'],['0','_','_','_','_','_','_','_','_','_'],['0','_','_','_','_','_','_','_','_','_'],['0','_','_','_','_','_','_','_','_','_']]
giv=[3,1,5,1,7,1,2,2,9,2,1,3,4,3,5,3,7,3,9,3,1,4,3,4,6,4,9,4,2,5,5,5,2,6,6,6,7,6,9,6,3,7,4,7,9,7,3,8,6,8,7,8,1,9,2,9,5,9,8,9]

#functions
def grid():
	screen.fill((20,100,110))
	for l in range(3):
		for k in range(3):
			for i in range(3):
				for j in range(3):
					x=100+100*i+310*k
					y=500+100*j+310*l
					pygame.draw.rect(screen,(20,200,100),(x,y,90,90))
	for i in range(0,(len(giv)),2):
		que(giv[i],giv[i+1])
	pygame.display.flip()
	
	
def num_pad():
	font=pygame.font.SysFont(None,200)
	global num
	num=[['1','2','3'],['4','5','6'],['7','8','9'],[' ']]
	for i in range(3):
		for j in range(3):
			x=300+200*i
			y=1500+200*j
			pygame.draw.rect(screen,(50,10,100),(x,y,190,190))
			img=font.render(num[j][i],True,(200,150,50))
			screen.blit(img,(50+x,50+y))
			pygame.display.flip()
			
def que(x,y):
	mx=102*x
	my=102*y+400
	pygame.draw.rect(screen,(20,200,100),(mx,my,90,90))
	img=font.render(q[x][y],True,(250,250,250))
	screen.blit(img,(mx,my))
	pygame.display.flip()
	
def change(x,y):
	mx=100*x+30
	my=100*y+430
	if x<=3 and y<=2:
		img=font.render(num[x][y],True,(0,250,250))
		screen.blit(img,(r,s))
	pygame.display.flip()


def print():
	mx=(posx(x)*100)+30
	my=(posy(y)*100)+430
	img=font.render(q[posx(x)][posy(y)],True,(250,250,250))
	screen.blit(img,(mx,my))
	pygame.display.flip()
	
def posx(x):
	for i in range(9):
		if (100+100*i)<x<(100+100*(i+1)):
			return(i+1)
	else:
		return(10)
def posy(y):
	for i in range(9):
		if (500+100*i)<y<(500+100*(i+1)):
			return(i+1)
	else:
		return(10)
def ponx(x):
	for i in range(3):
		if (300+200*i)<x<(300+200*(i+1)):
			return(i)
	else:
		return(10)
def pony(y):
	for i in range(3):
		if (1500+200*i)<y<(1500+200*(i+1)):
			return(i)
	else:
		return(10)

		





#screen
screen=pygame.display.set_mode((1,2))


grid()
num_pad()






#input
k=0
while run:
	for e in pygame.event.get():
		if e.type==pygame.QUIT:
			run=False
		elif e.type==pygame.MOUSEBUTTONDOWN:
			(x,y)=pygame.mouse.get_pos()
			if k%2==0 and posx(x)!=10 and posy(y)!=10:
				
				wer=posx(x)
				war=posy(y)
				r=int((posx(x)*100)+30)
				s=int((posy(y)*100)+430)
				leng=r-30+(2*posx(x))
				bread=s-30+(3*posy(y))
		
				k+=1
			elif k%2==1 and ponx(x)!=10 and pony(y)!=10:
				pygame.draw.rect(screen,(0,0,100),(leng,bread,90,90))
				zr=num[pony(y)][ponx(x)]
				ans[wer][war]=zr
				change(pony(y),ponx(x))
				for i in range(0,(len(giv)-1),2):
					que(giv[i],giv[i+1])
				for i in range(0,(len(giv)-1),2):
					ans[giv[i]][giv[i+1]]=q[giv[i]][giv[i+1]]
			
				k+=1
				pygame.display.flip()
				if q[wer][war]!=num[pony(y)][ponx(x)]:
					pygame.draw.rect(screen,(0,0,0),(100,50,100,100))
					pygame.display.flip()
				else:
					pygame.draw.rect(screen,(250,250,250),(100,50,100,100))
					pygame.display.flip()
				if q==ans:
					screen.fill((250,250,250))
					font=pygame.font.SysFont(None,300)
					img=font.render('YOU WON',True,(50,200,100))
					screen.blit(img,(10,500))
					pygame.display.flip()
		
		