@US10 @All
Feature:10.Add 'related to', to a Knowledge Article 

Scenario: Add 'related to' to a Knowledge Article
Given I have a accessed a Knowledge Article page
And 'related to' is displayed
When I select 'related to'
Then structured data is returned
