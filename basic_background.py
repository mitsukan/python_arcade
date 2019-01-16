import arcade

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600


def draw_background():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT*(1/3), arcade.color.SKY_BLUE)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT/3, 0, arcade.color.DARK_SPRING_GREEN)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Basic background")

    arcade.start_render()

    draw_background()

    arcade.finish_render()

    arcade.run()

if __name__ == "__main__":
    main()