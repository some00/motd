My MOTD script
=============

Usage
-------
- clone this repository
- download and extract [dataset](https://www.kaggle.com/datasets/manann/quotes-500k). registration required.
- run `motd.py` to generate sqlite database
- add `motd.sh` to the end of `.bashrc/.zshrc`.

Benchmark
--------------
```
> lscpu | grep 'Model name'
Model name:                      Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz
> time ./motd.sh
"Want to have a short phone call with someone? Call them at 11:55 a.m., right before lunch. They'll talk fast. You may think you are interesting, but you are not more interesting than lunch." - Randy Pausch, The Last Lecture
./motd.sh  0.08s user 0.06s system 99% cpu 0.143 total
```
```
> lscpu | grep 'Model name'
Model name:                      AMD Ryzen 9 5950X 16-Core Processor
> time ./motd.sh
"Never judge a book by its "spine"." - Stanley Victor Paskavich
./motd.sh  0.04s user 0.01s system 99% cpu 0.050 total
```
