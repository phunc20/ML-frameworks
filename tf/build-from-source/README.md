# Motivatoins
People have various reasons for getting motivated to build tensorflow from source.
In my case, around the end of year 2019, I got interested in old thinkpads like x220, x200, etc.
- From x220 on, i.e. x220, x230, x240, etc,  one can easily install tensorflow in python using <code>pip</code>, all versions included.
- But for x200, it's a different story.
    - Seemingly due to CPU structure, the only workable tensorflow versions are those <code><b>tensorflow\<=1.5.0</b></code>; once you go beyond that, you'd get a <code><b>core dump</b></code> message when you try to use tensorflow after <code>pip install</code> it.
    - <code><b>docker</b></code> won't help. <code><b>core dump</b></code> still takes place in docker containers regardless of tf versions.
- Old thinkpad series which have a 32-bit structure e.g. x60, it just seems that people abandoned the idea of running tensorflow on them. In any case, these machine are weak compared to modern standard.


## x200
This is the first use case which motivated me to build tensorflow from source, because I liked x200 so much that I'd like to make it my main laptop.

Not having much knowledge on this, on one hand, I postponed this issue for quite some time;
on the other hand, when I had spared time, I googled to try to solve it little by little.
Eventually I sort of concluded that there are at least two solutions:
01. I uses <code>arch linux</code> on this x200, so this approach might be a little <b>distro-specific</b>
    - <code><b>sudo pacman -S python-tensorflow</b></code> will install tensorflow to the system's default <code>pip</code>/<code>python</code>, which as of 2020/07/18, is <code>python3.8</code>
    - This solution has several drawbacks:
        - It affects the system <code>pip</code> which is not a good practice in python
        - It can only install one version, e.g. version <code>2.2.0rc3-2</code> as of 2020/07/18
02. Build from source
    - Pros
        - All different versions of tensorflow can be built and installed
        - Can be install into an isolated virtual environment
    - Cons
        - Building process takes long

