# lets review all Python things that I know :)
from collections import Counter

'''
class Point():
    def __init__(self, x = 0, y = 0):
        self.x =x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x ,y):
        self.x +=x
        self.y +=y
    def __add__(self, p):
        return Point(self.x + p.x , self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y)+")"  #this has to be a string value

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)


p5 = p1 + p2
p6 = p4 - p1
p7 = p2*p3
print(p5, p6, p7)

'''
class Cat():
    pelo = "suave"
    gaticos = []

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.gaticos.append(self)

    def talk(self):
        print("my name is " + self.name + " i am "+ str(self.age) + " year old and i am  "+self.color)

    def probando(self):
        return Cat("Fernando", "10000", "AZULLLL")

    def test(self, gato):
        return  gato.color
    @classmethod
    def num_cats(cls):
        return(len(cls.gaticos))

    @classmethod
    def clasemetodo(cls):
        Cat.num_cats()
        chica = Cat("Chica", 2,"Gris")
        chica.talk()
        print("puedo printear el color de un gato: ", chica.color)
    @staticmethod
    def printea_algo():
        print("this is a static method")


print(Cat.gaticos)
print(Cat.num_cats())

Luis = Cat("Luis", 20, "black")
Fernando = Cat("Fernando", 30, "yellow")

print("El numero de objeto gatos que he creado es", len(Cat.gaticos))
print("los gatos creados son")
for cadaelementodelarraygato in Cat.gaticos:
    print(cadaelementodelarraygato.name)


Cat.printea_algo()
Cat.clasemetodo()


'''

milista = [1,2,3,4,5,6,7,8,9,10]
milista2 = [100,200,300,400,500,600]
def functiontomap(x, y):
    return x+y
print(list(map(functiontomap, milista, milista2)))


verdaderos = [1,2,3,4,5,6,7,8,9,10]
def add100(x):
    return x+100

def isOdd(x):
    return x%2 != 0

print(list(filter(isOdd, verdaderos)))
a = list(filter(isOdd, verdaderos))
print(list(map(add100,a)))


funct2 = lambda x, y=100000: x+100 +y

print("the lambda function is: ", funct2(5,1))

a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: x+100, a)))
print(list(filter(lambda x: x%2==0, a)))

mic1 = Counter("probannndo")
mic2 = Counter(['a', 'a' , 'c','c', 'c', 'b'])
mic3 = Counter({'a':1 , "b":3, "c":2, "d":1})
mic4 = Counter( cats = 4, dogs =3
                )
print(mic1)
print(mic2)
print(mic3)
print(mic4)
print(mic1['n']) #me dice el numero de veces que aparece un elemento
print(list(mic4.elements())) #devuelve una lista con los elementos del count
print(mic1.most_common()) #devuelve una tuple
d = mic2 - mic3
mic2.subtract(mic3) #it subtract the list inside without the element with 0.
print(mic2)
print("this is restando: " , d)

dd = mic2+mic3 #It wont show element with 0 counters
mic2.update(mic3) # the opposite of .subtract it add the list
print(mic2)
print("this is sumando: " ,dd)

mic2.clear() #remove all the counters
print(mic2)


count1 = Counter(a=4, b=2, c=0, d=-2)
count2 = Counter(["a", "b", "c", "c"])
print(count1 & count2) #min element of the intersection between the counters
print(count1 | count2) #max element on each of our counters

'''
print("metaclasessssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")

'''
class Test:
    pass
the class avobe is the same than:
Test = type('Test',(),{})
('NAME, (BASES what we inheritance from a super class or parent class), {atributes}) 
'''

class Homie:
    x = 5
    pass
t = Homie()

#1
#this will be an inheritance of Homie2
class Foo:
    def show(self):
        print("hi")

#2
#this is a method that i wanna add to my Homie2
def add_attribute(self):
    self.z =9

#0
#Homie2 = type('Homie2',(),{"x":5})
#1
#Homie2 = type('Homie2', (Foo,), {"x":5}) #Homie2 con inheritance of Foo,
#2
Homie2 = type('Homie2', (Foo,), {"x":5, "add_attribute":add_attribute}) #we add the atribute the method created above

t2 = Homie2()
t2.show() #1 #this print hi as described on the method show from Foo, becuase Homie2 inheritance from Foo
print("atributo de homie: ", t.x)
print("atributo de homie2: ", t2.x)#0
t2.add_attribute()  #2
print(t2.z) #2



class Meta(type): #metaclasses need to have type inside
    def __new__(self, class_name, bases, attrs): #__new__ is called before init

        a ={} #it will represent our new attributes
        for name, val in attrs.items(): #we will loop through our attributes
            if name.startswith("__"): #if our attribute starts with __
                a[name] = val #we add it to our list
            else:
                a[name.upper()] = val  #otherwise we change them to upper case
        print(a)
        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x = 5
    y = 8
    def hello(self):
        print("hi")

d = Dog()
print("hello? ", d.X)

print("DECTORATORSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSs")

def funk(f):
    def wrapper(*args, **kwargs):
        print("started")
        rv = f(*args, **kwargs)
        print("ended")
        return rv
    return wrapper

@funk  #### funk2 = funk(funk2)
def funk2():
    print("I am funky 2 ")

@funk #### funk3 = funk(funk3)
def funk3(x, y=10):
    print("Iam funky3 and i print ", x, "this is y ", y)


funk2()
x = funk3(25, 1000)
print(x)

#EJEMPLO DE DECORATORSS

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print("time: ", total)
        return rv

    return wrapper

@timer
def timer_test(): #esta funcion no hace nada simplemente hace un for muy grande y tarda un rato
    for _ in range(100000):
        pass

@timer
def timer_test2(): #esta funcion no hace nada solo 'congela' el programa durante 2 seguntos
    time.sleep(2)

timer_test()
timer_test2()