require 'rspec'
require 'capybara'
require 'capybara/dsl'
require 'rspec'


include Capybara::DSL

Capybara.app_host = 'localhost:4567'
Capybara.default_selector = :css
Capybara.default_driver = :selenium
#Capybara.default_wait_time = 10

Capybara.register_driver :selenium do |app|
Capybara::Selenium::Driver.new(app, :browser => :firefox)
end

require 'test/unit'
include Test::Unit::Assertions

page.driver.browser.manage.window.maximize
