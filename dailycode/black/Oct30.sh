#!/bin/bash
# 過去に接続したSSIDの一覧を表示
netsh wlan show profile

# 指定したSSIDの記憶しているパスワードを表示
# セキュリティの設定 > 主要なコンテンツ に表示されているのがパスワード
netsh wlan show profile key=clear [パスワードを確認したいSSID]
