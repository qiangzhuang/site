# CSRF

## What is CSRF?
CSRF (pronounced sea-surf) stands for Cross Site Request Forgery. It's also known as the one-click attack or session riding.  It is a vulnerability in which unauthorized actions are transmitted from a user's browser (the victim) to a website that they are currently authenticated with. This issue exploits the trust that a website has with the user's web browser.

In order to be a security risk, this vulnerability must be targeted towards already authenticated users AND state-changing actions. Lack of CSRF protection on unauthenticated pages is just a lack of authentication issue. Lack of CSRF protection on pages which only read/display data is not a problem because the attacker will not be able to view the results of forged request as it is coming from the victims browser. A few examples of state-changing actions include: submission of a form, a write, or a modification/update.


##Why does the user have to be authenticated? Is CSRF an issue on unauthenticated pages?
If there is an unauthenticated web form which is lacking a CSRF token, technically an attacker could social engineer a victim into performing the action via the victim's browser. But couldn't the attacker could just do this themselves if it's unauthenticated? So, what is the risk here?



##How does it work?

As stated above, it works by exploiting the trust that a website has with the user's browser. 

When a user authenticates to a web application, they are typically issued a special cookie which is used for managing that user's session with the web application. This is accomplished by used the Set-Cookie HTTP Response header.

Modern web browser Browser's will automatically send 


###How does the browser know which cookies to send?


### If a web application doesn't use cookies, is it still an issue?


##Why is it an issue? What is the goal? Worst that could happen?


##When is it an issue?

##How severe is this issue?

##What is the typical exploit scenario? What is needed to exploit this?


##Can you give an example?



##How to detect?

##How to exploit?

##How to mitigate?
##What ways can it be mitigated?

##If X is mitigation? How to exploit?


##How to generate a token?

#Additional questions

##What about CSRF on login?

##CSRF on logout?

##What if it is combined with XSS?

##How would you implement a CSRF token?

##How many bits of entropy?

##Should I use token per form request or per user session?

##Why is CSRF token put into cookies?

##When should CSRF token be validated?

##Should it be used on GET or POST requests?

##What about putting CSRF token into a header?

##Can I use referrer for CSRF prevention?

## Does this affect mobile web applications?

## Does this affect Web APIs?