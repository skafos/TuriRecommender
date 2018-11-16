## Turi Recommendation Example

In this example, we provide a pre-baked recommendation engine model for movie ratings. The example in this repository comes from TuriCreate's own example that can be found [here](https://apple.github.io/turicreate/docs/userguide/recommender/). 

To get this model up and running on Skafos:
- Sign up for a Skafos account
- Fork and clone this repository
- Adapt your metis.config.yml to run on your new Skafos account
- git push skafos

For more information on getting a job up and running on Skafos, take a look at our documentation.

### Components
In this repository you will find:
- `recommender.py` - A script that loads some example data from a public S3 bucket, trains a recommender, validates the model and saves the model.
- `recommender.ipynb` - A notebook that replicates the `recommender.py` script. To see some example output, check out that notebook here on GitHub.
- `requirements.txt` and `metis.config.yml` - Two files that Skafos requires to run jobs.

### How do I integrate my own data?
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
