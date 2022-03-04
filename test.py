with open("login_info.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()    
    user_id = lines[0][4:]
    group_id = lines[2]
    print(group_id)
    f.close()