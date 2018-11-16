## Turi Recommendation Example

In this example, we provide a pre-baked recommendation engine model for movie ratings. Most The example in this repository originated [here](https://apple.github.io/turicreate/docs/userguide/recommender/)

## How do I integrate my own data?
Most likely you want to adapt this example to your own problem. Perhaps you have customers on your ecommerce app that you want to recommend new items to or you have a music streaming app and you want to recommend new music. 

Below you can see what the data look like and how you might input your own data to get a model up and running for your problem.


<table>
<tr><th>Actions </th><th>Items </th></tr>
<tr><td>

|   userId |   movieId |   rating |   timestamp |
|---------:|----------:|---------:|------------:|
|        1 |         2 |      3.5 |  1112486027 |
|        1 |        29 |      3.5 |  1112484676 |
|        1 |        32 |      3.5 |  1112484819 |
|        1 |        47 |      3.5 |  1112484727 |
|        1 |        50 |      3.5 |  1112484580 |

</td><td>

|   movieId | title                              | genres                                      |
|----------:|:-----------------------------------|:--------------------------------------------|
|         1 | Toy Story (1995)                   | Adventure|Animation|Children|Comedy|Fantasy |
|         2 | Jumanji (1995)                     | Adventure|Children|Fantasy                  |
|         3 | Grumpier Old Men (1995)            | Comedy|Romance                              |
|         4 | Waiting to Exhale (1995)           | Comedy|Drama|Romance                        |
|         5 | Father of the Bride Part II (1995) | Comedy                                      |

</td></tr> </table>
