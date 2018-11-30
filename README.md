## Turi Recommendation Example

*This public repository is designed for use in the Skafos ML delivery platform, which is available at metismachine.com.*

In this example, we provide a recommendation engine model for movie ratings. The example in this repository comes from TuriCreate's own example that can be found [here](https://apple.github.io/turicreate/docs/userguide/recommender/). 

To get this model up and running on Skafos:
- [Sign Up](https://dashboard.metismachine.io/sign-up) for a Skafos account
- Fork and clone this repository
- Adapt your metis.config.yml to run on your new Skafos account
- `git push skafos`

To adapt this to your own problem, check out more below.

## What can you find in this repo?
In this repository you will find:
- `recommender.py` - A script that loads some example data from a public S3 bucket, trains a recommender, validates the model and saves the model.
- `recommender.ipynb` - A notebook that replicates the `recommender.py` script. To see some example output, check out that notebook here on GitHub.
- `requirements.txt` and `metis.config.yml` - Two files that Skafos requires to run jobs.
- `Recommender_Data_Integration_Example.ipynb` - A Jupyter Notebook containing an example of how to get your own data working in the TuriCreate framework.
- `/models` - a directory that contains a saved TuriCreate model (.model) and a saved CoreML model (.mlmodel)
- `/common` - a directory that contains functions and code called from the main recommender script.

## How to use this repo.
1. Use the `.mlmodel` file in your app to start making recommendations.
2. Use the provided code and example data to train the recomemndation engine.
3. Train a recommender on different data.


### The Data
The example data for this example is also the example data used by Turi Create in their Recommender Engine Example, the MovieLens 20M Dataset. We have placed an example of this data on a public S3 bucket for this example. The format of this data is shown below. Note that there are two types of files that provide data in two formats: Actions (userID, movieID, rating, and timestamp.) and Metadata for each movie (movieID, title, genre).


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

### Integrating your own data

To build a recommender on your own data, it needs to be in the same format as the tables above. For example, if you had e-commerce data with shoppers, indexed by shopper_id, and products indexed by product_id, you could format it as shown below:

|  shopper_id |   product_id |   rating |   timestamp |
|---------:|----------:|---------:|------------:|
|        1 |        1231 |      5 |  1112586027 |
|        1 |        1411 |      3 |  1112584676 |
|        1 |        2332 |      4 |  1112684819 |
|        1 |        4132 |      2 |  1112184727 |
|        1 |        1241 |      4 |  1112484580 |


You could also read in any relevant metadata about each product_id, if desired.

To build a recommendation engine, you would make the following TC calls:

Your function call would look like: 
- ```python
     tc.recommender.create(observation_data = training_data, 'user_id' = 'shopper_id', item_id = 'product_id'```
