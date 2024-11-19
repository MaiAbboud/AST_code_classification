from utils import *


def programs():
    df = execute_query(
        '''
        SELECT program.classpercentage, program.interfacepercentage,
        program.enumpercentage, program.codeinpackages,
        program.defaultpackage, program.numberoftypesindefaultpackage,
        program.numberoftypesinpackages, program.user_class FROM program;
        ''')

    # DISCRETIZATION
    discretized_columns = {
        "classpercentage": [(0, 34), (34, 67), (67, inf)],  # min: 0 max: 100
        "interfacepercentage": [(0, 34), (34, 67), (67, inf)],  # min: 0 max: 100
        "enumpercentage": [(0, 14), (14, 28), (28, inf)],  # min: 0 max: 40
        "numberoftypesindefaultpackage": [(0, 19), (19, 38), (38, inf)],  # min: 0 max: 56
        "numberoftypesinpackages": [(0, 1476), (1476, 2952), (2952, inf)],  # min: 0 max: 4427
    }
    discretize_columns(df, discretized_columns)
    # print(df.groupby(['classpercentage']).size())
    # print(df.groupby(['interfacepercentage']).size())
    # print(df.groupby(['enumpercentage']).size())
    # print(df.groupby(['numberoftypesindefaultpackage']).size())
    # print(df.groupby(['numberoftypesinpackages']).size())

    # SINGLE FEATURE
    print("--- SINGLE FEATURE ---")
    print(get_statistics(df, ['classpercentage'], 10))
    print(get_statistics(df, ['interfacepercentage'], 10))
    print(get_statistics(df, ['enumpercentage'], 10))
    print(get_statistics(df, ['codeinpackages'], 10))
    print(get_statistics(df, ['defaultpackage'], 10))
    print(get_statistics(df, ['numberoftypesindefaultpackage'], 10))
    print(get_statistics(df, ['numberoftypesinpackages'], 10))

    # 2 FEATURES
    print("--- TWO FEATURES ---")
    print(get_statistics(df, ['classpercentage', 'codeinpackages'], 10))
    print(get_statistics(df, ['classpercentage', 'defaultpackage'], 10))
    print(get_statistics(df, ['classpercentage', 'numberoftypesindefaultpackage'], 10))
    print(get_statistics(df, ['classpercentage', 'numberoftypesinpackages'], 10))
    print(get_statistics(df, ['interfacepercentage', 'codeinpackages'], 10))
    print(get_statistics(df, ['interfacepercentage', 'defaultpackage'], 10))
    print(get_statistics(df, ['interfacepercentage', 'numberoftypesindefaultpackage'], 10))
    print(get_statistics(df, ['interfacepercentage', 'numberoftypesinpackages'], 10))
    print(get_statistics(df, ['enumpercentage', 'codeinpackages'], 10))
    print(get_statistics(df, ['enumpercentage', 'defaultpackage'], 10))
    print(get_statistics(df, ['enumpercentage', 'numberoftypesindefaultpackage'], 10))
    print(get_statistics(df, ['enumpercentage', 'numberoftypesinpackages'], 10))

    # 3 FEATURES
    print("--- THREE FEATURES ---")
    print(get_statistics(df, ['classpercentage', 'codeinpackages', 'numberoftypesinpackages'], 10))
    print(get_statistics(df, ['classpercentage', 'defaultpackage', 'numberoftypesindefaultpackage'], 10))
    print(get_statistics(df, ['interfacepercentage', 'codeinpackages', 'numberoftypesinpackages'], 10))
    print(get_statistics(df, ['interfacepercentage', 'defaultpackage', 'numberoftypesindefaultpackage'], 10))
    print(get_statistics(df, ['enumpercentage', 'codeinpackages', 'numberoftypesinpackages'], 10))
    print(get_statistics(df, ['enumpercentage', 'defaultpackage', 'numberoftypesindefaultpackage'], 10))

