from guizero import App , Box, PushButton, Drawing, Combo, ButtonGroup
#didnt get a lot done because I wasnt here so I was
#trying to figure out how grid worked

my_app = App(title = "Drawing App", layout = "grid")

menu_box = Box(my_app, height = 50, width = "fill", 
               layout = "grid", border = 2)
paint_box = Box(my_app, width = "fill", height = "fill")

painter = Drawing(paint_box,width="fill", height = "fill" )

#will have a popup to select color from hex code
color_select = PushButton(menu_box, text ="color select",
                          grid = [0,0])
brush_width = Combo(menu_box, grid = [1,0],
                    options = ["width",1,2,3,4,5,6,7,8],
                    selected = "width")
draw_type = ButtonGroup(menu_box, horizontal= True, options = ["Line", 
                                "Free", "Oval", "Rectangle", "Text"],
                                )
#will use drawing with white ink to erase mistakes
#eraser_button = PushButton(menu_box, text ="Eraser", 
                           #grid = [2,0])
#free_draw = PushButton(menu_box,grid=[3,0], text = "free")
#line_draw = PushButton(menu_box,grid=[4,0], text = "line")
#box_draw = PushButton(menu_box,grid= [5,0], text = "box")
#oval_draw = PushButton(menu_box,grid = [6,0], text = "oval")
#text_draw = PushButton(menu_box,grid= [7,0], text = "text") 

def start(event):
    painter.last_event = event
def draw(event):
    painter.line(painter.last_event.x, painter.last_event.y, 
                 event.x, event.y, painter.last_event = event)
#will use the fill comand to fill areas with selected color
painter.when_left_button_pressed = start
painter.when_mouse_dragged = draw


my_app.display()
