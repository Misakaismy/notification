class test(commands.Cog):
    whitelist = [540408470504079361]
    @commands.Cog.listener('on_message')
    async def test(self, message:message):
        if message.channel == None or not message.channel.guild.id in whitelist or message.author.bot:
            return
        if message.content == prefix,'test':
            await message.channel.send('Post OK!')