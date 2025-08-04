from src.data_loader import load_and_prepare_data
from src.train_model import train
from src.evaluate_model import evaluate

X, y = load_and_prepare_data(""C:\Users\neeha\Downloads\archive (4)\symbols_valid_meta.csv"", "target_column")
model, X_test, y_test = train(X, y)
evaluate(model, X_test, y_test)

def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

    y_scores = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_scores)
    auc = roc_auc_score(y_test, y_scores)

    plt.plot(fpr, tpr, label=f"AUC = {auc:.2f}", color='darkorange')
    plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.tight_layout()
    plt.show()
