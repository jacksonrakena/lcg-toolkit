import matplotlib.pyplot as plt

# Constants - range
RANGE_START = 0
RANGE_END = 10000

class LcgGenerator():
    """
    The LcgGenerator class provides access to an 
    isolated, abstract random number generator.
    A, C, M, and seed value are provided, and the
    generator machine takes care of keeping
    internal state consistent.
    """
    def __init__(self, a, c, m, seed):
        self._state = seed
        self.a = a
        self.c = c
        self.m = m

    def random(self):
        self._state = ((self.a * self._state) + self.c) % self.m
        return self._state

def run_plot(title, a, c, m, x0, colour):
    """
    The run_plot function creates an instance of LcgGenerator
    and opens a MPL GUI for viewing the plot.
    """
    generator = LcgGenerator(a, c, m, x0)

    x = []
    y = []
    z = []

    # For each number in the range (usually 10,000),
    # create one X, Y, and Z co-ordinate, using the generator's state.
    # This follows the rules of the function
    for i in range(RANGE_START, RANGE_END):
        x.append(generator.random())
        y.append(generator.random())
        z.append(generator.random())

    # Create the figure using a reasonable, tested size
    figure = plt.figure(figsize=(10,7.5))

    # Set the title
    plt.suptitle(f'{title} (A={a}, C={c}, M={m})')

    # Add our axes in 3D mode
    axe0 = figure.add_axes([0,0,1,1], projection='3d')

    # Use GGPLOT style
    plt.style.use('ggplot')

    # Set the face color of the figure
    figure.set_facecolor('w')

    # Move things around a bit
    plt.subplots_adjust(left=0.15, right=0.9, top=0.85, bottom=0.15)

    # Add our axe titles
    plt.xticks(fontname='Segoe UI', fontsize=12)
    plt.yticks(fontname='Segoe UI', fontsize=12)

    # Apply colour
    axe0.plot(x,y,z,'.', color=colour)

    # Set the initial view angle
    axe0.view_init(90, -90)
    
    # Draw
    plt.draw()

    # Wait 2 seconds
    plt.pause(2)

    # Begin a nice view rotation
    for angle in range(45, 110):
        axe0.view_init(angle,-45)
        plt.draw()
        plt.pause(.01)

    plt.show()