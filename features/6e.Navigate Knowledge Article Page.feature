@US6e @US6 @All
Feature: 6e.Knowledge Article page navigation

Scenario: As a user I want to navigate the knowledge article page
Given I am a user and want to navigate through the knowledge article page
When I navigate to the GOV UK Static page
Then the correct data for the GOV UK Static page is displayed
Then select Sole Proprietor
And the correct data for the Sole Proprietor is displayed
Then select Joint Proprietor
And the correct data for the Joint Proprietor is displayed
