def setOp():
    admins = set()
    users = {"Smile", "Tony", "Happy", "Sherry", "Allen", "Andy", "Mars"}
    admins.add("ihc")
    admins.add("Mars")

    print("admins", admins)
    print("users", users)

    print("&", admins & users)
    print("|", admins | users)
    print("^", admins ^ users)
    print("admins - users", admins - users)
    print("users - admins", users - admins)


setOp()
