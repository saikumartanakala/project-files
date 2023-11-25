import sys
def solve(N ,A):


    N = int(input())
    l = []
for  i in range(l):
	l.append(int(input()))
b = []
l.reverse()

for i in range(len(l)):
	if (l[i]>0):
		b.append(l[i])
for i in range(len(l)):
	if (l[i]<0):
		b.remove(l[i+1])
print(sum(b))
def main():
	N = int (sys.stdin.readline().strip())
	A=[]
	for i in range(N):
		A.append(int(sys.stdin.readline().strip()))
	result = solve(N,A)
	print(result)

if _name_ =="_main_":
	main()