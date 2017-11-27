# Running Red-Scare

To recreate all results, runner.sh found in the src folder is used. 
Run the file and store results in results.txt by executing the following in bash:

```
sh runner.sh | results.txt
```

A single graph are processed by running: 

```
python main.py -i ../data/gnm-4000-8000-0.txt -nsmalf
```

The *nsmaf* parameters describe which algorithms are applied to the graph and *l* describes the output format.
- ***s*** is Some
- ***n*** is None
- ***m*** is Many
- ***f*** is Few
- ***a*** is Any
- ***l*** is latex (which changes the output format)
