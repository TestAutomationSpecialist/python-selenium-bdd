@web
Feature: Cancel Ticket - Table And Popup Handling demo

Scenario: Cancel ticket successfully
	Given I have a booking reference number
	When I cancel the booking
	Then the cancelled ticket does not appear in the itinerary page