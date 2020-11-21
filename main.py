'''
A Discord bot for COVID 19: The COVID-19 Info Bot
Start date: August 15th 2020
Founder/Coder: Donald Lee
Researcher: Rosa Chen
Graphic Designer: Matthew Quock 
Beta Tester and Feature Requestor: Kenny Kwan
'''
import discord
from discord.ext import commands, tasks
from covid import Covid
import time
from datetime import datetime
import asyncio

import host

add_bot_link = 'https://discord.com/oauth2/authorize?client_id=744391461113561228&permissions=18432&scope=bot'
website = 'https://thecovid19infobot.github.io/'
#Gets data from https://www.worldometers.info/
covid = Covid(source="worldometers")
covid.get_data()

# For the icon to the left
embed_icon_url = 'https://raw.githubusercontent.com/TheCOVID19InfoBot/TheCOVID19InfoBot.github.io/master/logos/covid_bot_logo_outline.png'

# For the icon to the right/footer
embed_icon_url_right = 'https://raw.githubusercontent.com/TheCOVID19InfoBot/TheCOVID19InfoBot.github.io/master/logos/covidbotmainp.png'

wear_a_mask = "Medical professionals around the world are advising people to wear a mask in order to limit the spread of COVID-19! " + " " + ":mask: \n\nFor more information about masks, check out this [website](<https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection/prevention-risks/about-non-medical-masks-face-coverings.html>) by the Government of Canada!"

# a prefix to all the commands for this bot (ex: /help, /hello, /cool)
bot = commands.Bot(command_prefix='/')  #This can be ?,!, etc.

# removes the preset help command that comes with the discord library
bot.remove_command('help')


@tasks.loop(seconds=86400, count=99999)  #86400 = 24 hours
async def daily_count():
	world_info = covid.get_status_by_country_name('World')
	world_confirmed_cases = "{:,}".format(world_info['confirmed'])
	world_active = "{:,}".format(world_info['active'])
	world_deaths = "{:,}".format(world_info['deaths'])
	world_recovered = "{:,}".format(world_info['recovered'])
	world_new_cases = "{:,}".format(world_info['new_cases'])
	world_new_deaths = "{:,}".format(world_info['new_deaths'])
	world_critical_condition = "{:,}".format(world_info['critical'])
	world_confirmedcases_message = 'Globally, there are about **' + str(
	    world_confirmed_cases
	) + '** confirmed cases of COVID-19!\nIn those confirmed cases there are about:'
	now = time.localtime()
	#Extracting the year from localtime
	year = now[0]
	#Extracting the month from localtime
	x = now[1]
	months = [
	    'January', 'February', 'March', 'April', 'May', 'June', 'July',
	    'August', 'September', 'October', 'November', 'December'
	]
	month = months[x - 1]
	#Extracting the day from localtime
	day = now[2]
	todaydate = month + ' ' + str(day) + ', ' + str(year)
	etest = discord.Embed(
	    title='Here is your daily global cases update for ' + todaydate,
	    description=world_confirmedcases_message,
	    colour=discord.Colour.blue())

	etest.add_field(
	    name='Active Cases', value="`" + str(world_active) + "`", inline=True)
	etest.add_field(
	    name='Recovered', value="`" + str(world_recovered) + "`", inline=True)
	etest.add_field(
	    name='Deaths', value="`" + str(world_deaths) + "`", inline=True)
	etest.add_field(
	    name='New cases today',
	    value="`" + str(world_new_cases) + "`",
	    inline=True)
	etest.add_field(
	    name='Deaths today',
	    value="`" + str(world_new_deaths) + "`",
	    inline=True)
	etest.add_field(
	    name='People in critical condition',
	    value="`" + str(world_critical_condition) + "`",
	    inline=True)
	etest.add_field(name='Important', value=wear_a_mask, inline=False)
	etest.set_footer(
	    text="© 2020 The COVID-19 Info Bot", icon_url=embed_icon_url_right)
	print("I gave out daily global cases info!")
	for guild in bot.guilds:
		try:
			for num_of_channel in range(500):
				try:
					await guild.text_channels[num_of_channel].send(embed=etest)
					break
				except:
					if num_of_channel == 499:
						print("Could not send daily news to Server name: " +
						      str(guild))
		except:
			#This doesn't do anything
			print("Could not send daily news to Server name: " + str(guild))


daily_time = time.gmtime()
hour_gmt = daily_time[3]  #Extracting the hours from daily_time
min_for_daily = daily_time[4]  #Extracting the mins from daily_time
minutes_for_daily = 60 - min_for_daily
hour_pst = hour_gmt + 17
if hour_pst >= 24:
	hour_pst -= 24

