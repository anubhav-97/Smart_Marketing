# 🧑‍✈️ Smart Marketer
### Introducing GPT Marketing Navigator: Revolutionizing Marketing Campaign.

The goal of Smart Marketer is to research how much can GPT-4 or LLM's be utilized to generate personalised email, Engaging social media posts and reduce a lot of manual work which inturn can save time and resources.

---
About Smart Marketer:

1. Social Media Campaign: 
It Offers suggestions according to the provided Brand name, Industry and brand description
It Internally Generates a list of topics and formulates ideas for each one
Currently, Facilitates post creation for Twitter,Facebook,Instagram, and LinkedIn
Creates optimized post bodies automatically
Selects hashtags intelligently so that the post get a good out reach
It Allows you to write posts in any language
Currently it uses GPT-3 to provide responses

expected quality: Low (GPT-3: ⚡️), Medium (combination), or High quality (GPT-4: 🐢+💰)
Generates AI Images for each post using Stable Diffusion


2. Email Marketing Campaign: 
It can Generate personalized email content using ChatGPT.
It can draft subject lines, email body text, and call-to-action (CTA) messages tailored to individual recipient with context
It generate product recommendations, discount offer's or can Educate about the a particular product.
It can adjust the tone/style accordingly weather the email style should be Forma, Casual or Neutral.


Use ChatGPT to analyze your email list and segment subscribers based on various criteria, such as demographics, behavior, or engagement level.
ChatGPT can analyze recipient data and recommend the best times to send emails based on individual preferences and past behavior to increase open and click-through rates.


