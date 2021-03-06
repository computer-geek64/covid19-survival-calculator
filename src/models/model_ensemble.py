import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from xgb_model import create_xgboost_model
from lgbm_model import create_light_gradient_boosting_model

def predict(test_data):
    # Get probabilities from XGBoost and LGBM models
    xgb_prob = create_xgboost_model(test_data)
    lgbm_prob = create_light_gradient_boosting_model(test_data)

    # Apply model weights 
    prob_avg = xgb_prob * 0.65 + lgbm_prob * 0.35
    return prob_avg

    # OUTDATED: Calculate weight of each medical condition  
    '''
    condition_weights = {
        'cardiovascular disease': 0.015,
        'diabetes': 0.073,
        'chronic respiratory disease': 0.063,
        'hypertension': 0.06,
        'cancer': 0.056,
        'none': 0.009
    }

    factor = condition_weights[condition] / condition_weights['none']
    adjusted_prob_avg = prob_avg * factor
    if adjusted_prob_avg > 100:
        return 100
    elif adjusted_prob_avg < 0:
        return 0
    return adjusted_prob_avg
    '''
