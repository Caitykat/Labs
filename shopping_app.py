from guizero import App , Box, PushButton, Drawing, Combo, ButtonGroup, TextBox, ListBox, Text

#The audience is people who have trouble organizing. It is one 
#app that stores your necessary lists in one place so its easy to access 
my_app = App(width = 800, height = 800, layout = "grid"
             ,title = "Shopping Lists",)

list_items_grocery = []
list_items_todo = []
list_items_budget = []
list_items_misc = []


def add_list_item(list_item):
    item_text = my_type_box.value
    if list_item == "Grocery List":
        list_items_grocery.append(item_text)
        my_type_box.clear
    if list_item == "To-Do":
        list_items_todo.append(item_text)
        my_type_box.clear
    if list_item == "Budget Tracker":
        list_items_budget.append(item_text)
        my_type_box.clear
    if list_item == "Miscellaneous":
        list_items_misc.append(item_text)
        my_type_box.clear

def remove_list_item():
    pass


#Box for buttons to go in 
menu_box = Box(my_app, height = 50, width = "fill", 
               layout = "grid", border = 2, grid = [0,0])
#Text box to input list items
my_type_box = TextBox(my_app, width = 60, height = 54,grid = [0,1,1, 5],
                  multiline = True)

#Button to remove an item from a list
remove_list = PushButton(menu_box, grid = [1,0], text = "Remove",
                         command = remove_list_item())
my_text = Text(menu_box, grid = [3,0],text = "My List", size = 30,
               color = "black" )
#Choose what list to edit
list_type = Combo(menu_box, grid = [2,0],
                    options = ["List Type","Grocery List",
                                "To-Do", 
                               "Budget Tracker",
                               "Miscellaneous"],
                    selected = "List Type")
#Button to add an item to list
add_list = PushButton(menu_box, grid = [0,0], text = "Add", 
                      command= add_list_item(list_item = list_type.value))
#Displays your list you are currently editing
list_display = ListBox(my_app, width = 400, height = 700,
                       grid = [1,1,1, 5])





my_app.display()