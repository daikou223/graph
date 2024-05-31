mode = 0 #0なら近似直線を引く


import sys
sys.path.append('C:\\Users\\linha\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages')
import matplotlib.pyplot as plt
X = []
Y = []
D = open("data.txt","r")
d = D.readline().split()
print(d)
x_l,x_a,x_u,y_l,y_a,y_u = d
line = 0
while 1:
	try:
		x,y = map(float,D.readline().split())
		X.append(x)
		Y.append(y)
		line += 1
	except:
		break
XX = [X[i]**2 for i in range(line)]
YY = [Y[i]**2 for i in range(line)]
XY = [X[i]*Y[i] for i in range(line)]
a = (line*sum(XY)-sum(X)*sum(Y))/(line*sum(XX)-sum(X)**2)
b = (sum(Y)*sum(XX)-sum(X)*sum(XY))/(line*sum(XX)-sum(X)**2)
s = (1/(line-2)*sum(([(Y[i]-(a*X[i]+b))**2 for i in range(line)])))**0.5
sa = s*(line/(line*sum(XX)-(sum(X)**2)))**0.5
sb = s*(sum(XX)/(line*sum(XX)-(sum(X)**2)))**0.5
LX = [-(max(X)-min(X))*1.2+min(X),(max(X)-min(X))*1.2+max(X)]
LY = [a*LX[i]+b for i in range(2)]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.tick_params("both",direction = "in")
ax.set_xlabel(f'{x_l} ${x_a}$[{x_u}]')
ax.set_ylabel(f'{y_l} ${y_a}$[{y_u}]')
ax2 = ax.twiny()
ax3 = ax.twinx()
ax2.tick_params(labelsize=0,direction = "in")
ax3.tick_params(labelsize=0,direction = "in")
plt.xlim(-(max(X)-min(X))*0.1+min(X),(max(X)-min(X))*0.1+max(X))
plt.ylim(-(max(Y)-min(Y))*0.1+min(Y),(max(Y)-min(Y))*0.1+max(Y))
ax2.set_ylim(-(max(Y)-min(Y))*0.1+min(Y),(max(Y)-min(Y))*0.1+max(Y))
ax2.set_xlim(-(max(X)-min(X))*0.1+min(X),(max(X)-min(X))*0.1+max(X))
ax3.set_xlim(-(max(X)-min(X))*0.1+min(X),(max(X)-min(X))*0.1+max(X))
if mode == 0:
	ind = 0
	print(a,b,sa,sb)
	while abs(a) <= 1:
		a *= 10
		ind  -= 1
	while abs(a) >= 10:
		a /= 10
		ind  += 1
	if ind != 0:
		Ma = sa/(10**ind)
		Mb = sb/(10**ind)
		ka = 0
		kb = 0
		while not(10 <= Ma*10**ka < 100):
			ka += 1
		while not(10 <= Mb*10**kb < 100):
			kb += 1
		Ma = str(sa/(10**ind)*(10**ka)//1/(10**ka))
		Mb = str(sb/(10**ind)*(10**kb)//1/(10**kb))
		da = str(a*(10**ka)//1/(10**ka))
		db = str((b/(10**ind))*10**kb//1/(10**kb))
		plt.text(min(X), max(Y), f"${y_a}=(({da}\pm{Ma}){x_a}+({db}\pm{Mb}))10^{ {ind} }$")
	else:
		Ma = sa/(10**ind)
		Mb = sb/(10**ind)
		ka = 0
		kb = 0
		while not(10 <= Ma*10**ka < 100):
			ka += 1
		while not(10 <= Mb*10**kb < 100):
			kb += 1
		Ma = str(sa/(10**ind)*(10**ka)//1/(10**ka))
		Mb = str(sb/(10**ind)*(10**kb)//1/(10**kb))
		da = str(a*(10**ka)//1/(10**ka))
		db = str((b/(10**ind))*10**kb//1/(10**kb))
		plt.text(min(X), max(Y), f"${y_a}=({da}\pm{Ma}){x_a}+({db}\pm{Mb})$")
	plt.plot(LX,LY, label=' ', color='b', marker='')
plt.scatter(X,Y)
plt.show()