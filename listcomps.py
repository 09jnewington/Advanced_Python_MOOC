import math
def square_roots(numbers:list):
    """
    takes a list of integers as its argument.
    The function should return a new list containing the square roots of the original integers.
    """
    return [math.sqrt(i) for i in numbers]

def lengths(nums: list):
    return [len(i) for i in nums]


def remove_smaller_than(numbers: list, limit: int):
    return [i for i in numbers if i > limit]

def begin_with_vowel(words: list):
    return [i for i in words if i[0] in ['a', 'e', 'i', 'o', 'u']]


class LotteryNumbers():
    def __init__(self, week:int, nums:list):
        self.week = week
        self.nums = nums

    def number_of_hits(self, input_nums):
        return len([num for num in input_nums if num in self.nums])
    
    def hits_in_place(self, input_nums):
        return [num if self.nums[idx] == num else -1 for idx, num in enumerate(input_nums)]


def filter_forbidden(string: str, forbidden: str):
    return "".join([i for i in string if i not in forbidden])


class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.products):
            product = self.products[self.n]
            self.n += 1
            return product
        else:
            raise StopIteration
        

def products_in_shopping_list(shopping_list, amount: int):
    return [product[0] for product in shopping_list if product[1] > amount]

class RealProperty:
    def __init__(self, rooms: int , square_meters: int, price_per_sqm: int, description: str):
        self.rooms = rooms
        self.square_meters = square_meters
        self.price_per_sqm = price_per_sqm
        self.description = description

    def bigger(self, compared_to):
        return self.square_meters > compared_to.square_meters

    def price_difference(self, compared_to):
        # Function abs returns absolute value
        difference = abs((self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters))
        return difference

    def more_expensive(self, compared_to):
        difference = (self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters)
        return difference > 0


    def __repr__(self):
        return (f'RealProperty(rooms = {self.rooms}, square_meters = {self.square_meters}, ' + 
            f'price_per_sqm = {self.price_per_sqm}, description = {self.description})')


def cheaper_properties(properties: list, reference: RealProperty):
    return [(property, property.price_difference(reference)) for property in properties if (property.more_expensive(reference) == False and property.price_difference(reference) >0)]

def lengths(strings: list):
    """
    Takes a list of strings as its argument. 
    The function should return a dictionary with the strings 
    in the list as the keys and their lengths as the values.
    """
    return {string : len(string) for string in strings}


from string import punctuation
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        content = f.read()
        content = content.replace("\n", " ")
        content = content.replace(punctuation, " ")
        words = content.split(" ")
        print(words)
        return {word: words.count(word) for word in words if words.count(word) > lower_limit}
    
print(most_common_words('comprehensions.txt', 3))