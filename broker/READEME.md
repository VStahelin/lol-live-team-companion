## Setup

### Start the broker end enter the container
```shell
docker compose up -d
docker exec -it mqtt5 bash
```

### Setup broker
```shell
mosquitto_passwd -c /mosquitto/config/pwfile user1
```



# Test

## Subscribe
```shell
mosquitto_sub -v -t 'hello/topic' -u user1 -P 123456789
```

## Publish
```shell
mosquitto_pub -t 'hello/topic' -m 'hello world' -u user1 -P 123456789
```


# Reference
- [mosquitto](https://mosquitto.org/)
- [mosquitto-github](https://github.com/eclipse/mosquitto)