import arcade

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600


def draw_background():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT*(1/3), arcade.color.SKY_BLUE)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT/3, 0, arcade.color.DARK_SPRING_GREEN)

def draw_tree(x, y):
    # draw the leafy stuff
    arcade.draw_triangle_filled(
        x + 40, y,
        x, y - 100,
        x + 80, y - 100,
        arcade.color.DARK_GREEN
    )
    # draw the trunk
    arcade.draw_rectangle_filled(
        x + 40, y -125,
        20, 50,
        arcade.color.DARK_BROWN
    )

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Basic background")

    arcade.start_render()

    draw_background()
    draw_tree(400, 280)

    arcade.finish_render()

    arcade.run()

if __name__ == "__main__":
    main()