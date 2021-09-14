# Cookiecutter Py Package

## 个人用的Cookiecutter

* 抄的[Cookiecutter PyPackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)和[cookiecutter-python-package](https://github.com/tylerdave/cookiecutter-python-package)
* 用于生成python项目
* 基于pytest
* 带了versioneer

---

## 使用方式

```bash
pip install cookiecutter 
cookiecutter https://github.com/AngusWG/cookiecutter-py-package.git
```

### 参数说明

* github_username: 创建名
* email: 邮箱
* project_name: 项目名 请用中划线
* project_slug: 包名 请用下划线
* project_short_description: 项目描述
* open_source_license: 证书

---

* 设置`git commit`时执行`make check`

cmd 上运行下面脚本 设置pre-commit
```bash
python -c "from urllib.request import urlopen ;exec(urlopen('https://github.com/AngusWG/cookiecutter-py-package/raw/master/git_pre_commit_hook.py').read())"
```