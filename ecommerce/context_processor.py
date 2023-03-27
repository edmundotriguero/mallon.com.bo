def total_carrito(request):
    total = 0

    try: 

        if request.user.is_authenticated:
            if "carrito" in request.session.keys():
                for key, value in request.session["carrito"].items():
                    total += int(value["acumulado"])
    except Exception as err:
        total = 0
    return {"total_carrito": total}