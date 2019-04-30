Feature: Testing site pzz.by

  Scenario: run a simple test
    Given Start test
    Given open "https://pzz.by/"
      Then site should be opened
    #Given set address with street name "Победителей" and house number "1"
    #Given add to cart "1" of pizza "Грибная". Size: "big"
    #Given add to cart "10" of pizza "Гавайская". Size: "big"
    #Given remove from cart "1" of pizza "Гавайская". Size: "big"
    #Given checkout my order
