#!/usr/bin/python3
# encoding: utf-8
""" {{cookiecutter.project_slug}} 's entry_points"""
import fire
from traceback_with_variables import prints_exc


@prints_exc
def entry_point() -> None:  # pragma: no cover
    """
    默认函数 触发fire包
    https://github.com/google/python-fire
    """
    fire.core.Display = lambda lines, out: print(*lines, file=out)
    fire.Fire()


def ipython() -> None:  # pragma: no cover
    """打开ipython命令"""
    from IPython import embed

    embed()


def version() -> str:
    """显示当前版本"""
    import {{cookiecutter.project_slug}}

    return {{cookiecutter.project_slug}}.__version__


if __name__ == "__main__":
    entry_point()
