@US13 @All
Feature:13.Related Articles links to new page with Related Articles

Scenario:Related Articles links on a Knowledge Article page links to Related Articles
Given I access a Knowledge Article page
And a 'Related Articles' panel is displayed
When I select the 'Related Articles' panel link
Then structured data relating to the article is returned
And when I select another link
Then data relating to the link is returned
