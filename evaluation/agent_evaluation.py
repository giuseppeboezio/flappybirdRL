from utils import load_series, compare_boxplot, BASE, CNN, ENTROPY

if __name__ == "__main__":

    directory = "./data"
    base = load_series(f"{directory}/{BASE}.csv")
    cnn = load_series(f"{directory}/{CNN}.csv")
    entropy = load_series(f"{directory}/{ENTROPY}.csv")

    dictionary = {BASE: base, CNN: cnn, ENTROPY: entropy}
    compare_boxplot(dictionary, save=True, path="boxplot.png")
