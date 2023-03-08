import arcade
import random



list_color= [arcade.color.ALLOY_ORANGE, arcade.color.AFRICAN_VIOLET, arcade.color.ARMY_GREEN]

class Cercle():
    def __init__(self,x,y, rayon,color):
        self.rayon = rayon
        self.x=x
        self.y=y
        self.color=color

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
       # Call the parent class's init function
       super().__init__(width, height, title)
       self.list_cercle = []

    def setup(self):
        for i in range(20):
            posx = random.randint(20, 620)
            posy = random.randint(20, 460)
            rayon = 20
            couleur = random.choice(list_color)
            cercle = Cercle(posx, posy, rayon, couleur)
            self.list_cercle.append(cercle)
    def on_draw(self):
        arcade.start_render()
        for cercle in self.list_cercle:
            cercle.draw()


def main():
    window = MyGame(640, 480, "Drawing Example")
    window.setup()

    arcade.run()


main()
