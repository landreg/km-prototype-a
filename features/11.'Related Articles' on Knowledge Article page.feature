@US11 @All
Feature:11.'Related Articles' on Knowledge Article page

Scenario:'Related Articles' panel on a Knowledge Article page
Given I access a Knowledge Article page
And a 'Related Articles' panel is displayed
When I select the 'Related Articles' panel link
Then structured data relating to the article is returned
