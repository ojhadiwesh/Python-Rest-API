number1= {1,2,3,4,5}
numner2 = {2,4,66,7}
#print(number1.intersection(numner2))


def samples():
    print('This is the what the user wants')
    user_input =input('SHould we print again? (y/n)')
    if user_input=='y':
        print('This is what the user wants again')
    else :
        print('Lets go home now')


numbers = [1,2,3,4,5,6,7,8,9]
def flow_control(): # this shall print only the even number from the dictionary above
    evens= []
    for number in numbers:
        if number%2 ==0:
            evens.append(number)

    return evens
flow_control()
#choice = input('press q if you want to quit or a if not: ')
def user_choice(choice):
    if choice =='q':
        output = 'Quit'
        return output
    elif choice =='a':
        output ='Go on'
        return output

def do_you_know_them():
    people = input('Enter the names of people you know seperated by commas :')
    people_list = people.split(',')
    individuals= []
    for person in people_list:
        individuals.append(person.strip())
    return individuals

def you_know():
    someone = input('Type the name of the person you know :')
    if someone in do_you_know_them():
        print(' You know {}!'.format(someone))


student ={'name': 'jose', 'school': 'Computing', 'grades': [66,77,88]}

def average_grade(data):
    grades = data['grades']
    return sum(grades)/len(grades)



lottery_player_dict= {
        'name': 'Diwesh',
        'numbers': (5,9,12,13,1,21)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5,6,7,8,9)

    def total(self):
        return sum(self.numbers)

player_one= LotteryPlayer('Rofl')
player_one.numbers = (1,2,3,4,5)
player_two = LotteryPlayer('John')
#print(player_one.numbers == player_two.numbers)

class Store:
    def __init__(self, name, items):
        self.name= name
        self.items =[]
    def add_item(self, name, price):
        item = {
            'name':name,
            'price': price
        }
        self.items.append(item)

    def stock_price(self):

        total =sum(item['price'] for item in self.items)
        return total

    @classmethod
    def franchise(cls, store):
        return cls(store.name + "-franchise")

    @staticmethod
    def store_details(store):
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school= school
        self.marks = []
    def average(self):
        return sum(self.marks)/len(self.marks)
    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs)


#print(friend.name)
#print(friend.school)

class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


anna = WorkingStudent('Anna', 'Oxford', 23, 'Developer')
#print(anna.salary)
#print(friend.name)


friend = WorkingStudent.friend(anna, 'Greg', 25, job_title = 'Chef')
#print(friend.name)
#print(friend.salary)

#def addition_simplified (*args):
#    return sum(args)
#print(addition_simplified(3,4,5,6,7))

### Passing functions as parameters

def methodception(another):
    return another()

def add_two_nums():
    return 35 +77
#print(methodception(lambda : 35+77))

my_list = [12,14,14,345,5]

#print(list(filter(lambda x: x!= 12, my_list)))

import functools
def my_decorators(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print('in the decorator!')
        func()
        print('after the decorators')

    return function_that_runs_func
@my_decorators
def my_function():
    print('Im the functions')

def decorators_with_agruments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print('in the decorator!')
            if number ==54:
                print('not some number')
            func(*args, **kwargs)
            print('after the decorators')
        return function_that_runs_func
    return my_decorator


@decorators_with_agruments(56)
def my_function_too(x,y):
    print(x+y)
#my_function_too(56,53)
