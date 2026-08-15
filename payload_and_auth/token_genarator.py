import random,time


tiers = ['SEC-ADMIN',"SEC-ANALYST","SEC-AUDITOR","SEC-GUEST"]
nodes = ["cluster-alpha","cluster-beta","cluster-gamma","cluster-delta"]


def generate_session_token(username):
    tier = random.choice(tiers)
    node = random.choice(nodes)
    session_id = random.randint(1000,9999)
    token = f"{tier}:{username}:{session_id}@{node}"
    return token

def issue_token(user_list):
    for user in user_list:
        token = generate_session_token(user)
        print(f"TOKEN ISSUED: {token}")
        time.sleep(0.5)

user = ["cypher","root","dev_user","sec_ops"]

issue_token(user)