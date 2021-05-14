from pytest_bdd import scenarios, parsers, given, when, then

from xmtr_Relay2 import InputFrequency
#commit 1

EXTRA_TYPES = {
    'Number': int,
    'State': bool,
}

CONVERTERS2 = {
    'initial': int,
    'new' : int,
    'triggered' : bool,
}

scenarios('../features/9900_RelayHigh.feature',example_converters=CONVERTERS2)


@given(parsers.cfparse('the Input Frequency is "{initial:Number}" Hz', extra_types=EXTRA_TYPES), target_fixture='input_freq')
@given('the Input Frequency is "<initial>" Hz')
def input_freq(initial):
    return InputFrequency(initial_freq= initial)

@when(parsers.cfparse('the Input Frequency increases to "{new:Number}" Hz', extra_types=EXTRA_TYPES))
@when('the Input Frequency increases to "<new>" Hz')
def increase_input_freq(input_freq, new):
    if new > 1500:
        print(new)
        assert ValueError
    input_freq.increase_input_freq(new)

@when(parsers.cfparse('the Input Frequency decreases to "{new:Number}" Hz', extra_types=EXTRA_TYPES))
@when('the Input Frequency decreases to "<new>" Hz')
def decrease_input_freq(input_freq, new):
    input_freq.decrease_input_freq(new)

@then(parsers.cfparse('the 9900 Relay 2 state becomes "{triggered:State}"', extra_types=EXTRA_TYPES))
@then('the 9900 Relay 2 state becomes "<triggered>"')
def set_relay(input_freq, triggered):
    assert triggered == True
    