when_for_news = 8 - hour_pst
if when_for_news < 0:
	when_for_news += 23

minutes_to_seconds_for_daily = minutes_for_daily * 60
hours_to_seconds_for_daily = when_for_news * 60 * 60
when_to_send_daily = int(hours_to_seconds_for_daily) + int(
    minutes_to_seconds_for_daily)
print('We will send the next daily message in ' + str(when_to_send_daily) +
      ' seconds')


@tasks.loop(seconds=when_to_send_daily, count=999)
async def slow_count():
	await asyncio.sleep(when_to_send_daily)
	world_info = covid.get_status_by_country_name('World')
	world_confirmed_cases = "{:,}".format(world_info['confirmed'])
	world_active = "{:,}".format(world_info['active'])
	world_deaths = "{:,}".format(world_info['deaths'])
	world_recovered = "{:,}".format(world_info['recovered'])
	world_new_cases = "{:,}".format(world_info['new_cases'])
	world_new_deaths = "{:,}".format(world_info['new_deaths'])
	world_critical_condition = "{:,}".format(world_info['critical'])
	world_confirmedcases_message = 'Globally, there are about **' + str(
	    world_confirmed_cases
	) + '** confirmed cases of COVID-19!\nIn those confirmed cases there are about:'
	now = time.localtime()
	#Extracting the year from localtime
	year = now[0]
	#Extracting the month from localtime
	x = now[1]
	months = [
	    'January', 'February', 'March', 'April', 'May', 'June', 'July',
	    'August', 'September', 'October', 'November', 'December'
	]
	month = months[x - 1]
	#Extracting the day from localtime
	day = now[2]
	todaydate = month + ' ' + str(day) + ', ' + str(year)
	etest = discord.Embed(
	    title='Here is your daily global cases update for ' + todaydate,
	    description=world_confirmedcases_message,
	    colour=discord.Colour.blue())

	etest.add_field(
	    name='Active Cases', value="`" + str(world_active) + "`", inline=True)
	etest.add_field(
	    name='Recovered', value="`" + str(world_recovered) + "`", inline=True)
	etest.add_field(
	    name='Deaths', value="`" + str(world_deaths) + "`", inline=True)
	etest.add_field(
	    name='New cases today',
	    value="`" + str(world_new_cases) + "`",
	    inline=True)
	etest.add_field(
	    name='Deaths today',
	    value="`" + str(world_new_deaths) + "`",
	    inline=True)
	etest.add_field(
	    name='People in critical condition',
	    value="`" + str(world_critical_condition) + "`",
	    inline=True)
	etest.add_field(name='Important', value=wear_a_mask, inline=False)
	etest.set_footer(
	    text="© 2020 The COVID-19 Info Bot", icon_url=embed_icon_url_right)
	print("I gave out daily global cases info!")
	for guild in bot.guilds:
		try:
			for num_of_channel in range(500):
				try:
					await guild.text_channels[num_of_channel].send(embed=etest)
					break
				except:
					if num_of_channel == 499:
						print("Could not send daily news to Server name: " +
						      str(guild))
		except:
			#This doesn't do anything
			print("Could not send daily news to Server name: " + str(guild))
	await asyncio.sleep(86400)
	daily_count.start()


# bot on initialization
@bot.event
async def on_ready():
	# Initialization message
	print(
	    'The Bot is Online and Running \nGo back to the Discord Server to test it out! \n\n'
	)
	# changes the discord status
	await bot.change_presence(
	    activity=discord.Activity(
	        type=discord.ActivityType.watching, name='for /help'))

	#Gets the name of all the servers it's in
	store_server_info = open("servers_i_am_in.txt", "a")
	#Gets time and date
	now = time.localtime()  #Gets the local time
	year = now[0]  # Extracting the year from localtime
	x = now[1]  #Extracting the month from localtime
	months = [
	    'January', 'February', 'March', 'April', 'May', 'June', 'July',
	    'August', 'September', 'October', 'November', 'December'
	]
	month = months[x - 1]
	#Extracting the day from localtime
	day = now[2]
	hourmil = now[3]
	if hourmil > 12:
		hour = int(hourmil) - 12
		meridiem = 'PM'
	else:
		hour = hourmil
		meridiem = 'AM'
	minute = now[4]
	thecurrenttime = str(hour) + ":" + str(minute) + ' ' + meridiem
	todaydate = month + ' ' + str(day) + ', ' + str(year) + " at " + str(
	    thecurrenttime)
	store_server_info.write("\n" + todaydate + " GMT\n")
	store_server_info.write("Running in " + str(len(bot.guilds)) +
	                        " servers! \n\n")
	#Gets server information from the servers it is in
	for see_servers in bot.guilds:
		#Gets server name and number of users
		try:
			store_server_info.write("Server name: " + str(see_servers) +
			                        " --> Number of members: " +
			                        str(see_servers.member_count) + "\n")
		except:
			pass

	store_server_info.write("\nLarger data: \n" + str(bot.guilds) +
	                        "\n\n^^^^^^^^^^\n")
	store_server_info.close()
	slow_count.start()


