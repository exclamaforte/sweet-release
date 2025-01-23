# bc breaking
# deprecations
 - Deprecate torch._utils.is_compiling() ([#127690](https://github.com/pytorch/pytorch/pull/127690))
# new features
 - Add compiled_autograd_kwargs_override Dynamo config ([#136967](https://github.com/pytorch/pytorch/pull/136967))
# improvements
# bug fixes
 - dynamo: guard on FSDP module parameters ([#138819](https://github.com/pytorch/pytorch/pull/138819))
# performance
 - Support for accelerated sorting with x86-simd-sort ([#127936](https://github.com/pytorch/pytorch/pull/127936))
 - Enable extended MMA shapes in CUTLASS. ([#133686](https://github.com/pytorch/pytorch/pull/133686))
 - Port ExecuTorch bfdot improvement back to ATen BlasKernel ([#136331](https://github.com/pytorch/pytorch/pull/136331)) ([#137377](https://github.com/pytorch/pytorch/pull/137377))
 - Build ReducedPrecisionFloatGemvFastPathKernel & entry points for non-ARM architectures too ([#137917](https://github.com/pytorch/pytorch/pull/137917))
 - Hook up fp16_gemv_trans to gemv fast path for non-aarch64 architectures ([#138005](https://github.com/pytorch/pytorch/pull/138005))
 - Add Vectorizedc10::BFloat16 specialization for ARM ([#139090](https://github.com/pytorch/pytorch/pull/139090))
 - Build bf16 gemv fast path & entry points for non-ARM architectures too ([#139208](https://github.com/pytorch/pytorch/pull/139208))
 - Hook up bf16_gemv_trans to x86 bf16 GEMM ([#139220](https://github.com/pytorch/pytorch/pull/139220))
 - Don't go through dispatch for *_dot_with_fp32_arith ([#140834](https://github.com/pytorch/pytorch/pull/140834))
 - Add efficient isnan for NEON float ([#139082](https://github.com/pytorch/pytorch/pull/139082))
 - Add efficient isnan for NEON half ([#139083](https://github.com/pytorch/pytorch/pull/139083))
 - Hook up fp16_gemv_trans to x86 fp16 GEMM ([#137918](https://github.com/pytorch/pytorch/pull/137918))
 - Support non-zero beta in fp16_gemv_trans ([#138275](https://github.com/pytorch/pytorch/pull/138275))
 - Port X86_F16 from executorch half to PyTorch half ([#140720](https://github.com/pytorch/pytorch/pull/140720))
# documentation
# developers
# not user facing
 - Fix ir._WaitKernel ([#137401](https://github.com/pytorch/pytorch/pull/137401))
 - tls access helpers ([#138061](https://github.com/pytorch/pytorch/pull/138061))
 - Back out "tls access helpers " and Back out "Compiled autograd configs in TLS " ([#138061](https://github.com/pytorch/pytorch/pull/138061)) ([#137821](https://github.com/pytorch/pytorch/pull/137821)) ([#139086](https://github.com/pytorch/pytorch/pull/139086))
 - avoid specializing strides with DDPOptimizer + inductor ([#140751](https://github.com/pytorch/pytorch/pull/140751))
 - Unbreak fp16 dot issues caused by #137917 ([#139262](https://github.com/pytorch/pytorch/pull/139262))
 - Ensure scalar tensor device matches attn_mask for convert_boolean_attn_mask_cudnn. ([#139450](https://github.com/pytorch/pytorch/pull/139450))
# Untopiced (not relevant to inductor)
 - Add SVE implementation of embedding_lookup_idx ([#133995](https://github.com/pytorch/pytorch/pull/133995))
 - Add SVE implementation of embedding_lookup_idx ([#133995](https://github.com/pytorch/pytorch/pull/133995))
 - Adds support for accelerated sorting with x86-simd-sort ([#127936](https://github.com/pytorch/pytorch/pull/127936))
 - Reserve vector for NT GEMM Matmul ([#141130](https://github.com/pytorch/pytorch/pull/141130))
