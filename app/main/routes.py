import flask
import json
from datetime import datetime, timedelta
from app.main import bp

@bp.route("/")
def get_capabilities():
    data = "documentation yo"
    response = json.dumps(data)
    return response

@bp.route("/traps")
def roll_trap():
    #trap_list = json.load()
    return None #flask.jsonify(trap_list)
"""
@bp.route("/encounters/<string:region>")
def get_collection_id(self, collectionId):
    if not self.current_collections_caps:
        self.get_collections()

    # TODO move to config or something
    metadata = {
        "links": [
            {
                "href": "http://data.example.org/collections/observations",
                "rel": "item",
                "type": "application/geo+json",
                "title": "Observation data"
            },
            {
                "href": "http://example.org/concepts/building.html",
                "rel": "describedBy",
                "type": "text/html",
                "title": "List of available observation types"
            }
        ],
        "instances": None,
        "name": None,
        "title": None,
        "parameters": None
    }

    dummy_instance = {
        "id": None,
        "title": None,
        "description": None,
        "dataDetails": {
            "@context": {
                "@version": [
                    1.1
                ],
                "xsd": "http://www.w3.org/2001/XMLSchema#",
                "dc": "http://purl.org/dc/terms/",
                "dcam": "http://purl.org/dc/dcam/"
            },
            "dc:accessRights": {},
            "dc:source": {
                "dc:title": None,
                "dc:identifier": "https://www.link_to_datasource_details.org"
            },
            "dc:created": "2018-01-01T20:00:15Z",
            "dc:publisher": "midge-tracer@shyftsolutions.io",
            "dcam:domainIncludes": [
                "temperature"
            ]
        },
        "links": [
            {
                "href": "http://data.example.org/collections/observations",
                "rel": "item",
                "type": "application/geo+json",
                "title": "Observation data"
            },
            {
                "href": "http://example.org/concepts/building.html",
                "rel": "describedBy",
                "type": "text/html",
                "title": "List of available observation types"
            }
        ],
        "extent": {
            "spatial": {
                "bbox": None,
                "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
            },
            "temporal": {
                "interval": None,
                "trs": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
            }
        }
    }

@bp.route("/collections/<string:collectionId>/point")
def get_point(self, collectionId):
    try:
        response_array = []
        output_format = flask.request.args.get("outputFormat", "JSON")
        valid_output_formats = ["JSON", "fizz", "buzz"] #todo: add actual valid formats to this list
        if output_format not in valid_output_formats:
            raise TypeError(f"format not supported: {output_format}")
        param_name = flask.request.args.get("parametername", "removeme") #todo error handle and remove default, also make this a list again? list()
        time_string = flask.request.args.get("time") #todo error handle
        time = time_duration_parser.parse_duration_from_time_string(time_string)
        crs = flask.request.args.get("crs", "WSG:84")
        interp_method = flask.request.args.get("interpolation")  # todo add a default
        radius_within = flask.request.args.get("within")  # todo add a default
        radius_within_units = flask.request.args.get("withinUnits")  # todo add a default
        coords = flask.request.args.get("coords", "POINT(10 10)")  # todo remove default and error handle
        points_list = self.parse_points_from_request(coords)
        test = {} #todo
        for point in points_list:
            wkt_point = wkt.loads(point)
            long = wkt_point.x
            lat = wkt_point.y
            vw_response = self.make_vw_point_request(collectionId, param_name, long, lat, time_string)
            parsed_response = self.parse_wcs_point_response(vw_response)
            response_array.append(parsed_response)
        return self.convert_array_to_json_string(response_array)
    except TypeError as type_error:
        return self.response_builder(type_error, 400)
    except ValueError as value_error:
        return self.response_builder(value_error, 400)

@bp.route("/collections/<string:collectionId>/polygon")
def get_polygon(self, collectionId):
    # args checking, TODO might wanna not have defaults here and do some error checking
    output_format = flask.request.args.get("outputFormat", "JSON")
    param_name = flask.request.args.get("parametername", 'Temperature')
    time_string = flask.request.args.get("time", "2020-03-02T12:00:00Z")
    crs = flask.request.args.get("crs", "CRS:84")
    coords = flask.request.args.get("coords",
                                    "POLYGON((-6.1 50.3,-4.35 51.4,-2.6 51.6,-2.8 50.6,-5.3 49.9,-6.1 50.3))")
    interp_method_x = flask.request.args.get("interpolationX", "R15/linear")
    interp_method_y = flask.request.args.get("interpolationy", "R15/linear")
    z_level = flask.request.args.get("z", "850")

    time_string = time_duration_parser.parse_from_time_string(time_string)
    coords_string = self.parse_coords_from_polygon_request(crs, coords)

    # TODO need to figure out how this fancy new interpolation stuff works wrt WCS
    x_linspace_nodes, x_interp_method = self.parse_edr_interpolation_string(interp_method_x)
    y_linspace_nodes, y_interp_method = self.parse_edr_interpolation_string(interp_method_y)

    vw_response = self.make_polygon_coverage_request(collectionId, coords_string, param_name, output_format,
                                                        time_string, z_level)
    parsed_response = self.parse_vw_polygon_response(vw_response)
    return app.response_class(
        response=json.dumps(parsed_response),
        status=200,
        mimetype='application/json'
    )
"""
