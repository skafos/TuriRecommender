## Turi Recommendation Example

In this example, we provide a pre-baked recommendation engine model for movie ratings. The example in this repository comes from TuriCreate's own example that can be found [here](https://apple.github.io/turicreate/docs/userguide/recommender/). 

To get this model up and running on Skafos:
- [Sign Up](https://dashboard.metismachine.io/sign-up) for a Skafos account
- Fork and clone this repository
- Adapt your metis.config.yml to run on your new Skafos account
- `git push skafos`

For more information on getting a job up and running on Skafos, take a look at this example in our [documentation](https://docs.metismachine.io/v1.1/docs/step-by-step-tutorial-churn-modeling).

To adapt this to your own problem, check out more below.

### Components
In this repository you will find:
- `recommender.py` - A script that loads some example data from a public S3 bucket, trains a recommender, validates the model and saves the model.
- `recommender.ipynb` - A notebook that replicates the `recommender.py` script. To see some example output, check out that notebook here on GitHub.
- `requirements.txt` and `metis.config.yml` - Two files that Skafos requires to run jobs.

### The Data
Most likely you want to adapt this example to your own problem. Perhaps you have customers on your ecommerce app that you want to recommend new items to or you have a music streaming app and you want to recommend new music. 

Below you can see what the data look like and how you might input your own data to get a model up and running for your problem. The training data in this example is the **actions** data, which you can see below. The recommendations are being built based on just one dimension in this example, **rating**.


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
To build a recommender we call:
- `tc.recommender.create(observation_data = training_data, user_id = 'userId', item_id= 'movieId')`. 

Suppose you had some e-commerce data where you had `shoppers`, indexed by `shopper_id`, and `products` indexed by `product_id`. Here is what the data might look like, ignoring the items table for now and just the looking at the actions table:

|  shopper_id |   product_id |   rating |   timestamp |
|---------:|----------:|---------:|------------:|
|        1 |        1231 |      5 |  1112586027 |
|        1 |        1411 |      3 |  1112584676 |
|        1 |        2332 |      4 |  1112684819 |
|        1 |        4132 |      2 |  1112184727 |
|        1 |        1241 |      4 |  1112484580 |


Your function call would look like: 
- `tc.recommender.create(observation_data = training_data, 'user_id' = 'shopper_id', item_id = 'product_id'`
