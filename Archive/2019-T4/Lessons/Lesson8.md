# 📜 Day 8: Large Scale Attacks, Real World Defenses

### ⏱ Agenda

1. [🏆 [**5m**] Learning Objectives](#%f0%9f%8f%86-5m-learning-objectives)
2. [💻 [**20m**] In Class Activity: Dissecting a DDoS](#%f0%9f%92%bb-20m-in-class-activity-dissecting-a-ddos)
3. [📖 [**10m**] Overview: DDoS & Features](#%f0%9f%93%96-10m-overview-ddos--features)
4. [💻 [**10m**] In Class Activity: Think / Pair / Share](#%f0%9f%92%bb-10m-in-class-activity-think--pair--share)
5. [📖 [**10m**] Overview: Creating / Using a Botnet](#%f0%9f%93%96-10m-overview-creating--using-a-botnet)
6. [🌴 [**10m**] BREAK](#%f0%9f%8c%b4-10m-break)
7. [💻 [**60m**] In Class Activity](#%f0%9f%92%bb-60m-in-class-activity)
8. [🌃 After Class](#%f0%9f%8c%83-after-class)
9. [📚 Resources & Credits](#%f0%9f%93%9a-resources--credits)

## 🏆 [**5m**] Learning Objectives

1. Gain insight into real world large scale attacks and how to defend against them.
2. Implement the foundational architecture for your own custom botnet, using the BYOB framework.

## 💻 [**20m**] In Class Activity: Dissecting a DDoS

1. Read this article: [How To Accidentally Stop a Global Cyber Attack](https://www.malwaretech.com/2017/05/how-to-accidentally-stop-a-global-cyber-attacks.html).
2. **Challenge**: Reverse engineer Marcus Hutchins' solution that prevented the spread of the attack. How did he figure it out?
3. **Stretch Challenge**: Why did it work? Explain in detail.

## 📖 [**10m**] Overview: DDoS & Features

The work of a Distributed Denial of Service attack is typically done by a [botnet](https://en.wikipedia.org/wiki/Botnet).

**Computers can be co-opted into a botnet when they execute malicious software**.

This can be accomplished by luring users into making a drive-by download, exploiting web browser vulnerabilities, or by tricking the user into running a Trojan horse program, which may come from an email attachment.

Botnets typically **install modules** that allow the computer to be **commanded and controlled** by the botnet's operator.

After the software is downloaded, it will **call home** to the host computer. When the re-connection is made, a bot may then delete itself or remain present to update and maintain the modules at the operator's behest.

### Features of a Botnet

- **Submit as many requests as possible** to a single computer or service, overloading it and preventing it from servicing legitimate requests.
  - **Example**: A victim's server is bombarded with requests by the bots attempting to connect to the server, therefore, overloading it.
- **Install spyware** to gain access to sensitive information. See the Aurora botnet for more details.
- E-mail spam and phishing abilities **disguised as messages from people**.
  - Can be advertising, annoying, or malicious.
- **Click fraud**: when a user's computer visits websites without their awareness to create false web traffic.
  - For personal or commercial gain.
- **Bitcoin mining** in order to generate profits for the operator of the botnet.
- **Self-spreading functionality** to aim for more infection, is also spotted in several botnets. Some of the botnets are utilizing this function to automate their infections.

## 💻 [**10m**] In Class Activity: Think / Pair / Share

1. **Brainstorm** some features you'll incorporate into your botnet project.
2. **Choose one or two** that you're interested in implementing.
3. **Share** that feature with the person next to you and get feedback on it!

## 📖 [**10m**] Overview: Creating / Using a Botnet

This example illustrates **how a botnet is created and used for malicious gain**:

1. A hacker purchases or builds a Trojan and/or exploit kit and uses it to start infecting users' computers, whose payload is a malicious application—the bot.
2. The bot instructs the infected PC to connect to a particular command-and-control (C&C) server.
   1. This allows the botmaster to keep logs of how many bots are active and online.
3. The botmaster may then use the bots to gather keystrokes or use form grabbing to steal online credentials and may rent out the botnet as DDoS and/or spam as a service or sell the credentials online for a profit.
4. Depending on the quality and capability of the bots, the value is increased or decreased.

### Advanced Botnets

Newer, more advanced botnets will **scan the environment** and gain access to additional resources through a periodic system scan.

The most valuable botnets scan for the highest number most relevant system exploits and report back to the owner each and every vulnerability that exists in the system at the time of scanning.

## 🌴 [**10m**] BREAK

## 💻 [**60m**] In Class Activity

Break into groups of two or three, and get to know the features that the [BYOB Framework](https://github.com/malwaredllc/byob) offers you.

Make sure you work with your team to **read and understand the open source code** written for each feature!

Each team will **Slack a summary of the documented implementation details of their assigned feature, listed below**:

- **[Client](https://github.com/malwaredllc/byob#client)**
- **[Server](https://github.com/malwaredllc/byob#server)**
- **[Core](https://github.com/malwaredllc/byob#core)**
- [Modules](https://github.com/malwaredllc/byob#modules):
  - **Keylogger**
  - **Screenshot**
  - **Packet Sniffer**
  - **Persistence**
  - **Phone**
  - **Escalate Privileges**
  - **Port Scanner**
  - **Process Control**
  - **iCloud**
  - **Spreader**
  - **Miner**

If you finish early, skip ahead to the After Class section!

## 🌃 After Class

1. **Find a Partner**: You may work on the final project with a partner, as long as each of you implement your own feature in the botnet you submit!
2. **Scope the Project**: Which features will you use in your botnet?

## 📚 Resources & Credits

- [**Wikipedia: Botnets**](https://en.wikipedia.org/wiki/Botnet)
