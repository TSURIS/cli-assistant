# References

For some reason, a `pip install pyaudio` fails with the following, on both Windows and Linux:

```pypi
Collecting pyaudio
  Downloading PyAudio-0.2.11.tar.gz (37 kB)
  Preparing metadata (setup.py) ... done
Using legacy 'setup.py install' for pyaudio, since package 'wheel' is not installed.
Installing collected packages: pyaudio
  Running setup.py install for pyaudio ... error
  error: subprocess-exited-with-error

  × Running setup.py install for pyaudio did not run successfully.
  │ exit code: 1
  ╰─> [9 lines of output]
      running install
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-3.10
      copying src\pyaudio.py -> build\lib.win-amd64-3.10
      running build_ext
      building '_portaudio' extension
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure

× Encountered error while trying to install package.
╰─> pyaudio

note: This is an issue with the package mentioned above, not pip.
hint: See above for output from the failure.
```

Even after installing that "Microsoft C++ Build Tools", the error persists. So, this `.whl` file was retrieved from:

> **[https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)**

This file was copied here, and then referenced in the [requirements.txt](../src/requirements.txt) file.
