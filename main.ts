radio.onReceivedString(function (receivedString) {
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . # . .
        `)
    basic.showString("TOUCH GRASS! EARTHQUAKE")
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . # . .
        `)
    Force_the_Fornite_kid_to_touch_grass()
})
function Force_the_Fornite_kid_to_touch_grass () {
    for (let index = 0; index < 10; index++) {
        music.play(music.createSoundExpression(WaveShape.Square, 2163, 2251, 221, 0, 9999, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
    }
}
input.onGesture(Gesture.Shake, function () {
    radio.sendString("EarthQUAKE")
})
radio.setGroup(78)
