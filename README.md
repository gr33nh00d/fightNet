# Fight Net

By Gr33nH00d & [ИЧХ](https://www.linkedin.com/in/ethan-charles-holmes-225158189)

## About
We created a back-propagation, multi-layer perceptron network into which we input fighter physical stats and data from fighters' last 10 rounds of fights. Given the names of two fighters, the network outputs a prediction as to which fighter is most likely to win in a matchup. The purpose of this network is to provide data-driven insights for betting.


## Current Issues
Running the dataFormer.py will (unintentionally) DOS the ufc page to the point of being locked out (Error 429).

## Notes
Training Data format

{"fightID":1, "fightDate":dateTime, "fighterA":{Last 15 rounds}, "fighterB"" {Last 15 rounds}, "result":"0 or 1"}

{"fightID":1, "fightDate":dateTime, "fighterA":{Last 15 rounds}, "fighterB"" {Last 15 rounds}, "result":"0"}
{"fightID":1, "fightDate":dateTime, "fighterB"" {Last 15 rounds}, "fighterA":{Last 15 rounds}, "result":"1"}


assuming ufc.csv is in mongo and we can querry on it

Get list of fightIDs
for each ID
  get the last 15 rounds from each fighter prior to current fight id
  store fight result from this fight id as 0 or 1
  copy this datum and flip fighter A and B and the result


docker run --name some-mongo -d -v .:/var/lib/mongodb mongo:tag

docker run --name some-mongop -d -v /home/gribble/work/fightNew/mongo:/data mongo:latest
mongoimport --type csv -d test -c products --headerline --drop ufc.csv
