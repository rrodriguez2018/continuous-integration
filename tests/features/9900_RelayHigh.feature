Feature: We will trigger the 9900 Transmitter Relay 2 whenever
         the Input Frequency goes above 49.9 Hz and turn it OFF
         with a hysteresis of 5 Hz
  
  Scenario Outline: Apply some Input Frequency to the 9900 Transmitter

    Given the Input Frequency is "<initial>" Hz
    When the Input Frequency increases to "<new>" Hz
    Then the 9900 Relay 2 state becomes "<triggered>"

    Examples: Results
      |initial|new  |triggered|
      |0      |20   |False    |
      |0      |40   |False    |
      |40     |50   |True     |
      |50     |40   |False    |
      |50     |0    |False    |

  Scenario: Increase Input Frequency to trigger Relay 2
    Given the Input Frequency is "0" Hz
    When the Input Frequency increases to "50" Hz
    Then the 9900 Relay 2 state becomes "True"

  Scenario: Decrease Input Frequency to turn OFF Relay 2
    Given the Input Frequency is "50" Hz
    When the Input Frequency decreases to "40" Hz
    Then the 9900 Relay 2 state becomes "False"

  Scenario: Increase Input Frequency to turn ON Relay 2
    Given the Input Frequency is "50" Hz
    When the Input Frequency increases to "1600" Hz
    Then the 9900 Relay 2 state becomes "False"

