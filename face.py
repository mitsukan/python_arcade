import arcade

SCREEN_H = 600
SCREEN_W = 600


def draw_face():
    x = 300
    y = 300
    radius = 200
    arcade.draw_circle_filled(x, y, radius, arcade.color.AERO_BLUE)

def draw_left_eye():
    arcade.draw_circle_filled(250, 350, 10, arcade.color.BLACK)

def draw_right_eye():
    arcade.draw_circle_filled(350,350,10, arcade.color.BLACK)

def draw_mouth():
    arcade.draw_arc_outline(300, 230, 160, 20, arcade.color.BLACK, 70, 170, 100)


def main():
    arcade.open_window(SCREEN_W, SCREEN_H, "This is a face")

    arcade.set_background_color(arcade.color.ARSENIC)

    arcade.start_render()

    draw_face()
    draw_right_eye()
    draw_left_eye()
    draw_mouth()


    arcade.finish_render()

    arcade.run()

main()