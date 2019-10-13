# ismrpy

Reads ismr and provide with panda data frame

## Getting Started
### Prerequisites

Things needed before installation of package
```
pip install numpy
pip install pandas
```

### Installing

```
pip install ismrpy
```


## Usage
Inputs-

    filename= Name of the file
If provided with lat and lon, program  Calculate Ionospheric pierce points and Slant TEC(Stec)

    lat= latitude of station
    lon=longitude of station
    IPP=Height of ionospheric layer in kilometers (default 350 KM)

To read general ismr file
    
    '''
    import ismrpy
    data=ismrpy.read_ismr(filename=Name_of_file)
    '''
To read specific files with header extra number of columns

ismrpy.ismr_columns provides the column name, if there is a extra column in ismr (usually from LISN networks provides filename as extra column) add extra column using following command
        
        '''
        ismrpy.ismr_columns.append('Name of the column')
        '''
To skip the first line of the file use skiprows=1
        
        '''
        data=ismrpy.read_ismr(filename=Name_of_file,skiprows=1)
        '''
## Authors

All are welcome to contribute to the project
See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the GPL-3 License - see the [LICENSE.md](LICENSE.md) file for details
