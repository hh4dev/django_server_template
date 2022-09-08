# README #


## レポジトリについて ##
ゲームAPIバックエンドの雛型です。

ゲームクライアントやブラウザにHTTP(S)通信で以下の機能を提供します。
#### - ユニット、アイテム等のユーザ資産の永続化 ####
#### - ゲームクライアントから隠蔽する必要のあるゲームロジックの実装 ####
#### - ゲーム内時間等サーバリソースの提供 ####
#### - 社内向け管理ツールの提供 ####

## 1. システム要件 ##
以下の何かがインストールされていること
#### - docker for windows ####
#### - docker for mac ####

何かしらのコマンドラインツールが利用可能なこと
#### - GitBash ####
#### - MINGW ####
#### - iTerm ####

## 2. インストール ##

### 2-1. clone ###
適当なディレクトリにソースコードをcloneする
```

```

### 2-2. Configuration ###

必要であれば .env のポート番号を修正する。


## 3. ローカルサーバ起動 ##

### 3-1. initialize ###

初回のみ以下のコマンドでdockerイメージの初期化を行う
```
docker-compose build
```

### 3-2. run ###
以下のコマンドでサーバを起動する
```
docker-compose up -d app mysql
```


### 3-3. shutdown ###
終了する場合は以下コマンド
```
docker-compose down
```

### 3-4. ログを見る ###
```
docker-compose logs -f
```
中断時はCtrl + C で抜けてください

### 3-5. テスト ###
unityやhttpクライアントのツールからリクエストを送信すると
ローカルのゲームサーバに疎通することができます（現状サーバ時間取得のみ）
```
url : http://localhost:{port番号}/web/api/gametime/get
method : GET
header : "Content-Type:application/json; charset=utf-8"
```
`{port番号}` は 2-2. で追加設定していればその番号を使う（デフォルト8000）

e.g.)
```
curl -X GET "http://localhost:8000/web/api/gametime/get" -H "Content-Type:application/json; charset=utf-8"
```
↓ 成功すればdatetimeのレスポンスが返る
```
{"now": "2021-01-18 13:17:54.613787"}
```
