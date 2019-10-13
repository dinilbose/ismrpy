# ismrpy

    Reads ismr and provide with panda data frame

    Installation:
        Perquisite:
            pip install numpy
            pip install pandas

        ismpy installation
            pip install ismrpy

    Usage:
        Inputs-
            filename= Name of the file
            If provided with lat and lon, program  Calculate Ionospheric pierce points and Slant TEC(Stec)
                lat= latitude of station
                lon=longitude of station
                IPP=Height of ionospheric layer in kilometers (default 350 KM)



        To read general ismr file

            import ismrpy
            data=ismrpy.read_ismr(filename=Name_of_file)

        To read specific files with header extra number of columns

            ismrpy.ismr_columns provides the column name, if there is a extra column in ismr (usually from LISN networks provides filename as extra column)
            add extra column using following command

                ismrpy.ismr_columns.append('Name of the column')

            To skip the first line of the file use skiprows=1
                data=ismrpy.read_ismr(filename=Name_of_file,skiprows=1)