# When the bot joins a server
@bot.event
async def on_guild_join(guild):
	servers_i_joined = open("servers_i_joined.txt", "a")
	#Gets time and date
	now = time.localtime()  #Gets the local time
	# Extracting the year from localtime
	year = now[0]
	#Extracting the month from localtime
	x = now[1]
	months = [
	    'January', 'February', 'March', 'April', 'May', 'June', 'July',
	    'August', 'September', 'October', 'November', 'December'
	]
	month = months[x - 1]
	#Extracting the day from localtime
	day = now[2]
	hourmil = now[3]
	if hourmil > 12:
		hour = int(hourmil) - 12
		meridiem = 'PM'
	else:
		hour = hourmil
		meridiem = 'AM'
	minute = now[4]
	thecurrenttime = str(hour) + ":" + str(minute) + ' ' + meridiem
	todaydate = month + ' ' + str(day) + ', ' + str(year) + " at " + str(
	    thecurrenttime)
	servers_i_joined.write(
	    "Name: " + str(guild) + ' --> ID: ' + str(guild.id) +
	    ' --> Date I joined: ' + todaydate + ' GMT\n\n')  #Repl uses GMT time
	servers_i_joined.close()

	etest = discord.Embed(
	    title='Thanks for inviting me into your server! :smiley:',
	    description=
	    '**I am a bot that provides fast and reliable answers to your questions regarding COVID-19!**\n\n**-** My prefix is `/`\n**-** Check out what I can do by typing `/help` in this channel or by messaging me!\n**-** By having and using me in your server, you agree to my following [Terms of Service](<https://thecovid19infobot.github.io/tos.html>)!\n\n**Need help?** Join our [support server](<https://discord.gg/r4M4dbr>)! :star_struck:\n\nFor more information, check out our [website]('
	    + website +
	    ')! :smiley:\n\n**Note:**\nBy default, `daily COVID-19 news` will be sent out to the first text channel that I have “`Send messages`” permission on. If you want to restrict me into a specific text channel, check out this [tutorial](https://github.com/TheCOVID19InfoBot/TheCOVID19InfoBot.github.io/blob/master/RestrictBotToAChannel.md)!',
	    colour=discord.Colour.blue())

	etest.add_field(name='Important', value=wear_a_mask, inline=True)
	etest.set_footer(
	    text="© 2020 The COVID-19 Info Bot", icon_url=embed_icon_url_right)
	try:
		for num_of_channel in range(500):
			try:
				await guild.text_channels[num_of_channel].send(embed=etest)
				break
			except:
				if num_of_channel == 499:
					print("Could not welcome message to Server name: " +
					      str(guild))
	except:
		#This doesn't do anything
		print("Could not send welcome message to Server name: " + str(guild))


