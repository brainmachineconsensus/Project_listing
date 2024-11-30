require('dotenv').config();
const HDWalletProvider = require('@truffle/hdwallet-provider');

module.exports = {
  networks: {
    sepolia: {
      provider: () =>
        new HDWalletProvider(
          process.env.PRIVATE_KEY, // Votre clé privée
          process.env.SEPOLIA_URL  // URL du réseau Sepolia via Alchemy
        ),
      network_id: 11155111, // ID du réseau Sepolia
      gas: 4500000, // Limite de gas pour vos transactions
      gasPrice: 10000000000, // Prix du gas en wei (10 Gwei)
    },
  },
  compilers: {
    solc: {
      version: '0.8.20', // Choisissez une version compatible avec votre contrat
    },
  },
};
