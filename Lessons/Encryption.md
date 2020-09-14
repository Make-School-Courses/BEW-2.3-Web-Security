# 📜 Day 8: Intro to Encryption

[Source](https://medium.com/blockwhat/public-key-cryptography-a-comprehensive-guide-1e8489e08104)

<!-- omit in toc -->
## ⏱ Agenda {docsify-ignore}

- [[**05m**] 🏆 Objectives](#05m-%f0%9f%8f%86-objectives)
- [[**30m**] 💻 Warm Up: Decoding a Secret Message (Continued)](#30m-%f0%9f%92%bb-warm-up-decoding-a-secret-message-continued)
- [[**15m**] 📖 TT: History of Encryption](#15m-%f0%9f%93%96-tt-history-of-encryption)
- [[**15m**] 📖 TT: Public Key Encryption](#15m-%f0%9f%93%96-tt-public-key-encryption)
- [[**15m**] 📖 TT: Digital Signatures](#15m-%f0%9f%93%96-tt-digital-signatures)
- [[**15m**] 🌴 BREAK](#15m-%f0%9f%8c%b4-break-docsify-ignore)
- [[**45m**] 💻 Activity: Encoding a Secret Message](#45m-%f0%9f%92%bb-activity-encoding-a-secret-message)
- [🌃 After Class](#%f0%9f%8c%83-after-class)
- [📚 Resources & Credits](#%f0%9f%93%9a-resources--credits)

<!-- > -->

## [**05m**] 🏆 Objectives

<!-- |   Level   | Verbs |
| --------- | ----- |
| 6: Create | design, formulate, build, invent, create, compose, generate, derive, modify, develop |
| 5: Evaluate | choose, support, relate, determine, defend, compare, contrast, justify, support, convince, select |
| 4: Analyze | classify, break down, categorize, analyze, diagram, illustrate, criticize, simplify, associate |
| 3: Apply | calculate, predict, apply, solve, illustrate, use, demonstrate, determine, model, perform, present |
| 2: Understand | describe, explain, paraphrase, restate, summarize, contrast, interpret, discuss |
| 1: Remember | list, recite, outline, define, name, match, quote, recall, identify, label, recognize | -->

<!-- > -->

## [**30m**] 💻 Warm Up: Decoding a Secret Message (Continued)

[Cryptography](Lessons/Cryptography.md#35m-%f0%9f%92%bb-activity-decoding-a-secret-message ':include')

## [**15m**] 📖 TT: History of Encryption

Photo by [rawpixel](https://unsplash.com/photos/EF8Jr-uPS2Y?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

The origins of our story today reach a long time back into hour past, a couple thousands of years…

Cryptography has always played an important role in ensuring that sensitive information did not fall into the wrong hands — back then, these were mostly military secrets.

One of the most famous encryption methods used to be the so-called [**Julius Caesar Cypher**,](https://learncryptography.com/classical-encryption/caesar-cipher) which you all have probably also used in the exciting days of your childhood when you wanted to send secret messages to your friends. The way this method works is pretty straightforward — you apply a simple mathematical logic to the message that you want to encrypt. For example, that you move back three letters to the left from the original letter that you want to send.

So if we want to encrypt an “H”, we go three letters to the left and end up with an “E”.

ABCDEFG**H** -> ABCD**E**FGH

You can see a nice visualization of this concept below.

[Source](https://lisk.io/content/5-academy/2-blockchain-basics/4-how-does-blockchain-work/2-blockchain-cryptography-explained/5-julius-caesar-encryption.gif)

During the centuries, the methods of encrypting messages became more and more sophisticated. Especially the evolving field of complex mathematics lead to innovative and strong new ways of encrypting and decrypting of information. This made sure that the information could only be viewed by the intended recipients and nobody else.

The way these techniques work are known as **symmetric key encryption.** This method uses complex mathematical concepts to encrypt information with a so-called private key. The message was now unreadable to everybody and could only be reversed to the original state by applying the same private key. In order to use this form of encryption, the corresponding private key had to be shared with everybody who was supposed to be able to read the secret messages (e.g. generals in the army, ambassadors, etc.).

This system of using a private key to encrypt and decrypt information turned out to be pretty secure — as long as nobody unintended had also access to this private key. The keys had to be regularly changed though, just in case the key or the person carrying it fell into the wrong hands.

Below you can see a great visualization of this concept.

[Source](https://lisk.io/content/5-academy/2-blockchain-basics/4-how-does-blockchain-work/2-blockchain-cryptography-explained/4-symmetric-key-cryptography.jpg)

One very famous example of symmetric-key cryptography was the [**Enigma machine**](https://en.wikipedia.org/wiki/Enigma_machine) that the German Military used in the second world war to encrypt their messages. The allied forces had a very hard time breaking the code used by the Germans — [until Alan Turing brilliantly managed to crack it](https://www.iwm.org.uk/history/how-alan-turing-cracked-the-enigma-code).

So far we’ve read about the **Julius Caesar cypher** and **symmetric key encryption** (also known as private key encryption) — let’s focus on the truly revolutionary invention of **public key encryption** next!


<!-- > -->



<!-- > -->

## [**15m**] 📖 TT: Public Key Encryption

Photo by [Micah Williams](https://unsplash.com/photos/lmFJOx7hPc4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

The story of this groundbreaking invention is a fascinating one — involving the British intelligence service “British Government Communications Headquarter” (GCHQ).

In 1969, a research scientist named John Ellis made one of the greatest breakthroughs in modern encryption and code breaking while working for GCHQ. His invention was so essential and far fetching to the future of information security, that the GCHG decided to keep it a secret for over 27 years — it was only declassified in 1997.

It’s an absolutely stunning piece of modern computer science history and if you’re enticed to read more about it, [just click right here](https://www.telegraph.co.uk/history/12191473/The-unsung-genius-who-secured-Britains-computer-defences-and-paved-the-way-for-safe-online-shopping.html).

As an interesting twist of history, the same concept that John Ellis came up with originally, was replicated at a public institution in 1976 — a team of researchers at MIT and Stanford then had the ability to publish their findings and they were originally credited with the invention. It wasn’t until many years later, that John Ellis got the recognition for his idea.

[Source](https://secure.i.telegraph.co.uk/multimedia/archive/03593/james_ellis4_3593310b.jpg)

So what exactly was so important that the British intelligence community decided to keep it a secret?

It’s a marvelous concept known as **Public Key Encryption** and the idea behind it is truly exceptional. While up to that point the responsibility of encrypting a message always laid on the sender of it, he thought out of the box and reversed the process — including the recipient in encrypting a message in a truly ingenious way.

It works as follows:

We start by taking a random string of numbers (e.g. 3860280357), from now on this will be called our *private key*) and mathematically derive another string of numbers from it — the resulting new string of numbers is called *public key*. A very important aspect of this process is, that it’s a so called *trap door function*, which means that it’s very easy to calculate it into one direction (ergo from *private key* to *public key*), but not the other way around (aka it’s almost impossible to derive the *private key* from the *public key*), without having some important information (aka the trapdoor).

This very abstract sounding concept enables us to do some marvelous things though, because we can now take a piece of data, use our *public key*and scramble it up ([by using some encryption magic](https://medium.com/searchencrypt/what-is-encryption-how-does-it-work-e8f20e340537)). For everybody out there this new data set is incomprehensible and unreadable. In order to unscramble it and to make it readable, one need to be in possession of the corresponding *private key*. Whoever has that key, can now use some mathematical magic and unscramble the data. Voila!

You can see this process illustrated in the picture below:

[Source](https://lisk.io/content/5-academy/2-blockchain-basics/4-how-does-blockchain-work/2-blockchain-cryptography-explained/6-public-key-cryptography-1.jpg)

You can think of this abstractly like this — the public address is your bank account and the private key is your secret PIN. The address can be safely broadcasted to the public, while it is indispensable to keep your PIN safe and secret.

This amazing new way of encrypting information made it become an Important mathematical foundation for information and computer security, since it helps to ensure authenticity and integrity of a message when communication over an unreliable channel of communication (e.g. the internet).

> “Strong, relatively cheap encryption became ‘democratised’ and enabled more secure communications on a global scale. Encryption went from being a tool of strategic advantage between super-power blocs, but to a key enabler of individual freedom and safety.”- Robert Hannigan, Director of GCHQ
The fact that the mathematical functions used in Public Key Cryptography have the unique characteristic that they are almost irreversible, meaning that they can only easily be calculated into one direction and not the opposing one, enabled something truly revolutionary — the creation of unforgeable **digital signatures** and digital secrets.

<!-- > -->

## [**15m**] 📖 TT: Digital Signatures

[file:E197AE5C-CC6B-4EDB-B5CC-2C7FE3AEF4A5-17894-000031A01AEFEF95/1*DOkMZGpaJItaW3W1oa_Daw.jpeg?q=20]img

[image:E929DE48-AA73-48E7-8415-DE6F4AF9ECA4-17894-000031A023C96667/1*DOkMZGpaJItaW3W1oa_Daw.jpeg]img

Photo by [Art Lasovsky](https://unsplash.com/photos/8XddFc6NkBY?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

A really cool thing you can do with this **public key encryption** is to digitally sign a document. In order to do this, instead of using the public key to scramble a message, we now use the private key.

By doing so, everybody can easily verify that we have digitally “signed” the document by checking if the corresponding hashes matches.

Below you have a lovely visualization of how this works.

[image:F1BDF2AC-9040-4BFA-8342-D0ABC341303C-17894-000031A030B9F13C/0*_MKT3oUju5QzuDS0?q=20.jpeg]img

[image:B36D5A6E-9AEC-4344-81C1-1E04141CA6DF-17894-000031A03B7B434C/0*_MKT3oUju5QzuDS0.jpeg]img

[Source](https://exonum.com/blog/content/images/2018/02/CPKDSS@2x.jpg)

Digital signatures are at the core of how transactions work and can take place on a blockchain.

They are used as a mathematical scheme to prove the authenticity of a digital message, meaning that they prove ownership of a private key without revealing that private key. Crazy stuff!


<!-- > -->



<!-- > -->




## [**15m**] 🌴 BREAK {docsify-ignore}

## [**45m**] 💻 Activity: Encoding a Secret Message

Now that we can decode secret messages, it’s only natural that we want to encode some too! Provided in the starter code are a pair of functions called `write_text()` and `encode_image()`. `write_text()` will take a string and convert it to a black and white image of the string. You may use it as a helper function in completing your implementation of `encode_image()`.

<!-- > -->

## 🌃 After Class

`TODO`

<!-- > -->

## 📚 Resources & Credits

`TODO`

