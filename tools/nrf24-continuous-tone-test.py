#!/usr/bin/env python3
'''
  Copyright (C) 2016 Bastille Networks

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
  
   
  (Fork - 2024)
  This program has been developed and optimized for use with Python 3 
  by Einstein2150. The author acknowledges that further development 
  and enhancements may be made in the future. The use of this program is 
  at your own risk, and the author accepts no responsibility for any damages 
  that may arise from its use. Users are responsible for ensuring that their 
  use of the program complies with all applicable laws and regulations.
  
'''

import time
import logging
from lib import common

# Parse command line arguments and initialize the radio
common.init_args('./nrf24-continuous-tone-test.py')
common.parse_and_init()

# Set the initial channel
common.radio.set_channel(common.channels[0])

# Put the radio in continuous tone test mode
common.radio.enter_tone_test_mode()

# Run indefinitely
while True:
    pass