# Help and About this project
@bot.command(aliases=[
    'Help', 'HELP', 'help', 'help.', 'Help.', 'HELP.', '?', 'hello', 'HELLO',
    'Hello', 'About', 'ABOUT', 'credit', 'CREDIT', 'Credit'
])
async def about(ctx):
	in_x_servers = str(len(bot.guilds))
	in_x_servers_plus_one = int(in_x_servers) + 1
	etest = discord.Embed(
	    title='About',
	    description=
	    'The COVID-19 Info Bot is a bot that provides fast and reliable real time answers to your questions regarding COVID-19! With me, you can stay updated on COVID-19 while enjoying Discord! :star_struck: \nFor more information, check out our [website]('
	    + website + ')! :smiley:',
	    colour=discord.Colour.blue())

	cases_cite_message = 'This bot was made possible with the help of the [covid module](https://ahmednafies.github.io/covid/#requirements), an open source module that gathers COVID-19 case data provided by **[worldometers.info](https://www.worldometers.info/coronavirus)**\n\n**Additional note:** New cases and deaths reset after midnight GMT+0.\n'

	etest.set_thumbnail(url=embed_icon_url_right)
	etest.set_author(
	    name="The COVID-19 Info Bot",
	    url=add_bot_link,
	    icon_url=embed_icon_url)
	etest.add_field(
	    name='Our Team :raised_hands:',
	    value=
	    "[Find out who my creators are!](https://thecovid19infobot.github.io/team.html)",
	    inline=False)

	etest.add_field(
	    name=':question: Help and Info',
	    value="`/help` OR `/about`",
	    inline=True)
	etest.add_field(
	    name=':globe_with_meridians: For Global Cases',
	    value="`/world`",
	    inline=True)
	etest.add_field(
	    name='Cases for Continents', value="`/cases <continent>`", inline=True)
	etest.add_field(
	    name='Cases for Countries', value="`/cases <country>`", inline=True)
	etest.add_field(name='Symptoms', value="`/symptoms`", inline=True)
	etest.add_field(name=':newspaper: News', value="`/news`", inline=True)
	etest.add_field(name='Resources', value="`/resources`", inline=True)
	etest.add_field(
	    name=':no_entry_sign: Preventions',
	    value="`/preventions`",
	    inline=True)
	etest.add_field(
	    name=':white_check_mark: Vote', value="`/vote`", inline=True)

	etest.add_field(
	    name='Add us to your server! :star_struck:',
	    value='We are currently running in **' + str(in_x_servers) +
	    ' **servers!\n[Add us to your server now](' + add_bot_link +
	    ') to make that **' + str(in_x_servers_plus_one) +
	    '!** We are free! :smiley:',
	    inline=False)
	etest.add_field(
	    name='Sources',
	    value=
	    '[Find out where we got our information from!](<https://thecovid19infobot.github.io/sources.html>)',
	    inline=False)
	etest.add_field(
	    name='Need help?',
	    value='[Join our support server!](<https://discord.gg/r4M4dbr>)',
	    inline=False)
	etest.add_field(name='Note:', value=cases_cite_message, inline=False)
	etest.set_footer(
	    text="© 2020 The COVID-19 Info Bot", icon_url=embed_icon_url_right)

	await ctx.send(embed=etest)
	print('I told someone what this project is!')


# World
@bot.command(aliases=['World', 'WORLD', 'Global', 'GLOBAL', 'global'])
async def world(ctx):
	world_info = covid.get_status_by_country_name('World')
	world_confirmed_cases = "{:,}".format(world_info['confirmed'])
	world_active = "{:,}".format(world_info['active'])
	world_deaths = "{:,}".format(world_info['deaths'])
	world_recovered = "{:,}".format(world_info['recovered'])
	world_new_cases = "{:,}".format(world_info['new_cases'])
	world_new_deaths = "{:,}".format(world_info['new_deaths'])
	world_critical_condition = "{:,}".format(world_info['critical'])
	world_confirmedcases_message = 'Globally, there are about **' + str(
	    world_confirmed_cases
	) + '** confirmed cases of COVID-19!\nIn those confirmed cases there are about:'
	etest = discord.Embed(
	    title='Global cases',
	    description=world_confirmedcases_message,
	    colour=discord.Colour.blue())

	etest.add_field(
	    name='Active Cases', value="`" + str(world_active) + "`", inline=True)
	etest.add_field(
	    name='Recovered', value="`" + str(world_recovered) + "`", inline=True)
	etest.add_field(
	    name='Deaths', value="`" + str(world_deaths) + "`", inline=True)

	etest.add_field(
	    name='New cases today',
	    value="`" + str(world_new_cases) + "`",
	    inline=True)
	etest.add_field(
	    name='Deaths today',
	    value="`" + str(world_new_deaths) + "`",
	    inline=True)
	etest.add_field(
	    name='People in critical condition',
	    value="`" + str(world_critical_condition) + "`",
	    inline=True)
	etest.add_field(name='Important', value=wear_a_mask, inline=False)
	etest.set_footer(
	    text="© 2020 The COVID-19 Info Bot", icon_url=embed_icon_url_right)

	await ctx.send(embed=etest)

	print("I gave out global cases info!")


