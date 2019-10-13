# The module helps to read basic ismr file and convert it into panda dataframe for quick and easy analysis
import pandas as pd
import numpy as np


def read_ismr(filename='', lat='', lon='', addition=True, Ipp=350, skiprows=None):
    """"
    Reads ismr and provide with panda data frame
        filename= Name of the file
    If provided with lat and lon, program  Calculate Ionospheric pierce points and Slant TEC(Stec)
        lat= latitude of station
        lon=longitude of station
        IPP=Height of ionospheric layer in kilometers (default 350 KM)
    """
    data = pd.read_csv(filename, names=ismr_column, parse_dates=[['GPS_Week_Number', 'GPS_Time_Week']],
                       date_parser=__weeksecondstoutc, skiprows=skiprows)
    data = data.rename(columns={'GPS_Week_Number_GPS_Time_Week': 'Time'})
    data = data.set_index(['Time'])
    data['sv'] = data.SVID.apply(__navigation)
    data = data.convert_objects(convert_numeric=True)
    if not lat == '' and not lon == '':
        PHI = lat  # Values needed for Chaganassery
        LAMBDA = lon
        T_SCI = data.Total_S4_Sig1
        T_SCI = np.round((T_SCI * 100)) / 100;
        CORR_S4 = data.Correction_total_S4_Sig1
        CORR_S4 = np.round((CORR_S4 * 100)) / 100;
        SCI = (np.sqrt((T_SCI * T_SCI) - (CORR_S4 * CORR_S4)));
        SCI = np.round((SCI * 100)) / 100;
        SCI[SCI > 3] = np.nan
        SIGPHI = data.Phi60_Sig1_60
        SIGPHI[SIGPHI > 3] = np.nan
        # Locktime = data.Sig1_lock_time
        ELEV = data.Elevation
        AZI = data.Azimuth
        RE = 6378.1363 * 10 ** 3  # Earth radius in meter
        IPP = Ipp * 10 ** 3
        E = np.deg2rad(ELEV)
        A = np.deg2rad(AZI)
        PHI_U = np.deg2rad(PHI)
        LAMBDA_U = np.deg2rad(LAMBDA)
        Iono_ht = ((RE / (RE + IPP)) * np.cos(E))
        Shi_pp = (np.pi / 2) - E - np.arcsin(Iono_ht)
        # % ---------------------------Satellite latitude and IPP Lat calculation
        Phi_pp = np.sin(PHI_U) * np.cos(Shi_pp) + np.cos(PHI_U) * np.sin(Shi_pp) * np.cos(A)
        DLat_PP = np.rad2deg(Phi_pp)
        # %---------------------- Satellite longitude calculation
        TERM2 = ((np.sin(Shi_pp) * np.sin(A)) / np.cos(Phi_pp))
        Lambda_pp = LAMBDA_U + np.arcsin(TERM2)
        DLong_PP = np.rad2deg(Lambda_pp)
        data['S4_index'] = SCI
        data['Stec'] = data.TEC_TOW
        data['Dlat_IPP'] = DLat_PP
        data['Dlong_IPP'] = DLong_PP
    return data


def __weeksecondstoutc(gpsweek, gpsseconds):
    """"
    Convert gpsweek and gpseconds to time
    """
    import datetime, calendar
    gpsweek = float(gpsweek)
    gpsseconds = float(gpsseconds)
    # print(gpsweek,gpsseconds)
    leapseconds = 0
    datetimeformat = "%Y-%m-%d %H:%M:%S"
    epoch = datetime.datetime.strptime("1980-01-06 00:00:00", datetimeformat)
    elapsed = datetime.timedelta(days=(gpsweek * 7), seconds=(gpsseconds))
    # return datetime.datetime.strftime(epoch + elapsed,datetimeformat)
    return elapsed + epoch


def __navigation(x):
    sv = 'M' + str(x)
    if 0 < x < 38:
        sv = 'G' + str(x)
    elif 37 < x < 62:
        sv = 'R' + str(x)
    elif 70 < x < 107:
        if len(str(x)) > 2:
            x = str(x)[-2:]
        sv = 'E' + str(x)
    elif 119 < x < 139:
        if len(str(x)) > 2:
            x = str(x)[-2:]
        sv = 'S' + str(x)
    elif 140 < x < 177:
        if len(str(x)) > 2:
            x = str(x)[-2:]
        sv = 'C' + str(x)
    elif 181 < x < 187:
        if len(str(x)) > 2:
            x = str(x)[-2:]
        sv = 'J' + str(x)
    return sv


ismr_column = ['GPS_Week_Number',
               'GPS_Time_Week',
               'SVID',
               'Value',
               'Azimuth',
               'Elevation',
               'Sig1',
               'Total_S4_Sig1',
               'Correction_total_S4_Sig1',
               'Phi01_Sig1_1',
               'Phi03_Sig1_3',
               'Phi10_Sig1_10',
               'Phi30_Sig1_30',
               'Phi60_Sig1_60',
               'AvgCCD_Sig1_average_code-carrier_divergence',
               'SigmaCCD_Sig1_standard_deviation_code-carrier_divergence',
               'TEC_TOW-45s',
               'dTEC_TOW-60s_TOW-45s',
               'TEC_TOW-30s',
               'dTEC_TOW-45s_TOW-30s',
               'TEC_TOW-15s',
               'dTEC_TOW-30s_TOW-15s',
               'TEC_TOW',
               'dTEC_TOW-15s_TOW',
               'Sig1_lock_time',
               'sbf2ismr_version_number',
               'Lock_time_second_frequency_TEC',
               'Averaged_C/N0_second_frequency_TEC_computation',
               'SI_Index_Sig1',
               'SI_Index_Sig1_numerator',
               'p_Sig1_spectral_slope',
               'Average_Sig2_C/N0',
               'Total_S4_Sig2',
               'Correction_total_S4_Sig2',
               'Phi01_Sig2_1',
               'Phi03_Sig2_3',
               'Phi10_Sig2_10',
               'Phi30_Sig2_30',
               'Phi60_Sig2_60',
               'AvgCCD_Sig2_average_code-carrier_divergence',
               'SigmaCCD_Sig2_standard',
               'Sig2_lock',
               'SI_Index_Sig2',
               'SI_Index_Sig2_numerator',
               'p_Sig2_phase',
               'Average_Sig3_C/N0_last_minute',
               'Total_S4_Sig3',
               'Correction_total_S4_Sig3',
               'Phi01_Sig3_1_phase',
               'Phi03_Sig3_3_phase',
               'Phi10_Sig3_10_phase',
               'Phi30_Sig3_30_phase',
               'Phi60_Sig3_60_phase',
               'AvgCCD_Sig3_average_code-carrier_divergence',
               'SigmaCCD_Sig3_standard_deviation_code-carrier_divergence',
               'Sig3_lock_time',
               'SI_Index_Sig3',
               'SI_Index_Sig3_numerator',
               'p_Sig3_phase',
               'T_Sig1_phase',
               'T_Sig2_phase',
               'T_Sig3_phase']
