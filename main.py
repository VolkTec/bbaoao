def on_received_string(receivedString):
    basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . # . .
        """)
    basic.show_string("TOUCH GRASS! EARTHQUAKE")
    basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . # . .
        """)
    Force_the_Fornite_kid_to_touch_grass()
radio.on_received_string(on_received_string)

def Force_the_Fornite_kid_to_touch_grass():
    for index in range(10):
        music.play(music.create_sound_expression(WaveShape.SQUARE,
                496,
                1,
                221,
                0,
                100,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            music.PlaybackMode.UNTIL_DONE)

def on_gesture_shake():
    radio.send_string("EarthQUAKE")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

radio.set_group(78)