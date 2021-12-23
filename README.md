# raspi_radio_control

Raspberry Piで駆動するラジコンをブラウザで制御するプログラム

## 仕様

Raspberry PiのGPIOを制御することで両輪のモータを正転・逆転する仕組みになっている．

モータドライバを用いているため，動作環境によっては流用できない可能性あり．

## 遠隔制御

Apache2を使用することで，Webブラウザを外部公開することができる．

設定ファイルは[etc/apache2/sites-available](./etc/apache2/sites-available)の中にあり，このファイルを編集することでport 80/443に公開することができる．

