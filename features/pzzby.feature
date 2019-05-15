Feature: Testing site pzz.by
  Background:
    Given open "https://pzz.by/"
    Given set address with street name "Победителей" and house number "1"

  Scenario Outline: pzzBy Scenario
    When add to cart "<num>" of pizza "<name>". Size: "<size>"
      And checkout my order

    Examples:
      | name      | num | size  |
      | Грибная   | 5 | big   |
      | Гавайская   | 2 | big   |
