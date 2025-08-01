def analyze_users(users):
    risks = []
    for user in users:
        risk_flags = []
        if user["lastSignIn"] > 360:
            risk_flags.append("Stale login")
        if user["admin"]:
            risk_flags.append("Admin account")

        if risk_flags:
            risks.append({
                "name": user["name"],
                "risks": ", ".join(risk_flags)
            })
    return risks
