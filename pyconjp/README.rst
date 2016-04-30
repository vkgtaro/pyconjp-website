=====================
PyCon JP サイト！
=====================

ローカル開発
----------------------

* virtualenvを作成::

    $ virtualenv env/pycon
    $ . env/pycon/bin/activate

* 依存性をインストール::

    $ pip install -r requirements/dev.txt --trusted-host dist.pinaxproject.com

* データベースの初期化:

    $ ./pyconjp/init_db.sh

* 管理者アカウントを作成::

    $ ./manage.py createsuperuser

* ローカルサーバーを起動:

    python manage.py runserver


Vagrantの開発環境作り
---------------------------

（初めての方）
VagrandをDL&インストール http://lab.raqda.com/vagrant/
VirtualBoxをDL&インストール https://www.virtualbox.org/

インストール後、Vagrantfileファイルのディレクトリにてターミナルより
vagrant up

Web開発作業手順
--------------------

* 課題・機能・案件ごとにJIRAにてチケットを作成、チケットごとにトピックブランチを切る(ブランチの名前はTicketID
* git-flowに乗せる。機能開発はfeatureブランチにて
* 作業完了、要レビューの際はpull request、コミッターは小松さん
