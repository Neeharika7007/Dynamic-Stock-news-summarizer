from stock_market import app  # Or from stock_market.app import plot_roc
from evaluation.metrics import plot_roc_auc
plot_roc_auc(y_test, y_probs)

