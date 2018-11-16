## Turi Recommendation Example

In this example, we provide a pre-baked recommendation engine model for movie ratings. Most The example in this repository originated [here](https://apple.github.io/turicreate/docs/userguide/recommender/)

## How do I integrate my own data?
Most likely you want to adapt this example to your own problem. Perhaps you have customers on your ecommerce app that you want to recommend new items to or you have a music streaming app and you want to recommend new music. 

Below you can see what the data look like and how you might input your own data to get a model up and running for your problem.

### Actions
|    |   userId |   movieId |   rating |   timestamp |
|---:|---------:|----------:|---------:|------------:|
|  0 |        1 |         2 |      3.5 | 1.11249e+09 |
|  1 |        1 |        29 |      3.5 | 1.11248e+09 |
|  2 |        1 |        32 |      3.5 | 1.11248e+09 |
|  3 |        1 |        47 |      3.5 | 1.11248e+09 |
|  4 |        1 |        50 |      3.5 | 1.11248e+09 |

### Items
|    |   movieId | title                              | genres                                      |
|---:|----------:|:-----------------------------------|:--------------------------------------------|
|  0 |         1 | Toy Story (1995)                   | Adventure|Animation|Children|Comedy|Fantasy |
|  1 |         2 | Jumanji (1995)                     | Adventure|Children|Fantasy                  |
|  2 |         3 | Grumpier Old Men (1995)            | Comedy|Romance                              |
|  3 |         4 | Waiting to Exhale (1995)           | Comedy|Drama|Romance                        |
|  4 |         5 | Father of the Bride Part II (1995) | Comedy                                      |
