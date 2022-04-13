from flask import Flask, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session


app = Flask(__name__)

# Database configurations
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{username}:{password}@{host}:{port}/{database}".format(
                                            username="zqyqfyguvtfxuk",
                                            password="7393ce2a2d6dbd07ba5f839ab0a711fd61874ff123d5780a571d04e8ab88fea5",
                                            host="ec2-34-230-198-12.compute-1.amazonaws.com",
                                            port=5432,
                                            database="dcngkv91ei80uk"
                                        )
app.config["SECRET_KEY"] = "6435ca4c14cc707744340f1e2b4db651"
db=SQLAlchemy(app)

# Session configurations
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("name"):
        return redirect("/admin")

    if request.form.get("username") == "admin" and request.form.get("password") == "admin":
        session["name"] = "admin"
        return redirect("/admin")

    return render_template("index.html")


@app.route("/admin")
def admin():
    if not session.get("name"):
        return redirect("/")

    return render_template("admin.html")

# STRUCTURE CALC-------------------------------------------------------------------------------------------------------
@app.route("/structure_calc")
def structure_calc():
    if not session.get("name"):
        return redirect("/")

    # Structure Table
    # {product_subcategory:{product_type:{product_name:[functional_unit, gwp_per_funct_unit, recommended_shipping_method, [available_shipping_method1, available_shipping_method2, ...]]}}}
    structure_table_data=db.session.execute("SELECT * FROM Structure").fetchall()
    structure_table_data_packed={}
    for tup in structure_table_data:
        if tup[0] not in structure_table_data_packed:
            structure_table_data_packed[tup[0]]={tup[1]:{tup[2]:[tup[3], tup[4], tup[5], [tup[6]]]}}
        elif tup[1] not in structure_table_data_packed[tup[0]]:
            structure_table_data_packed[tup[0]][tup[1]]={tup[2]:[tup[3], tup[4], tup[5], [tup[6]]]}
        elif tup[2] not in structure_table_data_packed[tup[0]][tup[1]]:
            structure_table_data_packed[tup[0]][tup[1]][tup[2]]=[tup[3], tup[4], tup[5], [tup[6]]]
        else:
            structure_table_data_packed[tup[0]][tup[1]][tup[2]][3].append(tup[6])

    # MarineEmissionFactor Table.
    # {shipping_method: marine_emission_factor}
    marine_emission_factor_table_data_packed=dict(db.session.execute("SELECT * FROM MarineEmissionFactor").fetchall())

    # RoadVechicleType Table.
    # {road_vehicle_type: road_emission_factor}
    road_vehicle_type_table_data_packed=dict(db.session.execute("SELECT * FROM RoadVehicleType").fetchall())

    # CountryPort Table
    # {country:{port:average_sea_dist}}
    country_port_table_data = db.session.execute("SELECT * FROM CountryPort").fetchall()
    country_port_table_data_packed={}
    for tup in country_port_table_data:
        if tup[0] not in country_port_table_data_packed:
            country_port_table_data_packed[tup[0]]={tup[1]:tup[2]}
        else:
            country_port_table_data_packed[tup[0]][tup[1]]=tup[2]

    return render_template("structure_calc.html",
                           num_of_calc_table_rows=5,
                           structure_table_data_packed=structure_table_data_packed,
                           marine_emission_factor_table_data_packed=marine_emission_factor_table_data_packed,
                           road_vehicle_type_table_data_packed=road_vehicle_type_table_data_packed,
                           country_port_table_data_packed=country_port_table_data_packed)


# plastic CALC-------------------------------------------------------------------------------------------------------
@app.route("/plastic_calc")
def plastic_calc():
    if not session.get("name"):
        return redirect("/")

    # Structure Table
    # {product_subcategory:{product_type:{product_name:[functional_unit, gwp_per_funct_unit, recommended_shipping_method, [available_shipping_method1, available_shipping_method2, ...]]}}}
    structure_table_data=db.session.execute("SELECT * FROM Structure").fetchall()
    structure_table_data_packed={}
    for tup in structure_table_data:
        if tup[0] not in structure_table_data_packed:
            structure_table_data_packed[tup[0]]={tup[1]:{tup[2]:[tup[3], tup[4], tup[5], [tup[6]]]}}
        elif tup[1] not in structure_table_data_packed[tup[0]]:
            structure_table_data_packed[tup[0]][tup[1]]={tup[2]:[tup[3], tup[4], tup[5], [tup[6]]]}
        elif tup[2] not in structure_table_data_packed[tup[0]][tup[1]]:
            structure_table_data_packed[tup[0]][tup[1]][tup[2]]=[tup[3], tup[4], tup[5], [tup[6]]]
        else:
            structure_table_data_packed[tup[0]][tup[1]][tup[2]][3].append(tup[6])

    # MarineEmissionFactor Table.
    # {shipping_method: marine_emission_factor}
    marine_emission_factor_table_data_packed=dict(db.session.execute("SELECT * FROM MarineEmissionFactor").fetchall())

    # RoadVechicleType Table.
    # {road_vehicle_type: road_emission_factor}
    road_vehicle_type_table_data_packed=dict(db.session.execute("SELECT * FROM RoadVehicleType").fetchall())

    # CountryPort Table
    # {country:{port:average_sea_dist}}
    country_port_table_data = db.session.execute("SELECT * FROM CountryPort").fetchall()
    country_port_table_data_packed={}
    for tup in country_port_table_data:
        if tup[0] not in country_port_table_data_packed:
            country_port_table_data_packed[tup[0]]={tup[1]:tup[2]}
        else:
            country_port_table_data_packed[tup[0]][tup[1]]=tup[2]

    return render_template("plastic_calc.html",
                           num_of_calc_table_rows=5,
                           structure_table_data_packed=structure_table_data_packed,
                           marine_emission_factor_table_data_packed=marine_emission_factor_table_data_packed,
                           road_vehicle_type_table_data_packed=road_vehicle_type_table_data_packed,
                           country_port_table_data_packed=country_port_table_data_packed)

