# Test Meson project

CythonとMesonの組み合わせをするためのテストプロジェクト

## インストール方法
### pip利用
```bash
python -m pip install git+https://github.com/munechika-koyo/test_meson
```

### editableモードでインストールしたい場合
```bash
python -m pip install -e git+https://github.com/munechika-koyo/test_meson
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