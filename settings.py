# Tile Value Constants
WALL = 0
GROUND = 1
FINAL = 2

# Color Constants in RGB
BROWN = (99, 59, 30)
GREEN = (69, 122, 67)
LIGHTGREEN = (111, 206, 107)
BLUE = (50, 178, 229)
GRAY = (151, 152, 153)
WHITE = (255, 255, 255)
RED = (193, 44, 44)
YELLOW = (255, 255, 0)

# Pair tiles with color
colors = {
            WALL  : GRAY,
            GROUND : BROWN,
            FINAL : YELLOW
        }

# Create Map
TILESIZE = 50
MAPWIDTH = 15
MAPHEIGHT = 15
