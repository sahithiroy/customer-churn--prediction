from pydantic import BaseModel
from api.enums import Gender, YesNo, InternetService, ContractType, PaymentMethod, ZeroOne
'''
Schema for customer data
Data columns (total 21 columns):
 #   Column            Non-Null Count   Dtype  
---  ------            --------------   -----  
 0   id                594194 non-null  int64  
 1   gender            594194 non-null  object 
 2   SeniorCitizen     594194 non-null  int64  
 3   Partner           594194 non-null  object 
 4   Dependents        594194 non-null  object 
 5   tenure            594194 non-null  int64  
 6   PhoneService      594194 non-null  object 
 7   MultipleLines     594194 non-null  object 
 8   InternetService   594194 non-null  object 
 9   OnlineSecurity    594194 non-null  object 
 10  OnlineBackup      594194 non-null  object 
 11  DeviceProtection  594194 non-null  object 
 12  TechSupport       594194 non-null  object 
 13  StreamingTV       594194 non-null  object 
 14  StreamingMovies   594194 non-null  object 
 15  Contract          594194 non-null  object 
 16  PaperlessBilling  594194 non-null  object 
 17  PaymentMethod     594194 non-null  object 
 18  MonthlyCharges    594194 non-null  float64
 19  TotalCharges      594194 non-null  float64
 20  Churn             594194 non-null  object 
'''

class CustomerData(BaseModel):
    id: int
    gender: Gender
    senior_citizen: ZeroOne
    partner: YesNo
    dependents: YesNo
    tenure: int
    phone_service: YesNo
    multiple_lines: YesNo
    internet_service: InternetService
    online_security: YesNo
    online_backup: YesNo
    device_protection: YesNo
    tech_support: YesNo
    streaming_tv: YesNo
    streaming_movies: YesNo
    contract_type: ContractType
    payment_method: PaymentMethod
    monthly_charges: float
    total_charges: float


class PredictionResponse(BaseModel):
    id: int
    prediction: int
    churn_probability: float