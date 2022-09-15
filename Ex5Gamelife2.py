# package exercises
#  * Program for Conway's game of life.
#  * See https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
#  * This is a graphical program using pygame to draw on the screen.
#  * There's a bit of "drawing" code to make this happen (far below).
#  * You don't need to implement (or understand) any of it.
#  * NOTE: To run tests must uncomment in init() method, see comment
#  *
#  * Use functional decomposition!
#  *
#  * See:
#  * - UseEnum
#  * - PygameSample (don't need to understand, just if you're curious)
from enum import Enum
from typing import List
import pygame
# Main program
def game_of_life():
    pygame.init()
    world = World()
    GameOfLifeView(world)
    world.run()


class Cell(Enum):
    DEAD = 0
    ALIVE = 1



class World:
    all_cells: List[List[Cell]] = []
    observers = []

    def __init__(self):
        test()        # <--------------- Uncomment to test!
        n_locations = 10000
        distribution = 0.15   # % of locations holding a Cell
        self.create_world(n_locations, distribution)
        self.clock = pygame.time.Clock()

    def create_world(self, n_locations, distribution):
        self.all_cells = []  # TODO Create and populate world

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.notify()

    def update(self):
        # TODO Update (logically) the world
        pass
        self.notify_observers()  # Tell the view to render

    def run(self):
        # Variable to keep the main loop running
        running = True
        # Main loop
        while running:
            self.update()
            # Ensure program maintains a rate of 2 frames per second
            self.clock.tick(2)
            # Look at every event in the queue
            for event in pygame.event.get():
                # Did the user hit a key?
                if event.type == pygame.QUIT:
                    running = False


# -------- Write methods below this --------------


# ---------- Testing -----------------
# Here you run your tests i.e. call your logic methods
# to see that they really work
def test():
    # Hard coded test world
    test_world: List[List[Cell]] = [
        [Cell.ALIVE, Cell.ALIVE, Cell.DEAD],
        [Cell.ALIVE, Cell.DEAD, Cell.DEAD],
        [Cell.DEAD, Cell.DEAD, Cell.ALIVE]]
    check_cells(test_world)
    size = len(test_world)


def check_cells(test_world):
    for row in test_world: #takes row
        for cell in row: #loops all cells
            cell_nei = []
            if Cell.ALIVE is cell:
                i = row.index(cell)
                print(row[i::i+2])
                cell_nei.append(row[i-1:i+1])


def dead_or_alive(test_world, row, cell): #check if object is alive or dead
    pass


def check_neigbours_alive(test_world, row, cell):
    pass



def cell_starve():
    pass
def cell_survive():
    pass
def cell_born():
    pass

    # TODO tests!


# -------- Below is Pygame View stuff, nothing to do --------------
class GameOfLifeView:

    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 400

    def __init__(self, world_ref: World):
        self.the_world = world_ref
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.the_world.add_observer(self)

    def notify(self):
        self.render()

    def render(self):
        self.screen.fill((255, 255, 255))
        size = len(self.the_world.all_cells)
        for row in range(size):
            for col in range(size):
                x = 3 * col + 50
                y = 3 * row + 50
                self.render_cell(x, y, self.the_world.all_cells[row][col])

        pygame.display.flip()

    def render_cell(self, x, y, cell: Cell):
        if cell == Cell.ALIVE:
            color = (255, 0, 0)
        else:
            color = (255, 255, 255)
        surf = pygame.Surface((3, 3))
        surf.fill(color)
        self.screen.blit(surf, (x, y))


if __name__ == "__main__":
    game_of_life()
