const Discord = require('discord.js');

const client = new Discord.Client();

client.once('ready', () => {
  console.log('Dashboard bot is online!');
});

client.login('your-bot-token');

client.on('message', message => {
  if (message.content === '!dashboard') {
    message.channel.send('Dashboard is under construction. Stay tuned for updates!');
  }
});

client.on('messageDelete', message => {
  console.log(`Message deleted: ${message.content}`);
});

client.on('messageUpdate', (oldMessage, newMessage) => {
  console.log(`Message updated from ${oldMessage.content} to ${newMessage.content}`);
});

client.on('guildMemberAdd', member => {
  const channel = member.guild.channels.cache.find(ch => ch.name === 'general');
  if (!channel) return;
  channel.send(`Welcome to the server, ${member}!`);
});

client.on('guildMemberRemove', member => {
  const channel = member.guild.channels.cache.find(ch => ch.name === 'general');
  if (!channel) return;
  channel.send(`${member} has left the server. Goodbye!`);
});

client.on('guildBanAdd', (guild, user) => {
  const channel = guild.channels.cache.find(ch => ch.name === 'mod-logs');
  if (!channel) return;
  channel.send(`${user.tag} has been banned from the server.`);
});

client.on('guildBanRemove', (guild, user) => {
  const channel = guild.channels.cache.find(ch => ch.name === 'mod-logs');
  if (!channel) return;
  channel.send(`${user.tag} has been unbanned from the server.`);
});