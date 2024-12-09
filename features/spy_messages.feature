Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I enter a message about goblins
    When I click the shift amount dropdown
    When I click 1
    Then I expect to there to be a field with goblin words

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    # write your steps here