#Cases
@bot.command(aliases=['Cases', 'CASES', 'case', 'CASE', 'Case'])
async def cases(ctx, *, country):
	try:
		north_korea = 'n. korea'
		CNFD = 'Sorry, we could not find data regarding COVID-19 cases in'
		if country.lower() == north_korea:
			country_nofind_message = CNFD + ' North Korea. However, we can find you data regarding COVID-19 cases in most countries! :smiley:'

			etest = discord.Embed(
			    title='Cases for ' + country.capitalize(),
			    description=country_nofind_message,
			    colour=discord.Colour.blue())
			etest.add_field(name='Important', value=wear_a_mask, inline=False)
			etest.set_footer(
			    text="© 2020 The COVID-19 Info Bot",
			    icon_url=embed_icon_url_right)

			await ctx.send(embed=etest)

			print('Could not find data for ' + country + '!')

		elif country.lower() == 'marshall islands':
			country_nofind_message = CNFD + ' Marshall Islands. However, we can find you data regarding COVID-19 cases in most countries! :smiley:'

			etest = discord.Embed(
			    title='Cases for ' + country.capitalize(),
			    description=country_nofind_message,
			    colour=discord.Colour.blue())
			etest.add_field(name='Important', value=wear_a_mask, inline=False)
			etest.set_footer(
			    text="© 2020 The COVID-19 Info Bot",
			    icon_url=embed_icon_url_right)

			await ctx.send(embed=etest)

			print('Could not find data for ' + country + '!')

		elif country.lower() == 'kiribati':
			country_nofind_message = CNFD + ' Kiribati. However, we can find you data regarding COVID-19 cases in most countries! :smiley:'

			etest = discord.Embed(
			    title='Cases for ' + country.capitalize(),
			    description=country_nofind_message,
			    colour=discord.Colour.blue())
			etest.add_field(name='Important', value=wear_a_mask, inline=False)
			etest.set_footer(
			    text="© 2020 The COVID-19 Info Bot",
			    icon_url=embed_icon_url_right)

			await ctx.send(embed=etest)

			print('Could not find data for ' + country + '!')

		elif country.lower() == 'micronesia':
			country_nofind_message = CNFD + ' Micronesia. However, we can find you data regarding COVID-19 cases in most countries! :smiley:'

			etest = discord.Embed(
			    title='Cases for ' + country.capitalize(),
			    description=country_nofind_message,
			    colour=discord.Colour.blue())
			etest.add_field(name='Important', value=wear_a_mask, inline=False)
			etest.set_footer(
			    text="© 2020 The COVID-19 Info Bot",
			    icon_url=embed_icon_url_right)

			await ctx.send(embed=etest)

			print('Could not find data for ' + country + '!')

		elif country.lower() == 'kiribati':
			country_nofind_message = CNFD + ' Kiribati. However, we can find you data regarding COVID-19 cases in most countries! :smiley:'

			etest = discord.Embed(
			    title='Cases for ' + country.capitalize(),
			    description=country_nofind_message,
			    colour=discord.Colour.blue())
			etest.add_field(name='Important', value=wear_a_mask, inline=False)
			etest.set_footer(
			    text="© 2020 The COVID-19 Info Bot",
			    icon_url=embed_icon_url_right)

			await ctx.send(embed=etest)
			print('Could not find data for ' + country + '!')

		elif country.lower() == 'solomon islands':
			country_nofind_message = CNFD + ' Solomon Islands. However, we can find you data regarding COVID-19 cases in most countries! :smiley:'

			etest = discord.Embed(
			    title='Cases for ' + country.capitalize(),
			    description=country_nofind_message,
			    colour=discord.Colour.blue())

			etest.add_field(name='Important', value=wear_a_mask, inline=False)
			etest.set_footer(
			    text="© 2020 The COVID-19 Info Bot",
			    icon_url=embed_icon_url_right)

			await ctx.send(embed=etest)
			print('Could not find data for ' + country + '!')

		elif country.lower() == 'antarctica':

			etest = discord.Embed(
			    title='Cases for ' + country.capitalize(),
			    colour=discord.Colour.blue())

			etest.add_field(
			    name='Active Cases', value=":ice_cube:", inline=True)
			etest.add_field(name='Recovered', value=":ice_cube:", inline=True)
			etest.add_field(name='Deaths', value=":ice_cube:", inline=True)

			etest.add_field(
			    name='New cases today', value=":ice_cube:", inline=True)
			etest.add_field(
			    name='Deaths today', value=":ice_cube:", inline=True)
			etest.add_field(
			    name='People in critical condition',
			    value=":ice_cube:",
			    inline=True)
			etest.add_field(
			    name='Important',
			    value=
			    'Oh no! All the data from Antarctica has been frozen! :cold_face: \n\nClimate change will soon unfreeze this data, but sadly, the penguins, seals, and whales will eventually lose their homes. :penguin: \n\nFind out how you can help slow down climate change [here!](<https://davidsuzuki.org/what-you-can-do/top-10-ways-can-stop-climate-change/>)',
			    inline=False)

			etest.set_footer(
			    text="© 2020 The COVID-19 Info Bot",
			    icon_url=embed_icon_url_right)

			await ctx.send(embed=etest)
			print('Could not find data for ' + country + '!')

		else:
			info = covid.get_status_by_country_name(country)
			confirmedcases = "{:,}".format(info['confirmed'])
			active = "{:,}".format(info['active'])
			deaths = "{:,}".format(info['deaths'])
			recovered = "{:,}".format(info['recovered'])
			newcases = "{:,}".format(info['new_cases'])
			newdeaths = "{:,}".format(info['new_deaths'])
			criticalcondition = "{:,}".format(info['critical'])

			confirmedcases_message = 'There is a total of about **' + str(
			    confirmedcases
			) + ' **confirmed cases of COVID-19 in **' + country.capitalize(
			) + '**!'

			etest = discord.Embed(
			    title='Cases for ' + country.capitalize(),
			    description=confirmedcases_message,
			    colour=discord.Colour.blue())

			etest.add_field(
			    name='Active Cases',
			    value="`" + str(active) + "`",
			    inline=True)
			etest.add_field(
			    name='Recovered',
			    value="`" + str(recovered) + "`",
			    inline=True)
			etest.add_field(
			    name='Deaths', value="`" + str(deaths) + "`", inline=True)

			etest.add_field(
			    name='New cases today',
			    value="`" + str(newcases) + "`",
			    inline=True)
			etest.add_field(
			    name='Deaths today',
			    value="`" + str(newdeaths) + "`",
			    inline=True)
			etest.add_field(
			    name='People in critical condition',
			    value="`" + str(criticalcondition) + "`",
			    inline=True)
			etest.add_field(name='Important', value=wear_a_mask, inline=False)
			etest.set_footer(
			    text="© 2020 The COVID-19 Info Bot",
			    icon_url=embed_icon_url_right)

			await ctx.send(embed=etest)

			print("I told someone about COVID cases data!")

	except:
		etest = discord.Embed(
		    title='Please try again',
		    description=
		    'Sorry, we could not find your country or continent, please try again!\nYou may have made some common naming errors, so here are the corrections! :smiley:',
		    colour=discord.Colour.blue())

		etest.add_field(
		    name='United States', value="`/cases USA`", inline=True)
		etest.add_field(
		    name='United Kingdom', value="`/cases UK`", inline=True)
		etest.add_field(
		    name='Hong Kong', value="`/cases Hong Kong`", inline=True)
		etest.add_field(
		    name='Central African Republic', value="`/cases CAR`", inline=True)
		etest.add_field(
		    name='South Korea', value="`/cases S. Korea`", inline=True)
		etest.add_field(
		    name='Saint Vincent and the Grenadines',
		    value="`/cases St. Vincent Grenadines`",
		    inline=True)
		etest.add_field(
		    name='Democratic Republic of the Congo',
		    value="`/cases DRC`",
		    inline=True)
		etest.add_field(name='Important', value=wear_a_mask, inline=False)
		etest.set_footer(
		    text="© 2020 The COVID-19 Info Bot", icon_url=embed_icon_url_right)

		await ctx.send(embed=etest)
		print("/cases typo I think!")


