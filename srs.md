Software Requirements Specification for
Version 1.0 approved
Prepared by Riley Thompson, Nathan Sanchez, Levi Hafen, Ryan Larson
Revision History
Name, Date, Reason For Changes, Version


1. Introduction
1.1 Purpose
Social experiment using AI generated memes and users to obtain feedback to get the dankest of memes. 
1.2 Document Conventions
Priority is assumed equal for all requirements unless specified otherwise.
1.3 Intended Audience and Reading Suggestions
Renn. This document is split into 6 sections: Introduction, Overall Description, External Interface Requirement, System Features, Other nonfunctional Requirements, Other Requirements. It is recommended that you read this in order.
1.4 Product Scope
The software interacts with chatGPT using OpenAI to generate text and images for memes. Users will click a post button to generate memes to their own feed, and other users will be able to like and comment on their memes. Top ranking memes and users will be put on a leaderboard.
1.5 References
https://openai.com/blog/chatgpt/
2. Overall Description
2.1 Product Perspective
This is a new, self contained product. It does interact with existing AI image and text generators to generate memes and certain user data like gamertags.
2.2 Product Functions
Post memes
Comment
Add friends
Like posts
Have feed based off of friends memes
2.3 User Classes and Characteristics
The user class will have a like count, posts, a username, comments, and previously liked posts.
2.4 Operating Environment
Software will operate to the user via a website and the website will run through a server and its scripts.
2.5 Design and Implementation Constraints
It is limited to what the AI is able to do since it isn’t connected to the internet it is limited to the knowledge it has now. 
2.6 User Documentation
We’ll have a F&Q page explaining the website and things like the leaderboards.
2.7 Assumptions and Dependencies
We assume that OpenAI website is functioning and always the traffic that will be caused by using the ai.
3. External Interface Requirements
3.1 User Interfaces
We will include a feed page where you can see friends' posts. An area where you can make posts. An area where you can see your friends and add or remove friends. Users will be able to press buttons to allow them to do these things. There will be images displayed throughout the website.
3.2 Hardware Interfaces
Supported devices would be anything that can connect to the website and interact with the UI to send and receive data. So computers and phones.
3.3 Software Interfaces
It interacts with OpenAI and also the server where the website is stored. 
3.4 Communications Interfaces
There is no security or encryption. OpenAI and chatgpt will both be interacted with. There is no other form of interaction outside of the website.
4. System Features
4.1 Receiving Image and Text from Chat GPT
4.1.1 Description and Priority
High priority, the API will interact with chat gpt to receive the content of the meme and then interact with it again to receive the image.
4.1.2 Stimulus/Response Sequences
4.1.3 Functional Requirements
The server has to be able to interact with the api. If something goes wrong try again and if multiple attempts fail report a fatal error 
4.2 Chat GPT Making Meme and Formatting
4.2.1 Description and Priority
When the user is posting we need chatGTP to generate a meme and put it into the correct formatting so they can post it. High priority.
4.2.2 Stimulus/Response Sequences
4.2.1 Description and Priority
This would have the API interact with Chat GPT to send and receive data of the bottom and top text as well as the image. It is ranked high due to it being a necessity to the website.

4.3 Posting Meme
4.3.1 Description and Priority
High Priority: Let the user post a meme onto their friends feed.
4.3.2 Functional Requirements
Have a button, and limit the amount of times it can be pressed, so someone cannot click it 100 times in a second.

4.4 Comments
4.4.1 Description and Priority
Each user will be able to comment on the AI generated post
4.4.2 Functional Requirements
A comment button, and a text box to write in, and a post button.
4.5 Like leaderboard
4.5.1 Description and Priority
This is the way that ai memes are favorited and chosen above their peers. The more likes a meme has, the higher on the leaderboard it is.
4.5.2 Functional Requirements
A like button, and a counter on how many likes a post has.

4.6 generate feed based on friends
4.6.1 Description and Priority
The site needs to be able to show what the friends you are following posted. This is High priority.

4.6.2 Functional Requirements
A followers page that shows the posts that your friends have made.
5. Other Nonfunctional Requirements
5.1 Safety Requirements
 Feature to allow users that are admins to remove posts and also delete accounts. The only real appreciable risk is that of the memes being too funny and dank and inflicting cognitive damage to users.
5.2 Security Requirements
User data will be stored in a database, api will take all measures (what I just learned in 3200) to avoid sql injection and protect user information.
5.3 Software Quality Attributes
Usability: The website should be easy to navigate and use, with clear instructions and intuitive design.

Reliability: The website should be available and functioning properly at all times, with minimal downtime or errors.

Compatibility: The website should be compatible with a range of browsers and devices, ensuring that users can access it from anywhere.

Maintainability: The website should be easy to maintain and update, with clear documentation and well-organized code.
5.4 Business Rules
The website should have measures in place to prevent bots and fake accounts from being created. Only our bots are allowed.
Users should have the ability to customize their profiles and pretend to manage their own content.
The website should have a privacy policy that clearly outlines how user data is collected, stored, and used. It will all be technically truthful.
6. Other Requirements
There are no major other requirements other than those already enumerated in this SRS.
Appendix A: Glossary

Dank: Originally used to describe high-quality marijuana, "dank" now refers to anything that is cool, edgy, or subversive.

Meme: A piece of media (such as a picture or video) that is shared and spread widely on the internet, often with humorous or satirical intent.

Pepe the Frog: A cartoon frog character that became a popular meme on 4chan and other online forums, often used in ironic or satirical contexts.

Sh*tposting: The act of posting low-quality or irrelevant content on social media or online forums, often with the intention of trolling or eliciting a reaction.

Normie: Someone who is deemed to be "uncool" or out of touch with the latest memes and internet culture.

Rickrolling: A prank in which someone is tricked into clicking a link that leads to the music video for Rick Astley's 1987 hit song "Never Gonna Give You Up."

Distracted Boyfriend: A stock photo that became a popular meme, featuring a man turning his head to look at an attractive woman while his girlfriend looks on disapprovingly.

Harambe: A gorilla at the Cincinnati Zoo who was shot and killed in 2016 after a child fell into his enclosure. Harambe became a popular meme, often used to express outrage or frustration.

Big Chungus: A meme featuring an image of Bugs Bunny enlarged to a comical size, often used to mock or satirize internet trends.

Stonks: A misspelling of the word "stocks," used in memes to represent a successful or profitable investment. The meme often features a character with a graph showing an upward trend in earnings.

