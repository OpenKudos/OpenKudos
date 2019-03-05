# Kudos Python

Kudos Python is an scraping kudos library based on the  [kudos contract](https://github.com/gitcoinco/Kudos721Contract).
To begin to scrap kudos see [Setup](#Setup)


## Setup
This library depends on the packages `web3` and `requests` as mandatory dependencies to work and some other dependencies to pimp the script output.

So to install dependencies yo need to execute this:

```
$ pip install -r requirements.txt
```

Also is required by the script the ABI of the kudos contract to know how to intereract and retrieve the list of kudos.
So if you don't have the ABI kudos contract, you can build it with the following commands:

```
# Get the kudos source code
$ git clone https://github.com/gitcoinco/Kudos721Contract.git
$ cd Kudos721Contract
# Install dependencies
$ npm install -g truffle ganache-cli
$ npm install
# Compile contracts to get the ABI
$ truffle compile
```

## RUN

Now we need set some env varibles to indicate to the script where its located the build contract, the endpoint to connect to some eth instance and limit the displayed kudos if its neccesary. Note that this env variables are required only by the script and not by the kudos module, where you pass this info as parameter.


```sh
$ export CONTRACT_JSON_PATH='Kudos721Contract/build/contracts/Kudos.json'
$ export NETWORK_URL='https://mainnet.infura.io/v3/...'
$ export LIMIT_KUDOS=15
```

Now it's time to get some kudos, only you need run the following command and you're done!

```sh
$ python scripts/list_kudos.py 
Processing |################################| 15/15
  id  name                       description              art url
----  -------------------------  -----------------------  ---------------------------------
  13  Ruby Gem                   Is there anyone who ...  https://s.gitcoin.co/static/v2...
  14  Angular Royalty            AngularJS is a great...  https://s.gitcoin.co/static/v2...
  12  Unix Philosophy            Owners of this badge...  https://s.gitcoin.co/static/v2...
   4  Gitcoin Genesis            The Gitcoin Genesis ...  https://s.gitcoin.co/static/v2...
   8  Do More Faster             Is there anything be...  https://s.gitcoin.co/static/v2...
  10  Elixer Mixer               Elixer Mixers are kn...  https://s.gitcoin.co/static/v2...
...
```


## License
**TBD***
