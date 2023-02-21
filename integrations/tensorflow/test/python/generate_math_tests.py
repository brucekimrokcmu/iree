# Copyright 2021 The IREE Authors
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

# Generates runner variants for the tf math tests.

import generate_runner

TF_MATH_FUNCTIONS = [
    "abs",
    "accumulate_n",
    "acos",
    "acosh",
    "add",
    "add_n",
    "angle",
    "argmax",
    "argmin",
    "asin",
    "asinh",
    "atan",
    "atan2",
    "atanh",
    "bessel_i0",
    "bessel_i0e",
    "bessel_i1",
    "bessel_i1e",
    "betainc",
    "bincount",
    "ceil",
    "confusion_matrix",
    "cos",
    "cosh",
    "count_nonzero",
    "cumprod",
    "cumsum",
    "cumulative_logsumexp",
    "digamma",
    "divide",
    "divide_no_nan",
    "equal",
    "erf",
    "erfc",
    "erfinv",
    "exp",
    "expm1",
    "floor",
    "floordiv",
    "floormod",
    "greater",
    "greater_equal",
    "igamma",
    "igammac",
    "imag",
    "in_top_k",
    "invert_permutation",
    "is_finite",
    "is_inf",
    "is_nan",
    "is_non_decreasing",
    "is_strictly_increasing",
    "lbeta",
    "less",
    "less_equal",
    "lgamma",
    "log",
    "log1p",
    "log_sigmoid",
    "log_softmax",
    "logical_and",
    "logical_not",
    "logical_or",
    "logical_xor",
    "maximum",
    "minimum",
    "mod",
    "multiply",
    "multiply_no_nan",
    "ndtri",
    "negative",
    "nextafter",
    "not_equal",
    "polygamma",
    "polyval",
    "pow",
    "real",
    "reciprocal",
    "reciprocal_no_nan",
    "reduce_all",
    "reduce_any",
    "reduce_euclidean_norm",
    "reduce_logsumexp",
    "reduce_max",
    "reduce_mean",
    "reduce_min",
    "reduce_prod",
    "reduce_std",
    "reduce_sum",
    "reduce_variance",
    "rint",
    "round",
    "rsqrt",
    "scalar_mul",
    "segment_max",
    "segment_mean",
    "segment_min",
    "segment_prod",
    "segment_sum",
    "sigmoid",
    "sign",
    "sin",
    "sinh",
    "sobol_sample",
    "softmax",
    "softplus",
    "softsign",
    "sqrt",
    "square",
    "squared_difference",
    "subtract",
    "tan",
    "tanh",
    "top_k",
    "truediv",
    "unsorted_segment_max",
    "unsorted_segment_mean",
    "unsorted_segment_min",
    "unsorted_segment_prod",
    "unsorted_segment_sqrt_n",
    "unsorted_segment_sum",
    "xdivy",
    "xlog1py",
    "xlogy",
    "zero_fraction",
    "zeta",
]

# This list was generated by running:
#   bazel run integrations/tensorflow/e2e/math:math_test_manual -- --list_functions_with_complex_tests
# keep sorted
COMPLEX_FUNCTIONS = [
    "abs",
    "add",
    "angle",
    "asinh",
    "atanh",
    "conj",
    "cos",
    "cosh",
    "count_nonzero",
    "cumprod",
    "cumsum",
    "divide",
    "divide_no_nan",
    "exp",
    "expm1",
    "imag",
    "l2_normalize",
    "log",
    "log1p",
    "multiply",
    "multiply_no_nan",
    "negative",
    "pow",
    "real",
    "reciprocal",
    "reciprocal_no_nan",
    "reduce_euclidean_norm",
    "reduce_std",
    "reduce_variance",
    "rsqrt",
    "sigmoid",
    "sign",
    "sin",
    "sinh",
    "sqrt",
    "square",
    "squared_difference",
    "subtract",
    "tan",
    "tanh",
    "truediv",
    "xdivy",
    "xlog1py",
    "xlogy",
    "zero_fraction",
]

BACKENDS = [
    ("llvmcpu", "--target_backends=iree_llvmcpu"),
    ("vulkan", "--target_backends=iree_vulkan"),
]

# Non dynamic dim tests.
for variant, flags in BACKENDS:
  for math_fn in TF_MATH_FUNCTIONS:
    generate_runner.main([
        variant,
        f"{flags} --dynamic_dims=false --functions={math_fn} --artifacts_dir=%t",
        f"iree_tf_tests/math/math_test.py:{math_fn}"
    ])
  for math_fn in COMPLEX_FUNCTIONS:
    generate_runner.main([
        variant,
        f"{flags} --dynamic_dims=false --functions={math_fn} --artifacts_dir=%t",
        f"iree_tf_tests/math/math_test.py:complex_{math_fn}"
    ])

# Dynamic dim tests.
for variant, flags in BACKENDS:
  for math_fn in TF_MATH_FUNCTIONS:
    generate_runner.main([
        variant,
        f"{flags} --dynamic_dims=true --functions={math_fn} --artifacts_dir=%t",
        f"iree_tf_tests/math/math_test.py:dynamic_dim_{math_fn}"
    ])
  for math_fn in COMPLEX_FUNCTIONS:
    generate_runner.main([
        variant,
        f"{flags} --dynamic_dims=true --functions={math_fn} --artifacts_dir=%t",
        f"iree_tf_tests/math/math_test.py:complex_dynamic_dim_{math_fn}"
    ])