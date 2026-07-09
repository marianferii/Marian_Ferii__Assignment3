deposit_account = {
    "client_id": "C1025",
    "balance": 5000.0,
    "currency": "UAH",
    "interest_rate": 0.08,
    "is_active": True,
    "target": 9999999.0
}

fv = deposit_account["balance"]*deposit_account["interest_rate"] + deposit_account["balance"]
deposit_account["balance"] = fv
deposit_account["last_update_type"] = "Interest accrual"
deposit_account["is_active"] = False
left = deposit_account["target"] - deposit_account["balance"]
print(deposit_account)
print("-"*50)
print(f"Ваш баланс {deposit_account['balance']} грн, до вашої цілі залишилось {left} грн.")