#US1/D1 Sprint 1 CSV file content
Given(/^I have a structured content$/) do
mode = "r"
file = File.open("data.csv", mode)
$data = file.read
file.close
end

When(/^I access that content$/) do
  puts $data
end

Then(/^The structured data is returned$/) do
  assert_match('1,charge,Information on how to process a charge', $data, 'No Data Match')
end

#US2/D2 Sprint 1 Check mapping
Given(/^I access the elastic search database$/) do
  visit "https://cp94zbqxv3:estftr8mkx@km-prototype-1076374862.eu-west-1.bonsai.io/knowledge/_mapping"
end

Then(/^The basic field structure is as follows:\- \(itemid, title, sub title, body, meta\)$/) do
    assert page.has_content?("itemid")
    assert page.has_content?("title")
    assert page.has_content?("sub title")
    assert page.has_content?("body")
    assert page.has_content?("meta")
end

#US3/DS3 Add knowledge article to elastic search database PENDING todo
Given(/^I access and add a new knowledge article to the elastic search database containing tables and bullet points$/) do
  visit "https://cp94zbqxv3:estftr8mkx@km-prototype-1076374862.eu-west-1.bonsai.io/knowledge/_mapping"
end

When(/^I search for that article$/) do
  pending # express the regexp above with the code you wish you had
end

Then(/^the database must be able to correctly display it$/) do
  pending # express the regexp above with the code you wish you had
end

#US4/DS4 KM user access to Knowledge Article page/functionality
Given(/^I search for the article page$/) do
  visit "http://localhost:5001/test"
end

When(/^I access a new knowledge article page$/) do
  assert page.has_text?("Bankruptcy - Applications for Form J restrictions")
end

Then(/^the knowledge article page must be able to correctly display the selected data$/) do
  click_link('Contact Us')
end

#US5 KM user accesses selected Knowledge Article page
Given(/^I am a user and want to open the article page$/) do
  visit "http://localhost:5001/gov-base"
end

When(/^I access the article page$/) do
  assert page.has_content?("Casework Guidance Knowledge Base")
end

Then(/^the article page is displayed$/) do
  sleep 4
end

#US6/DS6a Knowledge Article page navigation
Given(/^as a user I want to navigate through the knowledge article page$/) do
  access_KM_page
end

When(/^I navigate to the Land Registry page$/) do
  first(:xpath, ".//*[@id='Land Registry']").click
end

Then(/^the correct data for the Land Registry page is displayed$/) do
  assert page.has_content?("Chargé d'affaires")
end

#US6/DS6b Knowledge Article page navigation
Given(/^I am a user and want to navigate through the knowledge article page$/) do
  access_KM_page
end

When(/^I navigate to the GOV UK page$/) do
  first(:xpath, ".//*[@id='GOV UK']").click
end

Then(/^the correct data for the GOV UK page is displayed$/) do
  assert page.has_content?("Chargé d'affaires")
end

#US6/DS6c Knowledge Article page navigation
Given(/^I want to navigate through the knowledge article page$/) do
  access_KM_page
end

When(/^I navigate to the Variable page$/) do
  first(:xpath, ".//*[@id='Variable']").click
end

Then(/^the correct data for the Variable page is displayed$/) do
  assert page.has_content?("Chargé d'affaires")
end

#US6/DS6d Knowledge Article page navigation
Given(/^I want to navigate through the knowledge article page$/) do
  access_KM_page
end

When(/^I navigate to the Land Registry Static page$/) do
  first(:xpath, ".//*[@id='Land Registry Static']").click
end

Then(/^the correct data is displayed$/) do
  assert page.has_content?("Bankruptcy - Applications for Form J restrictions")
end

Then(/^select Sole Proprietor$/) do
  first(:xpath, ".//*[@id='Sole Proprietor']").click
  assert page.has_content?("the trustee accepts that the registered estate has vested in them.")
end

