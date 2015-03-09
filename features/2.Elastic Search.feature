Feature: 2.Elastic Search

Scenario: As a KM author I want an elastic search database created with a basic field structure (itemid, title, sub title, body, meta) that can be accessed by the internet.
Given I access the elastic search database
Then The basic field structure is as follows:- (itemid, title, sub title, body, meta)
