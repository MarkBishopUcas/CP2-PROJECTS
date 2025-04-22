
# --- Import required modules and project files ---
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from helper_funcs.main import inq_select
from classes_project.shapes import shapes, add_shape, compare_shapes, sort_shapes


# --- Main program loop ---
def main():
    while True:
        # Show main menu
        selection = inq_select(
            "Welcome to Amber's Amazing Geometry Calculator!\nUse arrow keys to navigate:",
            "Add new shape",
            "View all shapes",
            "Compare two shapes",
            "Sort shapes by area/perimeter",
            "Exit"
        )

        # Handle menu options
        if selection == 1:
            add_shape(shapes)

        elif selection == 2:
            if not shapes:
                print("No shapes have been added yet.")
            else:
                for name, shape in shapes.items():
                    print(f"\n{name}:")
                    shape.display_info()

        elif selection == 3:
            compare_shapes(shapes)

        elif selection == 4:
            sort_shapes(shapes)

        elif selection == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid selection.")


# --- Entry point for the program ---
if __name__ == "__main__":
    main()
