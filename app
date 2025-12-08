from guizero import App , Box, PushButton, Drawing, Combo, ButtonGroup, TextBox, ListBox

my_app = App(width = 800, height = 800, layout = "grid"
             ,title = "Shopping Lists",)

#Box for buttons to go in 
menu_box = Box(my_app, height = 50, width = "fill", 
               layout = "grid", border = 2, grid = [0,0])
#Text box to input list items
my_text = TextBox(my_app, width = 60, height = 54,grid = [0,1,1, 5],
                  multiline = True)
#Button to add an item to list
my_button = PushButton(menu_box, grid = [0,0], text = "Add")
#Button to remove an item from a list
my_button = PushButton(menu_box, grid = [1,0], text = "Remove")
#Choose what list to edit
list_type = Combo(menu_box, grid = [2,0],
                    options = ["List Type","Grocery List",
                               "Clothes List", "To-Do", 
                               "Budget Tracker"],
                    selected = "List Type")
#Displays your list you are currently editing
list_display = ListBox(my_app, width = 400, height = 700,
                       grid = [1,1,1, 5])
my_text.value

my_app.display()
