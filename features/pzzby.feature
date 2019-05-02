Feature: Testing site pzz.by

  Scenario: pzzBy Scenario
    Given Start test
    Given open "https://pzz.by/"
      Then site title should be "Пицца Лисицца"
    Given set address with street name "Победителей" and house number "1"
    Given add to cart "1" of pizza "Грибная". Size: "big"
    #Given add to cart "1" of pizza "Гавайская". Size: "big"
    #Given remove from cart "1" of pizza "Гавайская". Size: "big"
    When checkout my order
    Given Stop test
