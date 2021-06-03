class fraction:
	def __init__(self, num=0, den=1):
		if den==0:
			# throw error
			den=1

		self.num=num
		self.den=den
	def print_fraction(self):
		if self.num==0:
			print(0)
		elif self.den==1:
			print(self.num)
		else:
			print(self.num,end='')
			print("/",end='')
			print(self.den)

	def simplify(self):
		if self.num==0:
			return
		current=min(self.num,self.den)
		while current>0:
			if self.num%current==0 and self.den%current==0:
				break
			current-=1
		self.num=self.num//current
		self.den=self.den//current

	def add_fraction(self,otherfraction):
		self.num=self.num*otherfraction.den+self.den*otherfraction.num
		self.den=self.den*otherfraction.den
		self.simplify()
		self.print_fraction()		

	def multipy_fraction(self,otherfraction):
		self.num=self.num*otherfraction.num
		self.den=self.den*otherfraction.den
		self.simplify()
		self.print_fraction()

	@staticmethod
	def hello():
		print("Hello!")


print("Enter fraction in form of a/b: " ,end='')
n,m= map(int,input().split("/"))
a=fraction(n,m)
a.hello()
print("If you want to add or multiply this fraction with other fraction press \"Y\": ",end='')
X=input()
if X=="Y":
	print("Enter other fraction in form of a/b: ",end='')
	x,y=map(int,input().split("/"))
	b=fraction(x,y)

	print("Enter what you what to do with this fractions press \"m\" for multiply, \"a\" for add: ",end='')
	X=input()
	if X=="a":
		a.add_fraction(b)
	if X=="m":
		a.multipy_fraction(b)
else:
	print("Want to simplify the fraction press \"s\": ",end='')
	X=input()
	if X=='s':
		a.simplify()
		a.print_fraction()