"""A WGS84/L-EST97 to L-EST97/WGS84 converter."""

from pyproj import Transformer


def converter_gcs_to_pcs(latitude_x, latitude_y):
    """
    Converts the GCS WGS84 coordinates to PCS L-est97.

    latitude_x = GCS WGS84 X coordinate.
    latitude_y = GCS WGS84 Y coordinate.
    """
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:3301")
    lat_x, lat_y = transformer.transform(latitude_x, latitude_y)
    lat_x = round(lat_x, 2)
    lat_y = round(lat_y, 2)
    return lat_x, lat_y


def converter_pcs_to_gcs(latitude_x, latitude_y):
    """
    Converts the PCS L-est97 coordinates to GCS WGS84.

    latitude_x = PCS L-est97 X coordinate.
    latitude_y = PCS L-est97 Y coordinate.
    """
    transformer = Transformer.from_crs("EPSG:3301", "EPSG:4326")
    lat_x, lat_y = transformer.transform(latitude_x, latitude_y)
    lat_x = round(lat_x, 6)
    lat_y = round(lat_y, 6)
    return lat_x, lat_y
