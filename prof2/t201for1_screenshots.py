# Author: Eyjolfur Ingi Asgeirsson
# Date: 2024-02-21
# Project: Automatic screenshots with random intervals

import os
import pyautogui
import random
import time

print('Welcome to the screenshots machine for T201FOR1.')

INTERVAL = [120,480]

screenshots_start_time = time.time()

username = os.getlogin()

the_seed = 0
for c in username:
    the_seed += ord(c)
random.seed(the_seed)

while True:
    current_time = time.time()
    current_name = username + '_{:0>6}'.format(int(current_time - screenshots_start_time))
    current_screenshot = pyautogui.screenshot()
    print(f'Capturing screenshot {current_name}')
    current_screenshot.save(current_name + '.png')
    time.sleep(random.randint(INTERVAL[0], INTERVAL[1]))