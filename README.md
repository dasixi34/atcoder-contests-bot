# atcoder-contests-bot
## 概要
- [AtCoder](https://atcoder.jp/) Beginner Contestの開催予定をDiscordに通知するプログラムです
- GitHub Actionsでの実行ではコンテスト開催日の15:00 (JST) に通知が届きます

## GitHub Actionsでの実行方法
1. [Discordの公式ドキュメント](https://discord.com/developers/docs/getting-started)にしたがって対象のサーバにDiscord Botをインストール
    - SCOPES: bot
    - BOT PERMISSIONS: Send Messages
1. [GitHubの公式ドキュメント](https://docs.github.com/ja/actions/security-guides/encrypted-secrets)にしたがってリポジトリに以下のシークレットを作成
    - DISCORD_BOT_TOKEN: インストールしたDiscord Botのトークン
    - DISCORD_CHANNEL_ID: 通知が届いてほしいDiscordチャンネルのID

## ローカル環境での実行手順
1. `.python-version` に書かれているバージョンのPythonをインストール
1. `python -m venv venv` を実行
1. `source venv/bin/activate` を実行
1. `pip install -r requirements.txt` を実行
1. [Discordの公式ドキュメント](https://discord.com/developers/docs/getting-started)にしたがって対象のサーバにDiscord Botをインストール
1. `.env.template` を `.env` という名前でコピーして環境変数を設定
1. `python src/main.py` を実行