# Finishes CALC-------------------------------------------------------------------------------------------------------
@app.route("/finishes_calc")
def finishes_calc():
    if not session.get("name"):
        return redirect("/")

    # Structure Table
    # {product_subcategory:{product_type:{product_name:[functional_unit, gwp_per_funct_unit, recommended_shipping_method, [available_shipping_method1, available_shipping_method2, ...]]}}}
    structure_table_data=db.session.execute("SELECT * FROM Structure").fetchall()
    structure_table_data_packed={}
    for tup in structure_table_data:
        if tup[0] not in structure_table_data_packed:
            structure_table_data_packed[tup[0]]={tup[1]:{tup[2]:[tup[3], tup[4], tup[5], [tup[6]]]}}
        elif tup[1] not in structure_table_data_packed[tup[0]]:
            structure_table_data_packed[tup[0]][tup[1]]={tup[2]:[tup[3], tup[4], tup[5], [tup[6]]]}
        elif tup[2] not in structure_table_data_packed[tup[0]][tup[1]]:
            structure_table_data_packed[tup[0]][tup[1]][tup[2]]=[tup[3], tup[4], tup[5], [tup[6]]]
        else:
            structure_table_data_packed[tup[0]][tup[1]][tup[2]][3].append(tup[6])

    # MarineEmissionFactor Table.
    # {shipping_method: marine_emission_factor}
    marine_emission_factor_table_data_packed=dict(db.session.execute("SELECT * FROM MarineEmissionFactor").fetchall())

    # RoadVechicleType Table.
    # {road_vehicle_type: road_emission_factor}
    road_vehicle_type_table_data_packed=dict(db.session.execute("SELECT * FROM RoadVehicleType").fetchall())

    # CountryPort Table
    # {country:{port:average_sea_dist}}
    country_port_table_data = db.session.execute("SELECT * FROM CountryPort").fetchall()
    country_port_table_data_packed={}
    for tup in country_port_table_data:
        if tup[0] not in country_port_table_data_packed:
            country_port_table_data_packed[tup[0]]={tup[1]:tup[2]}
        else:
            country_port_table_data_packed[tup[0]][tup[1]]=tup[2]

    return render_template("finishes_calc.html",
                           num_of_calc_table_rows=5,
                           structure_table_data_packed=structure_table_data_packed,
                           marine_emission_factor_table_data_packed=marine_emission_factor_table_data_packed,
                           road_vehicle_type_table_data_packed=road_vehicle_type_table_data_packed,
                           country_port_table_data_packed=country_port_table_data_packed)

# STRUCTURE CALC-------------------------------------------------------------------------------------------------------
@app.route("/enclosure_calc")
def enclosure_calc():
    if not session.get("name"):
        return redirect("/")

    # Structure Table
    # {product_subcategory:{product_type:{product_name:[functional_unit, gwp_per_funct_unit, recommended_shipping_method, [available_shipping_method1, available_shipping_method2, ...]]}}}
    structure_table_data=db.session.execute("SELECT * FROM Structure").fetchall()
    structure_table_data_packed={}
    for tup in structure_table_data:
        if tup[0] not in structure_table_data_packed:
            structure_table_data_packed[tup[0]]={tup[1]:{tup[2]:[tup[3], tup[4], tup[5], [tup[6]]]}}
        elif tup[1] not in structure_table_data_packed[tup[0]]:
            structure_table_data_packed[tup[0]][tup[1]]={tup[2]:[tup[3], tup[4], tup[5], [tup[6]]]}
        elif tup[2] not in structure_table_data_packed[tup[0]][tup[1]]:
            structure_table_data_packed[tup[0]][tup[1]][tup[2]]=[tup[3], tup[4], tup[5], [tup[6]]]
        else:
            structure_table_data_packed[tup[0]][tup[1]][tup[2]][3].append(tup[6])

    # MarineEmissionFactor Table.
    # {shipping_method: marine_emission_factor}
    marine_emission_factor_table_data_packed=dict(db.session.execute("SELECT * FROM MarineEmissionFactor").fetchall())

    # RoadVechicleType Table.
    # {road_vehicle_type: road_emission_factor}
    road_vehicle_type_table_data_packed=dict(db.session.execute("SELECT * FROM RoadVehicleType").fetchall())

    # CountryPort Table
    # {country:{port:average_sea_dist}}
    country_port_table_data = db.session.execute("SELECT * FROM CountryPort").fetchall()
    country_port_table_data_packed={}
    for tup in country_port_table_data:
        if tup[0] not in country_port_table_data_packed:
            country_port_table_data_packed[tup[0]]={tup[1]:tup[2]}
        else:
            country_port_table_data_packed[tup[0]][tup[1]]=tup[2]

    return render_template("enclosure_calc.html",
                           num_of_calc_table_rows=5,
                           structure_table_data_packed=structure_table_data_packed,
                           marine_emission_factor_table_data_packed=marine_emission_factor_table_data_packed,
                           road_vehicle_type_table_data_packed=road_vehicle_type_table_data_packed,
                           country_port_table_data_packed=country_port_table_data_packed)


