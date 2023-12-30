---
layout: post
title:  "Advent of Code in Ansible, The Oops!"
date:   2023-12-29 12:00:00 +0100
tags: [tech]
tabtitle: diademiemi | AoC 2023 Ansible, The Oops!

---
This post covers days 1 through 7... I made a mistake......

{% raw %}

# Oops!

In my [previous post](/blog/2023/12/04/AoC2023-Ansbible-Start/) I introduced how I'm challenging myself to write Advent of Code 2023 in Ansible. Please read that post first if you haven't already! It introduces why this is a challenge, and how I hope to do it.

I also mentioned that I would be posting a weekly update on my progress. A month later... Well, I made a mistake. I underestimated the amount of time I would need to complete the challenges, and how impossible they'd feel.. I did not think it would start this difficult, and the later challenges seem almost impossible.

For now, I'm taking a break, but I will continue this challenge and chip away at it. I will not be posting weekly updates, but I will post updates when I've completed a day. I will also post a final update when I've completed all the challenges (or when I officially give up).

I've completed days 1 through 7, with the exception of day 5 part 2. I'm currently stuck on that one... Brute forcing it is how I'd want to solve it, but well... I'll get into it.

Remember, the actual input is much much MUCH larger! Even if the example input looks easy, trust me, it gets worse!

# Days 1 through 7

