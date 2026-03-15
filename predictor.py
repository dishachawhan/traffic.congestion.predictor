def predict_congestion(bikes, cars, buses, trucks):

    # thresholds
    thresholds = {
        "bikes": 100,
        "cars": 80,
        "buses": 40,
        "trucks": 30
    }

    # vehicle weights (realistic traffic model)
    weights = {
        "bikes": 1,
        "cars": 2,
        "buses": 4,
        "trucks": 5
    }

    # total vehicles
    total = bikes + cars + buses + trucks

    # weighted load
    weighted_load = (
        bikes * weights["bikes"] +
        cars * weights["cars"] +
        buses * weights["buses"] +
        trucks * weights["trucks"]
    )

    # road capacity
    capacity = 250
    utilization = round((total / capacity) * 100, 2)

    # congestion score
    congestion_score = round((weighted_load / 500) * 10, 2)
    if congestion_score > 10:
        congestion_score = 10

    # congestion level
    if congestion_score < 4:
        level = "Low Traffic"
        risk = "LOW"
    elif congestion_score < 7:
        level = "Moderate Traffic"
        risk = "MEDIUM"
    else:
        level = "Heavy Traffic"
        risk = "HIGH"

    # detect main contributor
    vehicle_counts = {
        "Bikes": bikes,
        "Cars": cars,
        "Buses": buses,
        "Trucks": trucks
    }

    main_contributor = max(vehicle_counts, key=vehicle_counts.get)

    # reason detection
    reasons = []

    if bikes > thresholds["bikes"]:
        reasons.append("Bike count exceeded safe limit")

    if cars > thresholds["cars"]:
        reasons.append("Car count exceeded safe limit")

    if buses > thresholds["buses"]:
        reasons.append("Bus count exceeded safe limit")

    if trucks > thresholds["trucks"]:
        reasons.append("Truck count exceeded safe limit")

    if utilization > 80:
        reasons.append("Road capacity almost full")

    if len(reasons) == 0:
        reasons.append("Traffic within normal limits")

    # recommendations
    if risk == "HIGH":
        suggestion = "Activate alternate routes and reduce signal cycle"
    elif risk == "MEDIUM":
        suggestion = "Monitor traffic and adjust signals"
    else:
        suggestion = "Traffic flow is normal"

    # confidence score
    confidence = min(round(utilization * 0.9, 2), 100)

    return {
        "level": level,
        "risk": risk,
        "total": total,
        "utilization": utilization,
        "score": congestion_score,
        "contributor": main_contributor,
        "reasons": reasons,
        "suggestion": suggestion,
        "confidence": confidence
    }