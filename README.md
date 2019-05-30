# **Turi Recommender**

**DEPRECATION WARNING**

This code example was intended for use by the legacy Skafos platform and is no longer being maintained. On 05/29/2019, a new version of [Skafos](https://skafos.ai) was released, streamlining model delivery to the edge.

[Sign-up](https://dashboard.skafos.ai/sign-up) for an account, [join](https://join.slack.com/t/metismachine-skafos/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI) our Slack community, and explore some [example models](https://github.com/skafos/colab-example-models) to get started.

---

The following repo contains code for training a recommendation engine model on Skafos using the [Turi Create framework](https://apple.github.io/turicreate/docs/userguide/recommender/). The example model is based on movie ratings, and given a user (new or existing), will recommend

## What is here?
The components of this repo are:
-  `recommender.ipynb` - a Python notebook that trains and saves a recommendation engine model to use in your app. Start here.
-  `utilities/` - a directory that contains helper functions used by `recommender.ipynb`.
-  `advanced_usage/` - a directory that contains additional information about this recommendation engine model, how to incorporate your own data, advanced usage, and additional example models.
-  `requirements.txt` - a file describing all required Python dependencies.

## About the model
-  The recommender is trained on the [MovieLens 20M Dataset](https://grouplens.org/datasets/movielens/20m/), which we have placed in a public S3 bucket for convenience.
-  Once trained, you can give the model a "user id", and it will list movie suggestions from best recommendation to least.

## Going beyond the example
-  If you wish to incorporate your own data (*which you should*) or try another type of recommendation engine model, check out the `advanced_usage/` section.
- Turi Create has built-in model evaluation and prediction techniques. We use some of the functions in the `advanced_usage/` section, but for a more detailed description, refer to Turi Create's [documentation](https://apple.github.io/turicreate/docs/api/turicreate.toolkits.evaluation.html).

## Need Help?
Please contact us with questions or feedback! Here are two ways:


-  [**Signup for our Slack Channel**](https://join.slack.com/t/metismachine-skafos/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI)
-  [**Find us on Reddit**](https://reddit.com/r/skafos) 

Also check out Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/recommender/) on recommendation engine basics.
