import storage
from datetime import datetime

def generate_id():
    try:
        tem_list = storage.load_data()
    except:
        return 1
    for x in range(len(tem_list)):
        new_id = tem_list[x]["id"]
    new_id += 1
    return new_id

def validate_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj

def calculate_balance():
    total_expense = total_income = 0
    try:
        tem_list = storage.load_data()
    except:
        return ("File is empty yet")
    for x in range(len(tem_list)):
        if(tem_list[x]["type"]=="expense"):
            total_expense += int(tem_list[x]["amount"])
        else:
            total_income += int(tem_list[x]["amount"])
    balance_total = total_income - total_expense
    return balance_total

def filter_by_category(category):
    trans_list = []
    try:
        tem_list = storage.load_data()
    except:
        return ("File is empty yet")
    for x in range(len(tem_list)):
        if(category == tem_list[x]["category"]):
            trans_list.append(tem_list[x])
        else:
            print("No Category Found")
    return trans_list


def monthly_summary(month):
    try:
        date_obj = datetime.strptime(month.strip(), "%Y-%m")
        try:
            tem_list = storage.load_data()
        except:
            return ("File is empty yet")
        total_income = total_expense = 0
        for item in tem_list:
            t_date = datetime.strptime(item["date"], "%Y-%m-%d")
            if t_date.year == date_obj.year and t_date.month == date_obj.month:
                if item["type"] == "expense":
                    total_expense += int(item["amount"])
                else:
                    total_income += int(item["amount"])
        balance_total = total_income - total_expense
        return balance_total, total_income, total_expense
    except Exception as e:
        return e
    
def delete_transaction(user_id):
    try:
        try:
            data = storage.load_data()
        except:
            return ("File is empty yet")
        item_to_delete = next(item for item in data if item["id"] == int(user_id))
        data.remove(item_to_delete)
        storage.save_updated_data(data)
        return "ID deleted successfully"
    except StopIteration:
        return "ID not found"
    except Exception as e:
        return f"Error: {e}"
