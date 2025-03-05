### 1. **SQL Injection Vulnerability**
- **Flaw:** The login system was using raw SQL queries with unsanitized user input, which made it possible for attackers to manipulate the database.
- **Impact:** Hackers could bypass login, access sensitive data, or mess with the database.
- **Fix:** Replacing raw SQL with Django’s built-in authenticate method, which securely checks the login without risking SQL injection.

### 2. **Cross-Site Scripting (XSS)**
- **Flaw:** User comments were not checked for harmful code, so attackers could inject malicious JavaScript.
- **Impact:** Malicious code could run in users' browsers, steal information, or mess with the website.
- **Fix:** Using Django's `|escape` filter to clean user comments and prevent any harmful scripts from running. Replacing `<p>{{ comment.text|safe }}</p>` with `<p>{{ comment.text|escape }}</p>`

### 3. **Cross-Site Request Forgery (CSRF)**
- **Flaw:** There was no CSRF protection.
- **Impact:** Attackers could do things like submit forms or change settings without the user knowing.
- **Fix:** Adding Django’s CSRF protection by including `{% csrf_token %}`. This makes sure any action is coming from the user themselves and not an attacker.

### 4. **Insecure Direct Object References (IDOR)**
- **Flaw:** The app allowed users to access certain resources by just guessing or changing the URL, without checking if they had permission.
- **Impact:** Unauthorized users could view or change data they shouldn’t have access to.
- **Fix:** Adding checks to ensure that users can only access data they own, in code: 
` if question.user != request.user:         
	return HttpResponseForbidden("You do not have permission to access this 	resource.") `

### 5. **Security Misconfiguration**
- **Flaw:** The app was running in "debug mode" in production, which revealed sensitive information like error messages and database details.
settings.py:  
` DEBUG = True 
ALLOWED_HOSTS = [] `
- **Impact:** This gave attackers clues on how to exploit the app.
- **Fix:** 
settings.py:  
` DEBUG = False 
ALLOWED_HOSTS = ['localhost', '127.0,0,1'] `
