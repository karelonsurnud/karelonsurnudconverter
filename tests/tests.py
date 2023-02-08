from coordinate_converter_karel import converter


def test_converter_gcs_to_pcs():
    x, y = converter.converter_gcs_to_pcs(58.434387, 23.996824)
    assert x == 6477115.89, y == 499814.46
    x, y = converter.converter_gcs_to_pcs(58.830356, 24.102068)
    assert x == 6521223.97, y == 505894.83


def test_converter_pcs_to_gcs():
    x, y = converter.converter_pcs_to_gcs(6477115.89, 499814.46)
    assert x == 58.434387, y == 23.996824
    x, y = converter.converter_pcs_to_gcs(6557929.70, 584614.49)
    assert x == 59.151549, y == 25.478859
