TRAIN_PATH = 'Dane/train.csv'
TEST_PATH = 'Dane/test.csv'

ID_MAPPINGS_PATH = 'Dane/id_mappings.json'
SUBMISSION_FILE = 'Dane/submission.csv'

VALIDATION_SPLIT_RATIO = 0.8
VALIDATION_SAMPLE_PERCENT = 100.0

ALS_FACTORS = 15
ALS_REGULARIZATION = 0.001
ALS_ITERATIONS = 40
ALS_RANDOM_STATE = 42

K_CANDIDATES = 200

DEFAULT_COLD_START_PREDICTIONS = 'MOST_POPULAR_ITEMS_PLACEHOLDER'

SINGLE_MODEL_TRAINING = True
SKIP_VALIDATION = True
SKIP_SUBMISSION = False

# Parametry
ALS_CONFIG = [
    {
        'name': 'ALS: Najlepszy jak na razie',
        'factors': 15,
        'regularization': 0.001,
        'iterations': 40
    }
]