Then(/^select Joint Proprietor$/) do
  first(:xpath, ".//*[@id='Joint Proprietor']").click
  assert page.has_content?('certified copy of the bankruptcy order and')
end

#US6/DS6e Knowledge Article page navigation
Given(/^I want to navigate through the knowledge article page$/) do
  access_KM_page
end

When(/^I navigate to the GOV UK Static page$/) do
  first(:xpath, ".//*[@id='GOV UK Static']").click
end

Then(/^the correct data for the GOV UK Static page is displayed$/) do
  assert page.has_content?("Bankruptcy - Applications for Form J restrictions")
end

Then(/^the correct data for the Sole Proprietor is displayed$/) do
  first(:xpath, ".//*[@id='Sole Proprietor']").click
  page.has_content?("the trustee accepts that the registered estate has vested in them.")
end

Then(/^the correct data for the Joint Proprietor is displayed$/) do
  first(:xpath, ".//*[@id='Joint Proprietor']").click
  page.has_content?('certified copy of the bankruptcy order and')
end

#US6/DS6f Knowledge Article page navigation
Given(/^I navigate through the knowledge article page$/) do
  access_KM_page
end

When(/^I navigate to the Variable Static page$/) do
  first(:xpath, ".//*[@id='Variable Static']").click
end

Then(/^the correct data for the Variable Static page is displayed$/) do
  assert page.has_content?("Bankruptcy - Applications for Form J restrictions")
end

Then(/^I select Sole Proprietor$/) do
  first(:xpath, ".//*[@id='Sole Proprietor']").click
  page.has_content?("the trustee accepts that the registered estate has vested in them.")
end

Then(/^I select Joint Proprietor$/) do
  first(:xpath, ".//*[@id='Joint Proprietor']").click
  page.has_content?('certified copy of the bankruptcy order and')
end

#US6/DS6f Knowledge Article page navigation
When(/^I navigate to then select the Contact Us link$/) do
  click_link('Contact Us')
end

Then(/^the correct data for the Contact Us link is displayed$/) do
  assert page.has_content?("w3schools.com")
end

#Sprint 2
#US10/DS10.Add 'related to', to a Knowledge Article
Given(/^I am on a Knowledge Article page$/) do
  access_Article_page
end

When(/^a Related Article link is displayed on the page$/) do
  assert page.has_content?('Related Articles')
end

Then(/^a link is displayed under the Related Article$/) do
  assert page.has_content?('Transfer')
end

#US11/DS11.Link from 'Related Articles', to a Knowledge Article
Given(/^I access a Knowledge Article page$/) do
  access_Article_page
end

Given(/^a 'Related Articles' panel is displayed$/) do
  assert page.has_content?('Related Articles')
end

When(/^I select the 'Related Articles' panel link$/) do
  click_link('Transfer')
end

Then(/^structured data relating to the article is returned$/) do
  assert page.has_content?("One of the first examples was the Lefschetz principle")
end

#US12/DS12 Hover function - tests title in hover
Given(/^a Related Articles panel is displayed$/) do
  assert page.has_content?("Related Articles")
end

When(/^I hover over a link in the Related Articles panel the data relating to the link is displayed$/) do
  title = find(:xpath, './/*[@id="related_article_id_3"]')['title']

  assert_match title, "Information on how to process a transfer"
end

#US13/DS13.Related Articles links to new page with Related Articles
Then(/^when I select another link$/) do
  click_link('related_article_id_1')
end

Then(/^data relating to the link is returned$/) do
  assert page.has_content?("Types of chargés")
end

#Sprint 3
#US15/DS15.Display 'Initial Search' page
Given(/^I access an 'Initial Search' page$/) do
  access_search_page
end

Then(/^an 'Initial Search' page is displayed$/) do
  assert page.has_content?("Search Guidance")
end

#US16/DS16.Submit Search and display search result
When(/^I submit a search$/) do
  fill_in('searchString', :with=> 'charge')
  click_button('submit')
end

Then(/^a search result is displayed$/) do
  assert page.has_content?("charge")