## Day 1
Challenge: [adventofcode - day 1](https://adventofcode.com/2023/day/1)  
My solution: [diademiemi/ansible_advent_of_code_2023 / day1](https://github.com/diademiemi/ansible_advent_of_code_2023/blob/main/roles/day1/tasks/main.yml)

<details><summary>Day 1 Solution Code</summary>

<script src="https://gist.github.com/diademiemi/93ded02c55902b63b9168c29096432d9.js"></script>

</details>

We start off pretty easy! The challenge basically boils down to some basic string queries across a list of strings, then to sum the answers.

The most complicated part of this is needing to use a regex lookahead in part two. The reason for this is that integers can now overlap with each other.

Take for example an example "oneight", this should match both "one" and "eight". But if we were to use a regex like `one|two|three|four|five|six|seven|eight|nine`, it would match "one" and then stop, not counting "eight" as a seperate match. This is where the lookahead comes in, it allows us to match all the numbers in the string.

It's really not that bad! This is what gave me hope this challenge would be doable.

## Day 2
Challenge: [adventofcode - day 2](https://adventofcode.com/2023/day/2)  
My solution: [diademiemi/ansible_advent_of_code_2023 / day2](https://github.com/diademiemi/ansible_advent_of_code_2023/blob/main/roles/day2/tasks/main.yml)

<details><summary>Day 2 Solution Code</summary>

<script src="https://gist.github.com/diademiemi/4b3b071fb50136702ed67c9edb21fc8f.js"></script>

</details>

Day two ups the difficulty a bit, but it's still not too bad. We just need to first parse the data and then run some basic checks on it.


The most difficult part of this challenge is the parsing, but that's not too bad either. 
I don't have a lot to say about day 2 either, it's a pretty straightforward challenge. This definitely kept the dream alive that I could complete this challenge.

## Day 3
Challenge: [adventofcode - day 3](https://adventofcode.com/2023/day/3)  
My solution: [diademiemi/ansible_advent_of_code_2023 / day3](https://github.com/diademiemi/ansible_advent_of_code_2023/blob/main/roles/day3/tasks/main.yml)  

<details><summary>Day 3 Solution Code</summary>

<script src="https://gist.github.com/diademiemi/8b137a2d8df42cd856c8d266f865235f.js"></script>

</details>

NOWWWWWWW this is where it gets difficult. In day 3 we get some ASCII art, Ansible definitely isn't great at parsing that... And then we need to get data from it and do calculations based on the art... Uh oh.

What we do here is:
- Split the input into a list of strings
- Split each string into a list of characters, this gives us a two-dimensional array we can loop over!
- Loop over the array for every coordinate we need to check

For every coordinate we:
- Check if our current position is a number
- If it is, we parse the number
- For every position we're at / parsed, we add to a list so we don't count it twice
- We get a list of all surrounding characters
- We check if this number is surrounded by a special character
- (Part 2) we get the gears (* symbols) and create a dictionary with the gear coordinate along with the related numbers

After that, we just need to do some calculations and we're done!
- Sum all integers surrounded by special characters
- (Part 2) Multiply all numbers in the dictionary with the related gear if there are exactly 2 numbers

Now.. The input is 140x140 characters, and we need to loop over every single character and do MANY operations. This is what makes it. Really. REALLY. Slow.

Whew... That one... Took a while. Not only did it take a while to write, it also took a while to run. It took a whopping 7 hours to run on a Ryzen 9 7950X! This is where we REALLY run into Ansible's limitations. It's not really meant for this kind of stuff, but I'm not giving up yet!

## Day 4
Challenge: [adventofcode - day 4](https://adventofcode.com/2023/day/4)  
My solution: [diademiemi/ansible_advent_of_code_2023 / day4](https://github.com/diademiemi/ansible_advent_of_code_2023/blob/main/roles/day4/tasks/main.yml)  

<details><summary>Day 4 Solution Code</summary>

<script src="https://gist.github.com/diademiemi/4dde241de33e87497a03bfb228b6b897.js"></script>

</details>

Day 4 isn't tooooooo bad, we just gotta parse the input and do some pretty basic math in a loop. Part two gets really hard, since it involves recursion.

Part one is pretty self explanatory, we just compare numbers and get count how many points we've gotten.

Part two gets tough, it turns out we have to incorperate recursion.. Or do we?

Actually, we can just loop over the list once, and just increment the next card by how many cards of the current card we have already. You can read the code above to see how I did it, it's got comments in the Jinja2 template!

## Day 5
Challenge: [adventofcode - day 5](https://adventofcode.com/2023/day/5)  
My solution: [diademiemi/ansible_advent_of_code_2023 / day5](https://github.com/diademiemi/ansible_advent_of_code_2023/blob/main/roles/day5/tasks/main.yml)  

<details><summary>Day 5, Part 1 Solution Code</summary>

<script src="https://gist.github.com/diademiemi/498113659f8a76ed4b7a0f6ee9a130d9.js"></script>

</details>

Day 5 part one starts of pretty easy! It's part two thats tough...

For part one, we can just loop over the seed numbers and go through every map with them. We do this in a rather large Jinja2 loop, but it's doable.

Now...... Part two. Part two makes the seeds ranges. The smart way to do this is to create a "Range" class, and only compare the lowest number on every result. But this is Ansible, we don't have classes, we don't have functions, we don't have shit. It is possible to brute force this, and I've gotten this working on the test input. However, the numbers on the actual input are in the range of MILLIONS, not dozens. This means we really can't brute force this. Trust me, I tried, and my PC froze twice from running out of all 64GB of memory.

## Day 6
Challenge: [adventofcode - day 6](https://adventofcode.com/2023/day/6)  
My solution: [diademiemi/ansible_advent_of_code_2023 / day6](https://github.com/diademiemi/ansible_advent_of_code_2023/blob/main/roles/day6/tasks/main.yml)  

<details><summary>Day 6 Solution Code</summary>

<script src="https://gist.github.com/diademiemi/f05afa3ba1c70528639dda95057aefb3.js"></script>

</details>

Day 6! Almost at the end of the week... a month later. Day 6 is pretty easy, the input is small too.

Day 6 wants you to do some quadratics shit and some weird formulas. Wellllllll... I don't know any of those, so I just brute forced it.

The brute force does work this time! Even part two, which was obviously designed to prevent you from brute forcing it ran in a decent 6 minutes. Not bad!

## Day 7
Challenge: [adventofcode - day 7](https://adventofcode.com/2023/day/7)  
My solution: [diademiemi/ansible_advent_of_code_2023 / day7](https://github.com/diademiemi/ansible_advent_of_code_2023/blob/main/roles/day7/tasks/main.yml)  

<details><summary>Day 7 Solution Code</summary>

<script src="https://gist.github.com/diademiemi/828dada2d2ed08c58f581c06adbad8ba.js"></script>

</details>

Day 7, we're at the end of the week, at the end of the month!... 

This took me a while to even understand what's going on here, but it ends up pretty simple.

If we order count how many occurances there are of each card and order that list we can match that into hand types. Then if we count the points on that, we can compare that to the bids to get the answer!

Part two is a pretty straight forward change, we just create a map of possible upgrades, and move our hand up one for every "J" card. To make sure we don't count the "J" cards in the new hand, we do a messy trick and replace them with a different character.


# Conclusion
So... I kinda regret starting this to be perfectly honest. This is much more demanding than I anticipated! And to be very honest I don't expect to fully complete this challenge.

But! I will still be chipping away at it throughout the new year, and I will post updates when I feel like it's worth posting one! I'm hoping I can at least get half of the points for the 2023 year.

... Not a chance in hell I'm doing this again for 2024 though.

{% endraw %}
