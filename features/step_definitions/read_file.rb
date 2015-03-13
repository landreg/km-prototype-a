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
