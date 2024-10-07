<div id="top"</div>

<h1 align="center">Support Bot</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/Cmi1o/support-bot?color=56BEB8">
</p>


<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/Cmi1o" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Telegram bot for support. Your client write to this bot and it creates communication between him and admin using Telegram topics

## :sparkles: Features ##

:heavy_check_mark: Automatic cleaning of inactive users in database\
:heavy_check_mark: Infinity count of people can answer to clients questions, you just need to add them to the group

## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Telegram](https://telegram.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Poetry](https://python-poetry.org/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Python](https://www.python.org/downloads/release/python-3115/) and [PostgreSQL](https://www.postgresql.org/) installed. 

Also you need to create new PostgreSQL database in accordance with this structure:

|Table name    | Column name  | Data type                                              |
| :----------: | :----------: | :----------------------------------------------------: |
|users         | id           | int8(64,0); nextval('users_id_seq'::regclass); primary |
|users         | telegram_id  | int8(64,0)                                             |
|users         | thread_id    | int4(32,0); nullable                                   |
|users         | request_time | timestamp(6)                                           |

Besides this you need to create a new forum in Telegram, find out it's chat ID and add it to `.env`

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/Cmi1o/support-bot

# Access
$ cd support-bot

# Create a virtual env
$ python -m venv .venv

# Activate a virtual env
$ source .venv/bin/activate

# Install dependencies
$ pip install poetry

$ poetry install --no-root

# Run the project
$ poetry run python ./src/main.py

# The bot will work in Telegram in accordance with the link provided by @BotFather
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/Cmi1o" target="_blank">Vasin Georgiy</a>

&#xa0;

<a href="#top">Back to top</a>
