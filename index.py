print("Question 1 start")
count=1
def func():
    global count
    for i in (1,2,3):
        count+=1
func()
print(count)
print("Question 1 start")
print("Question 2 start")
st=[1,2,3]
st1=[[x for x in [st]] for x in range(3)]
print(st1)
print("Question 2 end")
print("Question 3 start")
t1=(1)
t2=(1,2)
t1+=1
print(t1)
print(t1+t2)
print("Question 3 end")
print("Question 4 start")
ist=[True,1,2]
ist.insert(2,3)
print(ist,sum(ist))
print("Question 4 end")
print("Question 5 start")
ist=[3,1,2,4]
tpl=(1.0,2,3,4.0)
ist.sort()
count=0
for x in tpl:
    ist[count]+=x
    count+=1
    break
print(ist)
print("Question 5 end")
print("Question 6 start")
def func():
    try:
        print(1)
    except:
        print(2)
    else:
        print(3)
        return
        print(4)
    finally:
        print(5)
func()
print("Question 2 end")
print("Question 7 start")

def dec(f):
    def n(*args):
        return  '*' +str(f(*args))
    return n
@dec
def func(a,t):
    return a+a*t
print(func(10,0))
print("Question 7 end")
print("Question 8 start")

def func(i,x=[]):
    x.append(i)
    return x
for i in range(2):
    print(func(i))
print("Question 8 end")
print("Question 9 start")

class Parent:
    def __init__(self):
        self.x=0
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.y=1
b=Child()
print(b.x,b.y)
print("Question 9 end")
print("Question 10 start")
class Parent:
    def __init__(self,x=1):
        self._x=x
class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()

