"""
This module contains a simple class modeling a 9900 Transmitter Relay 2.
9900 Input frequency may be increased or decreased.
The Relay 2 will turn ON at predetermined setpoint, with hysteresis for turning OFF.
"""


class InputFrequency:

    def __init__(self, initial_freq=0, freq=40):
        
        self.initial_freq = initial_freq
        self._freq = freq   
    
        
    @property
    def freq(self, freq=0):
        return self._freq
    #dummy line-void
    # def check_relay_state(self):
    #     return self._relay_state

    # @property
    # def turn_relay_on(self):
    #     return self._relay_state == self.turn_relay_on

    # @property
    # def turn_relay_off(self):
    #     return self._relay_state == self.turn_relay_off

    def increase_input_freq(self, freq=1):
        new_freq = self.freq + freq
        
        # if new_freq > self.max_freq:
        #     raise ValueError("Attempted to increase frequency too much")
        self._freq = new_freq

    def decrease_input_freq(self, freq=1):
        new_freq = self.freq - freq
        # if new_freq < 0:
        #     raise ValueError("Attempted to enter negative values")
        self._freq = new_freq
