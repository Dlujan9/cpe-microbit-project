# CPE micro:bit Term Project

Term project for students in the CPE 1040 course at MSUD, Fall 2018.

## Assignment

Design and implement some application of the [micro:bit](https://microbit.org/) educational computer. It can be a new design of your own or an already existing design from the Web.

### Language requirement

The implementation has to be in [MicroPython](https://microbit-micropython.readthedocs.io/en/latest/) (the version of Python that works on the micro:bit). 

**Note:** It is perfectly acceptable to take a project implemented in JavaScript/Blocks and rewrite it in MicroPython.

## Submission

### 1. Github

Fork and clone this directory and submit the URL of your fork (remote) on [Canvas](https://canvas.instructure.com/courses/1397722/assignments/10046266?module_item_id=20700270).

### 2. Individual

You can collaborate with one or two team mates on the design, implementation, and testing of the project, but you have to have *your own* separate Github repository and make an *individual* submission on Canvas.

### 3. Due date

**Sun, Dec 2, 2018, by 23:59**

**Note:** You can submit your URL at any time before the deadline on Canvas, but only your latest commit on Github before the deadline will be evaluated.

### 4. Project report

Write the project report in your README using the template provided below. 

**Note:** Projects without reports will receive **0 points** for the whole project.

### 5. Project demo

The project has to be demonstrated by the team in the lab period on **Wed, Nov 28**. Presentation slides are *optional* but will be noted in the evaluation of your submission. If you can't make this date, you can demo at any *earlier* date, but no later dates.

**Note:** The demo is not optional. If a project is not demonstrated, the grade will be at the discretion of the instructor.

## Grading

The project is worth a total of 600 points. Breakdown:

| Criterion | Points |
| --- |:---:|
| Functionality of application | 300 |
| Good use of [micro:bit](https://microbit.org/) capabilities | 100 |
| Input and output | 50 |
| Complexity of the application | 50 |
| Quality of demo | 50 |
| Clarity of report | 50 |

# Project Report

Fill out this template in place in the README of your own fork of the assignment repository. Put any supporting materials (diagrams, schematics, pictures, presentation slides, etc) in the [assets](assets) folder. You can reference them from this report. For example, [todo file](assets/todo.md). Use this [Markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) to format the report.

**Acknowledgement:** Adopted from [Bob Yusko](mailto:ryusko1@msudenver.edu).

## 1. Project Title

Multiplayer R.P.S.L.S.

## 2. Team

Daniela Lujan and Katya Torres

## 3. Project Objective

In the beginning, we set out to achieve a two-player rock, paper, scissors, lizard, and spock game but later we decided to make it multiplayer with an embedded score counter and the ability to talk. The [micro:bit](https://microbit.org/guide/features/) capabilities necessary for our implementation were the radio feature, the two programmable buttons, the 25 individually-programmable LEDs, the motion sensor and the pins for external connections.
## 4. Research

Throughout the process of constructing the project, my partner and I consulted the instructor, various internet sources, and the [BBC MicroPython reference manual](https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html). We consulted the instructor to help us correct some of our code and to ask questions regarding the project itself. We consulted multiple internet sources searching for ideas for the entire project. We found very advanced projects with step by step tutorials such as the [Flappy Bird Game](https://youtu.be/MO-2DiHDZvg) or [an arcade game](https://youtu.be/99Z4KU8yHyc) but we wanted to design a more original idea to get the most experience from the project. Finally, to implement counting, radio, and images into our project we consult the [BBC MicroPython reference manual](https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html).   

## 5. Design

Our game, Multiplayer R. P. S.L.S., is programmed to display one of the five weapons: rock, paper, scissors, lizard, or spock through the 25 individually-programmable LEDs when the micro:bit is shaken. Button a is programmed to increase the score of the player by one when it’s pressed, indicating a win. When a player reaches a score of 5 the micro:bit automatically sends a message to all micro:bits in the same channel saying “Game Over”, a random message from a list, and then displays as well as says ”I win” when connected to a pair of headphones or a speaker. Button b is programmed to send the message “I quit” to other micro:bits, verbally say “Thank you for playing,” and break away from the game loop. 

## 6. Development

While adding features to our game my partner and I came up with many ideas. A few are listed below along with a brief explanation on whether we succeeded in implementing them to our project.
1. We managed to implement a working counter to the R.P.S.L.S. by programming button a to increase the players score by one. We used the [rock, paper, scissors micro:bit tutorial](https://youtu.be/Jj4i0d27ZZI) in blocks as a quick guide for adding the counter.
2. We managed to make our game multiplayer by using the [micro:bit radio feature](https://microbit-challenges.readthedocs.io/en/latest/tutorials/radio.html 
) to communication between several micro:bits.
3. We thought about implementing a scoreboard for the game but ran into a significant amount of problems regarding how to effectively capture what we had in mind. Ultimately, we decide to move on to a different feature for the game.
4. We thought about implementing a timer for our game. We managed to be get a timer working by using the [running_time function](https://microbit-micropython.readthedocs.io/en/latest/tutorials/buttons.html?highlight=time) which returns the time in milliseconds since the device was turned on. In the end, we decided against it because it was what we were looking for the game.
5. We incorporated speech to our project by getting our micro:bits to talk through a pair of headphones throughout the game.
The article ["Make Your BBC Micro:Bit Talk Using MicroPython"](https://www.hackster.io/anish78/make-your-bbc-micro-bit-talk-using-micropython-7bdb10) made this final development possible.


## 7. Testing

Throughout the development of our project, my teammate and I found out that we couldn’t write the entire code first and then test it out. Doing so would merely cause many errors and we wouldn’t know what was working and what wasn’t. When I was working on making a new feature function such as making the micro:bit speak I would first write a very simplistic code and test it to find out if the micro: bit could indeed talk and be understood. I would then change the code a bit to make it meet my expectations and fix any errors that came up. Finally, I would implement the code to the larger project and test it out again. This process was successful, and therefore, continued throughout the project.

## 8. Demo

Despite being nervous about the in-class demo, we managed to answer all of the questions about the four parts of a computer (input, output, storage, and processing) for the demo and we had plenty of time to demonstrate our project. We used a [powerpoint](https://github.com/Dlujan9/cpe-microbit-project/blob/master/assets/Microbit%20Demonstration.pptx) with a few slides to reinforce our main points and didn’t add many words otherwise it would take away from our presentation. At the end of our presentation, I walked around the room to allow my classmates to hear the micro:bit talk. Overall, I think the demo went well each of us spoke around the same amount and kept eye contact with the class.


## 9. Summary

The idea for our project was to grow on the game rock, paper, scissors, lizard, spock by adding a counter, making it multiplier, adding speech, and adding a way to declare a winner and loser. The most important features that supported our application were the radio, the two programmable buttons, the 25 individually-programmable LEDs, the motion sensor and the pins for external connections. Without these features, the game would be unable to functions properly and several of the added features would not work. For instance, without the pins the micro:bits would be incapable of speech. The demos were delightful. It was enjoyable to see different projects with their own original ideas and sharing ours as well. Ultimately, I learned that starting a new project is hard and you have to do tons of research to figure out what you want to spend your time on. Afterward, you must create a plan to make sure that when the deadline rolls around you have a functional project to demonstrate. Creating a project is a learning process you have to find out what works and what doesn’t as well as make adjustments along the way.

