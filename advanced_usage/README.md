# Advanced Usage
The purpose of this Advanced Usage Guide is to provide additional tooling, tips, and guidance for building recommendation engine models.

## Tips and "Gotchas"
-  **Training Data**: The example model is trained on a dataset of movie ratings. The format of this data is shown below. Note that there are two types of files that provide data in two formats: Actions (userID, movieID, rating, and timestamp.) and Metadata for each movie (movieID, title, genre).

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
 
 - **Integrating Your Own Data**: Likely you aren't interested in building a recommendation engine for movies... What you will need to do is collect data that has a similar format. For example, if you had e-commerce data with shoppers, indexed by *shopper_id*, and products indexed by *product_id*, you could format it as shown below. At a minimum you need a column that contains a unique id for each "user" (shopper, viewer, rater, person, etc) and a column for the "item" (movie, product, item, etc).

|  shopper_id |   product_id |   rating |   timestamp |
|---------:|----------:|---------:|------------:|
|        1 |        1231 |      5 |  1112586027 |
|        1 |        1411 |      3 |  1112584676 |
|        1 |        2332 |      4 |  1112684819 |
|        1 |        4132 |      2 |  1112184727 |
|        1 |        1241 |      4 |  1112484580 |
-  **Recommendation Engine Types**: In general there are two types of recommendation engines that you could create. 
    -  **Implicit**: Implicit recommendation engines are trained on interaction data between users and items without any information about rating or how much they liked an item. These engines are simple and can learn preferences by simply observing what items users are interacting with. These models just require a dataset with 2 columns (user id and item id). Any product sales ledger would have this type of data as long as user ids and item ids are consistent across all transactions. 
    -  **Explicit**: Explicit recommendation engines are slightly more complex and can be more accurate than implicit ones. They are trained on interaction data between users and items with an additional piece of information that conveys sentiment (rating, starts, thumbs-up/down, etc). These models require a dataset with a user id, item id, and a column of ratings, also referred to as a "target". Data like this is easier to extract if you have an app or site that collects interactions along with a rating (stars or thumbs).
-  **Choosing The Right Type**: By default, you can let Turi Create choose the best model for you by using the `tc.recommender.create()` method. We recommend this for all beginners in the ML world.
    -  If your data is "explicit", meaning observations include a rating given by the user, then the best model choice is a [Ranking Factorization Recommender](https://apple.github.io/turicreate/docs/api/generated/turicreate.recommender.ranking_factorization_recommender.RankingFactorizationRecommender.html).
    -  If your data is "implicit", meaning observations don't contain any rating information, then the best model choice is either an [Item Similarity Recommender](https://apple.github.io/turicreate/docs/api/generated/turicreate.recommender.item_similarity_recommender.ItemSimilarityRecommender.html) or a Ranking Factorization Recommender.
    -  A thorough explanation of the different options and trade-offs can be found [here](https://apple.github.io/turicreate/docs/userguide/recommender/choosing-a-model.html).

```python
# Explicit recommender example
model = tc.ranking_factorization_recommender.create(
    dataset=data,
    user_id='user',
    item_id='movie',
    target='rating'
)

# Implicit recommender example
model = tc.item_similarity_recommender.create(
    dataset=data,
    user_id='user',
    item_id='movie'
)
```
-  **Making Recommendations**: Once a model is created, you can make recommendations of new items for users with the `model.recommend()` method, which takes an array of user ids. The model handles new users seamlessly by defaulting to recommending popular items. Learn more about this [here](https://apple.github.io/turicreate/docs/userguide/recommender/using-trained-models.html).

## Resources
-  `recommender_data_in_turicreate.ipynb`: Gives some tips on adapting your recommendation engine to a **NEW** set of data, detailing proper formatting and any helper functions.

## Need Help?
Didn't find something you need? Confused by something? Need more guidance?

Please contact us with questions or feedback! Here are two ways:
-  [**Signup for our Slack Channel**](https://skafosai.slack.com/)
-  [**Find us on Reddit**](https://reddit.com/r/skafos)

Also check out Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/recommender/) on recommendation engine basics.