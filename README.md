# Kudos Python

## Setup

Install dependencies:

```
$ pip install -r requirements.txt
```

## RUN

```sh
$ export CONTRACT_JSON_PATH='Kudos721Contract/build/contracts/Kudos.json'
$ export NETWORK_URL='https://mainnet.infura.io/v3/...'
$  export LIMIT_KUDOS=15
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
