def generate_review(
    score: int,
    citations: int,
    pages: int,
    fillers: list,
):

    strengths = []
    weaknesses = []
    warnings = []

    # Score analysis
    if score >= 85:
        strengths.append(
            "Strong overall research integrity."
        )

    elif score >= 70:
        strengths.append(
            "Acceptable academic quality."
        )

    else:
        weaknesses.append(
            "Low research integrity score."
        )

    # Citations
    if citations >= 20:
        strengths.append(
            "Well-supported with references."
        )

    else:
        weaknesses.append(
            "Limited citation support."
        )

    # Pages
    if pages < 5:
        warnings.append(
            "Paper is unusually short."
        )

    # Fillers
    if fillers:

        warnings.append(
            f"{len(fillers)} filler phrases detected."
        )

        weaknesses.append(
            "Contains generic academic language."
        )

    # Recommendation
    if score >= 85:
        recommendation = "ACCEPT"

    elif score >= 70:
        recommendation = "MINOR REVISION"

    elif score >= 50:
        recommendation = "MAJOR REVISION"

    else:
        recommendation = "REJECT"

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "warnings": warnings,
        "recommendation": recommendation,
    }