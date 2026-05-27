from enum import Enum

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
class YesNo(Enum):
    YES = "Yes"
    NO = "No"
class InternetService(Enum):
    DSL = "DSL"
    FIBER_OPTIC = "Fiber optic"
    NO = "No"
class ContractType(Enum):
    MONTH_TO_MONTH = "Month-to-month"
    ONE_YEAR = "One year"
    TWO_YEAR = "Two year"
class PaymentMethod(Enum):
    ELECTRONIC_CHECK = "Electronic check"
    MAILED_CHECK = "Mailed check"
    BANK_TRANSFER = "Bank transfer (automatic)"
    CREDIT_CARD = "Credit card (automatic)"
class ZeroOne(Enum):
    ZERO = 0    
    ONE = 1