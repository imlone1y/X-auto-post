# X-auto-post

[繁體中文](README_TW.md) | English

This project uses the automation tool Selenium to achieve functions such as automatic title fetching and captcha solving, enabling automatic posting on X.

## Running Guide

This project is based on the Python programming language and uses external libraries selenium and requests_oauthlib.

### Download External Libraries

```bash
cd [project_folder_path]
pip install -r requirements.txt
```

### Running Tests

- Apply for the consumer_key and consumer_secret of the relevant X account at [X Developers](https://developer.x.com/en) in [X API](https://developer.x.com/en/docs/authentication/oauth-1-0a/api-key-and-secret), and modify them in `post.py`.

- In `selenium_test.py`, change `YOUR-X-ACCOUNT` and `YOUR-X-PASSWORD` to the relevant X account and password for login when fetching the captcha.

After making the changes, run `post.py` to post.

### Change Post Content

This project can achieve 3 types of post content. When using any type of post content, the other 2 types must be commented out, otherwise the post will fail. The post contents include:

#### Lucky Number
In `post.py` lines 15 - 16.

```python
text = '幸運數字 - ' + str(random.randint(0,100))
```

#### Top 3 YouTube Trending Video Titles
In `post.py` lines 18 - 19.

*Note: When the title is too long, it may exceed X's post length limit. Please change the number of titles fetched in line 15 of `youtube_title.py`.*

```python
text = youtube_titles()
```

#### Top 3 News Titles from United Daily News
In `post.py` lines 21 - 22.

*Note: When the title is too long, it may exceed X's post length limit. Please change the number of titles fetched in line 15 of `news_title.py`.*

```python
text = news_titles()
```

### Change Captcha Fetching Method

When logging into the same account too many times, there may be a situation where login fails or secondary login is required, causing the crawler to fail to correctly fetch the captcha.

Comment out the automatic captcha fetching method in `post.py` lines 50 - 51, and uncomment lines 46 - 47 to switch back to manual captcha input.

```python
# 手動輸入
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# 自動，利用selenium抓取認證碼
# from selenium_test import get_PIN
# verifier = get_PIN(authorization_url)
```

After the account returns to normal, switch back to the automatic captcha input method.