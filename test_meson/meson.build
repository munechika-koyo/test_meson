# local modules for .pyx file
pyx_files = [
  ['cmain', 'cmain.pyx'],
]

foreach pyx_file : pyx_files
  py.extension_module(
    pyx_file[0],
    pyx_file[1],
    c_args: [numpy_nodepr_api],
    dependencies: [py_dep, np_dep],
    install: true,
    install_dir: py.get_install_dir() / 'test_meson',
  )
endforeach

python_sources = [
    '__init__.py',
    'main.py',
]

py.install_sources(
  python_sources,
  subdir: 'test_meson',
)

# move to subdirectories
subdir('lib1')
subdir('lib2')