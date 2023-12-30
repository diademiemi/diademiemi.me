---
layout: post
title:  "Advent of Code in Ansible, The Start"
date:   2023-12-04 12:00:00 +0100
tags: [tech]
tabtitle: diademiemi | AoC 2023 Ansible, The Start

---
Last year I had the terrible idea of doing AoC in Ansible. After 8 days, I gave up. This year, I'm determined.

{% raw %}
## Introduction

Hi! I work with Ansible every day, and it's a tool I love! I've been familiar with it for over 2 years now, and it's great for managing servers, automating desktop tasks and clusters. All stuff that it's intended for.

But I've always wondered, Ansible is very flexible, but how far can you push it?

Can you use it for something that it's not intended for? Can you use it for something that's not even remotely related to it's intended purpose? To find that out, I want to try this again, let's do Advent of Code in Ansible. Doing math and logic puzzles in Ansible sounds like it'd be impossible, but what if it isn't? 

I'll be documenting my progress here, showcasing my favourite (or most hated!) snippets from solutions and I'll be posting my full solutions to my GitHub [diademiemi/ansible_advent_of_code_2023 repository](https://github.com/diademiemi/ansible_advent_of_code_2023). My plan is to write a blog post at the end of each week, showcasing my solutions for that week with some commentary on how I got there, what I feel about the solution and what I learned from doing it!

Some solutions will likely end up being *very* out there, overengineered and hacky, but that's the fun of it, right? 

### So... Why is this interesting?

#### What's Ansible?
Ansible is a tool for automating deployments of servers and applications. It's a tool first and foremost designed for sysadmins and developers.

Let's see an example of some Ansible code, to get an idea of what it looks like and what it's intended for!
```yaml
- name: Install the latest version of Apache
  ansible.builtin.yum:
    name: httpd
    state: latest
  # Conditionally execute this task based on the ansible_pkg_mgr variable
  # These variables are automatically set by Ansible.
  # Ooh, conditionals.. We'll be using these a lot!
  # And variables... That will prove useful!
  when: ansible_pkg_mgr == 'yum'

- name: Install the latest version of Apache
  ansible.builtin.apt:
    name: apache2
    state: latest
  # Do the same thing, but for apt instead of yum
  when: ansible_pkg_mgr == 'apt'

- name: Start the Apache service and enable it on boot
  ansible.builtin.service:
    # Some inline templating, remember this!
    name: "{% if ansible_os_family == 'RedHat' %}httpd{% else %}apache2{% endif %}"
    state: started
    enabled: true

- name: Copy three configuration files
  ansible.builtin.copy:
    src: "{{ item.src }}"
    dest: "{{ item.dest }}"
  # Loop over a list of dictionaries
  # Hey, we can loop over stuff! That's useful!
  # Wait, did you say lists and dictionaries? Data structures? We'll need those!
  loop:
    - src: httpd.conf
      dest: /etc/httpd/conf/httpd.conf
    - src: ports.conf
      dest: /etc/httpd/conf.d/ports.conf
    - src: virtual.conf
      dest: /etc/httpd/conf.d/virtual.conf

```

Let's break down what this does:
 - It installs Apache, but it does it differently depending on the package manager (yum or apt)
 - It starts the Apache service and enables it on boot, this is done differently depending on the OS family (RedHat or Debian)
 - It copies three configuration files, this is done using a loop over a list of dictionaries with the source and destination for each file

So while Ansible is "just" a tool for automating deployments, it's a very flexible tool. It's not just a tool for installing packages, it's a tool for automating deployments, so to assist in that it features all kinds of flow control and templating features.

#### Wait! What's Advent of Code anyway?
For those unaware, Advent of Code is an annual event where every day in December, a new puzzle is released. These puzzles are logic puzzles, math problems, and other similar puzzles. They're intended to be solved with programming, and they're a lot of fun!

So wait, that doesn't sound like something you'd use Ansible for, right? Well, that's the point! :)
How far can we push Ansible? That's what I want to find out!

## Hope
So what gives me hope that this is even remotely possible?

### What could help us?

Well, like I showed in the example, Ansible features inline templating with the powerful Jinja2 engine. This allows us to manipulate the data given to us! Ansible also extends this by adding some filters and tests. Most of these are pretty limited wrappers around basic Python functions, but they're still useful.

Let's see some examples of this in action. Let's say I have a variable called `my_var` that contains the string `Hello, World`. I can use the `upper` filter to convert it to uppercase.

```yaml
- name: Convert my_var to uppercase
  ansible.builtin.debug:
    msg: "{{ my_var | upper }}"
```

This will output the following:
```json
"msg": "HELLO, WORLD"
```

### A practical example

Now that's not.. very helpful. But let's do something we'll need to do in AoC. Let's say we have this as input:
```yaml
my_var: |-  # All AoC input is a multiline string
  Example 1: Message is Hello
  Example 2: Message is World
  Example 3: Message is Goodbye
  Example 4: Message is World
```

We want to make this easier to parse, what are some ways we could transform this data into something easier to use?

We could easily simplify this to an easier to access data structure by using the following filters in this order:
 - `split('\n')`, which splits the string into a list of lines
 - `map('split', ': ')`, which executes `split(': ')` on each item in the list, resulting in a list of lists

```yaml
- name: Convert my_var to a dictionary
  ansible.builtin.debug:
    msg: "{{ my_var | split('\n') | map('split', ': ') | list }}"
```

Now... this still isn't that helpful, because look at the output:
```json
"msg": [
    [
        "Example 1",
        "Message is Hello"
    ],
    [
        "Example 2",
        "Message is World"
    ],
    [
        "Example 3",
        "Message is Goodbye"
    ],
    [
        "Example 4",
        "Message is World"
    ]
]
```

That doesn't make it much easier to access the data... We still have garbage in there, like the `Example ` part of the first item in each list.

### Basic data structures with Ansible & Jinja2

Let's see what we can do to make it easier to use!

```yaml
- name: Split lines
  ansible.builtin.set_fact:
    lines: "{{ my_var | split('\n') }}"

- name: Convert my_var to a BETTER dictionary
  ansible.builtin.set_fact:
    # Combine the current my_dict variable with the add_to_dict variable
    # But for the first iteration, my_dict is null, 
    # so we need to use the default filter to set it to an empty dictionary
    # This is my preferred way of initialising complex variables in Ansible!
    my_dict: "{{ my_dict | default({}) | combine(add_to_dict) }}"
  # Do this for each line in the lines variable we set earlier
  loop: "{{ lines }}"
  # These are temporary variables, recomputed for each iteration of the loop
  vars:
    # Split the current line into two parts
    # Example: ["Example 1", "Message is Hello"]
    current_line_split: "{{ item | split(': ') }}"

    # Extract the ID from the first part of the line
    # Example: 1
    id: "{{ current_line_split[0] | regex_search('[0-9]+') }}"
    
    # Remove the "Message is " part from the message
    # Example: "Hello"
    message: "{{ current_line_split[1] | regex_replace('^Message is ', '') }}"

    # Combine the ID and message into a dictionary, this will be added to the my_dict variable
    # Example: {"1": "Hello"}
    add_to_dict: "{{ {id: message} }}"

- name: Show dictionary
  ansible.builtin.debug:
    msg: "{{ my_dict }}"
```
I know it looks overwhelming, but bear with me here!

Let's break down in basic terms what we did here:
 - We split the input into lines
 - We loop over each line
 - We split the line into two parts
 - We extract the ID from the first part
 - We extract the message from the second part
 - We combine the ID and message into a dictionary
 - We merge the dictionary into the main dictionary

So what's the output of this? Well, it's a dictionary, which is a lot easier to use than a list of lists.
```json
"msg": {
    "1": "Hello",
    "2": "World",
    "3": "Goodbye",
    "4": "World"
}
```
Now we're getting somewhere! So Ansible allows us to manipulate data, and it allows us to loop over data.

With this new dictionary we can easily get the data! For example 3, we can just do this now:
```yaml
- name: Get message for example 3
  ansible.builtin.debug:
    msg: "{{ my_dict['3'] }}"
```
Which gives us the following output:
```json
"msg": "Goodbye"
```

As you can see, Ansible is very flexible. While all these tools were designed for better flow control and templating in deployments, we *can* and *will* abuse them for our own purposes.
## Despair
Well, let's see our challenges here. What are the problems we'll face?

### Looks easy, right? What could go wrong?

Well.. a lot of things. Let's not forget that Ansible isn't made for this. We'll have to do a lot of workarounds and hacks to get this to work. The previous example is something you could realistically actually use in a playbook!

#### Speed
First, there's the obvious problem of speed. Ansible is not a fast tool. It's not designed to be fast, it's designed to be safe, idempotent and reliable. 

Why? The way Ansible works behind the scenes is that it connects to a host, runs a Python script on the host, which then connects back to the Ansible controller and sends the results back. This is a very slow process, and it's not something you want to do for every single task, or even every single iteration of a loop.

We can partially optimise this by running Ansible in local mode, which means it doesn't connect to any hosts, but it still ends up needing to generate a Python script and then run it for every task/loop! This saves time, but we can expect more complicated tasks to literally take a second per iteration. While not disastrous for example input sizes, this will quickly become a problem for larger inputs.

I'm writing this as of day 4, and I can tell you that this is already a problem. I'm already having to wait 10-20 seconds for some tasks to complete, on example input! But let me tell you the worst part... Day 3 took ***7 HOURS*** to complete. I'm not joking!

#### Flow control restrictions
Ansible is also very restrictive in terms of flow control. It's not a programming language, so I don't blame it for this, but it's still a problem for us. For example, you can't use `break` or `continue` in loops, and you just don't 
have anything like functions or classes. This means we'll have to be very creative with how we structure our code.

Since we don't have functions, we'll probably need a lot of duplicate code. One way to include code from other files is to use the `ansible.builtin.include_tasks` module, which will include the contents of a different task file. This is a bit of a hack, but it works in some cases. Of course, that's only available in between tasks, so we can't use it in the middle of a task! That's a painful limitation, it means our code will be very repetitive and hard to debug.

#### Lack of data structures and types
Ansible also lacks a lot of data. It has lists, dictionaries, strings, integers bools, and that's about it. This means we'll have to be very creative with how we structure our data. We can't rely on making our own classes or data structures, we'll have to make do with what we have.

#### Lack of debugging tools
While I won't lie and say I always take advantage of them, I do love a good debugger. We'll have to do without one! Our only real options are inserting `ansible.builtin.debug` tasks in between other tasks to show the state of variables, or using the `ansible.builtin.fail` task to fail the playbook with a custom message. This is very limited, and it's not a good debugging experience. 

On top of that, we can't really debug the Jinja2 templates, so we'll have to be very careful with those. The best we can do is include the template in a `ansible.builtin.debug` task and see what it looks like. For debugging variables inside of templates, we're honestly out of luck. We can make it add the variables to the output, but that'll break the interpretation of the template, so we can't keep them in...

## Conclusion

Well, with what we've seen so far, it's clear that this is going to be a challenge. But it's not impossible! We'll just have to be creative with how we structure our code be very careful with how we use our very limited tools.

I'm very curious to see how far I can push Ansible, and I'm excited to see what I'll learn from this. I'll be a better Ansible developer after this, that's for sure! That, or I won't ever want to touch Ansible again after this.

Is this doable? Who knows! Maybe I'll realise why I gave up after day 8 last year and regret this. Maybe I'll make it all the way to the end. I don't know, but I'm going to try!

Be sure to check back here every week for updates on my progress, and check out my [GitHub repository](https://github.com/diademiemi/ansible_advent_of_code_2023) for my full solutions!

{% endraw %}