end

#US17/DS17.Display sub title to search result
Given(/^I submit a search on 'charge'$/) do
  access_search_page
  fill_in('searchString', :with=> 'charge')
  click_button('submit')
end

When(/^the search result is displayed$/) do
  assert page.has_content?("Charge")
end

Then(/^the scope is displayed on the search result page$/) do
  assert page.has_content?("Charge combined with transfers and leases")
end

#US18/DS18.Display sub title to search result
Given(/^I have navigated to the search results page$/) do
  access_search_page
  fill_in('searchString', :with=> 'charge')
  click_button('submit')
end

When(/^I select the title on the results page$/) do
  click_link('Charge combined with transfers and leases')
end

Then(/^the main bodytext is displayed$/) do
  content("Charges combined with transfers or leases are acceptable if an applicant can demonstrate why this would be advantageous.")
end

#US10a/DS10a.A Related Article link is displayed on a Knowledge Article page
#(Refactored for new code structure)
Given(/^I have navigated to a Knowledge Article page$/) do
  access_search_page
  fill_in('searchString', :with=> 'charge')
  click_button('submit')
  click_link('Charge combined with transfers and leases')
end

When(/^a Related Articles link is displayed on the page$/) do
  assert page.has_content?('Related Articles')
end

Then(/^a Related Article link is displayed$/) do
  assert page.has_content?('Agreement of occupier to postponement of rights')
end

#US10b/DS10b.A Related Article link is displayed on a Knowledge Article page
#(Refactored for new code structure)
Given(/^a Knowledge Article page is dispayed$/) do
  access_search_page

  submit
  click_link('Charge combined with transfers and leases')
end

When(/^Related External link is displayed on the page$/) do
  assert page.has_content?('Related External Links')
end

Then(/^a Related External link can be selected$/) do
  assert page.has_content?('Agreement of occupier to postponement of rights')
end

#Sprint 4
#Refactored for new code structure)
#US10c/DS10c.A Related Article link is displayed on a Knowledge Article page
Given(/^a Knowledge Article page is displayed$/) do
  access_search_page
  fill_in('search', :with=> 'charge')
  click_button('submit')
  assert page.has_content?('Charge combined with transfers and leases')
  click_link('Charge combined with transfers and leases')
end

When(/^the page displays a Related Article$/) do
  assert page.has_content?('Related Articles')
end

Then(/^the Related Article link is displayed$/) do
  assert page.has_content?('Agreement of occupier to postponement of rights')
end

#US10d/DS10d.A Related Article link is displayed on a Knowledge Article page
Given(/^the user is on Knowledge Article page$/) do
  access_search_page

  submit
  click_link('Charge combined with transfers and leases')
end

When(/^External Links is displayed on the page$/) do
  assert page.has_content?('External Links')
end

#For future use ......
#Then(/^an External Link can be selected$/) do
#  assert page.has_content?('foo')
#end

#US11a/DS11a.Related Articles displays on Knowledge Article page
Given(/^a Related Articles panel is displayed on a Knowledge Article page$/) do
  get_to_related_links_on_articles_page
  assert page.has_content?('Related Articles')
end

When(/^the Related Articles link is selected$/) do
  assert page.has_content?('Agreement of occupier to postponement of rights')
  click_link('Agreement of occupier to postponement of rights')
end

Then(/^the article structured data is returned$/) do
  assert page.has_content?('Charges containing a legal and equitable charge over the same property')
end

#12a.Hover on Related Articles links on Knowledge Article page
Given(/^a user is on the Knowledge Article page$/) do
  access_search_page
  submit_charge
  click_link('Further charges')
end

When(/^they hover over a Related Articles link$/) do
  assert page.has_content?('Related Articles')
  title = find(:xpath, './/*[@id="related_article_id_Chargeobligesfurtheradvances"]')['title']

  assert_match title, "Charges - obligations to make further advances"
end

#Then(/^the data relating to the link is displayed$/) do
#  assert_match title, "Some text describing the scope and content of the article"
#end

