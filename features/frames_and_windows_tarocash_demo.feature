@web
Feature: Tarocash.com Frames and Windows Demo

Scenario: Navigate to google home page from Tarocash home page
	Given I am on the Tarocash home page
	When I click on the title of the embedded video
	And I click on the youtube logo in the youtube page
	Then I am taken to the youtube home page