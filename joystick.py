class JoyStick:
    def __init__(self) -> None:
        self.state = [0] * 10

    def keypress(self, key, instruction, instruction_params=None):
        if key[5] and (self.state[5] != key[5]):
            print("INCREASE VOLUME")
            instruction()
            self.state[5] = key[5]
        elif key[5] == 0:
            self.state[5] = key[5]