# Symptoms
@bot.command(aliases=[
    'Symptoms',
    'SYMPTOMS',
])
async def symptoms(ctx):
	etest = discord.Embed(
	    title='COVID-19 Symptoms',
	    description=
	    'According to [Canada.ca](https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection/guidance-documents/signs-symptoms-severity.html) and [CDC](https://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/symptoms.html), the Coronavirus symptoms include:',
	    colour=discord.Colour.blue())

	etest.add_field(
	    name='Common',
	    value=
	    "```- fever\n- dry cough\n- fatigue\n- decreased sense of taste and smell\n- shortness of breath\n- loss of appetite\n- chills```",
	    inline=False)
	etest.add_field(
	    name='Uncommon',
	    value=
	    "```CSS\n- sore throat\n- muscle aches\n- headaches\n- difficulty swallowing\n- sputum production\n- chest pain\n- nausea or vomiting\n- diarrhea\n- dizziness\n- discolouration of fingers or toes\n- abdominal pain\n- runny or stuffy nose\n- conjunctivis (pink eye)```",
	    inline=False)
	etest.add_field(
	    name='Very Rare',
	    value=
	    "```diff\n- fainting\n- confusion\n- skin manifestations\n- congestion or a runny nose```",
	    inline=False)

	etest.set_footer(
	    text="© 2020 The COVID-19 Info Bot", icon_url=embed_icon_url_right)

	await ctx.send(embed=etest)
	print('I told someone the COVID-19 symptoms!')


# Resources
@bot.command(
    aliases=['Resources', 'RESOURCES', 'resource', 'RESOURCE', 'Resource'])
