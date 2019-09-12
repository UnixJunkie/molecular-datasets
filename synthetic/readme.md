# The `synthetic` collection

The `synthetic` collection comprises 1 225 descriptors for a large subset of the molecules contained in the `binding` collection (666 501 out of 686 675 molecules).

Unlike the `binding` collection however, our `synthetic` collection is dense : every molecule has a target for every synthetic task.

The full collection (86GB) can be dowloaded with the following script (requires Python) :
```
wget https://datasets-ressources.s3.us-east-2.amazonaws.com/synthetic-molecular-data/binding/download.py && python download.py && rm download
```


## The descriptors

We used a subset of the 1 613 2D descriptors from [mordred](https://github.com/mordred-descriptor/mordred) [1]


[1] Moriwaki H, Tian Y-S, Kawashita N, Takagi T (2018) Mordred: a molecular descriptor calculator. Journal of Cheminformatics 10:4.
