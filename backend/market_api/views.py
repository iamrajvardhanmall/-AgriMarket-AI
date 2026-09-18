from datetime import date, timedelta

from rest_framework.decorators import api_view
from rest_framework.response import Response


MARKETS = [
    {"id": "nashik", "name": "Nashik APMC", "district": "Nashik", "price": 2850, "trend": 6.8, "arrival": 4210, "distance": 18, "demand": "High", "confidence": 82},
    {"id": "lasalgaon", "name": "Lasalgaon Market", "district": "Nashik", "price": 2920, "trend": 4.2, "arrival": 3650, "distance": 34, "demand": "High", "confidence": 78},
    {"id": "pimpalgaon", "name": "Pimpalgaon Baswant", "district": "Nashik", "price": 2760, "trend": 8.9, "arrival": 2980, "distance": 42, "demand": "Medium", "confidence": 74},
    {"id": "manmad", "name": "Manmad Yard", "district": "Nashik", "price": 2680, "trend": 2.1, "arrival": 5120, "distance": 61, "demand": "Medium", "confidence": 69},
]


@api_view(["GET"])
def health(request):
    return Response({"status": "ok", "service": "agrimarket-api"})


@api_view(["GET"])
def markets(request):
    commodity = request.query_params.get("commodity", "Tomato")
    return Response({"commodity": commodity, "observed_on": str(date.today()), "markets": MARKETS})


@api_view(["POST"])
def recommendations(request):
    quantity_kg = max(float(request.data.get("quantity_kg", 5000)), 1)
    transport_rate = float(request.data.get("transport_rate", 38))
    storage_days = float(request.data.get("storage_days", 0))
    storage_rate = float(request.data.get("storage_rate", 4.5))
    options = []
    for market in MARKETS:
        transport = market["distance"] * transport_rate
        storage = storage_days * storage_rate * quantity_kg
        revenue = market["price"] * quantity_kg / 100
        net = revenue - transport * quantity_kg / 100 - storage
        options.append({**market, "transport_cost": round(transport * quantity_kg / 100), "storage_cost": round(storage), "net_realization": round(net)})
    best = max(options, key=lambda option: option["net_realization"])
    return Response({
        "recommendation": {"market": best["name"], "window": "22-24 September", "confidence": best["confidence"], "reason": "Best expected net realization after transport and storage."},
        "options": sorted(options, key=lambda option: option["net_realization"], reverse=True),
    })


@api_view(["GET", "POST"])
def lots(request):
    if request.method == "POST":
        payload = request.data.copy()
        payload.update({"id": "AGRI-10427", "status": "OPEN", "created_at": str(date.today())})
        return Response(payload, status=201)
    return Response({"lots": [{"id": "AGRI-10245", "commodity": "Tomato", "quantity_kg": 5000, "quality": "Grade A", "asking_price": 2800, "offers": 3, "status": "OPEN"}]})


@api_view(["GET"])
def buyers(request):
    return Response({"buyers": [{"name": "FreshKart Foods", "match": 94, "verified": True, "demand": "8-12 tonnes", "location": "Pune"}, {"name": "Sahyadri Processors", "match": 87, "verified": True, "demand": "5-8 tonnes", "location": "Nashik"}]})


@api_view(["GET"])
def offers(request):
    return Response({"offers": [{"buyer": "FreshKart Foods", "price": 2975, "lot": "AGRI-10245", "status": "PENDING"}, {"buyer": "Sahyadri Processors", "price": 2920, "lot": "AGRI-10245", "status": "PENDING"}]})
