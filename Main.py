import arcade
import random
list_color= [arcade.color.ALLOY_ORANGE, arcade.color.AFRICAN_VIOLET, arcade.color.ARMY_GREEN]

class MyGame(arcade.Window):
    def __init__(self, width, height, title, color):
       # Call the parent class's init function
       super().__init__(width, height, title, color)

    def on_draw(self):

        arcade.start_render()
        nombre = 20
        while nombre != 0:
            nombre -=1
            arcade.draw_circle_filled(random.randint(20, 620), random.randint(20, 460), 20, random.choice(list_color))



def main():
    window = MyGame(640, 480, "Drawing Example", (255, 54, 34))

    arcade.run()


main()
