@web
Feature: Adactin Login

Scenario: Valid Login
	Given I am on the home page
	When I enter the credentials "hiamal007" and "test"
	Then I am able to login successfully

Scenario: Invalid Login
	Given I am on the home page
	When I enter the credentials "amal" and "pass"
	Then I am not able to login successfully