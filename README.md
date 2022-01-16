Orininal model from: https://github.com/carrenD/Webthetics

## Predict only of Webthetics model

### Prepare env

- Ubuntu 18.04

```
$ conda create -n webthetics
$ conda env list
$ conda activate webthetics
$ conda install caffe
```

## Run predict

```
(webthetics) $ python baconbao-predict.py
```

Example results

```
I0117 04:51:44.439997 11533 blocking_queue.cpp:49] Waiting for data
    baconbao-sample/117.png  baconbao-sample/124.png  baconbao-sample/reddit-1.png  baconbao-sample/reddit-2.png  baconbao-sample/4chan-1.png  baconbao-sample/4chan-2.png
0                  3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
1                  3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
2                  3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
3                  3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
4                  3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
5                  3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
6                  3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
7                  3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
8                  3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
9                  3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
10                 3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
11                 3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
12                 3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
13                 3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
14                 3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
15                 3.431780                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
16                 3.431779                 6.349188                           NaN                           NaN                          NaN                          NaN
       baconbao-sample/117.png  baconbao-sample/124.png  baconbao-sample/reddit-1.png  baconbao-sample/reddit-2.png  baconbao-sample/4chan-1.png  baconbao-sample/4chan-2.png
count             1.700000e+01                17.000000                     16.000000                     16.000000                    16.000000                    16.000000
mean              3.431780e+00                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
std               1.156500e-07                 0.000000                      0.000000                      0.000000                     0.000000                     0.000000
min               3.431779e+00                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
25%               3.431780e+00                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
50%               3.431780e+00                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
75%               3.431780e+00                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
max               3.431780e+00                 6.349188                      3.033405                      4.485435                     3.309493                     3.373004
------------
baconbao-sample/117.png 3.43178
baconbao-sample/124.png 6.34919
baconbao-sample/reddit-1.png 3.03341
baconbao-sample/reddit-2.png 4.48543
baconbao-sample/4chan-1.png 3.30949
baconbao-sample/4chan-2.png 3.373
```
