# 派遣求人公募システム

## ①課題内容
- 建設現場の求人を派遣会社に公募できるシステム

## ②工夫した点・こだわった点
- マップ機能
bingmapAPIで求人をマップにピン刺しした。

## ③難しかった点・次回トライしたいこと(又は機能)
- テーブル設計の大事さを知った。あまり考えずに進めていった結果、後になって最初からやり直さないといけなくなったりして大変だった。
- djangoのフォームがis_valid()=Falseになるときに、なぜそのエラーが出るのかの解明が厄介だった。

## ④質問・疑問・感想、シェアしたいtips等なんでも
- ホットリロードでコードがリアルタイムに反映できるようになった。
実行時はターミナルを二つ立ち上げて、一つはpython manage.py livereload、もう一つはpython manage.py runserver
https://github.com/tjwalch/django-livereload-server
- ログインのデザイン（codepen）
https://codepen.io/colorlib/pen/rxddKy
- bingmapで住所からピン刺し
https://qiita.com/daisu_yamazaki/items/7281736f0a77cf8ab664
- ログインしていない状態だとページを見れなくする方法
https://noauto-nolife.com/post/django-login-required-mixin/
- コードでアイコンを表示できる
https://fonts.google.com/icons
- それっぽいサイドバー
https://johobase.com/bulma-create-web-page/#i-4
- widget_tweaks
https://hodalog.com/how-to-use-bootstrap-4-forms-with-django/