In what follows I will write about my own experience on building tensorflow from source.
The buidling process was largely guided by [Tensorflow's official website](https://www.tensorflow.org/install/source).
The reason why I rewrite it using my own words is that
- It might help others succeed in such a building process
- At least this helps myself next time when I tried to remember how I did it

### Step 01. <code>bazel</code>
I chose to use <code><b>bazelisk</b></code>. On arch linux, the installation of <code><b>bazelisk</b></code> can be done in the following steps:
01. <code><b>sudo pacman -S go</b></code>, i.e. first we install <code>go</code>.
02. <code><b>go get github.com/bazelbuild/bazelisk</b></code>, i.e. we use <code>go</code> to install <code>bazelisk</code>
03. Make a symlink named <code><b>bazel</b></code> to the installed <code>bazelisk</code> (normally under the path <code><b>~/go/bin/bazelisk</b></code>), e.g. <pre>
    ln -s ~/go/bin/bazelisk ~/.local/bin/bazel
</pre>
<b>Ref.</b>
<br>
- [https://github.com/bazelbuild/bazelisk](https://github.com/bazelbuild/bazelisk)
- One can check the <code>bazel</code> version by the command <code><b>bazel --version</b></code>


### Step 02. <code>tensorflow</code>
01. <pre>git clone https://github.com/tensorflow/tensorflow.git<br>cd tensorflow</pre>
02. <code><b>git checkout \<branch_name\></b></code>, e.g. if you want to build version 2.2.0, you can <code><b>git checkout v2.2.0</b></code>. (Cf. [https://github.com/tensorflow/tensorflow/releases?after=v2.2.0-rc2](https://github.com/tensorflow/tensorflow/releases?after=v2.2.0-rc2))
03. Make a new python virtual environment, or locate one, to which you'd like to install tensorflow.
<br>
For example, if you use <code>virtualenvwrapper</code> as I do, you can
<pre>
mkvirtualenv -p python3.6 tf2.2.0
</pre>
Besides, make sure you install the following python packages beforehand, <b>w/o</b> which the tensorflow building process will <b>fail</b> to succeed.
<pre>
# In the virtual environment of your choice, e.g. following our case above, in "tf2.2.0",
# install numpy<1.19.0
# e.g. numpy==1.18.3 but definitely NOT numpy==1.19.0
(tf2.2.0) $ pip install numpy==1.18.3
# otherwise won't build: Cf.
#https://github.com/tensorflow/tensorflow/issues/41061
#https://github.com/tensorflow/tensorflow/issues/40742
(tf2.2.0) $ pip install keras_preprocessing
</pre>
<br>
<b>Rmk.</b> The above-mentioned package installations are what I realized after a few failing installation attempts. However, not long after, I found that actually it was clearly described in [https://www.tensorflow.org/install/source#install_python_and_the_tensorflow_package_dependencies](https://www.tensorflow.org/install/source#install_python_and_the_tensorflow_package_dependencies).
04. If this is not the first time you build tensorflow using <b>bazel</b>, for example, if you have already built a <code><b>tensorflow==2.2.0</b></code> and you'd like to build a <code><b>tensorflow==1.15.0</b></code>, you might need to do <code><b>bazel clean</b></code> at this stage.
<br>
Example output:<pre>
$ bazel clean
Starting local Bazel server and connecting to it...
INFO: Options provided by the client:
  Inherited 'common' options: --isatty=1 --terminal_columns=104
INFO: Reading rc options for 'clean' from /home/phunc20/github/tensorflow/tensorflow/.bazelrc:
  Inherited 'common' options: --experimental_repo_remote_exec
INFO: Reading rc options for 'clean' from /home/phunc20/github/tensorflow/tensorflow/.bazelrc:
  Inherited 'build' options: --apple_platform_type=macos --define framework_shared_object=true --define
open_source_build=true --java_toolchain=//third_party/toolchains/java:tf_java_toolchain --host_java_toolchain=//third_party/toolchains/java:tf_java_toolchain --define=use_fast_cpp_protos=true --define=allow_oversize_protos=true --spawn_strategy=standalone -c opt --announce_rc --define=grpc_no_ares=true --noincompatible_remove_legacy_whole_archive --noincompatible_prohibit_aapt1 --enable_platform_specific_config --config=v2
INFO: Reading rc options for 'clean' from /home/phunc20/github/tensorflow/tensorflow/.tf_configure.bazelrc:
  Inherited 'build' options: --action_env PYTHON_BIN_PATH=/home/phunc20/.virtualenvs/tf2.2.0/bin/python --action_env PYTHON_LIB_PATH=/home/phunc20/.virtualenvs/tf2.2.0/lib/python3.6/site-packages --python_path=/home/phunc20/.virtualenvs/tf2.2.0/bin/python --config=xla --action_env TF_CONFIGURE_IOS=0
INFO: Found applicable config definition build:v2 in file /home/phunc20/github/tensorflow/tensorflow/.bazelrc: --define=tf_api_version=2 --action_env=TF2_BEHAVIOR=1
INFO: Found applicable config definition build:xla in file /home/phunc20/github/tensorflow/tensorflow/.bazelrc: --action_env=TF_ENABLE_XLA=1 --define=with_xla_support=true
INFO: Found applicable config definition build:linux in file /home/phunc20/github/tensorflow/tensorflow/.bazelrc: --copt=-w --define=PREFIX=/usr --define=LIBDIR=$(PREFIX)/lib --define=INCLUDEDIR=$(PREFIX)/include --cxxopt=-std=c++14 --host_cxxopt=-std=c++14 --config=dynamic_kernels
INFO: Found applicable config definition build:dynamic_kernels in file /home/phunc20/github/tensorflow/tensorflow/.bazelrc: --define=dynamic_loaded_kernels=true --copt=-DAUTOLOAD_DYNAMIC_KERNELS
INFO: Starting clean (this may take a while). Consider using --async if the clean takes more than several minutes.
</pre>
05. <code><b>./configure</b></code>
<pre>
$ ./configure
You have bazel 2.0.0 installed.
Please specify the location of python. [Default is /usr/bin/python]: /home/phunc20/.virtualenvs/tf1.15.0/bin/python Found possible Python library paths:
  /home/phunc20/.virtualenvs/tf1.15.0/lib/python3.6/site-packages
Please input the desired Python library path to use.  Default is [/home/phunc20/.virtualenvs/tf1.15.0/lib/python3.6/site-packages]
<br>
Do you wish to build TensorFlow with OpenCL SYCL support? [y/N]:
No OpenCL SYCL support will be enabled for TensorFlow.
<br>
Do you wish to build TensorFlow with ROCm support? [y/N]:
No ROCm support will be enabled for TensorFlow.
<br>
Do you wish to build TensorFlow with CUDA support? [y/N]:
No CUDA support will be enabled for TensorFlow.
<br>
Do you wish to download a fresh release of clang? (Experimental) [y/N]:
Clang will not be downloaded.
<br>
Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -march=native -Wno-sign-compare]:
<br>
Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]:
Not configuring the WORKSPACE for Android builds.
<br>
Preconfigured Bazel build configs. You can use any of the below by adding "--config=<>" to your build command. See .bazelrc for more details.
        --config=mkl            # Build with MKL support.
        --config=monolithic     # Config for mostly static monolithic build.
        --config=ngraph         # Build with Intel nGraph support.
        --config=numa           # Build with NUMA support.
        --config=dynamic_kernels        # (Experimental) Build kernels into separate shared objects.
        --config=v2             # Build TensorFlow 2.x instead of 1.x.
Preconfigured Bazel build configs to DISABLE default on features:
        --config=noaws          # Disable AWS S3 filesystem support.
        --config=nogcp          # Disable GCP support.
        --config=nohdfs         # Disable HDFS support.
        --config=nonccl         # Disable NVIDIA NCCL support.
Configuration finished
</pre>
06. Depending on the version of tensorflow that you want to build, the command in this step might be slightly different. (<b>Note</b> that this step could take a <b>very long time</b>, depending on your machine; on my first build on x200, it took <b>more than 1 day</b>, i.e. <b>btw 24 to 36 hours</b>, to finish building.)
<pre># Tensorflow1
bazel build --config=v1 //tensorflow/tools/pip_package:build_pip_package
# Tensorflow2
bazel build //tensorflow/tools/pip_package:build_pip_package
</pre>
Example output:
<pre>
$ bazel build //tensorflow/tools/pip_package:build_pip_package
Starting local Bazel server and connecting to it...
INFO: Options provided by the client:
  Inherited 'common' options: --isatty=1 --terminal_columns=104
INFO: Reading rc options for 'build' from /home/phunc20/github/tensorflow/tensorflow/.bazelrc:
  Inherited 'common' options: --experimental_repo_remote_exec
INFO: Reading rc options for 'build' from /home/phunc20/github/tensorflow/tensorflow/.bazelrc:
  'build' options: --apple_platform_type=macos --define framework_shared_object=true --define open_source_build=true --java_toolchain=//third_party/toolchains/java:tf_java_toolchain --host_java_toolchain=//third_party/toolchains/java:tf_java_toolchain --define=use_fast_cpp_protos=true --define=allow_oversize_protos=true --spawn_strategy=standalone -c opt --announce_rc --define=grpc_no_ares=true --noincompatible_remove_legacy_whole_archive --noincompatible_prohibit_aapt1 --enable_platform_specific_config --config=v2
INFO: Reading rc options for 'build' from /home/phunc20/github/tensorflow/tensorflow/.tf_configure.bazelrc:
  'build' options: --action_env PYTHON_BIN_PATH=/home/phunc20/.virtualenvs/tf1.15.0/bin/python --action_env PYTHON_LIB_PATH=/home/phunc20/.virtualenvs/tf1.15.0/lib/python3.6/site-packages --python_path=/home/phunc20/.virtualenvs/tf1.15.0/bin/python --config=xla --action_env TF_CONFIGURE_IOS=0
INFO: Found applicable config definition build:v2 in file /home/phunc20/github/tensorflow/tensorflow/.bazelrc: --define=tf_api_version=2 --action_env=TF2_BEHAVIOR=1
INFO: Found applicable config definition build:xla in file /home/phunc20/github/tensorflow/tensorflow/.bazelrc: --action_env=TF_ENABLE_XLA=1 --define=with_xla_support=true
INFO: Found applicable config definition build:v1 in file /home/phunc20/github/tensorflow/tensorflow/.bazelrc: --define=tf_api_version=1 --action_env=TF2_BEHAVIOR=0
INFO: Found applicable config definition build:linux in file /home/phunc20/github/tensorflow/tensorflow/.bazelrc: --copt=-w --define=PREFIX=/usr --define=LIBDIR=$(PREFIX)/lib --define=INCLUDEDIR=$(PREFIX)/include --cxxopt=-std=c++14 --host_cxxopt=-std=c++14 --config=dynamic_kernels
INFO: Found applicable config definition build:dynamic_kernels in file /home/phunc20/github/tensorflow/tensorflow/.bazelrc: --define=dynamic_loaded_kernels=true --copt=-DAUTOLOAD_DYNAMIC_KERNELS
Analyzing: target //tensorflow/tools/pip_package:build_pip_package (42 packages loaded, 9 targets configured)
    currently loading: tensorflow/core/kernels
WARNING: /home/phunc20/github/tensorflow/tensorflow/tensorflow/python/BUILD:848:1: in srcs attribute of
cc_binary rule //tensorflow/python:_pywrap_toco_api.so: please do not import '//tensorflow/lite/toco/pyt
hon:toco_python_api.h' directly. You should either move the file to this package or depend on an appropr
iate rule there. Since this rule was created by the macro 'tf_python_pybind_extension', the error might
have been caused by the macro implementation
WARNING: /home/phunc20/github/tensorflow/tensorflow/tensorflow/python/BUILD:4496:1: in py_library rule /
/tensorflow/python:standard_ops: target '//tensorflow/python:standard_ops' depends on deprecated target
'//tensorflow/python/ops/distributions:distributions': TensorFlow Distributions has migrated to TensorFl
ow Probability (https://github.com/tensorflow/probability). Deprecated copies remaining in tf.distributi
ons will not receive new features, and will be removed by early 2019. You should update all usage of `tf
.distributions` to `tfp.distributions`.
WARNING: /home/phunc20/github/tensorflow/tensorflow/tensorflow/python/BUILD:89:1: in py_library rule //t
ensorflow/python:no_contrib: target '//tensorflow/python:no_contrib' depends on deprecated target '//ten
sorflow/python/ops/distributions:distributions': TensorFlow Distributions has migrated to TensorFlow Pro
bability (https://github.com/tensorflow/probability). Deprecated copies remaining in tf.distributions wi
ll not receive new features, and will be removed by early 2019. You should update all usage of `tf.distr
ibutions` to `tfp.distributions`.
</pre>


## Result
<pre>
2020-07-20 16:14:42.008829: I tensorflow/lite/toco/toco_tooling.cc:471] Number of parameters: 0
INFO: From Executing genrule //tensorflow/lite/python/testdata:permute_float:
2020-07-20 16:14:42.317591: I tensorflow/lite/toco/graph_transformations/graph_transformations.cc:39] Before Removing unused ops: 1 operators, 3 arrays (0 quantized)
2020-07-20 16:14:42.317858: I tensorflow/lite/toco/graph_transformations/graph_transformations.cc:39] Before general graph transformations: 1 operators, 3 arrays (0 quantized)
2020-07-20 16:14:42.317999: I tensorflow/lite/toco/graph_transformations/graph_transformations.cc:39] After general graph transformations pass 1: 1 operators, 4 arrays (0 quantized)
2020-07-20 16:14:42.318057: I tensorflow/lite/toco/graph_transformations/graph_transformations.cc:39] Before Group bidirectional sequence lstm/rnn: 1 operators, 4 arrays (0 quantized)
2020-07-20 16:14:42.318096: I tensorflow/lite/toco/graph_transformations/graph_transformations.cc:39] Before dequantization graph transformations: 1 operators, 4 arrays (0 quantized)
2020-07-20 16:14:42.318130: I tensorflow/lite/toco/graph_transformations/graph_transformations.cc:39] Before Identify nearest upsample.: 1 operators, 4 arrays (0 quantized)
2020-07-20 16:14:42.318173: I tensorflow/lite/toco/allocate_transient_arrays.cc:345] Total transient array allocated size: 0 bytes, theoretical optimal value: 0 bytes.
2020-07-20 16:14:42.318209: I tensorflow/lite/toco/toco_tooling.cc:456] Estimated count of arithmetic ops: 36 ops, equivalently 18 MACs
2020-07-20 16:14:42.318234: I tensorflow/lite/toco/toco_tooling.cc:471] Number of parameters: 20
Target //tensorflow/tools/pip_package:build_pip_package up-to-date:
  bazel-bin/tensorflow/tools/pip_package/build_pip_package
