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
# Solution with the comments
class AquariumApp:
    def __init__(self, fish_count, eye_color, skin_color):
        self.skin_color = skin_color  
        self.__swim_count = 0  # 'private' attribute
        self.eye_color = eye_color  # public attribute
        self._dead_fish = 0  # 'protected' attribute
        self.fish_count = fish_count  # public attribute

    def start(self):
        if self.fish_count == 0:
            print("There are no alive fish left.")
            return
        self.__swim_count += 1

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
            + str(self._dead_fish)
            + " dead fish with them in the aquarium."
        )
        print(
            "The fish have now been swimming "
            + str(self.__swim_count)
            + " times."
        )

    def die_fish(self, number):
        if self.fish_count == 0:
            print("All fish are dead.")
            print("GAME OVER")
            print("=====")
            return
        self.fish_count -= number
        self._dead_fish += number
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

"""By convention, attributes that start with a single underscore _ are considered "protected,"
 indicating that they should not be accessed or modified from outside the class, although
 they are still accessible. Attributes that start with a double underscore __ are "mangled,"
 which means their names are modified to incorporate the class name, making them harder to access from outside the class.

However, it's important to note that these naming conventions are just conventions
and not strict access control mechanisms. Python programmers are expected to follow
these conventions and respect the intended visibility of attributes, but it is still
possible to access or modify them if necessary.

If you have a specific requirement for strict access control, such as private
or protected attributes that cannot be accessed from outside the class, there are
some techniques you can use, such as property decorators, naming conventions, 
or using the __slots__ attribute. However, these techniques involve more advanced
concepts and may not align with the typical Pythonic approach."""