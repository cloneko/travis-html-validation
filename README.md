Auto HTML Validation for Travis-CI
------------------------------------------

現在いるディレクトリ以下の階層の \.html? ファイルをW3CのValidationサービスに投げてError/Warningが無いかチェックするもにょもにょ。

for Travis-CIとか言うてるけど別にTravis-CI関係なく使える罠
(もともとはTravis-CIで使うために作っただけです。。。)

Require
=========================================

* Python2.x
* pip

Setup
=========================================

    pip install nose
    pip install https://bitbucket.org/nmb10/py_w3c/downloads/py_w3c-v0.1.1.tar.gz

Usage
=========================================

    nosetest

License
=========================================

Public Domain
