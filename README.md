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

Daniela Lujan, Katya Torres

## 3. Project Objective

At the beginning we set out to achieve a two player rock, paper, scissor, lizard, and spock game but later we decided to make it multiplayer with an embedded score counter and the ability to talk. The [micro:bit](https://microbit.org/guide/features/) capabilities necessary for our implementation were the radio feature, the two programmable buttons, the 25 individually-programmable LEDs, the motion sensor and the pins for external connections.

## 4. Research

Throughout the process of constructing the project my partner and I consulted the instructor, various internet sources, and the [BBC micropython reference manual](https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html). We consulted the instructor to help us correct some of our code and to ask questions regarding the project itself. We consulted multiple internet sources searching for ideas for the entire project. We found very advanced projects with step by step tutorials such as the [Flappy Bird Game](https://youtu.be/MO-2DiHDZvg) or [an arcade game](https://youtu.be/99Z4KU8yHyc) but we wanted to design a more original idea to get the most experience from the project. Finally, to implement counting, radio, and images into our project we consult the [BBC micropython reference manual](https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html).   

## 5. Design

Our game, Multiplayer R. P. S.L.S., is programed to display one of the five weapons: rock, paper, scissors, lizard, or spock through the 25 individually-programmable LEDs when the microbit is shaken. Button a is programed to increase the score of the player by one when it’s pressed, indicating a win. When a player reaches a score of 5 the micro:bit automatically sends a message to all micro:bits in the same channel saying “Game Over”, a random message from a list, and then displays as well as says ”I win” when connected to a pair of headphones or a speaker. Button b is programmed to send a “I quit” message to other micro:bits, verbally say “Thank you for playing,” and break away from the game loop. 

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

*Describe your testing approach. What was successful and what failed?*

## 8. Demo

*Briefly record the results of the in-class demo.*

## 9. Summary

*Summarize your project, from idea to demo. Point out lessons learned. Mention the most important features of the micro:bit that supported your application.*
