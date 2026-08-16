user_database = {
    "admin_root": {"role": "Administrator", "mfa_enabled": True, "failed_attempts": 0},
    "dev_cypher": {"role": "Developer", "mfa_enabled": False, "failed_attempts": 2},
    "guest_user": {"role": "Guest", "mfa_enabled": False, "failed_attempts": 5},
    "auditor_sec": {"role": "Security Analyst", "mfa_enabled": True, "failed_attempts": 1}
}


def audit_users(user_dict):
    for username ,info in user_dict.items():
        role = info["role"]
        mfa = info["mfa_enabled"]

        if info["role"]== "Administrator" and info['mfa_enabled'] == False:
           print("Critical risk!: Account has MFA disabled")
        elif info["role"] == "Administrator" and info['mfa_enabled'] == True:
           print(f"SECURE : Admin account '{username}' has MFA enabled" )
        else:
            
            print(f":Username '{username}' {role} : {mfa}")
            



def enforce_lockout(user_dict,max_failures):
    print("\n=======ENFORCING LOCKOUT POLICY=======\n")
    for username,info in user_dict.items():
      if info['failed_attempts'] >= max_failures:
        info["locked"] = True
        print(f"ACCOUNT LOCKED: '{username}' exceeded {max_failures}")
    return user_dict

audit_users(user_database)
enforce_lockout(user_database, 3)