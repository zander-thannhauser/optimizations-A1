
# optimizations-A1

## Carr's Numbers:
| File             | Original | Opt.Time |      Carr's LVN |    Opt. # Inst. |
|  :--             |      --: |      --: |            --:  |             --: |
| `arrayparam.il`  |      841 | 0m0.072s |   487 (172.69%) |   374 (224.27%) |
| `bubble.il`      |     4374 | 0m0.076s |  2855 (153.20%) |  1444 (302.91%) |
| `check.il`       |      140 | 0m0.031s |   130 (107.69%) |    64 (218.75%) |
| `dynamic.il`     |    39155 | 0m0.063s | 23579 (166.06%) | 12821 (304.64%) |
| `fib.il`         |      274 | 0m0.032s |   252 (108.73%) |   186 (147.31%) |
| `gcd.il`         |      103 | 0m0.070s |    83 (124.10%) |    52 (174.58%) |
| `newdyn.il`      |   136919 | 0m0.078s | 82256 (166.45%) | 44586 (307.09%) |
| `qs.il`          |     4574 | 0m0.057s |  3468 (131.89%) |  2240 (197.84%) |
| `while_array.il` |      377 | 0m0.036s |   315 (119.68%) |   165 (228.48%) |

# Dependencies

## Interpreter/Emulator
My interpreter combines the `comp`, `test{eq,ne,gt,ge,lt,le}` and `cbr{,ne}`
instructions into `cbr_{eq,ne,gt,ge,lt,le}` respectively. These instructions
seem to not be supported by the given interpreter, so I wrote my own interpreter
to support those instructions.

The git repo is here: `https://github.com/zander-thannhauser/Iloc-interpreter.git`

you should be able to build it by running:

```
struct apt install gcc-multilib make gcc findutils
git clone https://github.com/zander-thannhauser/Iloc-interpreter.git
cd Iloc-interpreter
make
```

you can run the examples like this:
```
./interpreter -i ./examples/arrayparam.il
./interpreter -i ./examples/bubble.il
./interpreter -i ./examples/gcd.il
./interpreter -i ./examples/dynamic.il
  ...
```

## Python 3.10

To make development easier I used python 3.10's structured pattern matching
statement `match`. To build from source on Ubuntu:

```
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev \
	libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget \
	libbz2-dev
wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz
tar -xf Python-3.10.*.tgz
cd Python-3.10.*/
./configure --enable-optimizations
make -j `nproc`
# sudo make altinstall # installs by the name 'python3.10'
```

Running the installation command is optional.
To run my optimizier on the example input files:

```
path/to/python3.10 ./main.py ./examples/arrayparam.il
path/to/python3.10 ./main.py ./examples/bubble.il
path/to/python3.10 ./main.py ./examples/check.il
path/to/python3.10 ./main.py ./examples/dynamic.il
path/to/python3.10 ./main.py ./examples/fib.il
path/to/python3.10 ./main.py ./examples/gcd.il
path/to/python3.10 ./main.py ./examples/helloworld.il
path/to/python3.10 ./main.py ./examples/newdyn.il
path/to/python3.10 ./main.py ./examples/qs.il
path/to/python3.10 ./main.py ./examples/while_array.il
```

To run my interpreter/emulator on the results:

```
./path/to/interpreter -si ./examples/arrayparam.oil
./path/to/interpreter -si ./examples/bubble.oil
./path/to/interpreter -si ./examples/check.oil
./path/to/interpreter -si ./examples/dynamic.oil
./path/to/interpreter -si ./examples/fib.oil
./path/to/interpreter -si ./examples/gcd.oil
./path/to/interpreter -si ./examples/newdyn.oil
./path/to/interpreter -si ./examples/qs.oil
./path/to/interpreter -si ./examples/while_array.oil
```


















