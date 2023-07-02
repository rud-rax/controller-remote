from read import *
import time
from instructions.volume import increaseVolume, decreaseVolume

# TIME_DELAY = 0.12

joy = XboxController()
state = [0] * 10

while True:
    ins = joy.read()
    # print(ins)
    # time.sleep(TIME_DELAY)

    # joy.keypress(ins[4], decreaseVolume)
    # joy.keypress(ins[5], increaseVolume)

    if ins[4] and (state[4] != ins[4]):
        print("DECREASE VOLUME")
        decreaseVolume()
        state[4] = ins[4]
    elif ins[4] == 0:
        state[4] = ins[4]

    if ins[5] and (state[5] != ins[5]):
        print("INCREASE VOLUME")
        increaseVolume()
        state[5] = ins[5]
    elif ins[5] == 0:
        state[5] = ins[5]
