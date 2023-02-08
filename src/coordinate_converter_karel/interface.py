"""User interface built on the conversion module."""
import converter


def interfacestart():
    """Start the interface with a prompt."""
    start_input = input("Enter input coordinate type (GCS/PCS).")
    if start_input == "GCS" or start_input == "gcs":
        return True
    elif start_input == "PCS" or start_input == "pcs":
        return False


def conversion():
    """Makes conversion happen."""
    value = interfacestart()
    if value:
        x = input("Enter the x-value (latitude).")
        y = input("Enter the y-value(longitude).")
        return f"The L-Est97 coordinates are: x = {converter.converter_gcs_to_pcs(x, y)[0]}, " \
               f"y = {converter.converter_gcs_to_pcs(x, y)[1]}"
    elif not value:
        x = input("Enter the x-value (latitude).")
        y = input("Enter the y-value(longitude).")
        return f"The L-Est97 coordinates are: x = {converter.converter_pcs_to_gcs(x, y)[0]}, " \
               f"y = {converter.converter_pcs_to_gcs(x, y)[1]}"


print(conversion())
