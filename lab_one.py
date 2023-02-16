from prefect import flow, task
import httpx

#lab 101

@flow
def get_stats(lat, lon):
    temperature = get_temperature_stats(lat, lon)
    rain = get_rain_stats(lat, lon)
    cape = get_cape_stats(lat, lon)
    print(f"hourly temp is: {temperature}")
    print(f"hourly rainfall is: {rain}")
    print(f"whatever metric cape is: {cape}")


@task
def get_rain_stats(lat, lon):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = httpx.get(base_url,
                params = dict(latitude=lat, longitude=lon, hourly="rain"),
                )
    most_recent_rain = float(weather.json()["hourly"]["rain"][0])
    return most_recent_rain

@task
def get_cape_stats(lat, lon):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = httpx.get(base_url,
                params = dict(latitude=lat, longitude=lon, hourly="cape"),
                )
    most_recent_cape = float(weather.json()["hourly"]["cape"][0])
    return most_recent_cape

@task
def get_temperature_stats(lat, lon):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = httpx.get(base_url,
                params = dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
                )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    return most_recent_temp


if __name__ == "__main__":
    get_stats(20, 10)
