def add_numbers_to_list(numbers: list):
    if len(numbers)% 5 != 0:
        numbers.append(numbers[-1]+1)
        print(len(numbers))
        add_numbers_to_list(numbers)

def recursive_sum(number:int):
    if number == 1:
        return number
    else:
        return number + recursive_sum(number-1)
    

class Node:
    """ The class represents a single node in a binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    greatest_value = root.value

    if root.left_child is not None:
        if greatest_node(root.left_child) > greatest_value:
            greatest_value =  greatest_node(root.left_child)
    
    if root.right_child is not None:
        if greatest_node(root.right_child) > greatest_value:
            greatest_value = greatest_node(root.right_child)

    return greatest_value


class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):
    count = 0
    if len(employee.subordinates) == 0:
        return 0
    count += len(employee.subordinates)
    for emp in employee.subordinates:
        count += count_subordinates(emp)
    return count
    

class Task():
    __running_id = 0
    def __init__(self, description: str, hoursreq: int, name:str):
        self.description = description
        self.hoursreq = int(hoursreq)
        self.name = name
        self.finished = False
        Task.__running_id = Task.__running_id +1
        self.__id = self.__running_id

    def __str__(self):
        return self.description, self.id, self.name, self.finished

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    @property
    def id(self):
        return self.__id

class OrderBook():

    def __init__(self):
        self.task_list = []

    def add_order(self, desc, name, hours):
        self.task_list.append(Task(desc, hours, name))

    def all_orders(self):
        return self.task_list
    
    def programmers(self):
        return list(set([task.name for task in self.task_list]))
    
    def mark_finished(self, id:int):
        for task in self.task_list:
            if task.id == id:
                task.mark_finished()
                return

        raise ValueError("No such id found")
    
    def status_of_programmer(self, programmer: str):
        finished_tasks = []
        unfinished_tasks = []
        for task in self.task_list:
            if task.name == programmer:
                if task.finished == False:
                    unfinished_tasks.append(task)
                elif task.finished == True:
                    finished_tasks.append(task)
        return (len(finished_tasks), len(unfinished_tasks), sum([task.hoursreq for task in finished_tasks]), sum([task.hoursreq for task in unfinished_tasks]))
    

class OrderBookApplication():
    def __init__(self):
        self.__order_book = OrderBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == '0':
                break
            if command == '1':
                desc = input("description: ")
                name = input("name: ")
                hours = input("hours: ")
                self.__order_book.add_order(desc, name, hours)

            elif command == '2':
                 print([task for task in self.__order_book.all_orders() if task.finished == True])
            
            elif command == '3':
                 print([task for task in self.__order_book.all_orders() if task.finished == False])
            elif command == '4':
                id_command = input("id: ")
                self.__order_book.mark_finished(id_command)

            elif command == '5':
                for prg in self.__order_book.programmers():
                    print(prg)

            elif command == '6':
                prg_command = input("programmer")
                self.__order_book.status_of_programmer(prg_command)


def sort_by_remaining_stock(items: list):

    def order_by_remaining_stock(item: tuple):
        return item[2]
    return sorted(items, key=order_by_remaining_stock)

def sort_by_seasons(items: list):
    def order_by_seasons(item:dict):
        return item['seasons']
    return sorted(items, key=order_by_seasons, reverse=True)



class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

def sort_by_length(li:list):
    def order_by_length(climb:ClimbingRoute):
        return climb.length
    return sorted(li,key=order_by_length, reverse=True)


def sort_by_difficulty(routes: list):
    def order_by_difficulty(route: ClimbingRoute):
        return route.grade
    return sorted(routes, key=order_by_difficulty, reverse=True)

class ClimbingArea:
    def __init__(self, name: str):
        self.name = name
        self.__routes = []

    def add_route(self, route: ClimbingRoute):
        self.__routes.append(route)

    def routes(self):
        return len(self.__routes)

    def hardest_route(self):
        def by_difficulty(route):
            return route.grade

        routes_in_order = sorted(self.__routes, key=by_difficulty)
        # last route
        return routes_in_order[-1]

    def __str__(self):
        hardest_route = self.hardest_route()
        return f"{self.name} {self.routes()} routes, hardest {hardest_route.grade}"
    
def sort_by_number_of_routes(ls:list):
    def order_by_number_of_routes(ca:ClimbingArea):
        return ca.routes()
    return sorted(ls,key=order_by_number_of_routes )

ca1 = ClimbingArea("Olhava")
ca1.add_route(ClimbingRoute("Edge", 38, "6A+"))
ca1.add_route(ClimbingRoute("Great cut", 36, "6B"))
ca1.add_route(ClimbingRoute("Swedish route", 42, "5+"))

ca2 = ClimbingArea("Nummi")
ca2.add_route(ClimbingRoute("Synchro", 14, "8C+"))

ca3 = ClimbingArea("Nalkkila slab")
ca3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
ca3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
ca3.add_route(ClimbingRoute("Piggy not likey", 12 , "6B+"))
ca3.add_route(ClimbingRoute("Orchard", 8, "6A"))


# ca1, ca2 and ca3 declared as above
areas = [ca1, ca2, ca3]
for area in sort_by_number_of_routes(areas):
    print(area)