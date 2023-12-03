pyx_files = [
  ['module', 'module.pyx'],
]

foreach pyx_file : pyx_files
  py.extension_module(
    pyx_file[0],
    pyx_file[1],
    c_args: [numpy_nodepr_api],
    dependencies: [py_dep, np_dep],
    install: true,
    install_dir: py.get_install_dir() / 'test_meson/lib2',
  )
endforeach

python_sources = [
    '__init__.py',
]

py.install_sources(
  python_sources,
  subdir: 'test_meson/lib2',
)
