##
consortium = "jules,"
##
project = "4dhydro,"
##
website = "https://opensciencedata.4dhydro.eu/,"
##
## this needs to be edited
##
region = "Po"
##
start_date = "1990-01-01"
end_date = "1990-12-31"
file_date = start_date + " - " + end_date 
##
resolution = "0.015625 degree"





##
##
fformat = "netcdf"
##
cat = ""
##
coord = "WG584"
##

##
time_step = "daily"
##
released = "01/12/2025" ### edit this
##
polygon =  "[[[6,44],[11,44],[11,46],[6,46],[6,44]]]" ## not sure what this is
##

##
doi = "https://doi.org/10.48758/ufz.14386" ## we need to get doi
##
theme1 = "land"
theme2 = ""
theme2 = ""
##
eo = ""

header = "ID,Project,Website,Collection,Product,Short_Name,Description,Access,Notebook,Format,Category,Start,End,Region,Coordinate,Spatial Resolution,Temporal Resolution,Released,Polygon,Variables,DOI,Theme1,Theme2,Theme3,EO_Missions,Consortium,\n"

mhm_emo_et_po_0p015625deg_daily_exp10_19900101_19901231,The mesoscale Hydrologic Model - mHM 0.015625 degree evapotranspiration output (forced using EMO) for the Po region in experiment 10 between 1990-01-01 and 1990-12-31,https://minio.ufz.de/4dhydro/mHM/tier2/mhm_emo_et_po_0p015625deg_daily_exp10_19900101_19901231.nc,,NetCDF,,01/01/1990,31/12/1990,Po,WGS84,0.015625 degree,daily,21/03/2024, ,evapotranspiration,https://doi.org/10.48758/ufz.14386,land,,,,UFZ
#### loop over time and variables
years = [ 1995]

var_names = { "et,": "Evapotranspiration,", "tws,": "Total water storage,"}

file_resos = { resolution: "0p015625deg"}


##
with open("test_csv_file.csv", "w") as fid:
##
## write header
    fid.write( header)
    for id, year in enumerate( years):
        for short_name in var_names:
            product =    "The JULES model - " + resolution + " " + var_names[ short_name] + " for " + region + " (" + file_date + ") in experiement 10"
            collection = "The JULES model - " + resolution + " " + var_names[ short_name] + " for " + region + " in experiment 10,"

            access = consortium + "_" + met "_" + short_name + "_" +  region + "_" + file_resos[ resolution] + "_" + var_names[ short_name] + "_"  + "\n"

            line_to_write = str( id) + ","  + project + website + collection + short_name + var_names[ short_name] + str( year) + consortium + "\n"

            fid.write( line_to_write)
