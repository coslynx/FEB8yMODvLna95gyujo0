const Discord = require('discord.js');

const client = new Discord.Client();

client.once('ready', () => {
    console.log('Bot is online!');
});

client.on('message', message => {
    if (message.content === '!ping') {
        message.channel.send('Pong!');
    }
});

client.login('your-token-goes-here');