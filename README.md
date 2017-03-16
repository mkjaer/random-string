# Random string

Ever needed a random string for a password or something easily from your shell? Me too.

## Build

`docker build --tag=random-string .`

## Usage

Run `docker run -p 8080:8080 random-string` after building the container and visit `http://<ip>:8080/40` to get a 40 character random string. 40 can be replaced with any number.

