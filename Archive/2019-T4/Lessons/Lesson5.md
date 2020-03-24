# 📜 Day 5: Client-Side Vulnerabilities

### ⏱ Agenda

1. [[**5m**] 🏆 Learning Objectives](#5m-%f0%9f%8f%86-learning-objectives)
2. [[**15m**] 💻 **Demo**: Jinja2 SSTI Activity Review](#15m-%f0%9f%92%bb-demo-jinja2-ssti-activity-review)
3. [[**10m**] 📖 **Overview**: Client-Side Attacks](#10m-%f0%9f%93%96-overview-client-side-attacks)
4. [[**15m**] 💻 **Activity**: Try Out XSS](#15m-%f0%9f%92%bb-activity-try-out-xss)
5. [[**10m**] 🌴 BREAK](#10m-%f0%9f%8c%b4-break)
6. [[**45m**] 💻 **Activity**: The XSS Games](#45m-%f0%9f%92%bb-activity-the-xss-games)
7. [[**20m**] 📖 **Overview**: Client-Side Defense](#20m-%f0%9f%93%96-overview-client-side-defense)
8. [🌃 After Class](#%f0%9f%8c%83-after-class)
9. [📚 Resources & Credits](#%f0%9f%93%9a-resources--credits)

## [**5m**] 🏆 Learning Objectives

By the end of this lesson, you should be able to...

1. Understand the difference between server-side and client-side attacks
1. Use Cross Site Scripting (XSS) to perform hacks
1. Identify XSS Exploits and Vulnerabilities

## [**15m**] 💻 **Demo**: Jinja2 SSTI Activity Review

Live demonstration and Q&A from the TA reviewing the activity we started on Day 3.

## [**10m**] 📖 **Overview**: Client-Side Attacks

So we've learned how we can be attacked on the server-side, and are now equipped with knowledge on how to level up our defenses. So now we need to make sure we're aware of what can go wrong on the client, and how we can defend against that.

![client](Lesson5Assets/client.jpeg)

A client-side attack is any kind of attack that doesn't involve tampering with the back-end or server-side code. It primarily involves exploiting client-side JavaScript, HTML, or CSS to create problems for the victims. It's worth noting that **the majority of attacks are invoked on the client side!**

Before we dive deep into attacks, you actually already know some of these!

Recall **Phishing** from the first lesson. _That's a type of client-side attack!_

![phishing](Lesson5Assets/phishing.jpg)

Other forms of client-side attacks can be more generally described as getting users to click on malicious links. There's a variety of ways to accomplish this as an attacker, one of which we'll do a deep dive into below...

### Cross Site Scripting (XSS)

**XSS attacks are client side attacks where hackers execute malicious code in the browser or insert code into web content, usually through forms.**

JavaScript is plain text. The source code for web pages is delivered to browsers and available for inspection by any client, this makes it easy to exploit when web apps are not diligently protected.

The goal of an attack using XSS is to _find a way to inject code into an existing page._

Any page that incorporates the following is potentially vulnerable to XSS attacks:

- User input into page content
- Any input from a user that gets parsed as HTML

Check out this illustrated example below to see how an XSS attack can be executed:

![xss](Lesson5Assets/xss.png)

### What Else Can I Gain Access To?

A scary amount of things!

Through XSS, _an attacker has access to anything the page source has access to._

This can include:

- Cookies, tokens etc.
- User data
- Manipulating the DOM
- Sending HTTP requests
- Access to Browser APIs like camera, mic, geolocation etc.
- Editing the page style
- Clickjacking
- Autofill/Keychain Data

## [**15m**] 💻 **Activity**: Try Out XSS

Remember that [Dev-Ops Security App](https://github.com/Make-School-Courses/DevOps-Security-App)? Open that back up and let's try out an XSS attack/defense with it.

Follow the instructions on the [How To Exploit](https://github.com/Make-School-Courses/DevOps-Security-App/blob/master/HOW-TO-EXPLOIT.md#xss) guide for XSS.

## [**10m**] 🌴 BREAK

## [**45m**] 💻 **Activity**: The XSS Games

1. Read through [this list of XSS attack vectors](https://www.acunetix.com/websitesecurity/cross-site-scripting/) to familiarize yourself with the vectors you can exploit.
2. Get through as many of the levels in the [XSS Games](https://xss-game.appspot.com) as you can with the time allotted for this activity

## [**20m**] 📖 **Overview**: Client-Side Defense

We've seen how to use these attacks, but how do we try to defend ourselves against them? Luckily there are a lot of tools we can use, most of them are already in place:

### Escaping Dynamic Content

We've seen this before with SQL injections! Making sure we're escaping characters that could cause problems (such as executing code) so that nothing is treated as raw HTML or JS. For example, replacing `<` and `>` with `&#60`and `&#62` respectively.

### Whitelisting

Only allowing certain values/characters to be used as input can help with maintaining an exploit-free environment as well! Don't even give those attackers the chance to enter that code.

### Use a Content Security Policy

Enforcing a content security policy will allow you to dictate where JS code can and cannot be loaded and executed in your web app.

You can read more about how to include a content security policy in [this quick reference guide](https://content-security-policy.com/)

### Quick Note on Reflected and DOM-Based XSS Attacks

#### Reflected XSS

A **Reflected XSS** attack can occur when query string parameters in a URL are assumed to be trustworthy, and therefore an attacker can exploit that to run code in the URL. These types of XSS attacks are much more common than the general XSS attack previously described.

You can protect yourself from these attacks in the same way: dynamically escaping your string parameters!  As these are the very same query parameters that we deal with in route handlers/controllers, sanitizing input in the endpoints is a good step in securing your application.

#### Stored XSS

A **Stored XSS** attack can occur when users are able to store unsanitized input in the database.  An attacker can exploit this by entering malicious code into a publicly requestable resource, like a posted text field or visitor logs.  The victim retrieves and unknowingly runs the malicious script when they request the information.  This can be in the form of posts, comments, usernames, and various alternatives that one user can expose to others.

You can protect yourself the same way that you protect yourself from reflected XSS attacks, but also making sure anything being stored in the database from user input is sanitized before entry.

#### DOM-Based XSS

A **DOM-Based XSS** attack can occur when an attacker can exploit URI fragments. A **URI fragment** is the piece of a url after the `#`. For example, click on the anchor link anywhere on this page next to a header, and see how the URL changes! Everything after the `#` is a URI fragment. So any time a URI fragment is used to execute malicious code, an attacker has successfully pulled off a DOM-Based XSS attack.

This is the rarest of the XSS attacks because it's also the easiest to defend against. Using templates provided in a JS framework will prevent these vulnerabilities from occurring, as will having a content security policy.

## 🌃 After Class

- Go through all 3 [Hacksplaining lessons on XSS](https://www.hacksplaining.com/lessons) and do the exercises and read the prevention page
- Finish any remaining [XSS Games](https://xss-game.appspot.com) levels

## 📚 Resources & Credits

- [XSS Prevention Cheat Sheet](https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet)
- [Acunetix XSS Article](https://www.acunetix.com/websitesecurity/cross-site-scripting/)
- [List of XSS attacks that can be used](https://gist.github.com/kurobeats/9a613c9ab68914312cbb415134795b45)
