# Behavior Driven Tests
This repository contains sample code for the
*Behavior-Driven Python with pytest-bdd* Training
from [Test Automation University](https://testautomationu.applitools.com/).

## Version 4 Warning
The Training was posted with `pytest-bdd` version 3.
Unfortunately, **the version 4 update has incompatible changes.**
`@given` methods must now include a `target_fixture` parameter in order to work like pytest fixtures.
The Training videos and transcripts use the old style of code,
but the sample code here now uses the new style of code.
Below is an example of the new style of code needed:

```python
@given("the basket has 2 cucumbers", target_fixture='basket')
def basket():
    return CucumberBasket(initial_count=2)
```

## Setup
This project requires an up-to-date version of Python 3.
It also uses [pipenv](https://pipenv.readthedocs.io/) to manage packages.

## Running Tests
Run tests simply using the `pytest` command.
Depending upon your environment, it may be better to use `python -m pytest`.
If you are using `pipenv`, then run `pipenv run python -m pytest`.
Use the "-k" option to filter tests by tags.

## Goal
Help develop set of Behavior Driven Test Suite to be used for Verification Process.

