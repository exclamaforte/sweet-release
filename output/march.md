# bc breaking
- Rename `use_absolute_path` to `use_relative_path` in AOTI. This reflects the option's true purpose: compile a cpp file using its basename instead of the its full path ([#147805](https://github.com/pytorch/pytorch/pull/147805)).
# deprecation
# new features
- Emit a CMakeLists.txt when package_cpp_only is specified in AOTI ([#143352](https://github.com/pytorch/pytorch/pull/143352))
- One Dynamo graph can now map to multiple inductor graphs with different `graph_partition` functions. Set the `graph_partition` function in inductor config to enable ([#147038](https://github.com/pytorch/pytorch/pull/147038))
# improvements
- Removed an unnecessarily struct runtime alignment assertion, allowing more flexible usecases of AOTI ([#143236](https://github.com/pytorch/pytorch/pull/143236))
- Support _int_mm in AOTI ([#144571](https://github.com/pytorch/pytorch/pull/144571))
- Add an option to skip optimizing generated wrapper code. Set `AOT_INDUCTOR_COMPILE_WRAPPER_WITH_O0=1` ([#144866](https://github.com/pytorch/pytorch/pull/144866))
- Add ConfigFuzzer support for Dynamo configs ([#145565](https://github.com/pytorch/pytorch/pull/145565))
- Support dynamic shape constraints in Export ([#146044](https://github.com/pytorch/pytorch/pull/146044))
- Handle MLIR scf.yield more accurately in user Triton code ([#147762](https://github.com/pytorch/pytorch/pull/147762)).
- Add a global_scratch arg to support Triton 3.3 ([#148051](https://github.com/pytorch/pytorch/pull/148051))
- Support AOTI + CUDAGraphs when calling from Python ([#148601](https://github.com/pytorch/pytorch/pull/148601))
# bug fixes
- Fix bug in AOTI one-pass codegen when max-autotune is turned on ([#143098](https://github.com/pytorch/pytorch/pull/143098))
- Updated triton support to account for changes in AttrsDescriptor ([#145051](https://github.com/pytorch/pytorch/pull/145051)) ([#145348](https://github.com/pytorch/pytorch/pull/145348)) ([#145575](https://github.com/pytorch/pytorch/pull/145575)) ([#145583](https://github.com/pytorch/pytorch/pull/145583)) ([#145515](https://github.com/pytorch/pytorch/pull/145515))
- Fix bug where the `benchmark_harness` isn't generated, but is called in some cases ([#145532](https://github.com/pytorch/pytorch/pull/145532))
- Make sure not using cpp wrapper when setting nvtx training annotation ([#145538](https://github.com/pytorch/pytorch/pull/145538))
- Fix a memory leak in package `AOTIModelPackageLoaderPybind::boxed_run` ([#146100](https://github.com/pytorch/pytorch/pull/146100))
- Fix bug where SVE256 features were run on SVE128 systems ([#146207](https://github.com/pytorch/pytorch/pull/146207))
- Fix an unaligned memory access issue in `mm_template` ([#146293](https://github.com/pytorch/pytorch/pull/146293))
- Fix intermediate debug information with cpp_wrapper ([#145527](https://github.com/pytorch/pytorch/pull/145527))
- Fix bug where inductor was codegen-ing wrong shapes for bucketize when it was fused as an epilogue ([#148769](https://github.com/pytorch/pytorch/pull/148769))
# performance
# docs
- Update AOTI tutorial ([#143390](https://github.com/pytorch/pytorch/pull/143390))
- inductor.config.descriptive_names = False is no longer a suggested option. ([#145523](https://github.com/pytorch/pytorch/pull/145523))
# devs