#16a.Submit Search and display search result
Given(/^I enter a search$/) do
  access_search_page
end

When(/^I submit the search$/) do
  submit_charge
end

Then(/^the search result is returned$/) do
  assert page.has_content?('Further charges')
end

#US17a/DS17a.Display sub title to search result
Given(/^a search is submitted$/) do
  access_search_page
  submit_charge
end

When(/^the search result is displayed$/) do
  assert page.has_content?("Further charges")
end

Then(/^the scope is displayed$/) do
  assert page.has_content?("Substituted charges")
end

#US18a/DS18a.Display sub title to search result
Given(/^I am on the search results page$/) do
  access_search_page
  submit_charge
end

When(/^the title on the results page is selected$/) do
  click_link('Second charges')
end

Then(/^the main bodytext is returned$/) do
  assert page.has_content?('Second charges')
  content ("A second charge is registered in the same way as a first charge, you must consider any existing chargee restrictions in the register and if consent is required. ")
end

#US19/DS19.Sort Related Article results
Given(/^a succesful search has beeen carried out$/) do
  access_search_page
  submit_charge
end

When(/^the results are displayed on the scope page$/) do
  assert page.has_content?("Helpful"), "********** No Matching Text Found **********"
end

Then(/^the results can be sorted by Helpful, Relevant & Latest$/) do
  click_link('helpful')
  assert page.has_content?("Checking the Charge")
  click_link('latest')
  assert page.has_content?("Charges - despatch and retention of documents")
  click_link('relevant')
  assert page.has_content?("Further charges")
end

#US21/DS21.Page through Helpful search results
Given(/^I am on the Helpful tab$/) do
  access_search_page
  submit_charge
end

When(/^I change the results per page$/) do
  click_link('helpful')

  pagesizeid2

  pagesizeid3

  pagesizeid1
end

  Then(/^the page will display the selected number of results$/) do
  assert page.has_content?("Checking the Charge")
  assert page.has_content?("Charges containing a legal and equitable charge over the same property")
  assert page.has_content?("Charge combined with transfers and leases")
  assert page.has_content?("Agreement of occupier to postponement of rights ")
  assert page.has_content?("Charges containing a legal and equitable charge over the same property")
end

#US21a/DS21a.Page through Latest search results
Given(/^I am on the Latest tab$/) do
  access_search_page
  submit_charge
end

When(/^the number of results per page changes$/) do
  click_link('latest')
  pagesizeid3

  pagesizeid2

  pagesizeid1
end

Then(/^the selected number of results will be displayed$/) do
  assert page.has_content?("Charges - despatch and retention of documents")
  assert page.has_content?("Agreement of occupier to postponement of rights")
  assert page.has_content?("Charges combined with transfers and leases")
  assert page.has_content?("Health and Social Services and Social Security Adjustments Act 1983")
  assert page.has_content?("HASSASSAA 1983 – joint proprietors - which restriction")
end

#US21b/DS21b.Page through Relevant search results
Given(/^I am on the Relevant tab$/) do
  access_search_page
  submit_charge
end

When(/^I change the number of results per page$/) do
  click_link('relevant')
  pagesizeid3

  pagesizeid2

  pagesizeid1
end

Then(/^the correct number of results will be returned$/) do
  assert page.has_content?("Further charges")
  assert page.has_content?("Substituted charges")
  assert page.has_content?("Substituted charges")
  assert page.has_content?("Second charges")
  assert page.has_content?("Charges combined with transfers and leases")
end

#US22/DS22.Results Page displays the number of search results
Given(/^I have completed a search$/) do
  access_search_page
  submit_bankruptcy
end

When(/^I am on the results page$/) do
  assert page.has_content?("Bankruptcy - overview")
  assert page.has_content?("Bankruptcy – applications for Form J restrictions")
end

Then(/^the page displays the number of search results$/) do
  assert page.has_content?("Search matches 2 results")
end
