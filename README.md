**Django Login Page**
This project is a simple login page created using the Django framework. It demonstrates basic user authentication, redirection, and rendering of HTML templates, with additional measures to ensure that browser caching does not interfere with navigation.

Features
User Authentication: Validates whether the user is registered in the system.
Redirection: Redirects users to the appropriate page based on their authentication status.
HTML Rendering: Renders HTML templates for the login page and other views.
Cache Prevention: Utilizes the @never_cache decorator to prevent the browser from caching the page, ensuring a smoother and more secure user experience.
Key Functions and Decorators
authenticate: Checks if the provided credentials match a registered user.
redirect: Directs the user to the specified page upon successful login or logout.
render: Renders the HTML files associated with various views.
@never_cache: Ensures that the login and other sensitive pages are not cached by the browser, which helps in avoiding issues related to navigation using the browser's back and forward buttons.
