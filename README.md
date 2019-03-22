# Bitly url shorterer

This project made for automatic shortering urls to bitly-links. Also you can check short link and show count of clicks.

### How to install

1. You should generate bit.ly-token. [Manual](https://dev.bitly.com/get_started.html).
2. Create file `.env` and copy token like below:

    ```
    TOKEN=YOUR_TOKEN
    ```

3. Python3 should be already installed. Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

    ```
    pip install -r requirements.txt
    ```


### How to usage

Run `python main.py [-h] link` in your terminal.

* Positional arguments:
    - `link` - link or bitly-link.

* Optional arguments:
    - `-h`, `--help` - show help message and exit.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).