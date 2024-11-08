from tkinter import *
import settings
import searcher

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.map = None

        self.__x_vals = ( )
        self.__y_vals = ()
    
    def __generate_grid(self):
        screen_res = (root.winfo_screenwidth() / 2, root.winfo_screenheight() / 2)
        
        self.__x_vals = ( (screen_res[0] / self.rows * i) for i in range(self.rows + 1) )
        self.__y_vals = ( (screen_res[1] / self.cols * i) for i in range(self.cols + 1) )
        
        self.map = [[ False for i in range(self.rows + 1)] for i in range(self.cols + 1)]

    def draw_grid(self, canvas):
        # First making grid
        self.__generate_grid()

        for x in self.__x_vals:
            print(x)
            canvas.create_line(x, 0, x, root.winfo_screenheight() / 2, fill = '#e0e0e0')
        for y in self.__y_vals:
            canvas.create_line(0, y, root.winfo_screenwidth() / 2, y, fill = '#e0e0e0')
        canvas.pack()

    def set_cell(self, x, y, value):
        self.map[x][y] = value

    def print_grid(self):
        if self.map:
            for row in range(self.rows):
                for col in range(self.cols):
                    if (self.map[row][col] == False):
                        print(0, end = ' ')
                    else:
                        print(1, end = ' ')
                print()
            print()

def setup_pathfinding():
    # Window
    win = Toplevel(root)
    win.title('Pathfinding')

    geo = f'{int(root.winfo_screenwidth() / 2)}x{int(root.winfo_screenheight() / 2)}'
    win.geometry(geo)

    # Grid
    grid = Grid(settings.THINK_GRID_X, settings.THINK_GRID_Y)
    can = Canvas(win, bg = "white", height = int(root.winfo_screenheight() / 2), width = int(root.winfo_screenwidth() / 2))
    grid.draw_grid(can)

    # Tree structure


# Tkinter init
root = Tk()
root.state('zoomed')
root.title('I Can Fix That')

# Main menu
main_menu = Menu(root)
root.config(menu = main_menu)

# File menu
file_menu = Menu(main_menu, tearoff = False)

main_menu.add_cascade(label = 'Fren', menu = file_menu)

file_menu.add_command(label = 'New Fren...')
file_menu.add_command(label = 'Get Fren...')
file_menu.add_command(label = 'Drop Off Fren...')

file_menu.add_separator()

file_menu.add_command(label = 'Save Fren')
file_menu.add_command(label = 'Save Fren As...')

# Testing and debug
debug_menu = Menu(main_menu, tearoff = False)

main_menu.add_cascade(label = 'Thinking?', menu = debug_menu)

debug_menu.add_command(label = "Pathfinding", command = setup_pathfinding)

root.mainloop()