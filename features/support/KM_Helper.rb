def access_KM_page
  visit "http://localhost:5001/landing"
end

def access_Article_page
  visit "http://localhost:5001/lr-page/1"
end

def access_search_page
  visit "http://localhost:5001"
end

def access_searchresult_page
  visit "http://localhost:5001/search-result"
end

def content (value1)
  assert page.has_content?(value1), "********** No Matching Text Found ********** "
end

def submit
  fill_in('searchString', :with=> 'charge')
  click_button('submit')
end

def get_to_related_links_on_articles_page
  access_search_page
  fill_in('search', :with=> 'charge')
  click_button('submit')
  assert page.has_content?('Charge combined with transfers and leases')
  click_link('Charge combined with transfers and leases')
end
