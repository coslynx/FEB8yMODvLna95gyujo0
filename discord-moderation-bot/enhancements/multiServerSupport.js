const multiServerSupport = {
  enableMultiServer: true,
  servers: [],

  addServer: (server) => {
    multiServerSupport.servers.push(server);
  },

  removeServer: (server) => {
    const index = multiServerSupport.servers.indexOf(server);
    if (index !== -1) {
      multiServerSupport.servers.splice(index, 1);
    }
  },

  operateOnServers: (action) => {
    multiServerSupport.servers.forEach((server) => {
      action(server);
    });
  }
};

module.exports = multiServerSupport;