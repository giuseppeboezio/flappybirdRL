from evaluation.base_evaluation import evaluate_agent
from constants import ENTROPY

if __name__ == "__main__":

    evaluate_agent(ENTROPY, num_games=10)
