from utils import *


def type_definitions():
    df = execute_query(
        '''
        SELECT typedefinition.typenodetype, typedefinition.typepublicvisibility, 
        typedefinition.isfinalclass, typedefinition.hasextends, 
        typedefinition.numberannotations, typedefinition.isindefaultpackage, 
        typedefinition.numberimplements, typedefinition.numbergenerictypes, 
        typedefinition.numbermethods, typedefinition.percentageoverloadedmethods,
        typedefinition.numberconstructors, typedefinition.numberfields, 
        typedefinition.numbernestedtypes, typedefinition.numberinnertypes, 
        typedefinition.namingconvention, typedefinition.isabstract,
        typedefinition.numberstaticnestedtypes, typedefinition.isinnerclass,
        typedefinition.isstrictfp, typedefinition.staticfieldpercentage, 
        typedefinition.staticmethodpercentage, typedefinition.numberstaticblocks, 
        typedefinition.isnestedclass, typedefinition.isstatic,
        typedefinition.user_class FROM typedefinition;
        ''')

    # DISCRETIZATION
    discretized_columns = {
        "numberannotations": [(0, 2), (2, 4), (4, inf)],  # min: 0 max: 6
        "numberimplements": [(0, 4), (4, 8), (8, inf)],  # min: 0 max: 10
        "numbergenerictypes": [(0, 2), (2, 4), (4, inf)],  # min: 0 max: 7
        "numbermethods": [(0, 234), (234, 468), (468, inf)],  # min: 0 max: 701
        "numberfields": [(0, 84), (84, 168), (168, inf)],  # min: 0 max: 250
        "numbernestedtypes": [(0, 90), (90, 180), (180, inf)],  # min: 0 max: 268
        "numberinnertypes": [(0, 90), (90, 180), (180, inf)],  # min: 0 max: 268
        "numberconstructors": [(0, 6), (6, 12), (12, inf)],  # min: 0 max: 16
        "numberstaticnestedtypes": [(0, 24), (24, 48), (48, inf)],  # min: 0 max: 69
        "numberstaticblocks": [(0, 4), (4, 8), (8, inf)],  # min: 0 max: 10
        "percentageoverloadedmethods": [(0, 34), (34, 67), (67, inf)],  # min: 0 max: 100
        "staticfieldpercentage": [(0, 34), (34, 67), (67, inf)],  # min: 0 max: 100
        "staticmethodpercentage": [(0, 34), (34, 67), (67, inf)]  # min: 0 max: 100
    }
    discretize_columns(df, discretized_columns)
    # print(df.groupby(['numberannotations']).size())
    # print(df.groupby(['numberimplements']).size())
    # print(df.groupby(['numbergenerictypes']).size())
    # print(df.groupby(['numbermethods']).size())
    # print(df.groupby(['numberfields']).size())
    # print(df.groupby(['numbernestedtypes']).size())
    # print(df.groupby(['numberinnertypes']).size())
    # print(df.groupby(['numberconstructors']).size())
    # print(df.groupby(['numberstaticnestedtypes']).size())
    # print(df.groupby(['numberstaticblocks']).size())
    # print(df.groupby(['percentageoverloadedmethods']).size())
    # print(df.groupby(['staticfieldpercentage']).size())
    # print(df.groupby(['staticmethodpercentage']).size())

    # SINGLE FEATURE
    print("--- SINGLE FEATURE ---")
    print(get_statistics(df, ['typenodetype'], 10))
    print(get_statistics(df, ['typepublicvisibility'], 10))
    print(get_statistics(df, ['isfinalclass'], 10))
    print(get_statistics(df, ['hasextends'], 10))
    print(get_statistics(df, ['numberannotations'], 10))
    print(get_statistics(df, ['isindefaultpackage'], 10))
    print(get_statistics(df, ['numberimplements'], 10))
    print(get_statistics(df, ['numbergenerictypes'], 10))
    print(get_statistics(df, ['numbermethods'], 10))
    print(get_statistics(df, ['percentageoverloadedmethods'], 10))
    print(get_statistics(df, ['numberconstructors'], 10))
    print(get_statistics(df, ['numberfields'], 10))
    print(get_statistics(df, ['numbernestedtypes'], 10))
    print(get_statistics(df, ['numberinnertypes'], 10))
    print(get_statistics(df, ['namingconvention'], 10))
    print(get_statistics(df, ['isabstract'], 10))
    print(get_statistics(df, ['numberstaticnestedtypes'], 10))
    print(get_statistics(df, ['isinnerclass'], 10))
    print(get_statistics(df, ['isstrictfp'], 10))
    print(get_statistics(df, ['staticfieldpercentage'], 10))
    print(get_statistics(df, ['staticmethodpercentage'], 10))
    print(get_statistics(df, ['numberstaticblocks'], 10))
    print(get_statistics(df, ['isnestedclass'], 10))
    print(get_statistics(df, ['isstatic'], 10))

    # 2 FEATURES
    print("--- TWO FEATURES ---")
    print(get_statistics(df, ['typepublicvisibility', 'typenodetype'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'isabstract'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'isstatic'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'numberconstructors'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'numbermethods'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'numberfields'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'numberannotations'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'hasextends'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'numberimplements'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'isfinalclass'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'isindefaultpackage'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'staticfieldpercentage'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'staticmethodpercentage'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'percentageoverloadedmethods'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'isinnerclass'], 10))
    print(get_statistics(df, ['typenodetype', 'numberannotations'], 10))
    print(get_statistics(df, ['typenodetype', 'numbermethods'], 10))
    print(get_statistics(df, ['typenodetype', 'numberfields'], 10))
    print(get_statistics(df, ['typenodetype', 'isindefaultpackage'], 10))
    print(get_statistics(df, ['typenodetype', 'numbergenerictypes'], 10))
    print(get_statistics(df, ['typenodetype', 'namingconvention'], 10))
    print(get_statistics(df, ['hasextends', 'numbermethods'], 10))
    print(get_statistics(df, ['hasextends', 'numberfields'], 10))
    print(get_statistics(df, ['hasextends', 'numberimplements'], 10))
    print(get_statistics(df, ['hasextends', 'isstatic'], 10))
    print(get_statistics(df, ['hasextends', 'numberconstructors'], 10))
    print(get_statistics(df, ['hasextends', 'numbernestedtypes'], 10))
    print(get_statistics(df, ['hasextends', 'numberinnertypes'], 10))
    print(get_statistics(df, ['numberimplements', 'numbermethods'], 10))
    print(get_statistics(df, ['isabstract', 'numberimplements'], 10))

    # 3 FEATURES
    print("--- THREE FEATURES ---")
    print(get_statistics(df, ['typepublicvisibility', 'typenodetype', 'isindefaultpackage'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'typenodetype', 'numbermethods'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'typenodetype', 'numberfields'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'hasextends', 'numberconstructors'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'hasextends', 'numberimplements'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'hasextends', 'numbermethods'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'hasextends', 'percentageoverloadedmethods'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'isabstract', 'numbermethods'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'isabstract', 'numberconstructors'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'isabstract', 'numberfields'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'isabstract', 'numberimplements'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'numberimplements', 'percentageoverloadedmethods'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'staticfieldpercentage', 'staticmethodpercentage'], 10))
    print(get_statistics(df, ['typenodetype', 'numbermethods', 'numberfields'], 10))
    print(get_statistics(df, ['isstatic', 'staticfieldpercentage', 'staticmethodpercentage'], 10))
    print(get_statistics(df, ['numberstaticblocks', 'staticfieldpercentage', 'staticmethodpercentage'], 10))
    print(get_statistics(df, ['hasextends', 'numberconstructors', 'numbermethods'], 10))
    print(get_statistics(df, ['hasextends', 'numberimplements', 'numbermethods'], 10))
    print(get_statistics(df, ['hasextends', 'numberfields', 'numbermethods'], 10))
    print(get_statistics(df, ['isabstract', 'numberfields', 'numbermethods'], 10))
    print(get_statistics(df, ['isabstract', 'numberconstructors', 'numbermethods'], 10))
    print(get_statistics(df, ['isabstract', 'hasextends', 'numberimplements'], 10))

    # 4 FEATURES
    print("--- FOUR FEATURES ---")
    print(get_statistics(df, ['typepublicvisibility', 'typenodetype', 'numbermethods', 'numberfields'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'hasextends', 'numberimplements', 'numberconstructors'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'hasextends', 'numberimplements', 'numbermethods'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'isabstract', 'numberimplements', 'numberconstructors'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'isstatic', 'staticfieldpercentage', 'staticmethodpercentage'], 10))
    print(get_statistics(df, ['typepublicvisibility', 'hasextends', 'isabstract', 'numberimplements'], 10))