# Fittings CALC-------------------------------------------------------------------------------------------------------
@app.route("/fittings_calc")
def fittings_calc():
    if not session.get("name"):
        return redirect("/")

    # Structure Table
    # {product_subcategory:{product_type:{product_name:[functional_unit, gwp_per_funct_unit, recommended_shipping_method, [available_shipping_method1, available_shipping_method2, ...]]}}}
    structure_table_data=db.session.execute("SELECT * FROM Structure").fetchall()
    structure_table_data_packed={}
    for tup in structure_table_data:
        if tup[0] not in structure_table_data_packed:
            structure_table_data_packed[tup[0]]={tup[1]:{tup[2]:[tup[3], tup[4], tup[5], [tup[6]]]}}
        elif tup[1] not in structure_table_data_packed[tup[0]]:
            structure_table_data_packed[tup[0]][tup[1]]={tup[2]:[tup[3], tup[4], tup[5], [tup[6]]]}
        elif tup[2] not in structure_table_data_packed[tup[0]][tup[1]]:
            structure_table_data_packed[tup[0]][tup[1]][tup[2]]=[tup[3], tup[4], tup[5], [tup[6]]]
        else:
            structure_table_data_packed[tup[0]][tup[1]][tup[2]][3].append(tup[6])

    # MarineEmissionFactor Table.
    # {shipping_method: marine_emission_factor}
    marine_emission_factor_table_data_packed=dict(db.session.execute("SELECT * FROM MarineEmissionFactor").fetchall())

    # RoadVechicleType Table.
    # {road_vehicle_type: road_emission_factor}
    road_vehicle_type_table_data_packed=dict(db.session.execute("SELECT * FROM RoadVehicleType").fetchall())

    # CountryPort Table
    # {country:{port:average_sea_dist}}
    country_port_table_data = db.session.execute("SELECT * FROM CountryPort").fetchall()
    country_port_table_data_packed={}
    for tup in country_port_table_data:
        if tup[0] not in country_port_table_data_packed:
            country_port_table_data_packed[tup[0]]={tup[1]:tup[2]}
        else:
            country_port_table_data_packed[tup[0]][tup[1]]=tup[2]

    return render_template("fittings_calc.html",
                           num_of_calc_table_rows=5,
                           structure_table_data_packed=structure_table_data_packed,
                           marine_emission_factor_table_data_packed=marine_emission_factor_table_data_packed,
                           road_vehicle_type_table_data_packed=road_vehicle_type_table_data_packed,
                           country_port_table_data_packed=country_port_table_data_packed)


# @app.route("/plastic_calc")
# def plastic_calc():
#     if not session.get("name"):
#         return redirect("/")

#     return "<h1>Plastic Calculator</h1>"


# @app.route("/finishes_calc")
# def finishes_calc():
#     if not session.get("name"):
#         return redirect("/")

#     return "<h1>Finishes Calculator</h1>"


# @app.route("/enclosure_calc")
# def enclosure_calc():
#     if not session.get("name"):
#         return redirect("/")

#     return "<h1>Enclosure Calculator</h1>"


# @app.route("/fittings_calc")
# def fittings_calc():
#     if not session.get("name"):
#         return redirect("/")

#     return "<h1>Fittings Calculator</h1>"


# @app.route("/machinery_info_calc")
# def machinery_info_calc():
#     if not session.get("name"):
#         return redirect("/")

#     return "<h1>Machinery Information Calculator</h1>"


# @app.route("/fuel_consumption_calc")
# def fuel_consumption_calc():
#     if not session.get("name"):
#         return redirect("/")

#     return "<h1>Fuel Consumption Calculator</h1>"


if __name__ == "__main__":
    app.run(debug=True)