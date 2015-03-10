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
  page.should have_content("itemid")
  page.should have_content("title")
  page.should have_content("sub title")
  page.should have_content("body")
  page.should have_content("meta")
end

#US3/DS3 Add knowledge article to elastic search database PENDING todo
Given(/^I access and add a new knowledge article to the elastic search database containing tables and bullet points$/) do
  pending # express the regexp above with the code you wish you had
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
  if page.has_text?("Bankruptcy - Applications for Form J restrictions")
    puts 'Response is Valid'
  else
    puts "*** ERROR - Response Invalid ***"
  end
end

Then(/^the knowledge article page must be able to correctly display the selected data$/) do
  click_link('Contact Us')
end

#US5 KM user accesses selected Knowledge Article page
Given(/^I am a user and want to open the article page$/) do
  visit "http://localhost:5001/gov-base"
end

When(/^I access the article page$/) do
  page.should have_content("Casework Guidance Knowledge Base")
end

Then(/^the article page is displayed$/) do
  sleep 4
end
