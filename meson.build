project(
  'test-meson',
  'cython',
  version: '0.1',
  meson_version: '>= 0.63.0',
  default_options: [
    'cython_args=-3',
    'c_args=-fopenmp',
    'c_link_args=-fopenmp',
  ]
)

py = import('python').find_installation(pure: false)
dep_py = py.dependency()

# NumPy include directory - needed in all submodules
incdir_numpy = run_command(
  py,
  [
    '-c',
    'import numpy; print(numpy.get_include())'
  ],
  check: true
).stdout().strip()

# numpy api
inc_np = include_directories(incdir_numpy)
numpy_nodepr_api = '-DNPY_NO_DEPRECATED_API=NPY_1_9_API_VERSION'

subdir('test_meson')
