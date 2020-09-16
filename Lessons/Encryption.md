# 📜 Day 8: Intro to Encryption

[Source](https://medium.com/blockwhat/public-key-cryptography-a-comprehensive-guide-1e8489e08104)

<!-- omit in toc -->
## ⏱ Agenda {docsify-ignore}

- [[**05m**] 🏆 Objectives](#05m-%f0%9f%8f%86-objectives)
- [[**05m**] 📄 Vocabulary](#05m-%f0%9f%93%84-vocabulary)
- [[**60m**] 💻 Activity: Decoding a Secret Message (Continued)](#60m-%f0%9f%92%bb-activity-decoding-a-secret-message-continued)
- [[**15m**] ☀️ Warm Up: Prompt](#15m-%e2%98%80%ef%b8%8f-warm-up-prompt)
- [[**10m**] 💬 Discuss: Prompt](#10m-%f0%9f%92%ac-discuss-prompt)
- [[**15m**] 🌴 BREAK {docsify-ignore}](#15m-%f0%9f%8c%b4-break-docsify-ignore)
- [[**15m**] 📖 TT: History of Encryption](#15m-%f0%9f%93%96-tt-history-of-encryption)
- [[**15m**] 📖 TT: Public Key Encryption](#15m-%f0%9f%93%96-tt-public-key-encryption)
- [[**10m**] 💻 Activity: Word Cloud](#10m-%f0%9f%92%bb-activity-word-cloud)
- [[**15m**] 📖 TT: Digital Signatures](#15m-%f0%9f%93%96-tt-digital-signatures)
- [[**10m**] 📊 Vibe Check: Day 8](#10m-%f0%9f%93%8a-vibe-check-day-8)
- [📚 Resources & Credits](#%f0%9f%93%9a-resources--credits)

<!-- > -->

## [**05m**] 🏆 Objectives

1. Explain the difference between symmetric and asymmetric encryption.
2. Describe the basic process of encrypting data using public key encryption
3. Explain the benefits of public key cryptography

<!-- > -->

## [**05m**] 📄 Vocabulary

- **Asymmetric Encryption** - used in public key encryption, it is scheme in which the key to encrypt data is different from the key to decrypt.
- **Modulo** - a mathematical operation that returns the remainder after integer division. Example: 7 MOD 4 = 3
- **Private Key** - In an asymmetric encryption scheme the decryption key is kept private and never shared, so only the intended recipient has the ability to decrypt a message that has been encrypted with a public key.
- **Public Key Encryption** - Used prevalently on the web, it allows for secure messages to be sent between parties without having to agree on, or share, a secret key. It uses an asymmetric encryption scheme in which the encryption key is made public, but the decryption key is kept private.

<!-- > -->

## [**60m**] 💻 Activity: Decoding a Secret Message (Continued)

See [Cryptography.md](Cryptography.md#35m--activity-encoding-a-secret-message) for instructions on how to complete the first part of the activity we started last class period.

## [**15m**] ☀️ Warm Up: Prompt

Watch this [video](https://youtu.be/ZghMPWGXexs), then respond to the prompt below:

**Prompt**: "How can two people send encrypted messages to each other if they can't communicate, or agree on an encryption key ahead of time, and the only way they have to communicate is over the Internet?"

You should assume that an adversary is always secretly eavesdropping on their conversation too.

**With a partner come up with a strategy they could use to send encrypted messages**.

## [**10m**] 💬 Discuss: Prompt

Discuss student answers and give feedback.

After 10 minutes of discussion, transition to TT:

Today we're going to dig in a little bit deeper to how this idea of using different keys actually works. The ideas behind how it works are sophisticated, and so to get a deeper understanding we're going to do a series of short activities that stringing together several different ideas, bringing them all together in the end.


## [**15m**] 🌴 BREAK {docsify-ignore}

## [**15m**] 📖 TT: History of Encryption

![](https://miro.medium.com/max/1400/1*_TOwTSw57Ze01xIMzCDr8w.jpeg)

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

## [**15m**] 📖 TT: Public Key Encryption

![](https://miro.medium.com/max/1400/1*ou27uef_kSZs9WBJhQ1Wnw.jpeg)

The lock box analogy from the video is a good start, but our first step to seeing how public key cryptography works requires us to look at the same process of using public and private keys but with an analogy that goes a step further.

### Analogy: Cups and Beans

1. Alice choose a private key (some number of beans)
2. Alice make a "public key cup" by placing beans in a clear cup and sealing it
3. Pass the cup to Bob over the "Internet"
4. Bob grab the "public key cup" and add a secret number (of beans) to it
5. Pass the cup back to Alice over the "Internet"
6. Alice open cup and subtract the number of beans she added originally
7. What's left is Bob's secret number

**Discuss**: Relate this process using cups and beans to the lockbox analogy from the video.

- What's similar?
- What's different?
- What took place of the public key? The message? The private key?

### History

The story of this groundbreaking invention is a fascinating one — involving the British intelligence service “British Government Communications Headquarter” (GCHQ).

In 1969, a research scientist named John Ellis made one of the greatest breakthroughs in modern encryption and code breaking while working for GCHQ. His invention was so essential and far fetching to the future of information security, that the GCHG decided to keep it a secret for over 27 years — it was only declassified in 1997.

It’s an absolutely stunning piece of modern computer science history and if you’re enticed to read more about it, [just click right here](https://www.telegraph.co.uk/history/12191473/The-unsung-genius-who-secured-Britains-computer-defences-and-paved-the-way-for-safe-online-shopping.html).

As an interesting twist of history, the same concept that John Ellis came up with originally, was replicated at a public institution in 1976 — a team of researchers at MIT and Stanford then had the ability to publish their findings and they were originally credited with the invention. It wasn’t until many years later, that John Ellis got the recognition for his idea.

![](https://secure.i.telegraph.co.uk/multimedia/archive/03593/james_ellis4_3593310b.jpg)

So what exactly was so important that the British intelligence community decided to keep it a secret?

It’s a marvelous concept known as **Public Key Encryption** and the idea behind it is truly exceptional. While up to that point the responsibility of encrypting a message always laid on the sender of it, he thought out of the box and reversed the process — including the recipient in encrypting a message in a truly ingenious way.

It works as follows:

We start by taking a random string of numbers (e.g. 3860280357), from now on this will be called our *private key*) and mathematically derive another string of numbers from it — the resulting new string of numbers is called *public key*. A very important aspect of this process is, that it’s a so called *trap door function*, which means that it’s very easy to calculate it into one direction (ergo from *private key* to *public key*), but not the other way around (aka it’s almost impossible to derive the *private key* from the *public key*), without having some important information (aka the trapdoor).

This very abstract sounding concept enables us to do some marvelous things though, because we can now take a piece of data, use our *public key*and scramble it up ([by using some encryption magic](https://medium.com/searchencrypt/what-is-encryption-how-does-it-work-e8f20e340537)). For everybody out there this new data set is incomprehensible and unreadable. In order to unscramble it and to make it readable, one need to be in possession of the corresponding *private key*. Whoever has that key, can now use some mathematical magic and unscramble the data. Voila!

You can see this process illustrated in the picture below:

![](https://lisk.io/content/5-academy/2-blockchain-basics/4-how-does-blockchain-work/2-blockchain-cryptography-explained/6-public-key-cryptography-1.jpg)

You can think of this abstractly like this — the public address is your bank account and the private key is your secret PIN. The address can be safely broadcasted to the public, while it is indispensable to keep your PIN safe and secret.

This amazing new way of encrypting information made it become an Important mathematical foundation for information and computer security, since it helps to ensure authenticity and integrity of a message when communication over an unreliable channel of communication (e.g. the internet).

> “Strong, relatively cheap encryption became ‘democratised’ and enabled more secure communications on a global scale. Encryption went from being a tool of strategic advantage between super-power blocs, but to a key enabler of individual freedom and safety.”- Robert Hannigan, Director of GCHQ
The fact that the mathematical functions used in Public Key Cryptography have the unique characteristic that they are almost irreversible, meaning that they can only easily be calculated into one direction and not the opposing one, enabled something truly revolutionary — the creation of unforgeable **digital signatures** and digital secrets.

<!-- > -->


## [**10m**] 💻 Activity: Word Cloud

Complete the word cloud activity on [PollEverywhere](https://pollev.com/droxey)

## [**15m**] 📖 TT: Digital Signatures

A really cool thing you can do with this **public key encryption** is to digitally sign a document. In order to do this, instead of using the public key to scramble a message, we now use the private key.

By doing so, everybody can easily verify that we have digitally “signed” the document by checking if the corresponding hashes matches.

Below you have a lovely visualization of how this works.

![](https://exonum.com/blog/content/images/2018/02/CPKDSS@2x.jpg)

Digital signatures are at the core of how transactions work and can take place on a blockchain.

They are used as a mathematical scheme to prove the authenticity of a digital message, meaning that they prove ownership of a private key without revealing that private key. Crazy stuff!

<!-- > -->

## [**05m**] 🔑  Key Takeaways

Public Key Encryption was (and is) considered a major breakthrough in computer science.

- Public key cryptography is what makes secure transactions on the Internet possible.
- In the history of the Internet, the creation of public key cryptography is one of the most = - significant innovations; without it we could not do much of what we take for granted today --we couldn’t buy things, communicate without being spied on, use banks, or keep our own conduct on the Internet secret or private.
- Until asymmetric encryption was invented, the only way to ensure secure transactions on the Internet was to establish a shared private key, or to use a third party to guarantee security.
- The implications of this are huge. It means any person can send any other person a secret message transmitting information over insecure channels!


## [**10m**] 📊 Vibe Check: Day 8

Ask students to complete the [check for understanding](https://PollEv.com/surveys/cEg1FxGArsHp2VmkJebWe/respond) poll.

Discuss the answers before dismissing class.

## 📚 Resources & Credits

- [Code.org: Public Key Cryptography](https://curriculum.code.org/csp-1718/unit4/7/#public-key-cryptography11)
- [Public Key Cryptography — A Comprehensive Guide | by Till Antonio Mahler | blockwhat? | Medium](https://medium.com/blockwhat/public-key-cryptography-a-comprehensive-guide-1e8489e08104)
