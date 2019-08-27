# CS Build Week 1 FAQ

## Contents

### Install

* [I'm getting a huge error/something about `ssl` when installing `psycopg2` with `pipenv install`](#q100)
* [`pipenv` command not found](#q300)

### Backend

* [I'm getting a 404 when I try to register](#q200)

<!--

-->

## Questions

<a name="q100"></a>
### I'm getting a huge error/something about `ssl` when installing `psycopg2` with `pipenv install`

Buried at the bottom of this error message is something that looks like this:

```
build/temp.macosx-10.14-x86_64-3.7/psycopg/microprotocols_proto.o
build/temp.macosx-10.14-x86_64-3.7/psycopg/typecast.o -L/usr/local/lib -lpq -lssl -lcrypto -o
build/lib.macosx-10.14-x86_64-3.7/psycopg2/_psycopg.cpython-37m-darwin.so',
'    ld: library not found for -lssl',
'    clang: error: linker command failed with exit code 1 (use -v to see invocation)',
"    error: command 'clang' failed with exit status 1", '    ----------------------------------------'
```

#### Mac

_These instructions won't work for Windows!_

If you don't have brew installed, [install it](https://brew.sh/).

Then:

```sh
brew install openssl
sudo cp $(brew --prefix openssl)/lib/libssl.1.0.0.dylib /usr/local/lib
sudo cp $(brew --prefix openssl)/lib/libcrypto.1.0.0.dylib /usr/local/lib
sudo ln -s /usr/local/lib/libssl.1.0.0.dylib /usr/local/lib/libssl.dylib
sudo ln -s /usr/local/lib/libcrypto.1.0.0.dylib /usr/local/lib/libcrypto.dylib
```

then try `pipenv install` again.

<a name="q200"></a>
### I'm getting a 404 when I try to register

The password needs to be at least 8 characters and include a number.

<a name="q300"></a>
### `pipenv` command not found

Install `pipenv` if not already installed.

On Windows, try a different shell, e.g. `cmd.exe` or PowerShell.