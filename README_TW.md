# X-auto-post

繁體中文 | [English](README.md)

本項目利用自動化工具 Selenium 實現標題、驗證碼自動抓取等功能，實現自動於 X 發文。

## 運行指南

本項目基於 Python 程式語言，使用到外部程式庫 selenium、requests_oauthlib。

### 外部程式庫下載

```bash
cd [項目資料夾路徑]
pip install -r requirements.txt
```

### 運行測試

- 於 [X Developers](https://developer.x.com/en) 裡的 [X API](https://developer.x.com/en/docs/authentication/oauth-1-0a/api-key-and-secret) 申請相關 X 帳號的 consumer_key 與 consumer_secret ，並更改於 `post.py`。

- 於 `selenium_test.py` 將 `YOUR-X-ACCOUNT` 及 `YOUR-X-PASSWORD` 改為相關 X 的帳號與密碼，用於抓取驗證碼時登入做使用。

更改完畢後，運行 `post.py` 即可發文。

### 更改發文內容

本項目可實現 3 種發文內容，使用任意項發文內容時，須將其餘 2 中發文內容註解，否則將導致推文無法發出。發文內容包括 :

#### 幸運數字
於 `post.py` 15 - 16 行。

```python
text = '幸運數字 - ' + str(random.randint(0,100))
```

#### YouTube 前 3 個發燒影片標題
於 `post.py` 18 - 19 行。

*特別注意 : 當標題過長時，可能會超出 X 發文長度限制，請至 `youtube_title.py` 裡第 15 行更改抓取標題數量。*

```python
text = youtube_titles()
```

#### 聯合新聞網前 3 個新聞標題 
於 `post.py` 21 - 22 行。

*特別注意 : 當標題過長時，可能會超出 X 發文長度限制，請至 `news_title.py` 裡第 15 行更改抓取標題數量。*

```python
text = news_titles()
```

### 更改驗證碼獲取方式

當重複登入同一個帳號太多次，可能會出現無法登入或需要二次登入的情況出現，這時爬蟲程式會無法正確抓取驗證碼。

須於 `post.py` 第 50 - 51 行自動抓取驗證碼方法註解，並將第 46 - 47 行反註解，改回手動輸入驗證碼。

```python
# 手動輸入
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# 自動，利用selenium抓取認證碼
# from selenium_test import get_PIN
# verifier = get_PIN(authorization_url)
```

待帳號回復正常後，改回自動輸入驗證碼方式即可。


