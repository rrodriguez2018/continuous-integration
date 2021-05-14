Feature: Cucumber Basket
  As a gardener,
  I want to carry cucumbers in a basket,
  So that I don't drop them all.

#a test case (specification/requirement)
  Scenario Outline: Add cucumbers to a basket
#Actual values improve understanding of behavior
    Given the basket has "<initial>" cucumbers
    When "<some>" cucumbers are added to the basket
    Then the basket contains "<total>" cucumbers

    Examples: Amounts
      |initial|some|total|
      |2      |3    |5   |
      |0      |3    |3   |
      |5      |5    |10  |

  Scenario: Add equal number of cucumbers to a basket
    Given the basket has "2" cucumbers
    When "2" cucumbers are added to the basket
    Then the basket contains "4" cucumbers

  Scenario: Remove cucumbers from a basket
    Given the basket has "17" cucumbers
    When "11" cucumbers are removed from the basket
    Then the basket contains "6" cucumbers
