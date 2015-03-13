@US3 @All
Feature: 3.Add to KM database

Scenario: As a KM author I want to add a new knowledge article to the elastic search database
Given I access and add a new knowledge article to the elastic search database containing tables and bullet points
When I search for that article
Then the database must be able to correctly display it