INFO: Elapsed time: 50544.042s, Critical Path: 322.97s
INFO: 14283 processes: 14283 local.
INFO: Build completed successfully, 15315 total actions
[phunc20@mushroom-x200 tensorflow]$ ls -l bazel-bin/tensorflow/tools/pip_package/build_pip_package
lrwxrwxrwx 1 phunc20 wheel 92 Jul 20 16:06 bazel-bin/tensorflow/tools/pip_package/build_pip_package -> /home/phunc20/github/tensorflow/tensorflow/tensorflow/tools/pip_package/build_pip_package.sh
[phunc20@mushroom-x200 tensorflow]$ #./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
[phunc20@mushroom-x200 tensorflow]$ ./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tens
orflow_pkg
Mon 20 Jul 2020 06:59:15 PM +07 : === Preparing sources in dir: /tmp/tmp.RhJEbyyoCS
~/github/tensorflow/tensorflow ~/github/tensorflow/tensorflow
~/github/tensorflow/tensorflow
~/github/tensorflow/tensorflow/bazel-bin/tensorflow/tools/pip_package/build_pip_package.runfiles/org_tensorflow ~/github/tensorflow/tensorflow
~/github/tensorflow/tensorflow
/tmp/tmp.RhJEbyyoCS/tensorflow/include ~/github/tensorflow/tensorflow
~/github/tensorflow/tensorflow
Mon 20 Jul 2020 06:59:31 PM +07 : === Building wheel
warning: no files found matching 'README'
warning: no files found matching '*.pyd' under directory '*'
warning: no files found matching '*.pyi' under directory '*'
warning: no files found matching '*.pd' under directory '*'
warning: no files found matching '*.dylib' under directory '*'
warning: no files found matching '*.dll' under directory '*'
warning: no files found matching '*.lib' under directory '*'
warning: no files found matching '*.csv' under directory '*'
warning: no files found matching '*.h' under directory 'tensorflow/include/tensorflow'
warning: no files found matching '*.proto' under directory 'tensorflow/include/tensorflow'
warning: no files found matching '*' under directory 'tensorflow/include/third_party'
Mon 20 Jul 2020 07:00:21 PM +07 : === Output wheel file is in: /tmp/tensorflow_pkg
[phunc20@mushroom-x200 tensorflow]$
</pre>


