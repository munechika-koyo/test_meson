"""
Developper CLI: building (meson) sources in place, document, etc.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

import rich_click as click

if sys.version_info < (3, 11):
    import tomllib as tomlib
else:
    import tomli as tomlib

BASE_DIR = Path(__file__).parent.resolve()
BUILD_DIR = BASE_DIR / "build"
SRC_PATH = BASE_DIR / "test_meson"
DOC_SRC = BASE_DIR / "docs"
ENVS = dict(os.environ)
N_CPUs = os.cpu_count()


@click.group()
def cli():
    """Developper CLI: building (meson) sources in place, document, etc."""
    pass


@cli.command()
@click.option("--build-dir", default=str(BUILD_DIR), help="Relative path to the build directory")
@click.option(
    "-j",
    "--parallel",
    default=N_CPUs,
    show_default=True,
    help="Number of parallel jobs for building.",
)
def build(build_dir, parallel):
    """Build & Install package using Meson build tool.

    \b
    ```python
    Examples:
    $ python dev.py build
    ```
    """
    # === setup build ===============================================
    cmd = ["meson", "setup", build_dir]
    if Path(build_dir).exists():
        cmd += ["--wipe"]
    click.echo(" ".join([str(p) for p in cmd]))
    ret = subprocess.call(cmd, env=ENVS, cwd=BASE_DIR)
    if ret == 0:
        print("Meson build setup OK")
    else:
        print("Meson build setup failed!")
        sys.exit(1)

    # === build project =============================================
    cmd = ["meson", "compile", "-C", build_dir, "-j", str(parallel)]
    click.echo(" ".join([str(p) for p in cmd]))
    ret = subprocess.call(cmd)

    if ret == 0:
        print("Build OK")
    else:
        print("Build failed!")
        sys.exit(1)

    # === install .so/.pyd files in source tree ==========================
    ext = ".pyd" if sys.platform == "win32" else ".so"
    for so_path in BUILD_DIR.glob(f"**/*{ext}"):
        src = so_path.resolve()
        dst = BASE_DIR / so_path.relative_to(BUILD_DIR)
        shutil.copy(src, dst)
        print(f"copy {src} into {dst}")
    print("Install .so files in place.")


@cli.command()
def install():
    """Install package as the editalbe mode.

    This command enables us to install the packages
    as an editable mode with the setuptools functionality.

    \b
    ```python
    Examples:
    $ python dev.py install
    ```
    """
    # install the package
    cmd = [sys.executable, "setup.py", "develop"]
    click.echo(" ".join([str(p) for p in cmd]))
    ret = subprocess.call(cmd)

    if ret == 0:
        print("Successfully installed.")
    else:
        print("install failed!")
        sys.exit(1)


@cli.command()
def clear():
    """Clear all git ignoring files."""
    cmd_base = ["rm", "-rf"]
    for label in ["__pycache__", "build", "*.so", "*.c"]:
        remove_path = [str(path) for path in BASE_DIR.glob(f"**/{label}")]
        cmd = cmd_base + remove_path
        subprocess.run(cmd)
        print(f"{label} were removed")


############


@cli.command()
@click.argument("targets", default="html")
@click.option(
    "-j",
    "--parallel",
    default=N_CPUs,
    show_default=True,
    help="Number of parallel jobs for building.",
)
def doc(parallel: int, targets: str):
    """:wrench: Build documentation
    TARGETS: Sphinx build targets [default: 'html']
    """
    # move to docs/ and run command
    os.chdir("docs")

    builddir = DOC_SRC / "build"
    SPHINXBUILD = "sphinx-build"
    if targets == "html":
        cmd = [SPHINXBUILD, "-b", targets, f"-j{parallel}", str(DOC_SRC), str(builddir / "html")]

    elif targets == "clean":
        cmd = ["rm", "-rf", str(builddir), "&&", "rm", "-rf", str(DOC_SRC / "_api")]

    elif targets == "help":
        cmd = [SPHINXBUILD, "-M", targets, str(DOC_SRC), str(builddir)]

    else:
        cmd = [SPHINXBUILD, "-M", targets, f"-j{parallel}", str(DOC_SRC), str(builddir)]

    click.echo(" ".join([str(p) for p in cmd]))
    ret = subprocess.call(cmd)

    if ret == 0:
        print("sphinx-build successfully done.")
    else:
        print("Sphinx-build has errors.")
        sys.exit(1)


############


@cli.command()
def format():
    """:art: Run black & isort formatting
    The default options are defined in pyproject.toml
    """
    cmd = ["black", str(SRC_PATH)]
    click.echo(" ".join([str(p) for p in cmd]))
    ret = subprocess.call(cmd)

    if ret == 0:
        print("black formated")
    else:
        print("black formatting errors!")
        sys.exit(1)

    cmd = ["isort", str(SRC_PATH)]
    click.echo(" ".join([str(p) for p in cmd]))
    ret = subprocess.call(cmd)

    if ret == 0:
        print("isort formated")
    else:
        print("isort formatting errors!")
        sys.exit(1)


@cli.command()
def cython_lint():
    """:art: Cython linter. Checking all .pyx files in the source directory.
    The default options are defined at the cython-lint table in pyproject.toml
    """
    # line length option
    max_line_length = config("cython-lint")["max-line-length"]

    # list of .pyx files
    pyx_files = [str(pyx_path) for pyx_path in SRC_PATH.glob("**/*.pyx")]

    cmd = ["cython-lint", "--max-line-length", str(max_line_length)] + pyx_files
    ret = subprocess.call(cmd)

    if ret == 0:
        print("cython-lint OK")
    else:
        print("cython-lint errors")
        sys.exit(1)


#######
def config(tool: str):
    """Load configure data from pyproject.toml for tool table."""
    pyproject = BASE_DIR / "pyproject.toml"
    if not pyproject.exists():
        raise FileNotFoundError("pyproject.toml must be placed at the root directory.")

    with open(pyproject, "rb") as file:
        conf = tomlib.load(file)

    if not conf["tool"].get(tool):
        raise ValueError(f"{tool} config data does not exist.")

    return conf["tool"].get(tool)


if __name__ == "__main__":
    cli()
