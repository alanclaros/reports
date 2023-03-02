# APIs Wallet Utilities for Tigo Money

## _Wallet Utilities made with Python_

![x][def]

[def]: /img/icon_utilities.png

Wallet Utilities: Is a service for send Push and OTP notifications.

Sending wallet push and OTP notifications to Tigo Money devices with Tigo App.

## Features

- Send Push Notifications.
- Send OTP Notifications.

## How it works ?

> Tigo's company sends notifications of the operations and transactions carried out with the mobile wallet app, to mobile devices.

## Tech

Wallet Utilities uses this items to work properly:

- [Python] - version>=3.10, <=3.9.9
- [AWS-Lambda] - Amazon Web Service, lambda functions

## Create an virtual environment

```shell
python -m venv venv
```

## Activate virtual environment

```shell
- macOx: source ./venv/bin/activate
- windows: ./venv/Scripts/activate.bat
- linux: source ./venv/bin/activate
```

## Upgrade pip

```shell
python -m pip install --upgrade pip
```

## Install dependencies

```shell
pip install -r requirements.txt
```

## APM Project Install

```shell
apm project install
```

## Create a new lambda.

```shell
apm lambda new
```

## Create a new lambda with apigateway integration.

```shell
apm endpoint new
```

## AWS SSO Login

```shell
aws sso login
```

## Run API

```shell
apm api run
```

# Amazon Api Gateway

<b>dev-wallet-utilities</b>

Panama dev enviroment:

https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/

## _EndPoints_

## Email

https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/email

- Curl

```shell
curl --location 'https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/email' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'x-api-key: 8VbDe8Xx7V77teF4vXOd53Ax0v81awk4DjTp2WCc' \
--data-raw '{
    "subject": "Subject Email Test",
    "message": "This is an Email Test message",
    "email": "mail@millicom.com"
}'
```

- Dependency

```shell
arn:aws:lambda:us-east-1:177933569100:layer:AWS-Parameters-and-Secrets-Lambda-Extension:4
```

- UnitTest

```shell
command test
```

- Sequence Diagram

![x][def1]

[def1]: /img/email.jpg
