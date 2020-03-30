@web
Feature: Book Ticket - Dropdowns and Explicit wait demo

Scenario: Book Ticket Successfully
	Given I am logged in to the hotel booking site
	When I book a ticket
	Then I get a booking reference number