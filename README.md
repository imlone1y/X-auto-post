# X-auto-post

這是一個用於在 Twitter 上發佈隨機數字、YouTube 熱門影片標題或聯合新聞網新聞標題的 Python 腳本。

## 功能

- 生成隨機數字並發佈到 Twitter
- 抓取 YouTube 前 20 個發燒影片標題並發佈到 Twitter
- 抓取聯合新聞網前三個新聞標題並發佈到 Twitter

## 使用方法

1. 克隆這個倉庫到本地：

    ```bash
    git clone https://github.com/yourusername/twitter-bot.git
    cd twitter-bot
    ```

2. 安裝所需的 Python 套件：

    ```bash
    pip install requests_oauthlib
    pip install selenium
    ```

3. 設定 Twitter API 的 `consumer_key` 和 `consumer_secret`：

    ```python
    consumer_key = 'YourConsumerKey'
    consumer_secret = 'YourConsumerSecret'
    ```

4. 選擇要發佈的內容，取消相應的註釋：

    ```python
    # 生成隨機數字
    text = '幸運數字 - ' + str(random.randint(0,100))

    # 抓取 YouTube 前 20 個發燒影片標題
    # text = youtube_titles()

    # 抓取聯合新聞網前三個新聞標題 
    # text = news_titles()
    ```

5. 執行腳本：

    ```bash
    python twitter_bot.py
    ```

6. 在終端機中輸入從授權 URL 獲取的 PIN 碼。

## 注意事項

- 請確保您的 Twitter API 金鑰和密鑰是正確的。
- 在使用 Selenium 抓取認證碼時，請確保已安裝並正確配置了 WebDriver。

## 貢獻

歡迎提交問題（Issues）和合併請求（Pull Requests）來改進此專案。

## 授權

此專案採用 MIT 授權條款。詳情請參閱 [LICENSE](LICENSE) 文件。

