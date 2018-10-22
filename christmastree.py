from gpiozero import LEDBoard

class ChristmasTree(LEDBoard):
    # Set up a ChristmasTree using GPIO Zero to build a class.
    # To use:
    # tree = ChristmasTree() for a simple instance using LED class.
    # tree = ChristmasTree(pwm=True) for a version which can use PWM.
    # See example files in this repo for more examples of use...
    def __init__(self, pwm=False, initial_value=False, pin_factory=None):
        super(ChristmasTree, self).__init__(
            baubles=LEDBoard(
                bottom=LEDBoard(
                    left=11, midleft=16, midright=17, right=18,
                    pwm=pwm, initial_value=initial_value,
                    _order=('left', 'midleft', 'midright', 'right'),
                    pin_factory=pin_factory),
                middle=LEDBoard(
                    left=19, midleft=20, midright=21, right=22,
                    pwm=pwm, initial_value=initial_value,
                    _order=('left', 'midleft', 'midright', 'right'),
                    pin_factory=pin_factory),
                top=LEDBoard(
                    left=23, right=24,
                    pwm=pwm, initial_value=initial_value,
                    _order=('left', 'right'),
                    pin_factory=pin_factory),
                ),
            star=12,
            pwm=pwm, initial_value=initial_value,
            _order=('baubles', 'star'),
            pin_factory=pin_factory
            )
                
