import pytest

from time import sleep

# Python Selenium Documentation: https://selenium-python.readthedocs.io/

@pytest.mark.interview_test
def test_user_can_log_in(driver):
    """
        Preconditions: The following username/password combination exists within the system:

            Username: <username_goes_here>
            Password: <password_goes_here>

        Steps:

        1. Navigate to https://app.fiscalnote.com/?error=notauthorized
        2. Click on the "Click Here to Log In" button.
        3. Enter the username above in the username field.
        4. Enter the password above in the password field.
        5. Click on the "Log In" button.
        6. Verify that the user is on the Home page by checking that the text "Welcome, <username_goes_here>"
        7. Hover the mouse over the gear icon on the bottom left corner of the screen.
        8. Click the "Log Out" link.
        9. Verify that the user is on the login screen.
    """
    driver.get('https://app.fiscalnote.com/?error=notauthorized')

    sleep(5)


@pytest.mark.interview_test
def test_user_can_create_edit_and_delete_notes(driver):
    """
        Preconditions: The following username/password combination exists within the system:

            Username: <username_goes_here>
            Password: <password_goes_here>

        Steps:

        1. Navigate to https://app.fiscalnote.com/?error=notauthorized
        2. Click on the "Click Here to Log In" button.
        3. Enter the username above in the username field.
        4. Enter the password above in the password field.
        5. Click on the "Log In" button.
        6. Verify that the user is on the Home page by checking that the text "Welcome, <username_goes_here>"
        7. Navigate to https://app.fiscalnote.com/notes
        8. Click the "Write Note" button.
        9. Enter "Angus King" in the linked item field.
        10. Click the option with the text "Angus King" in the dropdown.
        11. Enter some text in the summary field.
        12. Click the Save button.
        13. Verify that the new note is visible. (Just use summary text.)
        14. Click the edit icon for the note.
        15. Clear the current summary.
        16. Enter a new summary.
        17. Click the save button.
        18. Verify the new summary is visible.
        19. Click the delete icon for the note.
        20. Confirm deletion.
        21. Verify the note is no longer visible.
    """
    driver.get('https://app.fiscalnote.com/?error=notauthorized')

    sleep(5)