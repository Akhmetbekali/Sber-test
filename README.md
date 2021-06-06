# SBER test

MVP of chat bot for restaurant booking by:
- time
- number of people

## Installation
```shell script
docker build -t bot .
```

## Usage
```shell script
docker run --name bot bot
```
Got to [@sber_test_ali_bot](https://t.me/sber_test_ali_bot) and enter `/start` to start a bot

## Test cases

```shell script
docker exec -it bot pytest 
```