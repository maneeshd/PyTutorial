# Multi-Threading vs Multi-Processing
The threading module provides only Concurreny but not Parallelism as the GIL(Global Interpreter Lock) in Python prevents more 
than one thread to execute at a time. It allows exactly one thread to execute at a time, even if run on a multi-core processor.
If the task is CPU bound then a multi-threaded program will run slower than a single-threaded one.
For IO bound tasks threading will greatly improve the performance.

To achieve both Concurreny and Parallelism the multiprocessing module can be used, which uses processes instead of threads.
But this can be used in a multi-core cpus. May cause severe performance issues in single-core cpus.

So,
For IO bound tasks threading will help.
For CPU bound tasks multiprocessing will help.

## A Simple Example

Finding the sum of prime numbers till 2 million.  
This a CPU bound heavy task.

```
  $ python3 primes_single_thread.py
  The Sum of prime numbers till 2 million is 142913828922
  Execution Time= 26.732 Seconds
```
  
```
  $ python3 primes_multi_thread.py 
  The Sum of prime numbers till 2 million is 142913828922    
  Execution Time= 44.858 Seconds  
```
  
```
  $ python3 primes_multi_processing.py 
  The Sum of prime numbers till 2 million is 142913828922   
  Execution Time= 16.465 Seconds   
```
In the above simple example, the multi-threaded one took more time than the single-threaded one because of the GIL.    
The multi-processed one ran fastest because of the parallel running of the processes created.

###### A good example for multi-threading is the 'ping' operation done on a shell. When pinging a range of IPs multi-threading will
improve the performance. A single threaded one would take more time.
```
  Pinging all IPs in the range 10.242.128.0 - 10.242.128.255
  $ python3 ping_multi_thread.py
  Execution Time= 8.427 Seconds
```

### Source Files
* [primes_single_thread.py] (primes_single_thread.py)
* [primes_multi_thread.py] (primes_multi_thread.py)
* [primes_multi_processing.py] (primes_multi_processing.py)
* [ping_multi_thread.py] (ping_multi_thread.py)

## Authors

* **Maneesh D** - [maneeshd](https://github.com/maneeshd)

## License

This project is licensed under the MIT License - see the [LICENSE.md](/LICENSE.md) file for details
