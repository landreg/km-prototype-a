@US6f @US6 @All
Feature: 6f.Knowledge Article page navigation

Scenario: As a user I want to navigate the knowledge article page
Given I navigate through the knowledge article page
When I navigate to the Variable Static page
Then the correct data for the Variable Static page is displayed
Then I select Sole Proprietor
And the correct data for the Sole Proprietor is displayed
Then I select Joint Proprietor
And the correct data for the Joint Proprietor is displayed
