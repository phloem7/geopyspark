"""Constants that are used by ``geopyspark.geotrellis`` classes, methods, and functions."""
from enum import Enum


__all__ = ['LayerType', 'LayoutScheme', 'NO_DATA_INT']


"""The NoData value for ints in GeoTrellis."""
NO_DATA_INT = -2147483648


class LayerType(Enum):
    """The type of the key within the tuple of the wrapped RDD."""

    """
    Indicates that the RDD contains ``(K, V)`` pairs, where the ``K`` has a spatial attribute,
    but no time value. Both :class:`~geopyspark.geotrellis.ProjectedExtent` and
    :class:`~geopyspark.geotrellis.SpatialKey` are examples of this type of ``K``.
    """
    SPATIAL = 'spatial'

    """
    Indicates that the RDD contains ``(K, V)`` pairs, where the ``K`` has a spatial and
    time attribute. Both :class:`~geopyspark.geotrellis.TemporalProjectedExtent`
    and :class:`~geopyspark.geotrellis.SpaceTimeKey` are examples of this type of ``K``.
    """
    SPACETIME = 'spacetime'


class LayoutScheme(Enum):
    """How the tiles within a Layer should be laid out."""

    """Layout scheme to match resolution of the closest level of TMS pyramid."""
    ZOOM = 'zoom'

    """Layout scheme to match resolution of source rasters."""
    FLOAT = 'float'


class IndexingMethod(Enum):
    """How the wrapped should be indexed when saved."""

    """A key indexing method. Works for RDD that contain both :class:`~geopyspark.geotrellis.SpatialKey`
    and :class:`~geopyspark.geotrellis.SpaceTimeKey`.
    """
    ZORDER = 'zorder'

    """
    A key indexing method. Works for RDDs that contain both :class:`~geopyspark.geotrellis.SpatialKey`
    and :class:`~geopyspark.geotrellis.SpaceTimeKey`. Note, indexes are determined by the ``x``,
    ``y``, and if ``SPACETIME``, the temporal resolutions of a point. This is expressed in bits, and
    has a max value of 62. Thus if the sum of those resolutions are greater than 62,
    then the indexing will fail.
    """
    HILBERT = 'hilbert'

    """A key indexing method. Works only for RDDs that contain :class:`~geopyspark.geotrellis.SpatialKey`.
    This method provides the fastest lookup of all the key indexing method, however, it does not give
    good locality guarantees. It is recommended then that this method should only be used when locality
    is not important for your analysis.
    """
    ROWMAJOR = 'rowmajor'


class ResampleMethod(Enum):
    """Resampling Methods."""

    NEAREST_NEIGHBOR = 'NearestNeighbor'
    BILINEAR = 'Bilinear'
    CUBIC_CONVOLUTION = 'CubicConvolution'
    CUBIC_SPLINE = 'CubicSpline'
    LANCZOS = 'Lanczos'
    AVERAGE = 'Average'
    MODE = 'Mode'
    MEDIAN = 'Median'
    MAX = 'Max'
    MIN = 'Min'


class TimeUnit(Enum):
    """ZORDER time units."""

    MILLIS = 'millis'
    SECONDS = 'seconds'
    MINUTES = 'minutes'
    HOURS = 'hours'
    DAYS = 'days'
    MONTHS = 'months'
    YEARS = 'years'


class Operation(Enum):
    """Focal opertions."""

    SUM = 'Sum'
    MEAN = 'Mean'
    MODE = 'Mode'
    MEDIAN = 'Median'
    MAX = 'Max'
    MIN = 'Min'
    ASPECT = 'Aspect'
    SLOPE = 'Slope'
    STANDARD_DEVIATION = 'StandardDeviation'


class Neighborhood(Enum):
    """Neighborhood types."""

    ANNULUS = 'Annulus'
    NESW = 'Nesw'
    SQUARE = 'Square'
    WEDGE = 'Wedge'
    CIRCLE = "Circle"


class ClassificationStrategy(Enum):
    """Classification strategies for color mapping."""

    GREATERTHAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL_TO = "GreaterThanOrEqualTo"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL_TO = "LessThanOrEqualTo"
    EXACT = "Exact"


class CellType(Enum):
    """Cell types."""

    BOOLRAW = "boolraw"
    INT8RAW = "int8raw"
    UINT8RAW = "uint8raw"
    INT16RAW = "int16raw"
    UINT16RAW = "uint16raw"
    INT32RAW = "int32raw"
    FLOAT32RAW = "float32raw"
    FLOAT64RAW = "float64raw"
    BOOL = "bool"
    INT8 = "int8"
    UINT8 = "uint8"
    INT16 = "int16"
    UINT16 = "uint16"
    INT32 = "int32"
    FLOAT32 = "float32"
    FLOAT64 = "float64"


class ColorRamp(Enum):
    """ColorRamp names."""

    Hot = "Hot"
    COOLWARM = "CoolWarm"
    MAGMA = "Magma"
    INFERNO = "Inferno"
    PLASMA = "Plasma"
    VIRIDIS = "Viridis"
    BLUE_TO_ORANGE = "BlueToOrange"
    LIGHT_YELLOW_TO_ORANGE = "LightYellowToOrange"
    BLUE_TO_RED = "BlueToRed"
    GREEN_TO_RED_ORANGE = "GreenToRedOrange"
    LIGHT_TO_DARK_SUNSET = "LightToDarkSunset"
    LIGHT_TO_DARK_GREEN = "LightToDarkGreen"
    HEATMAP_YELLOW_TO_RED = "HeatmapYellowToRed"
    HEATMAP_BLUE_TO_YELLOW_TO_RED_SPECTRUM = "HeatmapBlueToYellowToRedSpectrum"
    HEATMAP_DARK_RED_TO_YELLOW_WHITE = "HeatmapDarkRedToYellowWhite"
    HEATMAP_LIGHT_PURPLE_TO_DARK_PURPLE_TO_WHITE = "HeatmapLightPurpleToDarkPurpleToWhite"
    CLASSIFICATION_BOLD_LAND_USE = "ClassificationBoldLandUse"
    CLASSIFICATION_MUTED_TERRAIN = "ClassificationMutedTerrain"