async def resources(ctx):

	#resources_message = "**Here is a list of categorized resources that you may find helpful:exclamation::**\n\n**Advice and Safety:**\n- [When and how to wear your mask properly](<https://www.cedars-sinai.org/newsroom/when-and-how-to-wear-a-mask/>)\n- [Disinfecting your household](<https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/cleaning-disinfection.html>)\n- [Advice regarding this pandemic](<https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public>)\n**Virology**\n- [COVID-19 FAQ](<https://www.cdc.gov/coronavirus/2019-ncov/faq.html>)\n- [About COVID-19 antibody testing](<https://www.cedars-sinai.org/newsroom/covid-19-what-you-need-to-know-about-antibody-testing/>)\n- [List of COVID-19 facts by CDC](<https://www.cdc.gov/coronavirus/2019-ncov/index.html>)\n- [Databases and journals related to COVID-19](<https://www.cdc.gov/library/researchguides/2019novelcoronavirus/databasesjournals.html>)\n**Status, Implications, and Data**\n- [Johns Hopkins COVID-19 cases dashboard](<https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6>)\n- [List of travel restrictions](<https://www.ca.kayak.com/travel-restrictions>)\n- [COVID-19 Vaccine Tracker by CBC](<https://newsinteractives.cbc.ca/coronavirusvaccinetracker/>)\n**Others**\n- [Canada's COVID-19 Self-Assessment Tool](<https://ca.thrive.health/covid19/en>)\n- [List of news articles and helpful resources](<https://covid19.who.int>)"

	advice_and_safety = "**Advice and Safety:**\n- [When and how to wear your mask properly](<https://www.cedars-sinai.org/newsroom/when-and-how-to-wear-a-mask/>)\n- [Disinfecting your household](<https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/cleaning-disinfection.html>)\n- [Advice regarding this pandemic](<https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public>)"

	virology = "**Virology:**\n- [About COVID-19 antibody testing](<https://www.cedars-sinai.org/newsroom/covid-19-what-you-need-to-know-about-antibody-testing/>)\n- [Databases and journals related to COVID-19](<https://www.cdc.gov/library/researchguides/2019novelcoronavirus/databasesjournals.html>)"

	s_i_and_d = "**Status, Implications, and Data:**\n- [Johns Hopkins COVID-19 cases dashboard](<https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6>)\n- [List of travel restrictions](<https://www.ca.kayak.com/travel-restrictions>)\n- [COVID-19 Vaccine Tracker by CBC](<https://newsinteractives.cbc.ca/coronavirusvaccinetracker/>)"

	others = "**Others:**\n- [Canada's COVID-19 Self-Assessment Tool](<https://ca.thrive.health/covid19/en>)\n- [List of news articles and helpful resources](<https://covid19.who.int>)\n- [List of COVID-19 facts by CDC](<https://www.cdc.gov/coronavirus/2019-ncov/index.html>)\n- [COVID-19 FAQ](<https://www.cdc.gov/coronavirus/2019-ncov/faq.html>)"

	resources_message = "**Here is a list of categorized resources that you may find helpful:exclamation::**\n\n" + advice_and_safety + "\n\n" + virology + "\n\n" + s_i_and_d + "\n\n" + others

	etest = discord.Embed(
	    title='Resources for COVID-19',
	    description=resources_message,
	    colour=discord.Colour.blue())

	etest.set_footer(
	    text="© 2020 The COVID-19 Info Bot", icon_url=embed_icon_url_right)

	await ctx.send(embed=etest)

	print("I gave someone resources!")


# How Can I protect myself
@bot.command(aliases=[
    'Prevention', 'PREVENTION', 'prevention', 'Preventions', 'PREVENTIONS'
])
async def preventions(ctx):

	preventions_message = "**Here are some ways on how you can protect yourself from COVID-19:**\n```1. Wash your hands with soap or sanitize it with an alcohol based sanitizer. \n\n2. Wear a mask to protect others! Especially elderlies and those who are immunocompromised!\n\n3. Stay 2 meters away from others when possible!\n\n4. Avoid touching your eyes, nose, or mouth. \n\n5. Avoid going to crowded areas or large social gatherings. \n\n6. Self-isolate and seek medical attention if you are experiencing any COVID-19 symptoms. View the list of symptoms with /symptoms \n\n7. Avoid personal greetings such as handshakes.\n\n8. Avoid non-essential travel, but if you do travel, please self-isolate for 14 days upon arrival.\n\n9. It is recommended to be in areas with good ventilation as it reduces the risk of exposure to infectious respiratory droplets.```"

	etest = discord.Embed(
	    title='Preventing COVID-19',
	    description=preventions_message,
	    colour=discord.Colour.blue())

	etest.add_field(
	    name='Sources',
	    value=
	    "- [Canada.ca](https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection/prevention-risks.html)\n",
	    inline=False)
	etest.set_footer(
	    text="© 2020 The COVID-19 Info Bot", icon_url=embed_icon_url_right)

	await ctx.send(embed=etest)
	print("I taught someone how to protect themself!")


