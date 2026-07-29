# This file contains the fields to be populated from the excel files

from typing import Optional

from pydantic import BaseModel

from typing import Literal


class RawExtractedItems(BaseModel):
    """ This class stores the raw data extracted from the excel spreadsheet
    
    """
    label: str
    value: float


class extracted_data(BaseModel):
    """ This class will be populated from the user's uploaded file

    """
    source_file: str
    source_sheet: str
    row_number: int
    label: str
    raw_value: str
    internal_name: Optional[str] = None
    cleaned_value: Optional[float] = None
    status: str = "raw"


class final_extracted_results(BaseModel):
    rows: list[extracted_data]
    missing_required: list[str]
    is_viable: bool