# CSRF

## What is CSRF?
CSRF (pronounced sea-surf) stands for Cross Site Request Forgery. It's also known as the one-click attack or session riding.  It is a vulnerability in which unauthorized actions are transmitted from a user's browser (the victim) to a website that they are currently authenticated with. This issue exploits the trust that a website has with the user's web browser.

In order to be a security risk, this vulnerability must be targeted towards already authenticated users AND be state-changing actions. Lack of CSRF protection on unauthenticated pages is just a lack of authentication issue. Lack of CSRF protection on pages which only read/display data is not a problem because the attacker will not be able to view the results of forged request as it is coming from the victims browser. A few examples of state-changing actions include: submission of a form, a write, or a modification/update.


##Is CSRF an issue on unauthenticated pages?
If there is an unauthenticated web form which is lacking a CSRF token, technically an attacker could social engineer a victim into performing the action via the victim's browser. But couldn't the attacker could just do this themselves if it's unauthenticated? So, unless there are other probable attack scenarios that I didn't think of, I would say it is not a security issue.


##How does it work?<a id="#abc"></a>

As stated above, it works by exploiting the trust that a website has with the user's browser. 

When a user authenticates to a web application, they are typically issued a special cookie which is used for managing that user's session with the web application. This is accomplished by the `Set-Cookie` HTTP response header. Cookies come with additional attributes in order to determine which website the cookie belongs to. These are the Domain and Path attributes. For example: `Set-Cookie: mysession=thesessionidvalue; Domain=example.com Path=/; Expires=Wed, 13 Jan 2021 22:23:01 GMT; Secure; HttpOnly`. Once stored by the browser in the cookie jar, it will be sent on all requests to `example.com` under the path of `/` while not expired.

Because modern web browser's will automatically send cookies on requests to the particular website which issued it, it allows CSRF to become a security issue. A form can be created on malicious Mallory's webpage which can contain all needed parameters to make a successful POST request to transfer money to her bank account number. Mallory knows or is betting on that everyday you like to view your bank account summary on Wells Fargo web application. So she's betting that you will already be authenticated with their web application and have valid session cookie. She also knows the required HTTP form parameters for submitting a successful transfer of money. Once you inadvertently visit her webpage, the HTTP request is submitted to Wells Fargo's website to transfer money. It succeeds because Mallory knows all needed parameters. There are no HTTP parameters which require any guessing.

###How does the browser know which cookies to send?
Please see [here](#abc)

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

## Can you upload files when exploiting CSRF?
