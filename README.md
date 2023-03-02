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
--header 'x-api-key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX' \
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

## Genera HTML OTP

https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/generaHTMLOTP

- Curl

```shell
curl --location --request GET 'https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/generaHTMLOTP' \
--header 'x-api-key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```

- Dependency

```shell
No dependencies
```

- UnitTest

```shell
command test
```

- Sequence Diagram

![x][def2]

[def2]: /img/genera_html_otp.jpg

## TOTP Validation

https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/totp

- Curl POST

```shell
curl --location --request POST 'https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/totp' \
--header 'x-api-key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX' \
--header 'Content-Type: application/json' \
--data-raw '{
    "secret": "NOXCFJKYLFL33KHTMW32MRTV72QHLL66",
    "token_id": "dfgDRGWER34"
}'
```

- Curl GET

```shell
curl --location --request GET 'https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/totp?code=457280&token_id=dfgDRGWER34' \
--header 'x-api-key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```

- Dependency

```shell
No dependencies
```

- UnitTest

```shell
command test
```

- Sequence Diagram POST

![x][def3]

[def3]: /img/totp_validation_post.jpg

- Sequence Diagram GET

![x][def4]

[def4]: /img/totp_validation_get.jpg

## Tokenized Cards

https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/tokenized-cards

- Curl POST

```shell
curl --location --request POST 'https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/tokenized-cards' \
--header 'Accept: application/json' \
--header 'X-Amz-Date: Mon, 20 Feb 2023 20:38:34 GMT' \
--header 'x-api-key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
--data-raw '{
    "customerPG": "918273645",
    "tokenizedCardId": "dfgDRGWER34",
    "email": "sixto.maxil@millicom.com",
    "customerName": "Sixto Maxil"
}'
```

- Curl GET

```shell
curl --location --request GET 'https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/localization?phoneNumber=50379238154&countryCode=503' \
--header 'Accept: application/json' \
--header 'X-Amz-Date: Mon, 20 Feb 2023 20:38:34 GMT' \
--header 'x-api-key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```

- Dependency

```shell
No dependencies
```

- UnitTest

```shell
command test
```

- Sequence Diagram POST

![x][def5]

[def5]: /img/tokenized_cards_post.jpg

- Sequence Diagram GET

![x][def6]

[def6]: /img/tokenized_cards_get.jpg

## Localization

https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/localization

- Curl

```shell
curl --location --request GET 'https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/localization?phoneNumber=50379238154&countryCode=503' \
--header 'Accept: application/json' \
--header 'X-Amz-Date: Mon, 20 Feb 2023 20:38:34 GMT' \
--header 'x-api-key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```

- Dependency

```shell
No dependencies
```

- UnitTest

```shell
command test
```

- Sequence Diagram

![x][def7]

[def7]: /img/localization.jpg

## Phone Validation

https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/phone-validation

- Curl

```shell
curl --location --request POST 'https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/phone-validation' \
--header 'x-api-key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX' \
--header 'Content-Type: application/json' \
--data-raw '{
  "phoneNumber": "090000000",
  "countryCode": "PY"
}'
```

- Dependency

```shell
No dependencies
```

- UnitTest

```shell
command test
```

- Sequence Diagram

![x][def8]

[def8]: /img/phone_validation.jpg

## Presigned S3 URL Wallet

https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/presinged-url

- Curl

```shell
curl --location --request POST 'https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/phone-validation' \
--header 'x-api-key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX' \
--header 'Content-Type: application/json' \
--data-raw '{
  "phoneNumber": "090000000",
  "countryCode": "PY"
}'
```

- Dependency

```shell
wallet_s3_bucket
```

- Hardcode Resource

```shell
wallet_s3_bucket:"dev.assets.rwallet.pa.tigomoney.io"
```

- UnitTest

```shell
command test
```

- Sequence Diagram

![x][def9]

[def9]: /img/presigned_s3_url_wallet.jpg

## Push Notification

https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/push-notification

- Curl

```shell
curl --location --request POST 'https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/push-notification' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'x-api-key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX' \
--data '{
    "token": "fZ-rRQ-kRKGUtVEihc7Xur:APA91bGNUELOrvyBvL144c8rAJhxRXFyOcS5hoTraw5lNUe3Jyr5J4qOJfU1nRB3alkkuRiPr7nfBPo-JzfCJhqNb-axeJAoHry-3_ZM8DERVVHubtK06cxI0iBKdj4Vcq47-dS4uyzd",
    "title": "Title test",
    "message": "Body Test",
    "countryCode": "PA",
    "os": "android",
    "image": "https://d2y71a4idrecl2.cloudfront.net/tigo-.jpg"
}'
```

- Dependency

```shell
pinpoint
```

- Hardcode Resource

```shell
appId: "8cbcf756d46247aeaa1a14878462a193",
appBOId: "7dbaec4ce71049ffadec9f8e0f9f3ebf",
appPYId:  "510d54476d6447c69adc51a3c762dafd"
```

- UnitTest

```shell
command test
```

- Sequence Diagram

![x][def10]

[def10]: /img/push_notification.jpg

## Validate OTP

https://dev.rwallet.pa.tigomoney.io/utilities/v1-0-0-0/utils/otp

- Curl

```shell
falta curl
```

- Dependency

```shell
No dependencies
```

- UnitTest

```shell
command test
```

- Sequence Diagram

![x][def11]

[def11]: /img/validate_otp.jpg