<!-- TOC -->
* [🔌 Requirements](#-requirements)
* [🚦How to start using gpt-pilot?](#how-to-start-using-gpt-pilot)
    * [🐳 How to start gpt-pilot in docker?](#-how-to-start-gpt-pilot-in-docker)
* [🧑‍💻️ Other arguments](#-other-arguments)
* [🔎 Examples](#-examples)
    * [Real-time chat app](#-real-time-chat-app)
    * [Markdown editor](#-markdown-editor)
    * [Timer app](#-timer-app)
* [🏛 Main pillars of GPT Pilot](#-main-pillars-of-gpt-pilot)
* [🏗 How GPT Pilot works?](#-how-gpt-pilot-works)
* [🕴How's GPT Pilot different from _Smol developer_ and _GPT engineer_?](#hows-gpt-pilot-different-from-smol-developer-and-gpt-engineer)
* [🍻 Contributing](#-contributing)
* [🔗 Connect with us](#-connect-with-us)
<!-- TOC -->

---
<div align="center">

### **[👉 Examples of apps written by GPT Pilot 👈](#-examples)**

</div>

<br>

https://github.com/Pythagora-io/gpt-pilot/assets/10895136/0495631b-511e-451b-93d5-8a42acf22d3d

# 🔌 Requirements

- **Python 3**
- **PostgreSQL** (optional, projects default is SQLite)
   - DB is needed for multiple reasons like continuing app development if you had to stop at any point or app crashed, going back to specific step so that you can change some later steps in development, easier debugging, for future we will add functionality to update project (change some things in existing project or add new features to the project and so on)...


# 🚦How to start using gpt-pilot?
After you have Python and PostgreSQL installed, follow these steps:
1. `git clone https://github.com/Pythagora-io/gpt-pilot.git` (clone the repo)
2. `cd Smart Marketing`
3. `python -m venv appenv` (create a virtual environment)
4. `source appenv/bin/activate` (or on Windows `appenv\Scripts\activate`) (activate the virtual environment)
5. `pip install -r requirements.txt` (install the dependencies)
6. `cd pilot`
7. `mv .env.example .env` (create the .env file)
8. Add your environment (OpenAI/Azure), your API key and the SQLite/PostgreSQL database info to the `.env` file
   - to change from SQLite to PostgreSQL in your .env just set `DATABASE_TYPE=postgres`
9. `python db_init.py` (initialize the database)
10. `python main.py` (start GPT Pilot)

After, this, you can just follow the instructions in the terminal.

All generated code will be stored in the folder `workspace` inside the folder named after the app name you enter upon starting the pilot.

**IMPORTANT: To run GPT Pilot, you need to have PostgreSQL set up on your machine**
<br>

## 🐳 How to start gpt-pilot in docker?
1. `git clone https://github.com/Pythagora-io/gpt-pilot.git` (clone the repo)
2. Update the `docker-compose.yml` environment variables
3. run `docker compose build`. this will build a gpt-pilot container for you.
4. run `docker compose up`.
5. access web terminal on `port 7681`
6. `python db_init.py` (initialize the database)
7. `python main.py` (start GPT Pilot)

This will start two containers, one being a new image built by the `Dockerfile` and a postgres database. The new image also has [ttyd](https://github.com/tsl0922/ttyd) installed so that you can easily interact with gpt-pilot. Node is also installed on the image and port 3000 is exposed.


# 🧑‍💻️ CLI arguments

## `app_type` and `name`
If not provided, the ProductOwner will ask for these values

`app_type` is used as a hint to the LLM as to what kind of architecture, language options and conventions would apply. If not provided, `prompts.prompts.ask_for_app_type()` will ask for it.

See `const.common.ALL_TYPES`: 'Web App', 'Script', 'Mobile App', 'Chrome Extension'


## `app_id` and `workspace`
Continue working on an existing app using **`app_id`**
```bash
python main.py app_id=<ID_OF_THE_APP>
```

_or_ **`workspace`** path:

```bash
python main.py workspace=<PATH_TO_PROJECT_WORKSPACE>
```

Each user can have their own workspace path for each App.


## `user_id`, `email` and `password`
These values will be saved to the User table in the DB.

```bash
python main.py user_id=me_at_work
```

If not specified, `user_id` defaults to the OS username, but can be provided explicitly if your OS username differs from your GitHub or work username. This value is used to load the `App` config when the `workspace` arg is provided.

If not specified `email` will be parsed from `~/.gitconfig` if the file exists.

See also [What's the purpose of arguments.password / User.password?](https://github.com/Pythagora-io/gpt-pilot/discussions/55)


## `advanced`
The Architect by default favours certain technologies including: 

- Node.JS
- MongoDB
- PeeWee ORM
- Jest & PyUnit
- Bootstrap
- Vanilla JavaScript
- Socket.io

If you have your own preferences, you can have a deeper conversation with the Architect.

```bash
python main.py advanced=True
```


## `step`
Continue working on an existing app from a specific **`step`** (eg: `user_tasks`)
```bash
python main.py app_id=<ID_OF_THE_APP> step=<STEP_FROM_CONST_COMMON>
```


## `skip_until_dev_step`
Continue working on an existing app from a specific **development step**
```bash
python main.py app_id=<ID_OF_THE_APP> skip_until_dev_step=<DEV_STEP>
```
This is basically the same as `step` but during the actual development process. If you want to play around with gpt-pilot, this is likely the flag you will often use.
<br>

Erase all development steps previously done and continue working on an existing app from start of development

```bash
python main.py app_id=<ID_OF_THE_APP> skip_until_dev_step=0
```


## `delete_unrelated_steps`


## `update_files_before_start`



# 🔎 Examples

Here are a couple of example apps GPT Pilot created by itself:

### 📱 Real-time chat app
- 💬 Prompt: `A simple chat app with real time communication`
- ▶️ [Video of the app creation process](https://youtu.be/bUj9DbMRYhA)
- 💻️ [GitHub repo](https://github.com/Pythagora-io/gpt-pilot-chat-app-demo)


### 📝 Markdown editor
- 💬 Prompt: `Build a simple markdown editor using HTML, CSS, and JavaScript. Allow users to input markdown text and display the formatted output in real-time.`
- ▶️ [Video of the app creation process](https://youtu.be/uZeA1iX9dgg)
- 💻️ [GitHub repo](https://github.com/Pythagora-io/gpt-pilot-demo-markdown-editor.git)


### ⏱️ Timer app
- 💬 Prompt: `Create a simple timer app using HTML, CSS, and JavaScript that allows users to set a countdown timer and receive an alert when the time is up.`
- ▶️ [Video of the app creation process](https://youtu.be/CMN3W18zfiE)
- 💻️ [GitHub repo](https://github.com/Pythagora-io/gpt-pilot-timer-app-demo)

<br>

The idea is that AI won't be able to (at least in the near future) create apps from scratch without the developer being involved. That's why we created an interactive tool that generates code but also requires the developer to check each step so that they can understand what's going on and so that the AI can have a better overview of the entire codebase.

Obviously, it still can't create any production-ready app but the general concept of how this could work is there.

# 🏗 How GPT Pilot works?
Here are the steps GPT Pilot takes to create an app:

![GPT Pilot workflow](https://github.com/Pythagora-io/gpt-pilot/assets/10895136/d89ba1d4-1208-4b7f-b3d4-76e3ccea584e)

1. You enter the app name and the description
2. **Product Owner agent** asks a couple of questions to understand the requirements better
3. **Product Owner agent** writes user stories and asks you if they are all correct (this helps it create code later on)
4. **Architect agent** writes up technologies that will be used for the app
5. **DevOps agent** checks if all technologies are installed on the machine and installs them if they are not
6. **Tech Lead agent** writes up development tasks that Developer will need to implement. This is an important part because, for each step, Tech Lead needs to specify how the user (real world developer) can review if the task is done (e.g. open localhost:3000 and do something)
7. **Developer agent** takes each task and writes up what needs to be done to implement it. The description is in human-readable form.
8. Finally, **Code Monkey agent** takes the Developer's description and the existing file and implements the changes into it. We realized this works much better than giving it to Developer right away to implement changes.

For more details on the roles of agents employed by GPT Pilot refer to [AGENTS.md](https://github.com/Pythagora-io/gpt-pilot/blob/main/pilot/helpers/agents/AGENTS.md)

![GPT Pilot Coding Workflow](https://github.com/Pythagora-io/gpt-pilot/assets/10895136/53ea246c-cefe-401c-8ba0-8e4dd49c987b)


<br>

# 🕴How's GPT Pilot different from _Smol developer_ and _GPT engineer_?
- **GPT Pilot works with the developer to create fully working production-ready app** - I don't think that AI can (at least in the near future) create apps without a developer being involved. So, **GPT Pilot codes the app step by step** just like a developer would in real life. This way, it can debug issues as they arise throughout the development process. If it gets stuck, you, the developer in charge, can review the code and fix the issue. Other similar tools give you the entire codebase at once - this way, bugs are much harder to fix both for AI and for you as a developer.
  <br><br>
- **Works at scale** - GPT Pilot isn't meant to create simple apps but rather so it can work at any scale. It has mechanisms that filter out the code so in each LLM conversation, it doesn't need to store the entire codebase in context, but it shows the LLM only the code that is relevant for the current task it's working on. Once an app is finished, you can always continue working on it by writing instructions on what feature you want to add.

# 🍻 Contributing
If you are interested in contributing to GPT Pilot, I would be more than happy to have you on board but also help you get started. Feel free to ping [zvonimir@pythagora.ai](mailto:zvonimir@pythagora.ai) and I'll help you get started.

## 🔬️ Research
Since this is a research project, there are many areas that need to be researched on both practical and theoretical levels. We're happy to hear how can the entire GPT Pilot concept be improved. For example, maybe it would work better if we structured functional requirements differently or maybe technical requirements need to be specified in a different way.

## 🖥 Development
Other than the research, GPT Pilot needs to be debugged to work in different scenarios. For example, we realized that the quality of the code generated is very sensitive to the size of the development task. When the task is too broad, the code has too many bugs that are hard to fix but when the development task is too narrow, GPT also seems to struggle in getting the task implemented into the existing code.

# 🔗 Connect with us
🌟 As an open source tool, it would mean the world to us if you starred the GPT-pilot repo 🌟

💬 Join [the Discord server](https://discord.gg/HaqXugmxr9) to get in touch.
<br><br>
<br><br>

<br><br>