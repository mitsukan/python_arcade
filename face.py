import arcade

SCREEN_H = 500
SCREEN_W = 500

arcade.open_window(SCREEN_W, SCREEN_H, "This is a face")

arcade.set_background_color(arcade.color.ARSENIC)

arcade.start_render()

x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.AERO_BLUE)

arcade.finish_render()

arcade.run()