# Raymond Ogunjimi
# Applied Machine Learning - HW 1

import pandas as pd
import numpy as np

def MAE(actual_data, predicted_data):
    return (predicted_data - actual_data).abs().mean()

def MAPE(actual_data, predicted_data):
    return ((predicted_data - actual_data)/actual_data).abs().mean()

def MSE(actual_data, predicted_data):
    return (predicted_data - actual_data).pow(2).mean()

def RMSE(actual_data, predicted_data):
    return np.sqrt((predicted_data - actual_data).pow(2).mean())

def main():
    # Data:
    rtng_actl = pd.Series([4.5, 4.7, 4.3, 4.5, 3.9, 4.8, 4.7, 4.1])
    rtng_prdctn_1 = pd.Series([4.7, 4.3, 4.6, 4.9, 3.9, 4.1, 4.2, 4.4])
    rtng_prdctn_2 = pd.Series([3.9, 4.5, 4.4, 4.2, 4.7, 4.2, 4.3, 4.4])

    # 1.
    # Based on the results from the code below, MODEL 1 is better than MODEL 2 becaues it consistently has lower error scores.
    print("MODEL 1:")
    print("MAE: %.3f" %MAE(rtng_actl, rtng_prdctn_1))
    print("MAPE: %.3f" %MAPE(rtng_actl, rtng_prdctn_1))
    print("MSE: %.3f" %MSE(rtng_actl, rtng_prdctn_1))
    print("RMSE: %.3f\n" %RMSE(rtng_actl, rtng_prdctn_1))

    print("MODEL 2:")
    print("MAE: %.3f" %MAE(rtng_actl, rtng_prdctn_2))
    print("MAPE: %.3f" %MAPE(rtng_actl, rtng_prdctn_2))
    print("MSE: %.3f" %MSE(rtng_actl, rtng_prdctn_2))
    print("RMSE: %.3f\n" %RMSE(rtng_actl, rtng_prdctn_2))

    # 2.
    # No, a smaller MAE does not necessarily indicate a smaller MAPE.
    # In the example below the MAE of MODEL 1 is smaller than MDOEL 2 however the MAPE of MODEL 1 is larger than MODEL 2.

    tst_actl = pd.Series([10, 100])
    tst_prdctn_1 = pd.Series([11, 101])
    tst_prdctn_2 = pd.Series([10.1, 102])

    print("MODEL 1:")
    print("MAE: %.3f" %MAE(tst_actl, tst_prdctn_1))
    print("MAPE: %.3f\n" %MAPE(tst_actl, tst_prdctn_1))

    print("MODEL 2:")
    print("MAE: %.3f" %MAE(tst_actl, tst_prdctn_2))
    print("MAPE: %.3f\n" %MAPE(tst_actl, tst_prdctn_2))

if __name__ == '__main__':
    main()