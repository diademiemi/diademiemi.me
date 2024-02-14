---
layout: post
title:  "ChatGPT 4 vs Gemini Ultra 1.0"
date:   2024-02-14 12:00:00 +0100
tags: [tech]
tabtitle: diademiemi | ChatGPT 4 vs Gemini Ultra 1.0

---

AI has been a quintessential part of my workflow for years now. Today I'll be comparing two conversational AI models.

I often use AI to help me with my work, and I've been using OpenAI's ChatGPT 4 for a while now. With the recent release of Google's Gemini Advanced, I thought it would be interesting to compare the two models and see how they stack up against each other. I was going to do some tests to figure out which one is better for my use case, and figured I might as well write a blog post about it, so please don't take this as a comprehensive review of either model! And keep in mind that these are just some quick tests relevant primarily to my use case.

This testing has been done as of February 13th 2024, and I will be testing the models on their usability, conversational skills, image recognition, and programming capabilities. I will be using the latest versions of both models, ChatGPT 4 (without enabled plugins) and Gemini Ultra 1.0.

I won't be testing simple things like asking for simple facts, as we all know that these models can do that nowaday. I'll be testing the models on more complex tasks, such as writing a Python script, identifying images, and troubleshooting.

{% raw %}

# Introduction

## UI

Both Gemini and ChatGPT have a similar UI, with a text input field and a submit button, a sidebar for previous conversations, and a settings menu.
Google obviously took inspiration from OpenAI's ChatGPT for their UI, but using Google's Material Design. I personally prefer the look of Gemini, but that's just personal preference. Both of these tools have a nice and clean UI, and are easy to use.

Code blocks are easy to copy with both AI sites having a button to copy the code to the clipboard, and both use code highlighting to make the code easier to read. I do prefer how the copy button is at the bottom of the code block in Gemini, as it's easier to find.

Both sites have a way to regenerate the response, which is a feature I use a lot. Gemini has a button to generate a list of 3 variant "drafts", while ChatGPT has a button to regenerate the response. I prefer the way ChatGPT does it, as it's more clear what the button does, but that's my personal preference.

## Integrations

Both models have a plugins/extensions system. On Gemini, these extensions can't be developed by third parties yet, while on ChatGPT, they can. 

Plugins/Extensions are very useful on both models, but ChatGPT is the clear winner here. From plugins such as Link Reader, Ask The Code, Wikipedia and Wolfram Alpha this can ensure your information in the chat is up to date and accurate. 

Gemini has a few extensions, but they are all developed by Google, and are not as useful as ChatGPT's plugins. Gemini's extensions are more focused on integrating with Google's other services, such as Google Flights and Google Maps. I've tried the Flights extension and it was able to find me cheaper flights than I would've found on my own, but it's not as useful as ChatGPT's plugins which I would use on a daily basis.

## Speed

Gemini is much faster than ChatGPT in most cases, especially writing code. This is something you'll see in the tests later on! It does seem however that for shorter responses, ChatGPT is faster, likely initiating quicker than Gemini, while Gemini is faster for longer responses.

# Tests

## Conversational Skills
How fluent and accurate are the models in a conversation? I'll be testing the models on their ability to answer questions, provide news, and write in style.

<details><summary>Test 1: Writing in style</summary>

<div style="border: 1px solid #aaaaff; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between;"> 
  <div style="flex-grow: 1; margin-right: 20px;"> 
    <h2 style="margin-top: 0; margin-bottom: 10px;">Prompt</h2> 
    <p style="color: #fff; margin-top: 0;">Write a haiku where every other sentence ends with an "e", and the letter "n" may not be used</p> 
  </div> 
</div>

<div style="border: 1px solid #3080f3; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #3080f3">Gemini Ultra 1.0</h2>
    <p>Warmth of summer's day,</p>
    <p>Birds softly chirp a sweet tune,</p>
    <p>Lazy clouds drift by.</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #3080f3; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">5.75 seconds</span>
    </div>
</div>

<div style="border: 1px solid #75ac9d; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #75ac9d">ChatGPT 4</h2>
    <p>Whispers of the breeze,</p>
    <p>A quiet lake does embrace,</p>
    <p>Stars gleam, pure and free.</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #75ac9d; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">3.5 seconds</span>
    </div>
</div>
<p>Here I wanted to see if the models would conform to my restrictions. Neither conformed to the restriction to not use the letter "n"! It just goes to show that even the most advanced AI models can't always follow instructions well when they contrast to the model's training data. This isn't really a useful test, but I wanted to lead with something simple.</p>
<p>Surprisingly, ChatGPT 4 was noticably faster in this test, which I don't see replicated in longer responses. </p>

<hr>

</details>

<details><summary>Test 2: News</summary>

<div style="border: 1px solid #aaaaff; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between;"> 
  <div style="flex-grow: 1; margin-right: 20px;"> 
    <h2 style="margin-top: 0; margin-bottom: 10px;">Prompt</h2> 
    <p style="color: #fff; margin-top: 0;">Show me todays news in The Netherlands. Also, who won the superbowl yesterday?</p> 
  </div> 
</div>

