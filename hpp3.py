from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor



datapath="Data/DataSet.xlsx"
df=pd.read_excel(datapath, sheet_name="FF")

heatmap_col=["LA_N","RA_N","BY_N","FLOOR","BEDROOM","BATHROOM","FACING_N","PRICE_N"]
df1=df[heatmap_col]
cormatrix=df[heatmap_col].corr()

plt.figure(figsize=(8,6))
plt.title("Correlation Heatmap")
sns.heatmap(cormatrix, annot=True, cmap='coolwarm', fmt='.2f', annot_kws={"size": 10})


X=df1.drop("PRICE_N",axis=1)
Y=df1["PRICE_N"]

X_train,X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

#lower MSE,MAE and higher R2 indicate better model performance
def LRegr_Model():
    model=LinearRegression()
    model.fit(X_train,Y_train)

    y_pred=model.predict(X_test)

    mse=mean_squared_error(Y_test, y_pred)
    mae=mean_absolute_error(Y_test, y_pred)
    r2=r2_score(Y_test,y_pred)
    
    #print("Linear Regression Model:")
    #print(f"Mean Squared Error (MSE): {mse}")
    #print(f"Mean Absolute Error (MAE): {mae}")
    print(f"LRM,R-squared (R2): {r2}")

def xgboost():
    model = xgb.XGBRegressor(objective ='reg:squarederror', random_state=42)
    model.fit(X_train, Y_train)

    # Predicting on the test set
    y_pred = model.predict(X_test)

    # Evaluating the model
    mse = mean_squared_error(Y_test, y_pred)
    mae = mean_absolute_error(Y_test, y_pred)
    r2 = r2_score(Y_test, y_pred)

    #print("XGBoost")
    #print(f"Mean Squared Error (MSE): {mse}")
    #print(f"Mean Absolute Error (MAE): {mae}")
    print(f"XGBoost R-squared (R2): {r2}")

def rfr():
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)  # You can adjust hyperparameters here
    rf_model.fit(X_train, Y_train)

    # Predicting on the test set
    y_pred = rf_model.predict(X_test)

    # Evaluating the model
    mse = mean_squared_error(Y_test, y_pred)
    mae = mean_absolute_error(Y_test, y_pred)
    r2 = r2_score(Y_test, y_pred)

    #print(f"Mean Squared Error (MSE): {mse}")
    #print(f"Mean Absolute Error (MAE): {mae}")
    feature_imp=rf_model.feature_importances_
    #print(feature_imp)
    print(f"RFR R-squared (R2): {r2}")

def gbr():
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, Y_train)

    # Predicting on the test set
    y_pred = model.predict(X_test)

    # Evaluating the model
    mse = mean_squared_error(Y_test, y_pred)
    mae = mean_absolute_error(Y_test, y_pred)
    r2 = r2_score(Y_test, y_pred)

    #print(f"Mean Squared Error (MSE): {mse}")
    #print(f"Mean Absolute Error (MAE): {mae}")
    feature_imp=model.feature_importances_
    print(df[heatmap_col].columns)
    print(feature_imp)
    print(f"GBR R-squared (R2): {r2}")


#LRegr_Model()
#xgboost()
#rfr()
#gbr()#most accurate so far
