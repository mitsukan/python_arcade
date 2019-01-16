import arcade

SCREEN_H = 600
SCREEN_W = 600

arcade.open_window(SCREEN_W, SCREEN_H, "This is a face")

arcade.set_background_color(arcade.color.ARSENIC)

arcade.start_render()

# Draw the face
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.AERO_BLUE)

#Right eye
arcade.draw_circle_filled(350,350,10, arcade.color.BLACK)

#Left eye
arcade.draw_circle_filled(250, 350, 10, arcade.color.BLACK)

#mouth
arcade.draw_arc_outline(300, 230, 160, 20, arcade.color.BLACK, 70, 170, 100)


arcade.finish_render()

arcade.run()