'''
SRP as Single Responsiblity principle state that a method should have single task. 
It is better to have multiple methods instead of single method handling everything.
It promotes and created a more maintainable and easy to understand code 
'''

class User:
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def save_to_database(self) -> None:
        # Code to save the user data to a database
        print(f"Saving user {self.username} to the database...")


class EmailService:
    def send_email(self, recipient: str, subject: str, message: str) -> None:
        # Code to send an email
        print(f"Sending email to {recipient} with subject '{subject}': {message}")


class UserManager:
    def create_user(self, username: str, email: str) -> None:
        user = User(username, email)
        user.save_to_database()
        email_service = EmailService()
        email_service.send_email(email, "Welcome", "Welcome to our system!")


# Usage
user_manager = UserManager()
user_manager.create_user("Priyansh Gautam", "gautam.priyansh98@gmail.com")

