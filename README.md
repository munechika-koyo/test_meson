# Test Meson project

CythonとMesonの組み合わせをするためのテストプロジェクト
詳細はこちらの記事を参照してください。
https://qiita.com/munechika-koyo/items/362f156b414e05dda6cd

## インストール方法
### pip利用
```bash
python -m pip install git+https://github.com/munechika-koyo/test_meson
```

### editableモードでインストールしたい場合
```bash
python -m pip install --no-build-isolation --editable git+https://github.com/munechika-koyo/test_meson
```

### 開発者向けインストール (conda利用)
```bash
git clone https://github.com/munechika-koyo/test_meson
cd test_meson
conda env create -f environment.yml
conda activate test_meson
python dev.py build
python dev.py install
```