<div style="border: 1px solid #3080f3; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #3080f3">Gemini Ultra 1.0</h2>
    <p>Absolutely! To get you the best information, here's a breakdown of where you can find the news you're looking for:</p>
    <p>Today's News in The Netherlands</p>
    <p> News Aggregators: These websites pull news stories from multiple sources and provide an overview of current events.</p>
    <p>     NU.nl: [https://www.nu.nl/](https://www.nu.nl/) (Dutch)</p>
    <p>     NOS.nl: [https://nos.nl/](https://nos.nl/) (Dutch)</p>
    <p>     Google News Netherlands Edition: [https://news.google.com/](https://news.google.com/) - set your location to the Netherlands</p>
    <p> Major Newspapers: These well-established papers offer national and international news with specific regional sections.</p> 
    <p>     De Telegraaf: [https://www.telegraaf.nl/](https://www.telegraaf.nl/) (Dutch)</p>
    <p>     De Volkskrant: [https://www.volkskrant.nl/](https://www.volkskrant.nl/) (Dutch) </p>
    <p>     NRC Handelsblad: [https://www.nrc.nl/](https://www.nrc.nl/) (Dutch)</p>
    <p>Super Bowl Winner</p>
    <p> The Kansas City Chiefs won Super Bowl LVIII yesterday. They defeated the San Francisco 49ers in overtime with a score of 25-22.</p>
    <p>Let me know if you'd like more specific news categories (sports, business, etc.) and I can suggest tailored sources!</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #3080f3; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">15.5 seconds</span>
    </div>
</div>

<div style="border: 1px solid #75ac9d; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #75ac9d">ChatGPT 4</h2>
    <p>For today's news in The Netherlands, I found various articles but couldn't specify the details due to the browsing tool limitations. However, you can stay updated on current events in The Netherlands by visiting reputable news websites such as NOS.nl, NU.nl, or DutchNews.nl.</p>
    <p>As for the Super Bowl, the Kansas City Chiefs won Super Bowl LVIII, defeating the San Francisco 49ers with a score of 25-22 in overtime.</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #75ac9d; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">14 seconds</span>
    </div>
</div>
<p>Neither models could show the news here with the additional second question, though both recommended me news sites. This does surprise me, as I would've guessed Google would integrate Gemini with Google News! </p>
<p>When just asking the models the news and not adding an additional Super Bowl question, I could get ChatGPT 4 to show me the news, using Bing for search. This showed accurate news summaries, but I couldn't get Gemini to show me the news. </p>
<p>Both models gave an accurate result for the Super Bowl winner, providing a source too. But Gemini Ultra 1.0 gave more detailed information about where to find news in The Netherlands. I consider this tied. </p>

<hr>

</details>

<details><summary>Test 3: Accessing websites</summary>

<div style="border: 1px solid #aaaaff; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between;"> 
  <div style="flex-grow: 1; margin-right: 20px;"> 
    <h2 style="margin-top: 0; margin-bottom: 10px;">Prompt</h2> 
    <p style="color: #fff; margin-top: 0;">What kind of website is https://diademiemi.me/? Who is the author?</p> 
  </div> 
</div>

<div style="border: 1px solid #3080f3; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #3080f3">Gemini Ultra 1.0</h2>
    <p>This is a personal website of a DevOps Engineer named Emilia, also known as Jasmine or diademiemi. She is 19 years old and from the Netherlands. Her interests include DevOps tools, 3D printing, coding, and gaming.</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #3080f3; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">7.25 seconds</span>
    </div>
</div>

<div style="border: 1px solid #75ac9d; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #75ac9d">ChatGPT 4</h2>
    <p>The website diademiemi.me is a personal website of someone who goes by the names Emilia or Jasmine, and uses the username "diademiemi." This individual identifies with the pronouns they/them and she/her, is 19 years old, and hails from the Netherlands. The site showcases their interests in DevOps tools like Ansible, Terraform, and Kubernetes, and highlights their work as a DevOps Engineer. Additionally, it reflects their hobbies, which include 3D printing, coding, and gaming.</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #75ac9d; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">11.5 seconds</span>
    </div>
</div>
<p>Both models were able to correctly identify the website and the author. Gemini Ultra 1.0 was faster and more concise, while ChatGPT 4 provided more detailed information. Honestly I would call this a tie. </p>

<hr>

</details>

In all these tests, the results were pretty close. Gemini Ultra 1.0 and ChatGPT 4 both provided accurate and relevant information to the best of their current abilities. I thought Gemini Ultra 1.0 would be faster in all tests, but it was only faster in the last test, where is also provided less information.

For conversational skills, I would call this a perfect tie!

## Image Recognition
In this category the main focus is on accuracy, as I want to see how well the models can identify text and objects in images.

<details><summary>Test 1: Random Object</summary>

<div style="border: 1px solid #aaaaff; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between;"> 
  <div style="flex-grow: 1; margin-right: 20px;"> 
    <h2 style="margin-top: 0; margin-bottom: 10px;">Prompt</h2> 
    <p style="color: #fff; margin-top: 0;">What is this?</p> 
  </div> 
  <div class="image-container">
    <img src="/assets/img/blog/photo-water-bottle.jpg" title="Water Bottle" alt="Plastic Water bottle with the text 'Prevent Cancer Foundation' and 'AGDQ 2924'" style="max-height: 128px; border-radius: 10px; flex-shrink: 0;"> 
  </div>
</div>

<div style="border: 1px solid #3080f3; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #3080f3">Gemini Ultra 1.0</h2>
    <p>The object is a green reusable water bottle with the text "prevent cancer" and "FOUNDATION 2024" written on it. It appears to be made of metal and has a screw-on lid. Reusable water bottles are becoming increasingly popular as people look for ways to reduce their environmental impact. They are also a good way to save money on bottled water.</p>
    <p>I cannot provide any information about the specific foundation or the campaign to prevent cancer that is mentioned on the water bottle. If you would like to learn more, you could try searching for the foundation name or the phrase "prevent cancer foundation 2024" online.</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #3080f3; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">9.5 seconds</span>
    </div>
</div>

<div style="border: 1px solid #75ac9d; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #75ac9d">ChatGPT 4</h2>
    <p>The image shows a bright green sports water bottle with a white cap. The bottle has text printed on it which reads "prevent cancer foundation AGDQ 2021." AGDQ likely stands for Awesome Games Done Quick, which is a charity speedrunning marathon that raises money for the Prevent Cancer Foundation. The water bottle seems to be a piece of merchandise related to that event from the year 2021.</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #75ac9d; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">11.5 seconds</span>
    </div>
</div>
<p>The picture is of a water bottle with the text "Prevent Cancer Foundation" and "AGDQ 2024" on it. The responses from either model have flaws, so I would call this a loss for both models. Both were able to correctly identify the model as a water bottle, but neither correctly read the text. This is unsurprising, as the teext are both from logos with intricate fonts. </p>
<p>Gemini Ultra 1.0 incorrectly identified the bottle as metal, while ChatGPT 4 correctly identified it as a green sports bottle. ChatGPT 4 also correctly identified the bottle as a piece of merchandise from the charity event AGDQ, however it got the year wrong, it should be 2024, not 2021.</p>

<hr>

</details>

<details><summary>Test 2: Math Equation</summary>

<div style="border: 1px solid #aaaaff; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between;"> 
  <div style="flex-grow: 1; margin-right: 20px;"> 
    <h2 style="margin-top: 0; margin-bottom: 10px;">Prompt</h2> 
    <p style="color: #fff; margin-top: 0;">What is this?</p> 
  </div> 
  <div class="image-container">
    <img src="/assets/img/blog/photo-math-equation.jpg" title="Water Bottle" alt="Plastic Water bottle with the text 'Prevent Cancer Foundation' and 'AGDQ 2924'" style="max-height: 128px; border-radius: 10px; flex-shrink: 0;">
  </div>
</div>


<div style="border: 1px solid #3080f3; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #3080f3">Gemini Ultra 1.0</h2>
    <p>Sure, the answer is 8.33.  The question is 100 divided by 12.  100 divided by 12 is 8.3333..., which rounds down to 8.33 to two decimal places.</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #3080f3; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">17.5 seconds</span>
    </div>
</div>

<div style="border: 1px solid #75ac9d; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #75ac9d">ChatGPT 4</h2>
    <p>The answer to the mathematical expression, rounded to two decimal places, is 27.26. ​​</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #75ac9d; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">28.5 seconds</span>
    </div>
</div>

<p>The correct equation here is "(100 - 41/2) / 35  12", with the correct result being 27.26.</p>
<p>Gemini Ultra 1.0 completely misses the mark here. It doesn't even come close to recognising the text correctly. Meanwhile, ChatGPT correctly identifies the formula and even shows the Python code it used to calculate the result.</p>

<hr>

</details>

<details><summary>Test 3: Identifying a location</summary>

<div style="border: 1px solid #aaaaff; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between;"> 
  <div style="flex-grow: 1; margin-right: 20px;"> 
    <h2 style="margin-top: 0; margin-bottom: 10px;">Prompt</h2> 
    <p style="color: #fff; margin-top: 0;">Where is this?</p> 
  </div> 
  <div class="image-container">
    <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Duquesne_Incline_%2850076338942%29_%28cropped%29.jpg" title="Water Bottle" alt="Plastic Water bottle with the text 'Prevent Cancer Foundation' and 'AGDQ 2924'" style="max-height: 128px; border-radius: 10px; flex-shrink: 0;"> 
  </div>
</div>

<div style="border: 1px solid #3080f3; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #3080f3">Gemini Ultra 1.0</h2>
    <p>Based on the image you sent, the skyline appears to be that of Pittsburgh, Pennsylvania, USA, with the Roberto Clemente Bridge in the foreground. The bridge spans the Allegheny River, and in the background you can see some of the city's skyscrapers, including The U.S. Steel Tower, PPG Place and One PNC Plaza.</p>
    <p>It is possible that the image is of another city with a similar appearance, but Pittsburgh is the most likely location.</p>
    <p>Let me know if you have any other questions.</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #3080f3; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">11 seconds</span>
    </div>
</div>

<div style="border: 1px solid #75ac9d; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #75ac9d">ChatGPT 4</h2>
    <p>The image you've uploaded is of Pittsburgh, Pennsylvania. You can tell by the distinctive skyline, including the U.S. Steel Tower, which is one of the tallest buildings in the city. The photo also shows the convergence of the Allegheny and Monongahela Rivers to form the Ohio River, and the yellow bridges, which are a notable feature of the city. The bridge in the forefront is the Fort Duquesne Bridge. This view is likely taken from the vicinity of the Duquesne Incline, a historic cable car that provides a scenic overlook of Pittsburgh's downtown area.</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #75ac9d; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">14.5 seconds</span>
    </div>
</div>
<p>Bingo! Both models correctly identified the location as Pittsburgh, Pennsylvania, USA. Gemini Ultra 1.0 was faster and more concise, while ChatGPT 4 provided more detailed information. I would call this a tie. </p>

<hr>

</details>

For image recognition, ChatGPT 4 is the obvious winner. It was more accurately able to identify the objects in the images and provide more relevant information. While it was slower in all cases, the accuracy of the responses is more important in this context, absolutely destroying Gemini Ultra 1.0 in the math equation recognition test. The location recognition test was a tie, as both models provided the same information.

This greatly surprised me, as I expected Gemini Ultra 1.0 to be better at this with the backing of Google's image recognition technology, but it was worse overall.

## Technical Skills

The primary focus here is speed and accuracy. I'll be testing the models on writing a simple Python script that clones some GitHub repositories, a real-world script and asking for technical advice.

<details><summary>Test 1: Writing a simple Python script</summary>

<div style="border: 1px solid #aaaaff; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between;"> 
  <div style="flex-grow: 1; margin-right: 20px;"> 
    <h2 style="margin-top: 0; margin-bottom: 10px;">Prompt</h2> 
    <p style="color: #fff; margin-top: 0;">Write a Python script that fetches all GitHub repositories from a given user (--user or -d argument, should prompt when unset) and clones them to a directory (--directory or -d, defaulting to current directory). Optionally takes a private token (--token or -t) to access private repos.</p> 
  </div> 
</div>

<div style="border: 1px solid #3080f3; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #3080f3">Gemini Ultra 1.0</h2>
    <p>Absolutely! Here's the Python script that incorporates the best aspects of clarity, error handling, and security considerations:</p>
    <pre style="background-color: #000; padding: 10px; border: 1px solid #ccc; overflow-x: auto;">
    <code>
import argparse
import os
import subprocess
from getpass import getpass
from requests import get

def fetch_repos(username, token, directory):
    """Fetches all GitHub repositories for a given user"""

    api_url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {token}"} if token else {}

    response = get(api_url, headers=headers)
    if not response.ok:
        if response.status_code == 401: 
            raise RuntimeError("Invalid GitHub token. Please provide a valid token for accessing private repos.")
        else:
            raise RuntimeError(f"Error fetching repositories: {response.status_code} - {response.text}")

    repos = response.json()

    for repo in repos:
        clone_url = repo["clone_url"]
        repo_dir = os.path.join(directory, repo["name"])

        print(f"Cloning {clone_url} into {repo_dir}")
        try:
            subprocess.run(["git", "clone", clone_url, repo_dir], check=True)
        except subprocess.CalledProcessError:
            print(f"Failed to clone {clone_url}")  # Be more specific with error handling if needed

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and clone all GitHub repositories from a user.")
    parser.add_argument("-u", "--user", help="GitHub username")
    parser.add_argument("-d", "--directory", default=".", help="Directory to clone repositories into")
    parser.add_argument("-t", "--token", help="GitHub personal access token (for private repos)")
    args = parser.parse_args()

    if not args.user:
        args.user = input("Enter GitHub username: ")

    if args.token is None and input("Access private repos? (y/n): ").lower() == 'y':
        args.token = getpass("Enter GitHub personal access token: ")

    try:
        fetch_repos(args.user, args.token, args.directory)
    except RuntimeError as e:
        print(f"Error: {e}")

</code>
</pre>
    <p>Key Improvements:</p>
    <ul>
    <li><strong>Password Security:</strong> Leverages <code>getpass</code> to securely prompt for and hide the private token.</li>
    <li><strong>Robust Error Handling:</strong>
      <ul>
        <li>Distinguishes between "Invalid Token" (401) and other errors for better feedback to the user.</li>
        <li>Provides a more informative error message if token is required but not provided.</li>
      </ul>
    </li>
    <li><strong>Enhanced Readability:</strong> Clear function, comments, and print statements explaining the process.</li>
    <li><strong>Flexibility:</strong> Handles both public and private repositories (with optional token).</li>
    <li><strong>User-Friendly:</strong> Makes sensible defaults explicit in the help message.</li>
    </ul>
    <p>How to Use:</p>
    <ol>
    <li><strong>Saving the Script:</strong> Save it as a Python file (e.g., <code>github_repo_downloader.py</code>)</li>
    <li><strong>Create Personal Access Token (if needed):</strong> See instructions: [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)</li>
    <li><strong>Run the Script:</strong>
      <ul>
        <li><strong>For public repos:</strong> 
          <pre><code>python github_repo_downloader.py -u username
          </code></pre>
        </li>
        <li><strong>Including private repos:</strong>
          <pre><code>python github_repo_downloader.py -u username -t your_personal_access_token
          </code></pre>
        </li>
      </ul>
    </li>
    </ol>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #3080f3; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">23.5 seconds (code done after 13 seconds)</span>
    </div>
</div>

<div style="border: 1px solid #75ac9d; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #75ac9d">ChatGPT 4</h2>
    <p>To create a Python script that fetches and clones all GitHub repositories from a given user, incorporating the specified command-line argument functionality, you can use the <code>argparse</code> module for handling arguments and the <code>requests</code> module for making API calls to GitHub. For cloning the repositories, you can use the <code>git</code> command through the <code>subprocess</code> module.</p>
    <p>This script will:</p>
    <ul>
        <li>Prompt the user for their GitHub username if it's not provided via <code>--user</code> or <code>-u</code> argument.</li>
        <li>Use the provided directory from <code>--directory</code> or <code>-d</code> argument as the destination for cloning, defaulting to the current directory if not specified.</li>
        <li>Optionally accept a private token via <code>--token</code> or <code>-t</code> argument for accessing private repositories.</li>
    </ul>
    <pre style="background-color: #000; padding: 10px; border: 1px solid #ccc; overflow-x: auto;">
    <code>
import argparse
import requests
import subprocess
import os

def fetch_and_clone_repos(user, directory, token=None):
    # GitHub API endpoint to list user repositories
    api_url = f"https://api.github.com/users/{user}/repos"
    headers = {}
    
    # Include the token in the request headers if provided
    if token:
        headers['Authorization'] = f'token {token}'
    
    # Make a request to the GitHub API
    response = requests.get(api_url, headers=headers)
    repos = response.json()

    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Clone each repository
    for repo in repos:
        clone_url = repo['clone_url']
        subprocess.run(["git", "clone", clone_url], cwd=directory)
        print(f"Cloned {repo['name']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and clone GitHub repositories.")
    parser.add_argument("-u", "--user", help="GitHub username", required=False)
    parser.add_argument("-d", "--directory", help="Directory to clone repositories into", default=os.getcwd())
    parser.add_argument("-t", "--token", help="GitHub private access token (optional)", required=False)

    args = parser.parse_args()

    if not args.user:
        args.user = input("Enter GitHub username: ")

    fetch_and_clone_repos(args.user, args.directory, args.token)
  </code>
  </pre>
    <p>Before running this script, ensure you have:</p>
    <ul>
        <li>Python installed on your system.</li>
        <li>The <code>requests</code> module installed (you can install it using <code>pip install requests</code>).</li>
        <li>Git installed and accessible from the command line.</li>
    </ul>
    <p>If you plan to access private repositories, you'll need to generate a personal access token on GitHub with the necessary permissions and pass it to the script using the <code>--token</code> or <code>-t</code> argument. You can generate a token by going to GitHub Settings &gt; Developer settings &gt; Personal access tokens.</p>
    <p>To use this script:</p>
    <ol>
        <li>Save it to a <code>.py</code> file, for example, <code>clone_github_repos.py</code>.</li>
        <li>Run it from the command line, providing the necessary arguments. For example:
            <ul>
                <li>To clone all public repositories of a user to the current directory:<br><code>python clone_github_repos.py --user username</code></li>
                <li>To clone all repositories (including private ones) of a user to a specific directory:<br><code>python clone_github_repos.py --user username --directory /path/to/directory --token your_token</code></li>
            </ul>
        </li>
    </ol>
    <p>Please replace <code>username</code>, <code>/path/to/directory</code>, and <code>your_token</code> with the actual GitHub username, directory path where you want to clone the repositories, and your personal access token, respectively.</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #75ac9d; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">110 seconds (code done after 58 seconds)</span>
    </div>
</div>
<p></p>

<p>Both the models produced a very similar script, Gemini Ultra 1.0 was much much faster than ChatGPT 4, and I do think it provided clearer code and instructions. I call this a clear win for Gemini Ultra 1.0. </p>

<hr>

</details>

<details><summary>Test 2: Writing a real world script</summary>

This prompt is one I recently used to create a bash script for this real-world use case. I wanted to see how the models would handle it.

<div style="border: 1px solid #aaaaff; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between;"> 
  <div style="flex-grow: 1; margin-right: 20px;"> 
    <h2 style="margin-top: 0; margin-bottom: 10px;">Prompt</h2> 
    <p style="color: #fff; margin-top: 0;">Write a bash script called <code>ansible-inventory-ssh</code> that looks like: <code>ansible-inventory-ssh -i inventories/dev host</code> Runs <code>ansible-inventory -i inventories/dev --list</code>. Omit <code>-i</code> and the argument for it if it is not given for the bash script. It should form an SSH command and echo it on basis of returned host info returned from the inventory, such as ansible_host (default to the given host if unset), ansible_ssh_pass (optional), ansible_user (default to root if unset), ansible_ssh_common_args (default to empty) and ansible_ssh_private_key_file (optional)</p> 
  </div> 
</div>

<div style="border: 1px solid #3080f3; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #3080f3">Gemini Ultra 1.0</h2>
    <p>Absolutely, let's craft that bash script. Here's how <code>ansible-inventory-ssh</code> could be written:</p>
    <pre style="background-color: #000; padding: 10px; border: 1px solid #ccc; overflow-x: auto;">
    <code>
#!/bin/bash

# Parse command-line arguments
inventory_file=""
host=""
while [[ $# -gt 0 ]]; do
  case $1 in
    -i)
      inventory_file="$2"
      shift 2 
      ;;
    *)
      host="$1"
      shift 
      ;;
  esac
done

# Run Ansible Inventory (if inventory file is provided)
if [[ -n "$inventory_file" ]]; then
  ansible_inventory_output=$(ansible-inventory -i "$inventory_file" --list)
else 
  # Just a placeholder output if no inventory file
  ansible_inventory_output='{"all": { "hosts": [ ]} }'
fi

# Extract host information from the inventory output 
inventory_json=$(echo $ansible_inventory_output | jq .)
default_host="$host"  # In case ansible_host is not set
ansible_host=$(echo "$inventory_json" | jq -r '.["_meta"]["hostvars"][\""$host"\"]["ansible_host"] // empty' | sed 's/^"//;s/"$//')
ansible_user=$(echo "$inventory_json" | jq -r '.["_meta"]["hostvars"][\""$host"\"]["ansible_user"] // "root"' | sed 's/^"//;s/"$//')
ansible_ssh_pass=$(echo "$inventory_json" | jq -r '.["_meta"]["hostvars"][\""$host"\"]["ansible_ssh_pass"] // empty' | sed 's/^"//;s/"$//')
ansible_ssh_common_args=$(echo "$inventory_json" | jq -r '.["_meta"]["hostvars"][\""$host"\"]["ansible_ssh_common_args"] // empty' | sed 's/^"//;s/"$//')
ansible_ssh_private_key_file=$(echo "$inventory_json" | jq -r '.["_meta"]["hostvars"][\""$host"\"]["ansible_ssh_private_key_file"] // empty' | sed 's/^"//;s/"$//')

# Use default host if extracted  ansible_host is empty
if [[ -z "$ansible_host" ]]; then
   ansible_host="$default_host"
fi

# Construct SSH command with gathered information
ssh_command="ssh $ansible_ssh_common_args"

if [[ -n "$ansible_ssh_private_key_file" ]]; then
  ssh_command="$ssh_command -i $ansible_ssh_private_key_file"
fi

if [[ -n "$ansible_ssh_pass" ]]; then
  ssh_command="$ssh_command -o PasswordAuthentication=yes"
fi

ssh_command="$ssh_command $ansible_user@$ansible_host"

# Echo the generated SSH command
echo $ssh_command 
    </code>
    </pre>
    <p><b>Key improvements and explanations:</b></p>
    <ul>
      <li><b>Optional Inventory File:</b>  Handles scenarios with  and without an inventory file.</li>
      <li><b>JSON Parsing with jq:</b> Uses `jq` for robust parsing of Ansible inventory output. Install `jq` if you don't have it (e.g., `sudo apt install jq`).</li>
      <li><b>Flexible Defaults:</b> Provides sensible defaults (e.g., `root` user) if inventory entries are missing.</li>
      <li><b>Password Support:</b> Includes the option to use `ansible_ssh_pass`.</li>
      <li><b>Clear SSH Command Construction:</b> The script meticulously builds the SSH command piece by piece.</li>
    </ul>
    <p><b>How to use it:</b></p>
    <ol>
      <li>Save the code as `ansible-inventory-ssh`</li>
      <li>Make it executable: `chmod +x ansible-inventory-ssh`</li>
      <li><b>With inventory:</b> `./ansible-inventory-ssh -i inventories/dev host`</li>
      <li><b>Without inventory:</b> `./ansible-inventory-ssh host`</li> 
    </ol>
    <p>Let me know if you have any other requests or modifications! </p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #3080f3; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">20 seconds (code done after 10 seconds)</span>
    </div>
</div>

<div style="border: 1px solid #75ac9d; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #75ac9d">ChatGPT 4</h2>
    <p>To create a bash script named <code>ansible-inventory-ssh</code> that takes an inventory and a host as arguments, and constructs an SSH command based on the output of <code>ansible-inventory</code>, you need to follow these steps:</p>
    <ol>
      <li>Parse command-line arguments to get the inventory file and host name. If the inventory file is provided, include it in the <code>ansible-inventory</code> command.</li>
      <li>Run <code>ansible-inventory</code> to get the details of the specified host.</li>
      <li>Extract necessary details like <code>ansible_host</code>, <code>ansible_ssh_pass</code>, <code>ansible_user</code>, <code>ansible_ssh_common_args</code>, and <code>ansible_ssh_private_key_file</code> from the output.</li>
      <li>Construct the SSH command based on the extracted details.</li>
      <li>Echo the constructed SSH command.</li>
    </ol>
    <p>Here's how you can write the <code>ansible-inventory-ssh</code> bash script:</p>
    <pre style="background-color: #000; padding: 10px; border: 1px solid #ccc; overflow-x: auto;">
    <code>
#!/bin/bash

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
  echo "Usage: $0 [-i inventory] host"
  exit 1
fi

# Initialize variables
inventory=""
host=""
ssh_user="root"
ssh_pass=""
ssh_common_args=""
ssh_key=""

# Parse command-line arguments
while getopts ":i:" opt; do
  case ${opt} in
    i )
      inventory=$OPTARG
      ;;
    \? )
      echo "Invalid option: $OPTARG" 1>&2
      exit 1
      ;;
    : )
      echo "Invalid option: $OPTARG requires an argument" 1>&2
      exit 1
      ;;
  esac
done
shift $((OPTIND -1))

host=$1

# Run ansible-inventory to get host details
if [[ -n "$inventory" ]]; then
  inventory_output=$(ansible-inventory -i "$inventory" --list)
else
  inventory_output=$(ansible-inventory --list)
fi

# Extract host information using jq (assuming ansible-inventory output is in JSON format)
ansible_host=$(echo "$inventory_output" | jq -r ".[\"$host\"].ansible_host // \"$host\"")
ansible_user=$(echo "$inventory_output" | jq -r ".[\"$host\"].ansible_user // \"root\"")
ansible_ssh_pass=$(echo "$inventory_output" | jq -r ".[\"$host\"].ansible_ssh_pass // \"\"")
ansible_ssh_common_args=$(echo "$inventory_output" | jq -r ".[\"$host\"].ansible_ssh_common_args // \"\"")
ansible_ssh_private_key_file=$(echo "$inventory_output" | jq -r ".[\"$host\"].ansible_ssh_private_key_file // \"\"")

# Construct the SSH command
ssh_cmd="ssh"
if [[ -n "$ansible_ssh_private_key_file" ]]; then
  ssh_cmd="$ssh_cmd -i \"$ansible_ssh_private_key_file\""
fi
if [[ -n "$ansible_ssh_common_args" ]]; then
  ssh_cmd="$ssh_cmd $ansible_ssh_common_args"
fi
ssh_cmd="$ssh_cmd ${ansible_user}@${ansible_host}"

# Echo the SSH command
echo $ssh_cmd
    </code>
    </pre>
    <p>This script assumes that <code>ansible-inventory</code> outputs JSON, which is parsed using <code>jq</code>. If <code>jq</code> is not installed on your system, you'll need to install it or modify the script to parse the output differently.</p>
    <p><strong>Important:</strong> This script directly outputs the SSH command including sensitive information like <code>ansible_ssh_pass</code> (if available), which is not used in the command construction but captured. SSH doesn't support passing passwords via command line</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #75ac9d; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">65 seconds (code done after 56 seconds)</span>
    </div>
</div>

<p>Both of the models did a great job here, providing correct and detailed code. Gemini Ultra 1.0 was much much faster here, providing the code in a fifth of the time. However, Gemini Ultra 1.0 did miss a vital part of my prompt, which was to omit <code>-i</code> and the argument for it if it is not given for the bash script, it just defaults to a placeholder output if no inventory file is provided. ChatGPT 4 correctly identified that it should run <code>ansible-inventory</code> without the inventory file if it is not provided. I would call this a win for Gemini Ultra 1.0, as this was easily fixed with the response "Running it without an inventory does not fetch the default inventory", still saving time over ChatGPT 4. </p>

<hr>

</details>

<details><summary>Test 3: Hosting a Minecraft server</summary>

<div style="border: 1px solid #aaaaff; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between;"> 
  <div style="flex-grow: 1; margin-right: 20px;"> 
    <h2 style="margin-top: 0; margin-bottom: 10px;">Prompt</h2> 
    <p style="color: #fff; margin-top: 0;">Give me the steps to host a Minecraft server on Hetzner Cloud where I want a plugin that provides /home and /back functionality</p> 
  </div> 
</div>

<div style="border: 1px solid #3080f3; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <p style="color: #3080f3">Gemini Ultra 1.0</p>
    <p>Absolutely! Here's a detailed guide on setting up a Minecraft server with /home and /back functionality on Hetzner Cloud.</p>

    <p><strong>Prerequisites:</strong></p>
    <ul>
    <li>A Hetzner Cloud account (https://www.hetzner.com/cloud)</li>
    <li>Basic familiarity with Linux and command-line usage</li>
    </ul>

    <p><strong>Steps:</strong></p>

    <p><strong>1. Creating a Hetzner Cloud Server</strong></p>
    <ol>
    <li>Log into your Hetzner Cloud console.</li>
    <li>Create a new project.</li>
    <li>Click "Add Server" and choose the following:
    <ul>
    <li><strong>Image:</strong> Ubuntu (Choose a recent stable version like Ubuntu 22.04)</li>
    <li><strong>Location:</strong> Pick a data center location that's geographically closest to your players for optimal performance.</li>
    <li><strong>Server Type:</strong> Select a server type with enough RAM and CPU to handle your expected player count (a good starting point could be something like the CX21 for smaller servers).</li>
    <li><strong>Add SSH Key (Optional but Recommended):</strong> If you have an existing SSH key, add it here for enhanced security.</li>
    </ul>
    </li>
    <li>Click "Create & Buy Now"</li>
    </ol>

    <p><strong>2. Connecting to Your Server</strong></p>
    <ol>
    <li>Once your server is provisioned, you'll find its IP address on the Hetzner Cloud console.</li>
    <li>Use an SSH client to connect to your server:
    <ul>
    <li><strong>Windows:</strong> PuTTY is a popular choice.</li>
    <li><strong>macOS/Linux:</strong> Use the built-in terminal (ssh root@your_server_ip_address)</li>
    </ul>
    </li>
    </ol>

    <p><strong>3. Installing Dependencies</strong></p>
    <pre><code>sudo apt update && sudo apt upgrade -y
    sudo apt install default-jdk -y
    sudo apt install screen -y
    </code></pre>

    <p><strong>4. Choosing a Minecraft Server Software</strong></p>
    <p>There are a few options, each with advantages:</p>
    <ul>
    <li><strong>Vanilla:</strong> The basic Minecraft server from Mojang (best for a standard experience, if you don't want heavy modifications).</li>
    <li><strong>PaperMC:</strong> A highly optimized version of Minecraft server software, excellent for performance (https://papermc.io/).</li>
    <li><strong>Spigot/Bukkit:</strong> Older but still popular choices if you need flexibility and a massive plugin ecosystem.</li>
    </ul>
    <p>For this example, we'll use PaperMC.</p>
    <p><strong>5. Downloading and Configuring PaperMC</strong></p>
    <ol> 
      <li>Create a directory for your Minecraft server:</li>
        <pre><code>mkdir minecraft
    cd minecraft
    </code></pre>
      <li>Download the latest PaperMC jar file from [https://papermc.io/downloads](https://papermc.io/downloads) (replace the version number if needed):
        <pre><code>wget https://papermc.io/api/v2/projects/paper/versions/1.19.3/builds/114/downloads/paper-1.19.3-114.jar
    </code></pre>
      </li>
      <li>Accept the EULA:
        <pre><code>echo eula=true > eula.txt
    </code></pre>
      </li>
      <li>Start the server for the first time to generate configuration files:
        <pre><code>java -Xms1G -Xmx1G -jar paper-1.19.3-114.jar nogui
    </code></pre>
        *Replace '1G' in the command with the amount of RAM you want to allocate to your server.*
      </li>
      <li>Stop the server by typing <strong>stop</strong> in the console.</li>
    </ol>

    <p><strong>6. Installing the /home and /back Plugin</strong></p>
    <ol>
      <li><strong>Choose a plugin:</strong>  Search for plugins like "EssentialsX" that provide /home, /back and other essential features. </li>
      <li><strong>Download:</strong> Get the plugin's .jar file.</li>
      <li><strong>Place the .jar file:</strong> Put it into the  <strong>plugins</strong> folder within your Minecraft server directory.</li>
    </ol>

    <p><strong>7. Starting Your Server</strong></p>
    <ol>
      <li>Start a new <strong>screen</strong> session to keep the server running after you disconnect:
        <pre><code>screen -S minecraft
    </code></pre>
      </li>
      <li>Start the server:
        <pre><code>java -Xms1G -Xmx1G -jar paper-1.19.3-114.jar nogui 
    </code></pre>
      </li>
    </ol>

    <p><strong>8. Connecting to Your Server</strong></p>
    <ol>
      <li>Launch Minecraft.</li>
      <li>Go to Multiplayer ->  Add Server.</li>
      <li>Enter your Hetzner server's IP address.</li>
      <li>Join and enjoy!</li>
    </ol>
  <p>Remember to always consult the documentation for the specific plugin you choose to install for precise configuration instructions.</p> 
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #3080f3; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">37.5 seconds</span>
    </div>
</div>

<div style="border: 1px solid #75ac9d; padding: 20px; border-radius: 10px; background-color: #15151f; color: #fff; margin-bottom: 25px;">
    <h2 style="color: #75ac9d">ChatGPT 4</h2>
    <p>Hosting a Minecraft server on Hetzner Cloud with specific plugins like those that provide <code>/home</code> and <code>/back</code> functionality involves several steps. You'll start by setting up a virtual server on Hetzner Cloud, installing the necessary software, and then configuring your Minecraft server with the desired plugins. Here's a simplified guide to get you started:</p>
    
    <p>1. Set Up a Hetzner Cloud Server</p>
    <ol>
        <li><strong>Create a Hetzner Account</strong>: Go to Hetzner's website and sign up for an account if you don't already have one.</li>
        <li><strong>Create a Project</strong>: Once logged in, create a new project.</li>
        <li><strong>Add a Server</strong>: Inside your project, click on the "Add Server" button. Choose the location closest to you or your intended player base for the best performance.</li>
        <li><strong>Select Server Type</strong>: For a small to medium-sized Minecraft server, you can start with a model like CX21 or CX31, which offers a balance between cost and performance. You can always resize later if needed.</li>
        <li><strong>Choose an Operating System</strong>: Select a Linux distribution; Ubuntu Server 20.04 LTS is a popular choice for its ease of use and support.</li>
        <li><strong>SSH Key Setup</strong>: For security, set up SSH keys for remote access. If you don't have SSH keys, you'll need to generate them and add the public key to your Hetzner project.</li>
        <li><strong>Create the Server</strong>: After configuring your server options, click to create your server. Hetzner will provision the server and provide you with an IP address.</li>
    </ol>

    <p>2. Connect to Your Server</p>
    <ol>
        <li><strong>SSH into Your Server</strong>: Use an SSH client with the command <code>ssh root@your_server_ip</code> to connect to your server, replacing <code>your_server_ip</code> with the IP address Hetzner provided.</li>
    </ol>

    <p>3. Install Java and Screen</p>
    <ol>
        <li><strong>Update Your Server</strong>: Run <code>apt update && apt upgrade</code> to update your server's package list and software.</li>
        <li><strong>Install Java</strong>: Minecraft servers run on Java, so install it with <code>apt install default-jdk</code>.</li>
        <li><strong>Install Screen</strong>: This utility allows you to run your Minecraft server in a detachable session. Install it with <code>apt install screen</code>.</li>
    </ol>

    <p>4. Set Up Your Minecraft Server</p>
    <ol>
        <li><strong>Download the Minecraft Server Software</strong>: You can use the Vanilla server software or opt for a modded server like Spigot or PaperMC, which allows plugins. For <code>/home</code> and <code>/back</code> functionality, you'll need PaperMC or Spigot. Download it using <code>wget</code> with the appropriate URL.</li>
        <li><strong>Initialize Your Server</strong>: Run your server software once to generate configuration files. Agree to the EULA by editing <code>eula.txt</code>.</li>
        <li><strong>Configure Your Server</strong>: Adjust server properties in <code>server.properties</code> as needed.</li>
    </ol>

    <p>5. Install Plugins</p>
    <ol>
        <li><strong>Download Plugins</strong>: Essential plugins like EssentialsX provide <code>/home</code>, <code>/back</code>, and other essential commands. Download EssentialsX from its official website or a trusted source.</li>
        <li><strong>Install Plugins</strong>: Place the plugin <code>.jar</code> files in the <code>plugins</code> folder of your server directory. Restart your server to activate them.</li>
    </ol>

    <p>6. Configure Firewall and Networking</p>
    <ol>
        <li><strong>Adjust Firewall Rules</strong>: Ensure your server's firewall allows traffic on the Minecraft server port (default is 25565).</li>
        <li><strong>Port Forwarding</strong>: If necessary, configure your network or Hetzner Cloud

 firewall to forward port 25565 to your server.</li>
    </ol>

    <p>7. Start Your Minecraft Server</p>
    <ol>
        <li><strong>Run the Server</strong>: Use Screen to start your server in a detachable session. Command example: <code>screen -S minecraft java -Xmx1024M -Xms1024M -jar server.jar nogui</code>.</li>
        <li><strong>Detach Screen</strong>: Press <code>Ctrl+A</code> then <code>D</code> to detach from the Screen session, leaving your server running in the background.</li>
    </ol>

    <p>8. Connect to Your Server</p>
    <p>- Launch Minecraft, select Multiplayer, and add your server using the IP address provided by Hetzner.</p>
    
    <p>Remember, server management involves regular maintenance, updates, and backups to ensure smooth operation and security. Adjust your server size and configuration based on performance and player count as needed.</p>
    <div style="margin-top: 20px; padding: 10px; background-color: #000000; border-radius: 5px; border-left: 5px solid #75ac9d; font-size: 0.9em;">
        <strong>Response Time:</strong> <span style="color: #ccc;">68 seconds</span>
    </div>
</div>
<p>Both models took a similar approach to this question, providing a detailed guide to setting up a Minecraft server on Hetzner Cloud. Gemini Ultra 1.0 was much faster at providing the response, and I think it was a bit more detailed and clear. I would call this a win for Gemini Ultra 1.0. However, it did suggest a very outdated Minecraft server version, and it didn't provide any steps on how to get a newer version aside from mentioning to change the URL, not mentioning what to change it to. ChatGPT 4 did not even mention how to get the server software, so I would call this a win for Gemini Ultra 1.0, but with a caveat. </p>
<p>Neither models provided the exact steps to install the plugin, and neither mentioned how to get back into the <code>screen</code> session after detaching from it. So both answers definitely have room for improvement, but I would still call this a win for Gemini Ultra 1.0. </p>

<hr>

</details>

Both models have good technical skill, but Gemini Ultra 1.0 is much faster at writing code and longer responses. For asking changes to code, Gemini Ultra 1.0 was also much faster, basically instantly providing the code. ChatGPT 4 took a long time to rewrite the code.

For these responses, I asked the models to return the output in HTML as well so I could embed the code in this blog post. Gemini Ultra 1.0 was MUCH faster at transforming the output, giving me it within seconds, while ChatGPT 4 took a full minute to transform the output, and it ended up being a mess of formatting codes where I had to manually replace `&lt;` and `&gt;` with `<` and `>`.

For these reasons I would call Gemini Ultra 1.0 the winner in this category, though most of that win is based on it's incredible speed.

# Conclusion

It's very much a mixed bag. Gemini Ultra 1.0 was much faster at pretty much everything, but had much worse image recognition.

Both models are very good at writing code, but Gemini Ultra 1.0 was much faster at writing the code, and transforming the output or asking for follow-up questions.

For now, I think this is a win for Gemini Ultra 1.0 for my personal usecase of writing code snippets and assisting in troubleshooting. But which model wins for you is going to depend on your usecase. If you need to write code quickly, Gemini Ultra 1.0 is the clear winner. If you need the plugin ecosystem, image recognition and the growing ecosystem around ChatGPT 4, it's going to be the better choice For the time being, I think I'll stick with both while I can use the Gemini Advanced free trial. I might post an update in a few months if I've made a definitive choice between the two after development.

If I had to choose between the two, I think I would pick Gemini Ultra 1.0, as it's also the better deal as it comes with Google One, and it's much faster at writing code.

I hope this comparison has been helpful to someone, and I hope it's been a good read. I'm excited to see how both models improve in the future!

{% endraw %}


