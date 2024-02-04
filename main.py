import pyray as rl

def main():
    # Initialization
    screen_width, screen_height = 350, 350
    rl.init_window(screen_width, screen_height, "Greedy Stopwatch")

    # Set window icon
    rl.set_window_icon(rl.load_image("static/icon.png"))

    font_size = 100
    elapsed_time = 0
    continue_timer = False

    stop_button = rl.Rectangle(screen_width // 2 + 25, screen_height // 2 + 50, 100, 40)
    start_button = rl.Rectangle(stop_button.x - 150, screen_height // 2 + 50, 100, 40)

    while not rl.window_should_close() :
        # Calculate text size and position
        text = f"{elapsed_time:.2f}"
        text_size = rl.measure_text(text, font_size)
        text_x = (screen_width - text_size) // 2
        text_y = (screen_height - font_size) // 2 - 50
            

        # Check if the mouse is over the stop button and start button
        mouse_point = rl.get_mouse_position()
        is_over_button = rl.check_collision_point_rec(mouse_point, stop_button)
        is_start_button = rl.check_collision_point_rec(mouse_point, start_button)

        # Check for user input to stop the timer
        if is_over_button and rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            continue_timer = False

        # Check for user input to start the timer
        if is_start_button and rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            continue_timer = True

        # Draw
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)
        rl.draw_text(text, text_x, text_y, font_size, rl.MAROON)

        # Draw stop button
        rl.draw_rectangle_rec(stop_button, rl.GRAY)
        rl.draw_text("Stop", int(stop_button.x) + 25, int(stop_button.y) + 10, int(20), rl.BLACK)

        # Draw start button
        rl.draw_rectangle_rec(start_button, rl.GRAY)
        rl.draw_text("Start", int(start_button.x) + 25, int(start_button.y) + 10, int(20), rl.BLACK)

        if continue_timer:  
            # Update timer
            elapsed_time = rl.get_time()

        rl.end_drawing()

    rl.close_window()

if __name__ == "__main__":
    main()
