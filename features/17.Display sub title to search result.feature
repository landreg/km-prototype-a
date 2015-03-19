@US17 @All
Feature:17.Display scope to search result

Scenario:Display scope to search result
Given I submit a search on 'lender'
When the search result is displayed
Then the scope is displayed on the search result page
