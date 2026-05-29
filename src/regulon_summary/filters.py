import pandas as pd


def filter_by_min_genes(regulon: pd.DataFrame, min_genes: int) -> pd.DataFrame:
    return regulon[regulon["genes"].apply(len) >= min_genes]


def filter_by_type(regulon: pd.DataFrame, regulator_type: str) -> pd.DataFrame:
    if regulator_type == "all":
        return regulon

    return regulon[regulon["type"] == regulator_type]


def filter_interactions_by_regulon(interactions: pd.DataFrame, regulon: pd.DataFrame,) -> pd.DataFrame:
    valid_tfs = set(regulon["TF"])

    # Se filtran las interacciones para solo preservar aquellas cuyo TF está en el regulón filtrado. 
    return interactions[interactions["TF"].isin(valid_tfs)]