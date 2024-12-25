# id3Modifier


## 目的

ディレクトリに配置した音楽ファイルにtag情報を設定します。
`/hoge/music/MyAlbum`というパスに下記のような配置でファイルがあるとします

* Myalbum
  * track01.wav
  * track02.wav
  * track03.wav
  * artwork.png

これに対して実行すると各wavファイルに対してアルバム名、トラック名、トラック番号、アートワークが設定されます。

## 動作

* アルバム名は指定したディレクトリの名前になります
* アルバムアートは指定したディレクトリ内の名前順にソートしたときに最初にくる画像ファイルになります
  * 画像ファイルがない場合は設定されません
* track番号は名前でソートされた順になります
* track名はファイル名から拡張子を削除したものになります。
* 細かい編集をしたい場合は `prepare.sh` を実行した時にできる tag_settings.yaml を編集してから `execute.sh` を実行してください

## セットアップ

python製です。
開発時のversionは3.12です。

好きにセットアップしましょう。
必要なライブラリは `requirements.txt` にあります。

## 操作方法

```shell
work_path=/パスを/指定する
sh ./prepare.sh ${work_path}
sh ./execute.sh ${work_path}
```
設定ファイルを編集する場合は一つずつ実行してください。

