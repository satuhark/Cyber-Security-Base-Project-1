### 1. **SQL Injection Vulnerability**
- **Flaw:** The login system was using raw SQL queries with unsanitized user input, which made it possible for attackers to manipulate the database.
- **Impact:** Hackers could bypass login, access sensitive data, or mess with the database.
- **Fix:** Replacing raw SQL with Django’s built-in authenticate method, which securely checks the login without risking SQL injection.

2. Cross-Site Scripting (XSS):
  Flaw: User comments were being shown without checking for harmful code, so attackers could inject malicious JavaScript.
  Impact: Malicious code could run in users' browsers, steal information, or mess with the website.
  Fix: Using Django's |escape filter to clean user comments and prevent any harmful scripts from running.

3. Cross-Site Request Forgery (CSRF):
  Flaw: There was no CSRF protection
  Impact: Attackers could do things like submit forms or change settings without the user knowing.
  Fix: Adding Django’s CSRF protection by including {% csrf_token %}. This makes sure any action is coming from the user themselves and not an attacker.

4. Insecure Direct Object References (IDOR):
  Flaw: The app allowed users to access certain resources by just guessing or changing the URL, without checking if they had permission.
  Impact: Unauthorized users could view or change data they shouldn’t have access to.
  Fix: Adding checks to ensure that users can only access data they own, using Django’s get_object_or_404 and making sure they have permission.

5. Security Misconfiguration:
  Flaw: The app was running in "debug mode" in production, which revealed sensitive information like error messages and database details.
  Impact: This gave attackers clues on how to exploit the app.
  Fix: Turning off debug mode by setting DEBUG = False and set up proper logging to track errors safely without revealing sensitive details.
