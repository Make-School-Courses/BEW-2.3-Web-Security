# 📜 Day 5: Client-Side Vulnerabilities

## ⏱ Agenda

## 🏆 Learning Objectives

By the end of this lesson, you should be able to...

1. Understand the difference between server-side and client-side attacks
1. Use Cross Site Scripting (XSS) to perform hacks
1. Identify XSS Exploits and Vulnerabilities

## 📖 Overview

So we've learned how we can be attacked on the server-side, and are now equipped with knowledge on how to level up our defenses. So now we need to make sure we're aware of what can go wrong on the client, and how we can defend against that.

## Client-Side Attacks

![client](Lesson5Assets/client.jpeg)

A client-side attack is any kind of attack that doesn't involve tampering with the back-end or server-side code. It primarily involves exploiting client-side JavaScript, HTML, or CSS to create problems for the victims. It's worth noting that **the majority of attacks are invoked on the client side!**

Before we dive deep into attacks, you actually already know some of these!

Recall **Phishing** from the first lesson. _That's a type of client-side attack!_

![phishing](Lesson5Assets/phishing.jpg)

Other forms of client-side attacks can be more generally described as getting users to click on malicious links. There's a variety of ways to accomplish this as an attacker, one of which we'll do a deep dive into below...

## Cross Site Scripting (XSS)

**XSS attacks are client side attacks where hackers execute malicious code in the browser or insert code into web content, usually through forms.**

JavaScript is plain text. The source code for web pages is delivered to browsers and available for inspection by any client, this makes it easy to exploit when web apps are not dilligently protected.

The goal of an attack using XSS is to _find a way to inject code into an existing page._

Any page that incorporates the following is potentially vulnerable to XSS attacks:

- User input into page content
- Any input from a user that gets parsed as HTML

Check out this illustrated example below to see how an XSS attack can be executed:

![xss](Lesson5Assets/xss.png)

## 💻 Think / Pair / Share

2 minutes each for think, pair, and share:

We saw in the example above that session cookies are stolen. What are other examples of things an attacker can gain access to?

**Answer:**

A scary amount of things! Through XSS, _an attaker has access to anything the page source has access to._ This can include:

- Cookies, tokens etc.
- User data
- Manipulating the DOM
- Sending HTTP requests
- Access to Browser APIs like camera, mic, geolocation etc.
- Editing page style
- Click jacking

## 💻 Try Out XSS

Remember that [Dev-Ops Security App](https://github.com/Make-School-Courses/DevOps-Security-App)? Open that back up and let's try out an XSS attack/defense with it.

Follow the instructions on the [How To Exploit](https://github.com/Make-School-Courses/DevOps-Security-App/blob/master/HOW-TO-EXPLOIT.md#xss) guide for XSS

## 🌴 BREAK

## 💻 The XSS Games

1. Read through [this list of XSS attack vectors](https://www.acunetix.com/websitesecurity/cross-site-scripting/) to familiarize yourself with the vectors you can exploit
1. Get through as many of the levels in the [XSS Games](https://xss-game.appspot.com) as you can with the time allotted for this activity

## How to Defend Against XSS

We've seen how to use these attacks, but how do we try to defend ourselves against them? Luckily there are a lot of tools we can use, most of them are already in place:

### Escaping Dynamic Content

We've seen this before with SQL injections! Making sure we're escaping characters that could cause problems (such as executing code) so that nothing is treated as raw HTML or JS. For example, replacing `<` and `>` with `&#60`and `&#62` respectively.

### Whitelisting

Only allowing certain values/characters to be used as input can help with maintaining an exploit-free environment as well! Don't even give those attackers the chance to enter that code.

### Use a Content Security Policy

Enforcing a content security policy will allow you to dictate where JS code can and cannot be loaded and executed in your web app. 

You can read more about how to include a content security policy in [this quick reference guide](https://content-security-policy.com/)

## Quick Note on Reflected and DOM-Based XSS Attacks

### Reflected XSS

A **Reflected XSS** attack can occur when query string parameters in a URL are assumed to be trustworthy, and therefore an attacker can exploit that to run code in the URL. These types of XSS attacks are much more common than the general XSS attack previously described.

You can protect yourself from these attacks in the same way: dynamically escaping your string parameters!

### DOM-Based XSS

A **DOM-Based XSS** attack can occur when an attacker can exploit URI fragments. A **URI fragment** is the piece of a url after the `#`. For example, click on the anchor link anywhere on this page next to a header, and see how the URL changes! Everything after the `#` is a URI fragment. So any time a URI fragment is used to execute malicious code, an attacker has succesfully pulled off a DOM-Based XSS attack.

This is the rarest of the XSS attacks because it's also the easiest to defend against. Using templates provided in a JS framework will prevent these vulnerabilities from occuring, as will having a content security policy.


## 🌃 After Class

- Go through all 3 [Hacksplaining lessons on XSS](https://www.hacksplaining.com/lessons) and do the exercises and read the prevention page
- Finish any remaining [XSS Games](https://xss-game.appspot.com) levels

## 📚 Resources & Credits

- [XSS Prevention Cheat Sheet](https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet)
- [Acunetix XSS Article](https://www.acunetix.com/websitesecurity/cross-site-scripting/)
- [List of XSS attacks that can be used](https://gist.github.com/kurobeats/9a613c9ab68914312cbb415134795b45)