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

import sys
import usb
import logging

# Check pyusb dependency
try:
    from usb import core as _usb_core
except ImportError as ex:
    print('''
------------------------------------------
| PyUSB was not found or is out of date. |
------------------------------------------

Please update PyUSB using pip:

sudo pip install -U -I pip && sudo pip install -U -I pyusb
''')
    sys.exit(1)

# USB commands
TRANSMIT_PAYLOAD = 0x04
ENTER_SNIFFER_MODE = 0x05
ENTER_PROMISCUOUS_MODE = 0x06
ENTER_TONE_TEST_MODE = 0x07
TRANSMIT_ACK_PAYLOAD = 0x08
SET_CHANNEL = 0x09
GET_CHANNEL = 0x0A
ENABLE_LNA_PA = 0x0B
TRANSMIT_PAYLOAD_GENERIC = 0x0C
ENTER_PROMISCUOUS_MODE_GENERIC = 0x0D
RECEIVE_PAYLOAD = 0x12

# nRF24LU1+ registers
RF_CH = 0x05

# RF data rates
RF_RATE_250K = 0
RF_RATE_1M = 1
RF_RATE_2M = 2

# nRF24LU1+ radio dongle
class nrf24:
    usb_timeout = 2500  # Sufficiently long timeout for use in a VM

    def __init__(self, index=0):
        try:
            self.dongle = list(usb.core.find(idVendor=0x1915, idProduct=0x0102, find_all=True))[index]
            self.dongle.set_configuration()
        except usb.core.USBError as ex:
            raise ex
        except Exception:
            raise Exception('Cannot find USB dongle.')

    def enter_promiscuous_mode(self, prefix=[]):
        self.send_usb_command(ENTER_PROMISCUOUS_MODE, [len(prefix)] + list(prefix))
        self.dongle.read(0x81, 64, timeout=nrf24.usb_timeout)
        if prefix:
            logging.debug('Entered promiscuous mode with address prefix {0}'.format(':'.join('{:02X}'.format(b) for b in prefix)))
        else:
            logging.debug('Entered promiscuous mode')

    def enter_promiscuous_mode_generic(self, prefix=[], rate=RF_RATE_2M, payload_length=32):
        self.send_usb_command(ENTER_PROMISCUOUS_MODE_GENERIC, [len(prefix), rate, payload_length] + list(prefix))
        self.dongle.read(0x81, 64, timeout=nrf24.usb_timeout)
        if prefix:
            logging.debug('Entered generic promiscuous mode with address prefix {0}'.format(':'.join('{:02X}'.format(b) for b in prefix)))
        else:
            logging.debug('Entered promiscuous mode')

    def enter_sniffer_mode(self, address):
        self.send_usb_command(ENTER_SNIFFER_MODE, [len(address)] + list(address))
        self.dongle.read(0x81, 64, timeout=nrf24.usb_timeout)
        logging.debug('Entered sniffer mode with address {0}'.format(':'.join('{:02X}'.format(b) for b in address[::-1])))

    def enter_tone_test_mode(self):
        self.send_usb_command(ENTER_TONE_TEST_MODE, [])
        self.dongle.read(0x81, 64, timeout=nrf24.usb_timeout)
        logging.debug('Entered continuous tone test mode')

    def receive_payload(self):
        self.send_usb_command(RECEIVE_PAYLOAD, [])
        return self.dongle.read(0x81, 64, timeout=nrf24.usb_timeout)

    def transmit_payload_generic(self, payload, address=b"\x33\x33\x33\x33\x33"):
        data = [len(payload), len(address)] + list(payload) + list(address)
        self.send_usb_command(TRANSMIT_PAYLOAD_GENERIC, data)
        return self.dongle.read(0x81, 64, timeout=nrf24.usb_timeout)[0] > 0

    def transmit_payload(self, payload, timeout=4, retransmits=15):
        data = [len(payload), timeout, retransmits] + list(payload)
        self.send_usb_command(TRANSMIT_PAYLOAD, data)
        return self.dongle.read(0x81, 64, timeout=nrf24.usb_timeout)[0] > 0

    def transmit_ack_payload(self, payload):
        data = [len(payload)] + list(payload)
        self.send_usb_command(TRANSMIT_ACK_PAYLOAD, data)
        return self.dongle.read(0x81, 64, timeout=nrf24.usb_timeout)[0] > 0

    def set_channel(self, channel):
        if channel > 125: channel = 125
        self.send_usb_command(SET_CHANNEL, [channel])
        self.dongle.read(0x81, 64, timeout=nrf24.usb_timeout)
        logging.debug('Tuned to {0}'.format(channel))

    def get_channel(self):
        self.send_usb_command(GET_CHANNEL, [])
        return self.dongle.read(0x81, 64, timeout=nrf24.usb_timeout)

    def enable_lna(self):
        self.send_usb_command(ENABLE_LNA_PA, [])
        self.dongle.read(0x81, 64, timeout=nrf24.usb_timeout)

    def send_usb_command(self, request, data):
        data = [request] + list(data)
        self.dongle.write(0x01, data, timeout=nrf24.usb_timeout)
