m = True
title = 1
thumb = 1
author = 1
footer = 1

while m == True:
    print('Discord.py Embed Generator - Re-Furnished By skip#9665\n[1] Title\n[2] Thumbnail URL\n[3] Footer\n[4] Author\n[5] Set Image\n[6] Add Field\n[7] Quit')
    val = int(input())

    # Quit Command
    if val == 7:
        m = False
    
    elif val == 1:
        if title == 1:
            title = input("Title of your Embed? -\n")
            description = input('Description of your Embed? -\n')
            print('For your color make sure that you put "0x" before your hex code.')
            color = input('Color of your Embed? -\n')
            finalsend1 = 'discord.Embed(title = "{}", description = "{}", color = {})'.format(title, description, color)
            x = open('Embeds.txt', 'a')
            x.write(finalsend1 + '\n')
            x.close()
            print(finalsend1)
            title = 0
        elif title == 0:
            print("Whoops! I can't add another title. Sorry!")

    elif val == 2:
        if thumb == 1:
            url = input("Thumbnail URL? - ")
            finalsend2 = "embed.set_thumbnail(url = {})".format(url)
            x = open('Embeds.txt', 'a')
            x.write(finalsend2 + '\n')
            x.close()
            print(finalsend2)
            thumb = 0
        elif thumb == 0:
            print("Yikes.. I can only add one thumbnail, I know.. Boomers right!")
    
    elif val == 3:
        if footer == 1:
            name = input("Footer Name? -\n")
            icon = input("Footer Icon URL? -\n")
            finalsend3 = "embed.set_footer(name = '{}', icon_url = '{}')".format(name, icon)
            x = open('Embeds.txt', 'a')
            x.write(finalsend3 + '\n')
            x.close()
            print(finalsend3)
            footer == 0
        elif footer == 0:
            print("Ouch broskie, I really can't add another footer, my bad matey.")

    elif val == 4:
        if author == 1:
            name = input("Author Name? -\n")
            icon = input("Author Icon URL? -\n")
            finalsend4 = "embed.set_author(name = '{}', icon_url = '{}')".format(name, icon)
            x = open('Embeds.txt', 'a')
            x.write(finalsend4 + '\n')
            x.close()
            print(finalsend4)
            author = 0
        elif author == 0:
            print("Bro there can only be one author. Look don't get mad at me I did not make Discord.py!")

    elif val == 5:
        image = input("What image would you like to use? -\n")
        finalsend5 = "embed.set_image(url = '{}')".format(image)
        x = open('Embeds.txt', 'a')
        x.write(finalsend5 + '\n')
        x.close()
        print(finalsend5)

    elif val == 6:
        ask = input("Would you like your fields to be inline with eachother? Reply with either Y/N -\n")
        if ask == 'y' or ask == 'Y':
            name = input("Name inside the field? -\n")
            value = input("What would you like it to say? -\n")
            finalsend6 = "embed.add_field(name = {}, value = '{}', inline = {True})" .format(name, value)
            x = open('Embeds.txt', 'a')
            x.write(finalsend6 + '\n')
            x.close()
            print(finalsend6)
        elif ask == 'n' or ask == 'N':
            name = input("Name inside the field? -\n")
            value = input("What would you like it to say? -\n")
            finalsend8 = "embed.add_field(name = {}, value = '{}', inline = {False})".format(name, value)
            x = open('Embeds.txt', 'a')
            x.write(finalsend8 + '\n')
            x.close()
            print(finalsend8)