## <code><b>export USE_BAZEL_VERSION=0.26.1</b></code>
To install <code>tf1</code>, the bazel version has to be downgraded.

<pre>
(tf1.15.0) [phunc20@mushroom-x200 tensorflow]$ ./configure
WARNING: Running Bazel server needs to be killed, because the startup options are different.
You have bazel 3.4.1 installed.
Please downgrade your bazel installation to version 0.26.1 or lower to build TensorFlow! To downgrade: download the installer for the old version (from https://github.com/bazelbuild/bazel/releases) then run the installer.
(tf1.15.0) [phunc20@mushroom-x200 tensorflow]$ bazel clean
ERROR: Config value xla is not defined in any .rc file
(tf1.15.0) [phunc20@mushroom-x200 tensorflow]$ ./configure
WARNING: Running Bazel server needs to be killed, because the startup options are different.
You have bazel 3.4.1 installed.
Please downgrade your bazel installation to version 0.26.1 or lower to build TensorFlow! To downgrade: download the installer for the old version (from https://github.com/bazelbuild/bazel/releases) then run the installer.
(tf1.15.0) [phunc20@mushroom-x200 tensorflow]$ pstree -p | grep bazel
(tf1.15.0) [phunc20@mushroom-x200 tensorflow]$ ./configure
You have bazel 3.4.1 installed.
Please downgrade your bazel installation to version 0.26.1 or lower to build TensorFlow! To downgrade: download the installer for the old version (from https://github.com/bazelbuild/bazel/releases) then run the installer.
(tf1.15.0) [phunc20@mushroom-x200 tensorflow]$ export USE_BAZEL_VERSION=0.26.1
(tf1.15.0) [phunc20@mushroom-x200 tensorflow]$ ./configure
2020/07/20 19:38:29 Downloading https://releases.bazel.build/0.26.1/release/bazel-0.26.1-linux-x86_64...
Extracting Bazel installation...
lrwxrwxrwx  1 phunc20 wheel    108 Jul 20 19:52 bazel-out -> /home/phunc20/.cache/bazel/_bazel_phunc20/e581daf60d16499850c4a37e5fc33d00/execroot/org_tensorflow/bazel-out
</pre>





