var Web3 = require('web3');

if (typeof web3 !== 'undefined') {
  web3 = new Web3(web3.currentProvider);
} else {
  // set the provider you want from Web3.providers
  web3 = new Web3(new Web3.providers.HttpProvider("https://mainnet.infura.io/MaaVBVQmkcdH9PUQMSp7"));
}

web3.eth.getBlock(48, function(error, result){
    if(!error)
        console.log(result)
    else
        console.error(error);
})
