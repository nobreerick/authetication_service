import datetime

class ControllerGeneric:
    @staticmethod
    def date_format(year: str, month: str, day: str) -> str:
        return f"{year}-{month}-{day}"

    @staticmethod 
    def phone_format(ddi: str, phone: str) -> str:
        return f'(+{ddi}){phone}'

    @staticmethod
    def validate_day(year: str, month: str, day: str) -> bool:
        MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
        MONTHS_WITH_30_DAYS = [4, 6, 9, 11]
        MONTH_WITH_28_OR_29_DAYS = 2
        if int(month) in MONTHS_WITH_31_DAYS: 
            if int(day) > 0 and int(day) <= 31: return True
            else: return False
        elif int(month) in MONTHS_WITH_30_DAYS:
            if int(day) > 0 and int(day) <= 30: return True
            else: return False
        elif int(month) == MONTH_WITH_28_OR_29_DAYS:
            if int(year) % 4 :
#               is_leap_year = False
                if int(day) > 0 and int(day) <= 28: return True
                else: return False
            else: 
#               is_leap_year = True
                if int(day) > 0 and int(day) <= 29: return True
                else: return False
        else: return False

    @staticmethod
    def validate_month(month: str) -> bool:
        if int(month) > 0 and int(month) < 13:
            return True
        else: return False

    @staticmethod
    def validate_year(year: str) -> bool:
        if int(year) > 0:
            return True
        else: return False
    
    @staticmethod
    def is_date_future(year: str, month: str, day: str) -> bool:
        actual_year = int(datetime.datetime.now().strftime("%Y"))
        actual_month = int(datetime.datetime.now().strftime("%m"))
        actual_day = int(datetime.datetime.now().strftime("%d"))
        if int(year) <= actual_year:
            if int(month) <= actual_month:
                if int(day) <= actual_day: return False
                else: return True
            else: return True
        else: return True
