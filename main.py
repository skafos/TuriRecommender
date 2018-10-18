import turicreate as tc

actions = tc.SFrame.read_csv('https://s3.amazonaws.com/skafos.example.data/MovieLensDataset/ml-20m/ratings.csv')

items = tc.SFrame.read_csv('https://s3.amazonaws.com/skafos.example.data/MovieLensDataset/ml-20m/movies.csv')

training_data, validation_data = tc.recommender.util.random_split_by_user(actions, 'userId', 'movieId')

model = tc.recommender.create(training_data, 'userId', 'movieId')

results = model.recommend()

validation_data.print_rows(num_rows=30)

model.evaluate(validation_data)

