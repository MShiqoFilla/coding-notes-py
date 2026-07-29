from sqlalchemy import create_engine, URL, Engine
from shapely.geometry import Point
import geopandas as gpd
from dotenv import load_dotenv
import os

load_dotenv()

def _create_engine(
        user:str, password:str, dbname:str, host:str, port:int=5432
) -> Engine:
    return create_engine(
        url=URL.create(drivername="postgresql+psycopg2", username=user, password=password, host=host, port=port, database=dbname),
        pool_size=10,
        max_overflow=5,
        pool_timeout=5,
        pool_recycle=1800,
    )

def example_directly_using_geopandas():
    data = {
        "id": [1, 2, 3],
        "name": ["Jakarta", "Bandung", "Surabaya"],
        "population": [11000000, 2500000, 2800000],
        "geometry" : [
            Point(106.8456, -6.2088),   # Jakarta
            Point(107.6191, -6.9175),   # Bandung
            Point(112.7521, -7.2575)    # Surabaya
        ]
    }

    gdf = gpd.GeoDataFrame(data, crs="EPSG:4326")

    local_engine = _create_engine(
        user=os.getenv("PG_USER"), password=os.getenv("PG_PASS"), dbname=os.getenv("PG_DBNM"), host=os.getenv("PG_HOST"), port=os.getenv("PG_PORT")
    )
    gdf.to_postgis(name="example_postgis_table", con=local_engine, if_exists="replace", index=False)