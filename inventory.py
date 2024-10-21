import csv
#create a food category of all the foods from the items_food file.
#append all the items on the 'food_category' list
food_category = []
with open('items_food.csv') as csv_food:
    csv_reader_food = csv.reader(csv_food)
    for line in csv_reader_food:
        food_category.append(line[0])
#create a food category of all the foods from the items_beverages file.
#append all the items on the 'beverages_category' list
beverages_category = []
with open('items_beverages.csv') as csv_beverages:
    csv_reader_beverages = csv.reader(csv_beverages)
    for line in csv_reader_beverages:
        beverages_category.append(line[0])

class Inventory:
    def __init__(self):
        print("Welcome to the Inventory")
    # adds a new item to the desired category
    def add_item(self, item,category):
        if category == 'Beverages' and item not in category:
            beverages_category.append(item)
        elif category == 'Foods' and item not in category:
            food_category.append(item)
        else:
            print("Item already exists")

    # removes an item from the category selected
    def remove_item(self, item,category):
        if category == 'Beverages':
            beverages_category.remove(item)
        elif category == 'Foods':
            food_category.remove(item)

    # prints the items of the Inventory by categories
    def list_items(self):
        print(f"Foods: {food_category}")
        print(f"Beverages: {beverages_category}")

    # creates a new category for the inventory
    def update_inventory(self, category):
        category = []
        return category

class Item(Inventory):
    __name = ""
    __category = None
    __expiration_date = None
    def __init__(self):
        pass
    def set_name(self, name):
        #sets the name of the item created
        self.__name = name
        return self.__name
    def set_category(self, category):
        #sets the category of the item created
        self.__category = category
    def set_expiry(self, date):
        #sets the expiration date
        self.__expiration_date = date
        return self.__expiration_date
    def get_details(self):
        #prints details(name, category, exp.date) of the item
        print(f"Name: {self.__name}")
        print(f"Category: {self.__category}")
        print(f"Expiration Date: {self.__expiration_date}")
item = Item()
class Report(Inventory):
    def __init__(self):
        pass
    def items_in(self, category):
        #prints the number of items in the desired category
        if category == 'Foods':
            lengthOf = len(food_category)
        elif category == 'Beverages':
            lengthOf = len(beverages_category)
        print(f"There are currently {lengthOf} items in the '{category}' category")
        print("You can add or remove more")

    #displays all of the current recipes of the inventory
    def recipes(self):
        list_of_recipes = []
        with open('recipes.csv') as csv_recipes:
            csv_reader_recipes = csv.reader(csv_recipes)

            for line in csv_reader_recipes:
                list_of_recipes.append(line[0])
        print(list_of_recipes)
    #creates a new recipe for the inventory
    def create_new_recipe(self,name,items):
        #creates a new recipe for the Inventory to store
        #items argument must be in a list
        print("Here you can create a new recipe!")
        print(f"The name of your recipe is '{name}'")
        print(f"Your new recipe includes these items from the inventory: {items}")
