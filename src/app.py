#!/usr/bin/env python


"""class aquarium_app:
    def __init__(this, FISHCOUNT, EyeColor, skinColor):
        this.SkinColor = skinColor
        this.PRIVATE_SWIM_COUNT = 0
        this.EYECOLOR = EyeColor
        this.protected_DEAD_FISH = 0
        this.fishCount = FISHCOUNT

    def _start(those):
        if those.fishCount == 0:
            print("There are no alive fish left.")
            return
        those.PRIVATE_SWIM_COUNT += 1

        print(
            str(those.fishCount)
            + " fish are swimming. Their eyes are "
            + those.EYECOLOR
            + " and their skin is "
            + those.SkinColor
            + "."
        )
        print(
            "There are "
            + str(those.protected_DEAD_FISH)
            + " dead fish with them in the aquarium."
        )
        print(
            "The fish have now been swimming "
            + str(those.PRIVATE_SWIM_COUNT)
            + " times."
        )

    def __die_fish(__that, _number):
        if __that.fishCount == 0:
            print("All fish are dead.")
            print("GAME OVER")
            print("=====")
            return
        __that.fishCount -= _number
        __that.protected_DEAD_FISH += _number
        if _number > 1:
            print(str(_number) + " fish have died.")
        else:
            print("A fish has died.")


if __name__ == "__main__":
    MyAquariumApp = aquarium_app(5, "blue", "red")
    MyAquariumApp._start()
    MyAquariumApp._aquarium_app__die_fish(2)
    MyAquariumApp._start()
    MyAquariumApp._aquarium_app__die_fish(1)
    MyAquariumApp._start()
    MyAquariumApp._aquarium_app__die_fish(2)
    MyAquariumApp._start()
    MyAquariumApp._aquarium_app__die_fish(1)"""

# Solution Modified code
class AquariumApp:
    def __init__(self, fish_count, eye_color, skin_color):
        self.skin_color = skin_color
        self.private_swim_count = 0
        self.eye_color = eye_color
        self.protected_dead_fish = 0
        self.fish_count = fish_count

    def start(self):
        if self.fish_count == 0:
            print("There are no alive fish left.")
            return
        self.private_swim_count += 1

        print(
            str(self.fish_count)
            + " fish are swimming. Their eyes are "
            + self.eye_color
            + " and their skin is "
            + self.skin_color
            + "."
        )
        print(
            "There are "
            + str(self.protected_dead_fish)
            + " dead fish with them in the aquarium."
        )
        print(
            "The fish have now been swimming "
            + str(self.private_swim_count)
            + " times."
        )

    def die_fish(self, number):
        if self.fish_count == 0:
            print("All fish are dead.")
            print("GAME OVER")
            print("=====")
            return
        self.fish_count -= number
        self.protected_dead_fish += number
        if number > 1:
            print(str(number) + " fish have died.")
        else:
            print("A fish has died.")


if __name__ == "__main__":
    my_aquarium_app = AquariumApp(5, "blue", "red")
    my_aquarium_app.start()
    my_aquarium_app.die_fish(2)
    my_aquarium_app.start()
    my_aquarium_app.die_fish(1)
    my_aquarium_app.start()
    my_aquarium_app.die_fish(2)
    my_aquarium_app.start()
    my_aquarium_app.die_fish(1)
print("_______________________________________")

# Solution with the comments
class AquariumApp:
    def __init__(self, fish_count, eye_color, skin_color):
        self.skin_color = skin_color
        self.private_swim_count = 0
        self.eye_color = eye_color
        self.protected_dead_fish = 0
        self.fish_count = fish_count

    def start(self):
        """
        Starts the aquarium simulation by printing the current status of the fish.
        """
        if self.fish_count == 0:
            print("There are no alive fish left.")
            return
        self.private_swim_count += 1

        print(
            str(self.fish_count)
            + " fish are swimming. Their eyes are "
            + self.eye_color
            + " and their skin is "
            + self.skin_color
            + "."
        )
        print(
            "There are "
            + str(self.protected_dead_fish)
            + " dead fish with them in the aquarium."
        )
        print(
            "The fish have now been swimming "
            + str(self.private_swim_count)
            + " times."
        )

    def die_fish(self, number):
        """
        Simulates the death of fish by reducing the fish count and increasing the dead fish count.
        Prints the appropriate message based on the number of fish that died.
        """
        if self.fish_count == 0:
            print("All fish are dead.")
            print("GAME OVER")
            print("=====")
            return
        self.fish_count -= number
        self.protected_dead_fish += number
        if number > 1:
            print(str(number) + " fish have died.")
        else:
            print("A fish has died.")


if __name__ == "__main__":
    # Create an instance of the AquariumApp class
    my_aquarium_app = AquariumApp(5, "blue", "red")
    
    # Start the simulation
    my_aquarium_app.start()
    
    # Simulate the death of 2 fish
    my_aquarium_app.die_fish(2)
    
    # Start the simulation again
    my_aquarium_app.start()
    
    # Simulate the death of 1 fish
    my_aquarium_app.die_fish(1)
    
    # Start the simulation again
    my_aquarium_app.start()
    
    # Simulate the death of 2 fish
    my_aquarium_app.die_fish(2)
    
    # Start the simulation again
    my_aquarium_app.start()
    
    # Simulate the death of 1 fish
    my_aquarium_app.die_fish(1)

##########
"""
Here's a brief summary of what I added to the original code:
Added comments to provide explanations and context for each
method and section of the code.
Modified the class name from aquarium_app to AquariumApp to follow
the recommended Python class naming convention (PascalCase).
Modified the parameter names in the constructor (__init__ method)
 and other methods to use lowercase with underscores (snake_case)
to follow the recommended Python naming convention.
Renamed the instance variable PRIVATE_SWIM_COUNT to private_swim_count
to follow the recommended Python naming convention.
Renamed the instance variable protected_DEAD_FISH to protected_dead_fish
to follow the recommended Python naming convention.
Renamed the private method __die_fish to die_fish to follow
the recommended Python naming convention.
Renamed the instance variable MyAquariumApp to my_aquarium_app
to follow the recommended Python naming convention.

Overall, these changes improve the readability and
adherence to Python naming conventions in the code.

"""
