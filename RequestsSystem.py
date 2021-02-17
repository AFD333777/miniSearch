import requests


class RequestsSystem:
    def getMap(self, coords: list, scale: str, viewMap="map", mark=""):
        url = "http://static-maps.yandex.ru/1.x/"
        params = {
            "ll": ",".join(coords),
            "l": viewMap,
            "z": scale,
            "size": "500,450",
        }
        if mark != "":
            params["pt"] = ",".join(coords) + ",pmwtm"
        # mapRequest = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map"
        response = requests.get(url, params=params)
        return response
