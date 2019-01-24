import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SPRITE_COIN_SCALING = 0.25
SPRITE_PLAYER_SCALING = 0.1
COIN_COUNT = 50

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        # Use super to inherit arcade.Window's properties
        super().__init__(width, height)

        # Instantiate the class with a player list. List is used to keep postition of the sprite(s)
        self.player_list = None
        self.player_sprite = None
        self.coin_list = None
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # start a new sprite list
        self.player_list = arcade.SpriteList()
        # set up the player sprite
        self.player_sprite = arcade.Sprite("images/rabbitstand120.gif", SPRITE_PLAYER_SCALING)
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 300
        # Adding the player sprite to the list
        self.player_list.append(self.player_sprite)

        self.coin_list = arcade.SpriteList()
        for i in range(COIN_COUNT):
            coin = arcade.Sprite("images/coin_sprite.png", SPRITE_COIN_SCALING)
            coin.center_y = random.randint(0, SCREEN_HEIGHT)
            coin.center_x = random.randint(0, SCREEN_WIDTH)
            self.coin_list.append(coin)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Draw the list
        self.player_list.draw()
        self.coin_list.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        # This is an override of the method to activate the functionality.
        # On mouse motion, update the player sprite with the following:
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()


