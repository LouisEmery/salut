import arcade
import random



list_color= [arcade.color.ALLOY_ORANGE, arcade.color.AFRICAN_VIOLET, arcade.color.ARMY_GREEN]

class Cercle():
    def __init__(self,rayon,x,y,color):
        self.rayon = rayon
        self.x=x
        self.y=y
        self.color=color

    def draw(self):
        arcade.draw_circle_filled(10, 10, 20, (255, 54, 34))

class MyGame(arcade.Window):
    def __init__(self, width, height, title, color):
       # Call the parent class's init function
       super().__init__(width, height, title, color)
       self.list_cercle = []

    def setup(self):
        for i in range(20):
            posx = random.randint(20, 620)
            posy = random.randint(20, 460)
            rayon = 20
            couleur = random.choice(list_color)
            cercle = Cercle(posx, posy, rayon, couleur)
            self.liste_cercle.append(cercle)
    def on_draw(self):
        arcade.start_render()

def main():
    window = MyGame(640, 480, "Drawing Example", (255, 54, 34))


    arcade.run()


main()
