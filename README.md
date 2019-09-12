# Molecular Datasets

This repository contains a curated collection of datasets linking molecules to their activity.

## Motivations

Many methodologies have been developed to tackle the data inefficiency of traditional machine learning. Most of them use the meta-learning paradigm, where the algorithm is trained on a collections of tasks to extract prior knowledge, which is then used at test time to better generalise on a novel problem.

Although this setting has shown impressive results, the testbeds are for the most part disconnected real-world applications.

Hence, we present three dataset collections that map molecules to scalar values. These can be of value for the community because :

1. This is an actual, real-world problem with tremendous potential. Solving molecular scoring will lead the way to _in silico_ drug optimisation, which will in turn change healthcare as we know it.

2. Molecules are best represented with graphs, but cheap vectorisation methods exist. As such, molecular datasets can be used to try out an array of different methods.


## Collections

Each collection can be seen as a dataset matrix, where the columns are the tasks and the rows are the examples. Note that said matrices are not necessarily dense.

The collections have three main properties, which we report hereafter :

1. The number of individual _tasks_
2. The number of molecules
3. The _density_ of the colection matrix

### TL;DR

| Collection      | Category  | # tasks | # molecules | # examples | density |
| --------------- |:---------:| -------:| -----------:| ----------:| -------:|
| `binding`       | measured  |   5 717 |     573 035 |   1 088 K |   0.03% |
| `antibacterial` | measured  |   3 255 |      26 993 |      90 K |   0.04% |
| `synthetic`     | synthetic |   1 225 |     666 501 | 816 464 K | 100.00% |

### Description

We provide three collections, that can be divided into two main categories :

* Two **measured** collections :

    * [`binding`](binding/) is a collection that measures the binding force between a given protein and molecules. In this context, the task is equivalent to the protein.

    * [`antibacterial`](antibacterial/), wherein we report the measured antibacterial activivty of a set of molecules.

  Note that in the measured collections, the collection matrix is _sparse_ : not all `(molecule, task)` tuples have been tested.

* One **synthetic** collection :

  * In the [`synthetic`](synthetic) collection, we report 1370 _computed_ metrics, coming from various sources. Since these metrics are computed using the structure of the molecules, they give a suitable tested for algorithms aiming at giving a good molecular representation, while limiting/canceling the amount of noise.