# News
@bot.command(aliases=['NEWS', 'News', 'Article', 'ARTICLES', 'article'])
async def news(ctx):

	#news_message = '**Here are some great news outlets regarding COVID-19:**\n- [CBC](<https://www.cbc.ca/news/covid-19>)\n- [Global News](<https://globalnews.ca/tag/coronavirus/>)\n- [BBC](<https://www.bbc.com/news/coronavirus>) \n- [World Health Organization](<https://www.who.int/emergencies/diseases/novel-coronavirus-2019/media-resources/news>)'

	american_news = "**America:**\n- [Associated Press News ](<https://apnews.com/hub/health>)\n- [CBS News](<https://www.cbsnews.com/feature/coronavirus/>)\n- [USA Today](<https://www.usatoday.com/news/coronavirus/>)\n- [The New York Times](<https://www.nytimes.com/news-event/coronavirus>)"

	canadian_news = "**Canada:**\n- [CBC](<https://www.cbc.ca/news/covid-19>)\n- [National Post](<https://nationalpost.com/tag/coronavirus/>)\n- [The Globe and Mail](<https://www.theglobeandmail.com/topics/coronavirus/>)\n- [CTV News](<https://www.ctvnews.ca/health/coronavirus/>)\n- [Global News](<https://globalnews.ca/tag/coronavirus/>)"

	europe_news = "**Europe:**\n- [EUobserver](<https://euobserver.com/coronavirus>)\n- [The Telegraph](<https://www.telegraph.co.uk/coronavirus/>)\n- [The Independent](<https://www.independent.co.uk/topic/covid-19>)\n- [BBC](<https://www.bbc.com/news/coronavirus>)"

	africa_news = "**Africa:**\n- [Africanews](<https://www.africanews.com/tag/coronavirus/>)"

	asia_news = "**Asia:**\n- [South China Morning Post](<https://www.scmp.com/coronavirus?src=main_menu_primary>)\n- [Hong Kong Free Press](<https://hongkongfp.com/covid-19/>)"

	australia_news = "**Australia:**\n- [ABC News Australia](<https://www.abc.net.au/news/story-streams/coronavirus/>)"

	worldwide_news = "**:earth_americas: Global News Outlets: **\n- [World Health Organization](<https://www.who.int/emergencies/diseases/novel-coronavirus-2019/media-resources/news>)"

	news_message = "**Here are some great news outlets regarding COVID-19:**\n\n" + worldwide_news + "\n\n" + american_news + "\n\n" + canadian_news + "\n\n" + europe_news + "\n\n" + africa_news + "\n\n" + australia_news + "\n\n" + asia_news

	etest = discord.Embed(
	    title=':newspaper: Credible news outlets for COVID-19',
	    description=news_message,
	    colour=discord.Colour.blue())

	etest.set_footer(
	    text="© 2020 The COVID-19 Info Bot", icon_url=embed_icon_url_right)

	await ctx.send(embed=etest)
	print('I gave out some useful news articles!')


@bot.command(aliases=['VOTE', 'Vote'])
async def vote(ctx):
	vote_message = 'Hi there, :wave:\nIf you find our bot helpful, please give it an upvote! :white_check_mark:\n\n**Feel free to upvote it in one or more of these websites:**\n- [top.gg](<https://top.gg/bot/744391461113561228>)          :trophy: \n- [Discord Bot List](<https://discordbotlist.com/bots/the-covid-19-info-bot>)\n- [Discord Boats](<https://discord.boats/bot/744391461113561228>)\n\n**We strive to make our bot more helpful! Let us know how we can improve in our [support server](<https://discord.gg/r4M4dbr>)!**'

	etest = discord.Embed(
	    title='Upvote The COVID-19 Info Bot',
	    description=vote_message,
	    colour=discord.Colour.blue())

	etest.set_footer(
	    text="© 2020 The COVID-19 Info Bot", icon_url=embed_icon_url_right)

	await ctx.send(embed=etest)
	print('I gave out the vote link')


@bot.event
async def on_command_error(error, ctx):
	print("Not a command")


# Tells how many servers we are running in
@bot.command(aliases=['Server', 'SERVER', 'server', 'Servers', 'SERVERS'])
async def servers(ctx):
	in_x_servers = str(len(bot.guilds))
	in_x_servers_plus_one = int(in_x_servers) + 1

	etest = discord.Embed(
	    title='How many servers are we running in?',
	    description='We are currently running in **' + str(in_x_servers) +
	    ' **servers!\n[Add us to your server now](' + add_bot_link +
	    ') and make that **' + str(in_x_servers_plus_one) +
	    '! **We are free! No strings attached! :smiley:',
	    colour=discord.Colour.blue())

	etest.set_footer(
	    text="© 2020 The COVID-19 Info Bot", icon_url=embed_icon_url_right)
	await ctx.send(embed=etest)
	print('I told someone how many servers we are running it!')


# run keepAlive() script and run bot on token
host.keepAlive()

infile = open('bot_token.txt')
TOKEN = infile.readline()

bot.run(TOKEN)
