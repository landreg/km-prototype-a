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

def submit_charge
  fill_in('search', :with=> 'charge')
  click_button('submit')
end

def pagesizeid1
  click_button('pagesizedropdown')
  click_link('pagesizeid1')
  assert page.has_content?("Page 1 of 5")
end

def pagesizeid2
  click_button('pagesizedropdown')
  click_link('pagesizeid2')
  assert page.has_content?("Page 1 of 3")
end

def pagesizeid3
  click_button('pagesizedropdown')
  click_link('pagesizeid3')
  assert page.has_content?("Page 1 of 1")
end

def submit_bankruptcy
  fill_in('search', :with=> 'Bankruptcy')
  click_button('submit')
end
