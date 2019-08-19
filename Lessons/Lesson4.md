# 📜 Day 4: Securing Data: Sanitization & Validation

## ⏱ Agenda

- Learning Objectives
- What is Sanitization?
- Client Side Sanitization using String Parsers
- Server Side Sanitization
- Client Side Sanitzation using server side code

## 🏆 Learning Objectives

By the end of this lesson, you should be able to...

1. Identify where sanitization should be applied
1. Differentiate and apply frontend and backend sanitization

## 📖 Overview

![xkcd](Lesson4Assets/xkcd.png)

Most web applications allow for some form of user input, whether it's a search bar, writing a message, filling out a form, or some other form of user input.

If we allow for anyone to put whatever they want, this leaves us open to vulnerabilities due to potential attackers providing malicious input. While we can provide safeguards as discussed in previous lessons, we can also just make sure that all areas of user input have proper **sanitization and validation** to avoid an exploit.

## What is Sanitization?

Cleaning up input so that it can not be executed as code. Any plain text that is part of the the content for page that is code will be treated as code!

To prevent malicious scripts from running in your pages all input needs to be sanitized. This process converts all special characters to HTML entities or removes dangerous elements like `<script>` or `' OR 1 = 1;`

### Client Side vs Server Side

Some of the code you write only runs on the server. These are things like getting and putting information into the database.

Other code runs in the browser or client computer. This is usually code that handles user interaction and manages content from the browser.

Depending on where you are using user input you will want to sanitize from one side or the other, probably both.

## Client Side Sanitization - String Parser

### String Parser

One method of client side santization is by using a **string parser** to replace certain – generally problematic – strings with sanitized equivalents. We can do this a few different ways:

- [**HTML Entities**](https://developer.mozilla.org/en-US/docs/Glossary/Entity) - HTML entities are character sequences that represent special characters. For example, `&` can be equally represented as `&amp;`
- [**CSS Escapes**](https://developer.mozilla.org/en-US/docs/Web/API/CSS/escape) - escapes any string passed as a parameter. For example: `CSS.escape(".foo#bar") // "\.foo\#bar"`
- [**URL Encoding**](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding) - Similar to HTML entities, URL encoding is a way to encode certain characters that have specific meaning in the context of URLs without actually using the characters themselves. For example, `+` can be represented as `%2B`

### 💻 Activity: Write Your Own Sanitization Script

Using any of the above techniques, write a sanitization function that prevents a user from inputting `<script>`, `' OR 1 = 1;`, or any type of URL manipulation that you can think of.

The instructor will check in on progress throughout this and then have 1-2 students present their script for review. We'll also take this time for the instructor to share some tips/tricks/info writing these sanitization scripts.

## Server Side Sanitization

On the server side, there's a lot more tools available for us to use. Use a library like [DOMPurify](https://github.com/cure53/DOMPurify) or write your own sanitization script but, if you're working with Express JS you have access to middleware, such as [express-sanitzier](https://www.npmjs.com/package/express-sanitizer)

### 💻 Activity: Write Your Own Sanitization Script

Take an old project or tutorial, and integrate express-sanitzier or DOMPurify to it to sanitize your server side code!

The instructor will check in on progress throughout this and then have 1-2 students present their script for review. We'll also take this time for the instructor to share some tips/tricks/info writing these sanitization scripts.

## 🌴 Break

## Client Side Sanitization - Browserify

When working with Node and Express you are managing dependancies on the server side. These files are not accessible in the browser.

You can use [Browserify](http://browserify.org/) to bundle JavaScript files into a single file that can be used by the client browser. This allows you to leverage NPM libraries on the Client.

You'll use Browserify to collect JavaScript libraries into a single file that you can link to from the client.

### Quick Note: Immediately Invoked Function Expressions (IIFE)

**Immediately Invoked Function Expression (IIFE)** is the key to managing large amounts of JavaScript code. By using IIFEs, you can:

- Isolate variables and functions from the global name space.
- Make code portable

This allows you to further protect your code. [Read more about IIFEs here](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)


### 💻 Activity: Browserify + DOMPurify Santization

- Follow the [instructions](http://browserify.org) to install and set up Browserify
- Define a Public static folder in Express. Express only serves files from routes. To serve static files you will need to designate a static folder:

```js
// Serve static resources from the public folder
app.use(express.static('public'));
```

- Install [DOMPurify](https://github.com/cure53/DOMPurify) and use it to make a client-side sanitization script. You will have to run all of your client JS from a module! 


## 🌃 After Class

Add server/client sanitzation to another project, and put the link to your commit in the course tracker