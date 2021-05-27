# -*- coding: utf-8 -*-
#
#   Copyright (C) 2012 -2021  Christian Ledermann
#
#   This library is free software; you can redistribute it and/or
#   modify it under the terms of the GNU Lesser General Public
#   License as published by the Free Software Foundation; either
#   version 2.1 of the License, or (at your option) any later version.

#   This library is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.

#   You should have received a copy of the GNU Lesser General Public License
#   along with this library; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
"""Types for geometries."""
from typing import Any
from typing import Dict
from typing import Sequence
from typing import Tuple
from typing import Union

from typing_extensions import Protocol
from typing_extensions import TypedDict

Point2D = Tuple[float, float]
Point3D = Tuple[float, float, float]
PointType = Union[Point2D, Point3D]
LineType = Sequence[PointType]
PolygonType = Union[
    Tuple[LineType, Sequence[LineType]],
    Tuple[LineType],
]
MultiGeometryType = Sequence[Union[PointType, LineType, PolygonType]]
Bounds = Tuple[float, float, float, float]

CoordinatesType = Union[
    PointType,
    LineType,
    Sequence[LineType],
]
MultiCoordinatesType = Sequence[CoordinatesType]

GeoInterface = TypedDict(
    "GeoInterface",
    {
        "type": str,
        "coordinates": Union[CoordinatesType, MultiCoordinatesType],
        "bbox": Bounds,
    },
    total=False,  # bbox is optional
)

GeoCollectionInterface = TypedDict(
    "GeoCollectionInterface",
    {"type": str, "geometries": Sequence[GeoInterface]},
)

GeoFeatureInterface = TypedDict(
    "GeoFeatureInterface",
    {
        "type": str,
        "geometry": GeoInterface,
        "bbox": Bounds,
        "properties": Dict[str, Any],
        "id": Union[str, int],
    },
    total=False,  # bbox, propertis and id are optional
)

GeoFeatureCollectionInterface = TypedDict(
    "GeoFeatureCollectionInterface",
    {
        "type": str,
        "bbox": Bounds,
        "features": Sequence[GeoFeatureInterface],
        "id": Union[str, int],
    },
    total=False,  # bbox and id are optional
)


class GeoType(Protocol):
    """Any compatible type that implements the __geo_interface__."""

    __geo_interface__: GeoInterface
