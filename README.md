# ismrpy

Reads ismr files and provides with a panda data frame

## Getting Started
### Prerequisites

Things needed before installation of package
```
pip install numpy
pip install pandas
```

### Installation

```
pip install ismrpy
```


## Usage
Inputs-

    filename= Name of the file

If provided with lat and lon program calculates Ionospheric pierce points.

    lat= latitude of station
    lon=longitude of station
    IPP=Height of ionospheric layer in kilometers (default 350 KM)
    skiprows=Number of rows to be skipped(default None)
    
To read general ismr file
    
```
import ismrpy
data=ismrpy.read_ismr(filename=Name_of_file)
```

To read specific files with header and with extra number of columns:

ismrpy.ismr_column provides the column names, if there is an extra column in ismr (usually from ismr files from LISN networks has filename as extra column) add extra column using following command
        
```
ismrpy.ismr_column.append('Name of the column')
```
    
To skip the first line of the file use skiprows=1
        
```
data=ismrpy.read_ismr(filename=Name_of_file,skiprows=1)
```
    
## Authors

All are welcome to contribute to the project
See also the list of [contributors](https://github.com/dinilbose/ismrpy/contributors) who participated in this project.

## License

This project is licensed under the GPL-3 License - see the [LICENSE.md](LICENSE.txt) file for details
