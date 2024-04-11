![Screenshot 2024-04-11 155834](https://github.com/jakejacobsen975/youface-Graphical-Network/assets/122470500/987c6a28-0986-40eb-ae2a-0377c59d671f)
### Installing Requirements

The requirements are listed in `requirements.txt`. With `pip`, they can be
easily installed in one command:

`pip3 install -r requirements.txt`

### Running the Server

The server main is found in `youface.py`. It requires Python 3 and can be run
with the following command:

`python3 youface.py`

By default, the server can be accessed at `http://127.0.0.1:5000`

Press `CTRL+C` to stop the server

### posting

if you want to post and generate a meme. Run youface with an openai api key.
```
python3 youface.py sk-123456789
```

### File Tree

```
.
├── db
│   ├── posts.py
│   └── users.py
├── db.json
├── handlers
│   ├── copy.py
│   ├── friends.py
│   ├── login.py
│   ├── posts.py
├── README.md
├── requirements.txt
├── static
│   ├── bootstrap.min.css
│   └── youface.css
├── templates
│   ├── base.html
│   ├── feed.html
│   ├── friend.html
│   ├── loggedin.html
│   ├── login.html
│   └── nav.html
├── test_youface.py
└── youface.py
```

![Screenshot 2024-04-11 155912](https://github.com/jakejacobsen975/youface-Graphical-Network/assets/122470500/5a104eff-9e84-4721-8eae-392b8abb0b43)

# Summary

## Introduction
Purpose: Make a social experiment with AI-generated memes to find the best memes.
Audience: Renn.
Scope: The software lets users create and share memes, like and comment on them, and has a leaderboard.

## Overall Description
Product: A standalone product that works with AI generators for memes and user data.
Functions: Posting, commenting, adding friends, liking posts, and viewing friends' memes.
Constraints: Limited by the AI's capabilities and doesn't require internet access.
Documentation: FAQ page will explain website features and leaderboards.
Assumptions: Assumes functioning OpenAI website and manages resulting traffic.

## External Interface Requirements
Interfaces: Website with feed, post, friend management sections.
Hardware: Works on computers and phones.
Software: Interacts with OpenAI and server.
Communication: No security or encryption, interacts with OpenAI and ChatGPT via website.

# System Features

Receiving Content from ChatGPT: Get text and image from ChatGPT.
ChatGPT Meme Generation: Generate memes in correct format for posting.
Posting: Let users post memes.
Comments: Allow users to comment on posts.
Like Leaderboard: Rank memes by likes.
Feed Based on Friends: Show friends' posts.
Other Nonfunctional Requirements
Safety: Admins can remove posts and delete accounts; memes should not cause cognitive harm.
Security: User data stored securely, protected against SQL injection.
Quality Attributes: User-friendly, reliable, compatible, and maintainable website.
Business Rules: Prevent bots and fake accounts, allow user customization, provide truthful privacy policy.

# Assignment description

YouFace is a mock social media platform. Originally designed as an assignment
for CS 1410, it has been simplified and modernized for CS 2450. This repository
houses a rough implementation of the completed version of the original
assignment, yet still provides only minimal functionality. Your group will take
this social media baseline and make it your own. Consider yourselves a small
startup with a new and unique take on the social media market.

## Collaborators 
Reily Thompson,
Ryan Larson,
Levi,
Nathanial 

