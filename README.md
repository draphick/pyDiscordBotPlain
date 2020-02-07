# A Plain Discord Bot
This repo contains a python file that allows you to run a discord bot. Currently just being used for training purpose.  Please ignore. :D

# Base Install
Without spelling out the small steps, do this:

+ Install Python
+ Install pip
+ Install pip requirements
+ Create a discord bot - https://discordapp.com/developers/applications/
+ Get token from discord bot you created
  + _They call this a CLIENT SECRET in your developer's application portal_
+ Change `TOKEN` variable in `pyDiscordBot.py` to the new one you got
+ Execute the discord bot script: `python pyDiscordBot.py`
+ Send messages to your new discord bot!

# Docker Setup
Again, without all the inbetween steps written out, do the following:

+ Install docker
+ Use `docker build` to create a docker image using the `Dockerfile` in this repo.
+ Run a docker container mounting this repo's directory to `/discordbot/`
  + Tip: `docker run -d -v {PATH_TO}/pyDiscordBotPlain:/discordbot:ro {dockerimagename}
+ Enjoy your containerized Discord Bot

# Extra Credit
No one likes a teacher's pet.

+ Add new commands to the discord bot
+ Join your discord bot to a server
+ Have someone test and break one of your bot commands