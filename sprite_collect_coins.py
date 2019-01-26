import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SPRITE_COIN_SCALING = 0.25
SPRITE_PLAYER_SCALING = 0.1
COIN_COUNT = 50
MOVEMENT_SPEED = 10

class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1




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

        self.score = 0

    def setup(self):
        # start a new sprite list
        self.player_list = arcade.SpriteList()
        # set up the player sprite
        self.player_sprite = Player("images/rabbitstand120.gif", SPRITE_PLAYER_SCALING)
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
        # Draw the sprites in lists
        self.player_list.draw()
        self.coin_list.draw()

        #put some text on the screen
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if self.score == 50:
            arcade.draw_text("YOU WIN!", 100,300, arcade.color.WHITE, 60)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.player_list.update()

        self.coin_list.update()
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coins_hit_list:
            coin.kill()
            self.score += 1



def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()


